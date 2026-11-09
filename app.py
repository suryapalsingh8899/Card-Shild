"""
CardShield – ATM Card Fraud Detection Backend API & Web Server
Powered by Flask, Scikit-Learn, and Ensemble Behavioral Intelligence.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')
CORS(app)

model_path = os.path.join(BASE_DIR, 'fraud_model.pkl')
model = None
encoders = None
model_metrics = {
    "roc_auc": 0.865,
    "fraud_recall": 0.784,
    "balanced_accuracy": 0.810,
    "baseline_naive_accuracy": 0.995,
    "paradox_note": "A naive model predicting all legitimate transactions achieves 99.5% accuracy but 0% fraud detection. CardShield solves this Accuracy Paradox using class-balanced Random Forest learning."
}

if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        data = pickle.load(f)
        model = data.get('model')
        encoders = data.get('encoders')
        if 'metrics' in data:
            model_metrics.update(data['metrics'])
    print("[INFO] Model and Encoders loaded successfully from", model_path)
else:
    print("[WARNING] Model not found. Please run train_model.py first.")

# Frontend to Dataset Encoders Mappings
CARD_TYPE_MAP = {
    'debit': 'Debit',
    'credit-classic': 'Credit - Classic',
    'credit-gold': 'Credit - Gold',
    'credit-platinum': 'Credit - Platinum'
}

STATUS_MAP = {
    'active': 'Active',
    'expired': 'Expired',
    'blocked': 'Blocked'
}

def safe_encode(encoder, value):
    """Safely encode categorical values, falling back to 'Unknown' if not seen during training."""
    classes = encoder.classes_.tolist()
    if value in classes:
        return encoder.transform([value])[0]
    return encoder.transform(['Unknown'])[0]

def compute_heuristic_score(data):
    """
    Computes heuristic risk modifier from real-time behavioral dimensions 
    (Time, Geolocation, Velocity, Credit Utilization) that complement the tabular ML model.
    """
    amount = float(data.get('txnAmount', 0))
    limit = float(data.get('creditLimit', 0))
    freq = int(data.get('frequency', 3))
    loc = str(data.get('txnLocation', 'domestic')).lower()
    time_str = str(data.get('txnTime', '12:00'))
    status = str(data.get('cardStatus', 'active')).lower()
    
    score = 0
    
    # 1. Card status
    if status == 'blocked':
        return 98
    elif status == 'expired':
        score += 35
    else:
        score += 2
        
    # 2. Transaction magnitude variance (baseline mean = ~1850)
    avg_legit = 1850.45
    if amount < 100:
        score += 8  # micro card-testing probe
    elif amount <= avg_legit * 1.5:
        score += 3
    elif amount <= avg_legit * 3:
        score += 10
    elif amount <= avg_legit * 5:
        score += 16
    else:
        score += 24 # extremely high deviation
        
    # 3. Geolocation scrutiny
    if loc == 'international':
        score += 18
    else:
        score += 2
        
    # 4. Temporal window (Midnight to 4 AM high risk)
    try:
        hour = int(time_str.split(':')[0])
        if 0 <= hour < 4:
            score += 18
        elif 4 <= hour < 7:
            score += 10
        elif 7 <= hour < 22:
            score += 2
        else:
            score += 8
    except Exception:
        score += 2
        
    # 5. Velocity / Frequency spike (24h)
    if freq <= 3:
        score += 2
    elif freq <= 6:
        score += 6
    elif freq <= 10:
        score += 14
    else:
        score += 22
        
    # 6. Credit limit utilization
    if limit > 0:
        util = amount / limit
        if util > 1.0:
            score += 16
        elif util > 0.8:
            score += 10
        elif util > 0.5:
            score += 5
            
    return min(95, score)

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "online",
        "service": "CardShield AI Fraud Detection API",
        "model_loaded": model is not None,
        "metrics": model_metrics
    })

@app.route('/analyze', methods=['POST'])
def analyze():
    if not model or not encoders:
        return jsonify({"error": "ML Model not loaded on server"}), 500

    data = request.json or {}
    
    amount = float(data.get('txnAmount', 0))
    category = data.get('category', 'Unknown')
    
    # Map frontend card type to trained encoder labels
    card_type_raw = str(data.get('cardType', 'Unknown')).strip()
    card_type = CARD_TYPE_MAP.get(card_type_raw.lower(), card_type_raw)
    
    # Map frontend card status to trained encoder labels
    status_raw = str(data.get('cardStatus', 'Unknown')).strip()
    status = STATUS_MAP.get(status_raw.lower(), status_raw.capitalize())
    
    credit_limit = float(data.get('creditLimit', 0))
    
    # Safely encode categorical features
    cat_encoded = safe_encode(encoders['merchant_category'], category)
    type_encoded = safe_encode(encoders['card_type'], card_type)
    status_encoded = safe_encode(encoders['status'], status)
    
    # Prepare features vector for Random Forest
    features = np.array([[amount, cat_encoded, type_encoded, status_encoded, credit_limit]])
    
    # ML model prediction (balanced probability of fraud)
    proba = float(model.predict_proba(features)[0][1])
    
    # Calibrate probability:
    # Balanced Random Forest outputs ~0.36 for benign records, ~0.60+ for fraud
    if proba <= 0.36:
        ml_score = (proba / 0.36) * 30
    elif proba <= 0.50:
        ml_score = 30 + ((proba - 0.36) / (0.50 - 0.36)) * 30
    else:
        ml_score = 60 + ((proba - 0.50) / 0.50) * 35
        
    ml_score = max(5, min(95, ml_score))
    
    # Compute behavioral heuristic score from all 7 dimensions
    heuristic_score = compute_heuristic_score(data)
    
    # Ensemble fusion: 40% ML Model tabular risk + 60% Real-time behavioral heuristics
    scaled_score = int(round(0.40 * ml_score + 0.60 * heuristic_score))
    
    # Critical state overrides
    if status.lower() == 'blocked':
        scaled_score = max(scaled_score, 98)
    elif status.lower() == 'expired':
        scaled_score = max(scaled_score, 88)
        
    scaled_score = min(99, max(1, scaled_score))
    
    return jsonify({
        "success": True,
        "score": scaled_score,
        "ml_probability": proba,
        "metrics": model_metrics
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"[INFO] Starting CardShield server on port {port} ...")
    app.run(host='0.0.0.0', port=port, debug=False)

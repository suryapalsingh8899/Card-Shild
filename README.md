# 🛡️ CardShield – ATM Card Fraud Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Backend-Flask%203.x-green.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Deployment](https://img.shields.io/badge/Deployment-Ready%20(Render%2FRailway)-brightgreen.svg)]()

**CardShield** is a real-time ATM & credit card fraud detection web platform powered by Machine Learning and multi-dimensional behavioral intelligence. Developed as a 5th-Semester Problem-Based Learning (PBL) academic project, CardShield evaluates transaction signals across 7 behavioral dimensions in sub-second latency to prevent fraud before settlement.

---

## 🌟 Key Highlights & Features

- **⚡ Real-Time Hybrid Scoring:** Combines a trained **Cost-Sensitive Random Forest** model with real-time heuristic rules for robust anomaly detection.
- **⚖️ Solves the "Accuracy Paradox":** Employs balanced class weighting to overcome extreme dataset imbalance (0.5% fraud rate), optimizing for **ROC-AUC (86.5%)** and **Fraud Recall (78.4%)** rather than deceptive raw accuracy.
- **🎨 Editorial High-Contrast UI:** Modern, responsive dashboard with animated SVG risk speedometer, dynamic factor breakdown bars, and interactive portfolio analytics.
- **🧪 One-Click Presets:** Instant simulation profiles (*Standard Domestic Debit*, *Gold Credit*, and *Platinum High-Risk Attack*).
- **📋 Live Session Audit Log:** Ephemeral transaction history log with manual verification actions (*Mark Safe* / *Report Fraud*).
- **🛡️ Resilient Client-Side Fallback:** If the ML backend server is offline, the frontend seamlessly fails over to an internal 7-factor rule engine without crashing.
- **☁️ Cloud-Ready Unified Server:** Flask backend serves both the REST API and the frontend dashboard as a single production web application.

---

## 🧠 Machine Learning & The Accuracy Paradox

### The Problem
In financial datasets, fraud accounts for only **~0.5% of total transactions**.
* A naive, non-learning model that labels **every transaction as legitimate** achieves **99.5% raw accuracy**.
* Despite high accuracy, it detects **0% of actual frauds**, making raw accuracy a misleading metric.

### The CardShield Solution
CardShield resolves this paradox in [`train_model.py`](train_model.py):
1. **Cost-Sensitive Learning:** Configured `class_weight='balanced'` in Scikit-Learn's `RandomForestClassifier` to heavily penalize false negatives (missed frauds).
2. **Prioritizing Actionable Metrics:**
   - **ROC-AUC Score:** **86.5%**
   - **Fraud Recall (Sensitivity):** **78.4%** (catches rare fraud signals)
   - **Balanced Accuracy:** **81.0%**
3. **Calibrated Probability Scaling:** Transforms model probabilities into an intuitive `0–100` composite risk score without false-positive saturation.

---

## 🔍 The 7 Behavioral Dimensions

| Step | Dimension | Evaluation Logic |
|:---:|:---|:---|
| **01** | **Card Status** | Immediate critical override (`98+`) for blocked or expired cards. |
| **02** | **Amount Magnitude** | Compares transaction amount against historical spending means (₹1,850 baseline). |
| **03** | **Temporal Window** | Flags off-hours point-of-sale and ATM attempts (00:00–04:00 AM high risk). |
| **04** | **Cross-Border Geolocation** | Elevates scrutiny on international conversions and overseas merchants. |
| **05** | **Merchant Profiling** | Evaluates historical fraud density across 14 merchant categories (e.g. Fund Transfers, ATM Withdrawals). |
| **06** | **Velocity Spike** | Detects high-frequency transaction bursts (24h) characteristic of automated card-testing bots. |
| **07** | **Credit Limit Utilization** | Identifies limit-exhausting transactions exceeding 80–100% of cardholder credit. |

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, Modern CSS3 (CSS Grid, Variables, Responsive Layouts), Vanilla JavaScript (ES6+, Fetch API, Dynamic SVG Rendering)
- **Backend:** Python 3.10+, Flask, Flask-CORS, Gunicorn (Production WSGI)
- **Machine Learning:** Scikit-Learn (`RandomForestClassifier`, `LabelEncoder`), Pandas, NumPy
- **Serialization:** Pickle (`fraud_model.pkl`)

---

## 📁 Repository Structure

```text
├── index.html              # Main web dashboard layout
├── style.css               # Clean architectural UI design & animations
├── app.js                  # Frontend state management, charts, and API hooks
├── app.py                  # Flask REST API & static web server
├── train_model.py          # ML training pipeline resolving Accuracy Paradox
├── fraud_model.pkl         # Serialized Scikit-Learn model & label encoders
├── requirements.txt        # Production Python dependencies
├── Procfile                # Gunicorn startup instruction for cloud PaaS
├── .gitignore              # Ignores large raw dataset (>100MB) & cache files
└── README.md               # Project documentation
```

---

## ⚙️ Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/suryapalsingh8899/Card-Shild.git
cd Card-Shild
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. (Optional) Retrain the Model
```bash
python train_model.py
```
*(Loads from `Bank Transaction dataset/` and exports an updated `fraud_model.pkl`)*.

### 5. Start the Application
Run the unified Flask server:
```bash
python app.py
```
Open your browser and navigate to:  
👉 **`http://localhost:5000`**

---

## ☁️ Deployment Guide (Render.com)

1. Fork or push this repository to GitHub.
2. Sign in to **[Render.com](https://render.com/)** and click **New +** → **Web Service**.
3. Select your `Card-Shild` repository.
4. Configure the service:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** `Free`
5. Click **Create Web Service**. Your application will be live in ~2 minutes with a secure HTTPS URL!

---

## 🔌 API Documentation

### `POST /analyze`
Analyzes transaction parameters and returns calibrated fraud probability.

**Request Payload:**
```json
{
  "cardType": "debit",
  "cardStatus": "active",
  "txnAmount": 1250,
  "category": "Groceries",
  "txnTime": "14:30",
  "txnLocation": "domestic",
  "frequency": 2,
  "creditLimit": 0
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "score": 18,
  "ml_probability": 0.354,
  "metrics": {
    "roc_auc": 0.865,
    "fraud_recall": 0.784,
    "balanced_accuracy": 0.810
  }
}
```

### `GET /health`
Returns service status, model availability, and evaluation benchmarks.

---

## 👥 Authors & Academic Context

- **Course:** 5th Semester Problem-Based Learning (PBL)
- **Project:** CardShield – Intelligent ATM Card Fraud Detection
- **Lead Developer:** [Suryapal Singh](https://github.com/suryapalsingh8899)

*Disclaimer: This system is an academic research prototype intended for educational and analytical purposes.*

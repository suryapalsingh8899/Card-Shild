"""
CardShield – ATM Card Fraud Detection Model Training
Demonstrating Solution to the 'Accuracy Paradox' in Imbalanced Banking Datasets.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, roc_auc_score, balanced_accuracy_score, confusion_matrix
import pickle
import os

print("=" * 60)
print("  CARDSHIELD ML PIPELINE – TRAINING & EVALUATION")
print("=" * 60)

print("\n[1/5] Loading datasets...")
df_txns = pd.read_csv("Bank Transaction dataset/card_transactions.csv", nrows=100000)
df_cards = pd.read_csv("Bank Transaction dataset/cards.csv")

print("[2/5] Merging and preprocessing...")
df = pd.merge(df_txns, df_cards, on="card_id", how="left")

features = ['amount', 'merchant_category', 'card_type', 'status', 'credit_limit']
X = df[features].copy()
y = df['is_fraud']

# Handle missing values
X['merchant_category'] = X['merchant_category'].fillna('Unknown')
X['card_type'] = X['card_type'].fillna('Unknown')
X['status'] = X['status'].fillna('Unknown')
X['credit_limit'] = X['credit_limit'].fillna(0)

# Categorical Label Encoding with 'Unknown' safety class
encoders = {}
for col in ['merchant_category', 'card_type', 'status']:
    le = LabelEncoder()
    unique_vals = list(X[col].unique())
    if 'Unknown' not in unique_vals:
        unique_vals.append('Unknown')
    le.fit(unique_vals)
    X[col] = le.transform(X[col])
    encoders[col] = le

total_samples = len(y)
fraud_count = int((y == 1).sum())
legit_count = int((y == 0).sum())
fraud_rate = fraud_count / total_samples

print(f"      Total records: {total_samples:,}")
print(f"      Legitimate:    {legit_count:,} ({100 - fraud_rate*100:.2f}%)")
print(f"      Fraudulent:    {fraud_count:,} ({fraud_rate*100:.2f}%)")

print("\n" + "-" * 60)
print("  DEMONSTRATING THE 'ACCURACY PARADOX':")
print(f"  A naive baseline model predicting ALL 0 (legitimate) achieves:")
print(f"  >> Raw Accuracy: {100 - fraud_rate*100:.2f}%")
print(f"  >> Fraud Recall: 0.00% (catches ZERO frauds!)")
print("  Hence, raw accuracy is deceptive. We solve this using Cost-Sensitive")
print("  Balanced Random Forest Learning (class_weight='balanced').")
print("-" * 60)

print("\n[3/5] Splitting dataset (80% train, 20% test)...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("[4/5] Training Cost-Sensitive Balanced Random Forest Classifier...")
clf = RandomForestClassifier(
    n_estimators=60,
    max_depth=12,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)
clf.fit(X_train, y_train)

print("\n[5/5] Comprehensive Evaluation...")
y_pred = clf.predict(X_test)
y_proba = clf.predict_proba(X_test)[:, 1]

roc_auc = float(roc_auc_score(y_test, y_proba))
bal_acc = float(balanced_accuracy_score(y_test, y_pred))

print("\n" + "=" * 60)
print(f"  KEY BALANCED PERFORMANCE METRICS:")
print(f"  * ROC-AUC Score:         {roc_auc * 100:.2f}%")
print(f"  * Balanced Accuracy:     {bal_acc * 100:.2f}%")
print("=" * 60)

print("\nClassification Report (Handling Imbalance):")
report = classification_report(y_test, y_pred, target_names=['Legitimate (0)', 'Fraud (1)'], output_dict=True)
print(classification_report(y_test, y_pred, target_names=['Legitimate (0)', 'Fraud (1)']))

fraud_recall = float(report['Fraud (1)']['recall'])

metrics_payload = {
    "roc_auc": round(roc_auc, 3),
    "fraud_recall": round(fraud_recall, 3),
    "balanced_accuracy": round(bal_acc, 3),
    "baseline_naive_accuracy": round(1.0 - fraud_rate, 3),
    "accuracy_paradox_status": "Resolved (Using ROC-AUC & Recall instead of raw 99.5% accuracy)"
}

print("Saving model, encoders, and metrics to fraud_model.pkl ...")
with open("fraud_model.pkl", "wb") as f:
    pickle.dump({
        'model': clf,
        'encoders': encoders,
        'metrics': metrics_payload
    }, f)

print("[DONE] Training complete. fraud_model.pkl successfully generated!\n")

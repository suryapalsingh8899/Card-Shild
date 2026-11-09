# CardShield – ATM Card Fraud Detection

**CardShield** is a 5th-semester academic project designed to predict and analyze the likelihood of ATM card fraud in real-time. It features a modern, glassmorphism-inspired frontend dashboard and a robust Python-based Machine Learning backend.

## 🚀 Features

- **Real-Time Risk Analysis:** Enter transaction details (amount, time, category, etc.) to get an instant fraud probability score.
- **Machine Learning Powered:** Utilizes a Random Forest Classifier trained on a dataset of bank transactions to predict fraud accurately.
- **Modern UI/UX:** A stunning, fully responsive dashboard built with Vanilla CSS (Dark Glassmorphism Theme) and interactive JavaScript animations.
- **Detailed Factor Breakdown:** Provides a visual breakdown of which factors (e.g., transaction time, location, amount) contributed to the risk score.
- **History Tracking:** Keeps a session log of your recent transaction checks.
- **Smart Fallback Logic:** If the Python ML backend is offline, the frontend automatically falls back to a simulated rule-based logic engine.

## 🛠️ Tech Stack

**Frontend:**
- HTML5
- CSS3 (Custom Variables, Flexbox/Grid, Animations)
- Vanilla JavaScript (DOM manipulation, Fetch API)

**Backend & Machine Learning:**
- Python 3.x
- Flask & Flask-CORS (REST API)
- Pandas & NumPy (Data Processing)
- Scikit-Learn (Random Forest Classifier, Label Encoders)
- Pickle (Model Serialization)

## 📁 Dataset Details

The AI model is trained on a synthetic **Bank Transaction Dataset**. The project specifically uses:
- `card_transactions.csv`: Contains transaction amounts, categories, and the `is_fraud` labels.
- `cards.csv`: Contains card statuses, types, and credit limits.

## ⚙️ Setup and Installation

### 1. Prerequisites
Make sure you have [Python](https://www.python.org/downloads/) installed on your system. 

### 2. Install Dependencies
Open your terminal/command prompt in the project folder and run:
```bash
pip install pandas scikit-learn flask flask-cors numpy
```

### 3. Train the Model
Before running the backend, you must train the ML model so it generates the `fraud_model.pkl` file:
```bash
python train_model.py
```
*(Note: This trains on a subset of 100,000 rows for speed and efficiency).*

### 4. Start the Backend Server
Start the Flask API server:
```bash
python app.py
```
The server will start running at `http://127.0.0.1:5000`.

### 5. Start the Frontend
You can open `index.html` directly in your browser, or start a simple local server to view the UI:
```bash
python -m http.server 8000
```
Then, open your browser and navigate to `http://localhost:8000`.

## 🧠 How It Works

1. The user inputs transaction details in the frontend UI.
2. The frontend sends a `POST` request to the Flask backend (`/analyze`).
3. The Flask API encodes the categorical inputs using the saved Scikit-Learn encoders.
4. The Random Forest model predicts the probability of fraud based on the input features.
5. The backend scales the probability into a user-friendly score (0-100) and sends it back to the frontend.
6. The UI dynamically updates the gauge charts, verdicts, and recommendations based on the ML result.

---
*Disclaimer: This project is for educational and analytical purposes only. It is not a substitute for official banking security systems.*

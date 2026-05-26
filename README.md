# 👥 Employee Attrition Predictor

An end-to-end Machine Learning project that predicts employee attrition risk,
built for HR analytics with a clean interactive Streamlit dashboard.

---

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python train_model.py
```

### 3. Launch the app
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
attrition_predictor/
├── app.py                  # Main Streamlit app
├── train_model.py          # Model training script
├── requirements.txt        # Dependencies
├── data/
│   ├── generate_data.py    # Synthetic IBM HR data generator
│   └── hr_data.csv         # Generated after training
└── models/
    ├── xgb_model.pkl       # Trained XGBoost model
    ├── encoders.pkl        # Label encoders
    ├── scaler.pkl          # StandardScaler
    └── results.json        # Model evaluation metrics
```

---

## 🗂️ App Pages

| Page | What it shows |
|------|--------------|
| 🏠 Home | Key metrics, attrition overview |
| 📊 EDA & Insights | Interactive charts, business insights |
| 🤖 Model Performance | ROC curves, confusion matrix, SHAP |
| 🔮 Predict | Upload CSV → get risk scores + cost analysis |

---

## 🤖 ML Pipeline

- **Data**: IBM HR Analytics (1,470 records, 35 features)
- **Balancing**: SMOTE for class imbalance
- **Models**: Logistic Regression → Random Forest → XGBoost
- **Explainability**: SHAP feature importance
- **Best Model**: XGBoost

---

## 📝 Resume Summary

> Built an end-to-end Employee Attrition Predictor using XGBoost on IBM HR data, with SHAP-based explainability and an interactive Streamlit dashboard showing attrition risk scores, department heatmaps, key churn drivers, and a business turnover cost calculator — enabling data-driven HR retention strategies.

---

## 🛠️ Tech Stack

Python • XGBoost • Scikit-learn • SHAP • Streamlit • Plotly • Pandas • imbalanced-learn

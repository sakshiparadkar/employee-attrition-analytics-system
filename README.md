<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=32&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Employee+Attrition+Predictor;HR+Intelligence+Platform;End-to-End+ML+Project" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge&logo=xgboost&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

<br/>


---

## 🧠 About the Project

Employee attrition costs companies **50–200% of an employee's annual salary** per departure — yet most HR teams only find out someone is leaving when they hand in their resignation.

I built this project to answer a real business question:

> *"Can we predict who is likely to quit — and why — early enough to actually do something about it?"*

This is a **complete, end-to-end machine learning project** — from raw data and EDA all the way to a deployed web application with SHAP explainability and auto-generated retention recommendations.

**Dataset:** IBM HR Analytics dataset — 1,470 employees, 35 features  
**Model:** XGBoost Classifier (80.95% accuracy, ROC-AUC: 0.82)  
**Interface:** Streamlit with custom dark-mode UI


---

## ✨ Features

✨ Features

📊 Interactive EDA — 12+ charts on who leaves and why
🏆 Model Benchmarking — Logistic Regression vs Random Forest vs XGBoost with ROC curves
🔍 SHAP Explainability — understand why someone got flagged as high-risk
🔮 Batch Prediction — upload a CSV, get instant risk scores for everyone
💡 Retention Recommendations — auto-generated action items from the data
📥 Export to CSV — download results and share them
🎨 Custom Dark UI — built with Streamlit + CSS, actually looks goo

---

✨ What it does

📊 EDA Dashboard — 12+ interactive charts exploring who leaves and why
🏆 Model Comparison — Logistic Regression vs Random Forest vs XGBoost, head-to-head
🔍 SHAP Explainability — not just what the model predicted, but why
🔮 Batch Predictions — upload a CSV, get risk scores for everyone instantly
💡 Retention Recommendations — auto-generated action items based on the data
📥 Export to CSV — download results and share with your team

---

## 🛠 Tech Stack

Language: Python 3.10+

ML: XGBoost · Random Forest · Logistic Regression · Scikit-learn · SHAP

Data & Viz: Pandas · NumPy · Plotly

App: Streamlit · Custom CSS (dark mode) · Joblib

---

## 📁 Project Structure

```
employee-attrition-predictor/
│
├── app.py                      # Main Streamlit application
├── train_model.py              # Model training script
├── requirements.txt
├── README.md
│
├── data/
│   ├── hr_data.csv             # IBM HR Analytics dataset
│   ├── generate_data.py        # Sample data generator
│   ├── single_employee_1.csv   # Test profiles
│   └── single_employee_2.csv
│
└── models/
    ├── xgb_model.pkl           # Trained XGBoost model
    ├── encoders.pkl            # LabelEncoders for categorical cols
    ├── scaler.pkl              # StandardScaler
    ├── feature_cols.pkl        # Feature column list
    ├── feature_names.pkl       # Human-readable feature names
    └── results.json            # Model evaluation metrics
```

---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/employee-attrition-predictor.git
cd employee-attrition-predictor
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the model
```bash
python train_model.py
```
> This generates all `.pkl` files and `results.json` inside the `models/` folder.

### 5. Run the app
```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

### 📋 Requirements

```
streamlit
pandas
numpy
plotly
scikit-learn
xgboost
shap
joblib
```

---

## 📊 Results

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | 88.1% | 0.76 |
| Random Forest | 85.7% | 0.79 |
| **XGBoost** ✅ | **80.95%** | **0.82** |

> XGBoost was selected for its superior ROC-AUC score, which matters more than raw accuracy on this imbalanced dataset (84% stayed, 16% left).



---

## 💡 What I Learned

Building this project taught me things no tutorial ever covered cleanly:

- **Class imbalance is real** — accuracy alone is a misleading metric when only 16% of your data is "Yes". ROC-AUC is far more honest.
- **SHAP changed how I think about ML** — getting a prediction is step one. Explaining *why* the model made it is what makes it actually useful in the real world.
- **Feature engineering matters more than model choice** — choosing the right 27 features beat throwing all 35 at every model.
- **The UI is part of the product** — a model nobody wants to use doesn't solve any problems. Streamlit with custom CSS made this something I'd actually show to a non-technical audience.
- **End-to-end means the full loop** — data → training → evaluation → serialization → deployment → inference → output. I can now trace every step.

---

## 🙋 Author

**[SAKSHI PARADKAR]**  
MSc COMPUTER SCIENCE STUDENT 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:youremail@gmail.com)

---

<div align="center">

**If this project helped you or gave you ideas, a ⭐ on the repo means a lot!**

*Built with curiosity, a lot of Plotly docs, and way too many hours of debugging SHAP.*

</div>

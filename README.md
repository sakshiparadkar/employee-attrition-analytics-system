<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=32&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Employee+Attrition+Predictor;HR+Intelligence+Platform;End-to-End+ML+Project" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge&logo=xgboost&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

<br/>

> **Predict which employees are about to quit — before they actually do.**  
> A production-grade ML web app that turns raw HR data into instant attrition risk scores, visual insights, and data-driven retention strategies.

<br/>

![App Screenshot Placeholder](https://via.placeholder.com/900x450/0a0d14/6366f1?text=Employee+Attrition+Predictor+%E2%80%94+Live+Demo)

<br/>

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit_Cloud-FF4B4B?style=for-the-badge)](https://your-app-link.streamlit.app)
[![Dataset](https://img.shields.io/badge/📦_Dataset-IBM_HR_Analytics-0052CC?style=for-the-badge)](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

</div>

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Live Demo](#-live-demo)
- [Features](#-features)
- [App Pages](#-app-pages)
- [ML Pipeline](#-ml-pipeline)
- [Charts & Visualizations](#-charts--visualizations)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Results](#-results)
- [What I Learned](#-what-i-learned)
- [Author](#-author)

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

## 🚀 Live Demo

👉 **[Try the app here](https://your-app-link.streamlit.app)**

No setup needed. You can download a sample CSV directly from the app's Predict page and test it instantly.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📊 **Interactive EDA** | 12+ charts exploring who leaves and why, across demographics, satisfaction, and compensation |
| 🏆 **Model Benchmarking** | Logistic Regression, Random Forest, and XGBoost compared head-to-head with ROC curves |
| 🔍 **SHAP Explainability** | Understand *why* the model flagged an employee as high-risk |
| 🔮 **Batch Prediction** | Upload any employee CSV → get instant risk scores for the whole team |
| 💡 **Retention Recommendations** | Auto-generated, data-driven action items for HR managers |
| 📥 **Report Export** | Download predictions as a CSV for sharing with leadership |
| 🎨 **Production UI** | Custom dark-mode Streamlit interface — looks like a real product |

---

## 📱 App Pages

### 🏠 Home — Executive Dashboard
The landing page gives a full workforce health snapshot in under 60 seconds.
- Overall attrition rate, total churned, avg income, highest-risk department
- Attrition distribution donut chart
- Top 3 attrition drivers with rankings
- "Did You Know?" live-calculated insight (e.g., "Overtime employees are **3.0x** more likely to leave")

---

### 📊 EDA & Insights — 3 Tabs, 12+ Charts

**Demographics Tab**
- Attrition rate by Department, Gender, Job Role, Marital Status
- Age distribution overlaid by attrition

**Satisfaction & Balance Tab**
- Job Satisfaction, Work-Life Balance, and Environment Satisfaction vs. Attrition — as line and bar charts
- Overtime vs. Attrition (the most dramatic visual in the app)
- Distance from Home histogram

**Compensation & Tenure Tab**
- Monthly Income box plot (churned vs. retained)
- Years at Company histogram by attrition
- Attrition rate by experience band (0–2, 3–5, 6–10, 10+ years)
- Feature correlation heatmap

> **Key Business Insights** are auto-generated below the tabs — no manual analysis required.

---

### 🏆 Model Performance — Full ML Evaluation
- Side-by-side model comparison table (Accuracy + ROC-AUC)
- ROC curves for all 3 models on one chart
- XGBoost confusion matrix (True/False Positives & Negatives)
- **SHAP Feature Importance** bar chart — Top 15 features driving predictions

---

### 🔮 Predict — The Operational Core
- Upload a CSV → preprocessing → inference → results in seconds
- Every employee gets a **Risk Score (%)** and a colored badge — 🔴 High / 🟡 Medium / 🟢 Low
- Filter table by risk level
- **Retention Recommendations** auto-generated from the uploaded data:
  - Salary flags, overtime burnout, low satisfaction, poor WLB, new hire risk, dept-level hotspots
- Risk distribution bar chart
- Full report CSV download

---

## 🔧 ML Pipeline

```
Raw CSV
  │
  ▼
Data Cleaning & EDA
  │
  ▼
Feature Engineering
  └─ Label Encoding (7 categorical cols)
  └─ StandardScaler (numeric features)
  └─ 27 final features selected
  │
  ▼
Model Training & Comparison
  └─ Logistic Regression (baseline)
  └─ Random Forest
  └─ XGBoost ← selected (best ROC-AUC)
  │
  ▼
Evaluation
  └─ Accuracy, ROC-AUC, Confusion Matrix
  └─ SHAP TreeExplainer (feature importance)
  │
  ▼
Serialization (joblib)
  └─ xgb_model.pkl
  └─ encoders.pkl
  └─ scaler.pkl
  └─ feature_cols.pkl
  │
  ▼
Streamlit Web App
  └─ Upload → Preprocess → Predict → Recommend → Export
```

---

## 📈 Charts & Visualizations

| Chart | Type | Key Insight |
|---|---|---|
| Attrition Distribution | Donut | 16.1% overall attrition rate |
| Attrition by Department | Bar | Sales has highest attrition |
| Age Distribution by Attrition | Histogram | 25–35 age band is highest risk |
| Job Satisfaction vs Attrition | Line | Score 1 employees churn most |
| Overtime vs Attrition | Bar | Overtime → ~3x higher churn |
| Monthly Income vs Attrition | Box Plot | Churned employees earn less |
| Years at Company by Attrition | Histogram | Most churn in first 3 years |
| Experience Band Attrition | Bar | Freshers (0–2 yrs) highest risk |
| ROC Curves | Line (multi) | XGBoost AUC = 0.82 |
| Confusion Matrix | Heatmap | TP/TN/FP/FN breakdown |
| SHAP Feature Importance | Horizontal Bar | OverTime is #1 driver |
| Correlation Heatmap | Matrix | Feature relationship analysis |

---

## 🛠 Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.10+ |
| Web Framework | Streamlit |
| ML Models | XGBoost, Random Forest, Logistic Regression |
| ML Utilities | Scikit-learn (encoding, scaling, metrics) |
| Explainability | SHAP |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly Express, Plotly Graph Objects |
| Serialization | Joblib |
| Styling | Custom CSS (dark mode) |

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

**Top 5 Attrition Drivers (SHAP):**
1. OverTime
2. MonthlyIncome
3. Age
4. JobSatisfaction
5. YearsAtCompany

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

**[Your Name]**  
B.Tech / B.Sc [Your Branch] | [Your College Name]

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:youremail@gmail.com)

---

<div align="center">

**If this project helped you or gave you ideas, a ⭐ on the repo means a lot!**

*Built with curiosity, a lot of Plotly docs, and way too many hours of debugging SHAP.*

</div>

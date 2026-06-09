<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=700&size=32&pause=1000&color=6366F1&center=true&vCenter=true&width=600&lines=Employee+Attrition+Predictor;HR+Intelligence+Platform;End-to-End+ML+Project" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-189AB4?style=for-the-badge&logo=xgboost&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

> Predict which employees are about to quit — before they actually do.

</div>

---
🔗 **Live Application:** https://employee-attrition-analytics-system-2tzhtnn9bzhwno5pbvcugi.streamlit.app/

## 🧠 What's this about?

I wanted to answer one question: *can you actually predict when someone's going to quit their job before they do?*

Turns out — yes, pretty well. This is my end-to-end ML project using the IBM HR Analytics dataset (1,470 employees, 35 features). I built the whole thing from scratch — EDA, model training, SHAP explainability, and a Streamlit web app with a custom dark UI.

**Dataset:** IBM HR Analytics — 1,470 employees, 35 features

**Model:** XGBoost (80.95% accuracy, ROC-AUC: 0.82)

**Interface:** Streamlit + custom dark-mode CSS


---

## ✨ Features

- 📊 **Interactive EDA** — 12+ charts on who leaves and why
- 🏆 **Model Benchmarking** — LR vs RF vs XGBoost, head-to-head with ROC curves
- 🔍 **SHAP Explainability** — not just *what* the model predicted, but *why*
- 🔮 **Batch Prediction** — upload a CSV, get risk scores for everyone instantly
- 💡 **Retention Recommendations** — auto-generated action items from the data
- 📥 **Export to CSV** — download results and share them
- 🎨 **Custom Dark UI** — Streamlit + CSS, actually looks good

---

## 📱 App Pages

**🏠 Home** — attrition rate, avg income, highest-risk dept, top 3 drivers, and a live "did you know?" stat (e.g. overtime employees are 3x more likely to leave)

**📊 EDA** — 3 tabs covering demographics, satisfaction & work-life balance, and compensation & tenure. Key insights auto-generated below.

**🏆 Model Performance** — side-by-side accuracy + ROC-AUC, confusion matrix, and SHAP feature importance for top 15 features

**🔮 Predict** — upload CSV → get risk scores with 🔴 High / 🟡 Medium / 🟢 Low badges, retention recommendations, and a downloadable report

---

## 📸 Screenshots

### 🏠 Home
![Home](https://raw.githubusercontent.com/sakshiparadkar/employee-attrition-analytics-system/main/attrition_system_screenshots/home.png)

### 📊 EDA
![EDA](https://raw.githubusercontent.com/sakshiparadkar/employee-attrition-analytics-system/main/attrition_system_screenshots/eda.png)

### 🏆 Model Performance
![Model Performance](https://raw.githubusercontent.com/sakshiparadkar/employee-attrition-analytics-system/main/attrition_system_screenshots/Model_performance.png)

### 🔮 Predict
![Predict](https://raw.githubusercontent.com/sakshiparadkar/employee-attrition-analytics-system/main/attrition_system_screenshots/predict.png)

### ✅ Prediction Result
![Prediction Result](https://raw.githubusercontent.com/sakshiparadkar/employee-attrition-analytics-system/main/attrition_system_screenshots/prediction_result.png)

## 📄 Business Analyst Documentation

Apart from the ML side, I also created proper BA docs for this project — something I wanted to practice alongside the technical stuff.

| # | Document |
|---|---|
| 0 | Business Case Document |
| 1 | Business Requirements Document |
| 2 | Data Dictionary |
| 3 | EDA & Insights Report |
| 4 | Project One-Pager |
| 5 | User Story Document |

---

## 📊 Results

| Model | Accuracy | ROC-AUC |
|---|---|---|
| Logistic Regression | 88.1% | 0.76 |
| Random Forest | 85.7% | 0.79 |
| **XGBoost** ✅ | **80.95%** | **0.82** |

> Raw accuracy is misleading on imbalanced data (84% stayed, 16% left) — ROC-AUC is the metric that actually matters here.

**Top 5 drivers (SHAP):** OverTime → MonthlyIncome → Age → JobSatisfaction → YearsAtCompany

---

## 🛠 Tech Stack

**Language:** Python 3.10+

**ML:** XGBoost · Random Forest · Logistic Regression · Scikit-learn · SHAP

**Data & Viz:** Pandas · NumPy · Plotly

**App:** Streamlit · Custom CSS (dark mode) · Joblib

---

## 📁 Project Structure

```bash
employee-attrition-predictor/
├── app.py                  # Streamlit app
├── train_model.py          # Model training
├── requirements.txt
├── data/
│   ├── hr_data.csv
│   └── generate_data.py
└── models/
├── xgb_model.pkl
├── encoders.pkl
├── scaler.pkl
└── results.json
```
---

## ⚡ Run it locally

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

## 💡 What I actually learned

- **Accuracy is a trap** on imbalanced data — ROC-AUC tells the real story
- **SHAP changed how I think about ML** — a prediction without an explanation isn't very useful
- **Feature selection > model choice** — the right 27 features beat throwing all 35 at every model
- **The UI is part of the project** — a model nobody wants to use doesn't help anyone
- **End-to-end is a real skill** — data → training → serialization → deployment → inference, I can trace every step now

---

## 🙋 Author

SAKSHI PARADKAR — MSc COMPUTER SCIENCE

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:youremail@gmail.com)

---

<div align="center">

*Built with curiosity, a lot of Plotly docs, and way too many hours debugging SHAP.*

⭐ If this helped you or gave you ideas, a star means a lot!

</div>

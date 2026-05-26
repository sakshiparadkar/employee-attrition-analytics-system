import pandas as pd
import numpy as np
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (roc_auc_score, accuracy_score,
                              classification_report, confusion_matrix, roc_curve)
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.generate_data import generate_hr_data


CATEGORICAL_COLS = [
    "BusinessTravel", "Department", "EducationField",
    "Gender", "JobRole", "MaritalStatus", "OverTime"
]

FEATURE_COLS = [
    "Age", "BusinessTravel", "Department", "DistanceFromHome", "Education",
    "EducationField", "EnvironmentSatisfaction", "Gender", "JobInvolvement",
    "JobLevel", "JobRole", "JobSatisfaction", "MaritalStatus", "MonthlyIncome",
    "NumCompaniesWorked", "OverTime", "PercentSalaryHike", "PerformanceRating",
    "RelationshipSatisfaction", "StockOptionLevel", "TotalWorkingYears",
    "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany",
    "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager"
]


def preprocess(df, encoders=None, scaler=None, fit=True):
    df = df.copy()
    if encoders is None:
        encoders = {}
    for col in CATEGORICAL_COLS:
        if col not in df.columns:
            continue
        if fit:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            encoders[col] = le
        else:
            le = encoders[col]
            df[col] = df[col].astype(str).map(
                lambda x, le=le: le.transform([x])[0]
                if x in le.classes_ else 0
            )
    X = df[[c for c in FEATURE_COLS if c in df.columns]]
    if fit:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
    else:
        X_scaled = scaler.transform(X)
    return X_scaled, encoders, scaler


def train():
    print("📊 Generating data...")
    df = generate_hr_data()
    df.to_csv("data/hr_data.csv", index=False)

    y = (df["Attrition"] == "Yes").astype(int)
    X_scaled, encoders, scaler = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    sm = SMOTE(random_state=42)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "XGBoost": XGBClassifier(n_estimators=100, random_state=42,
                                  use_label_encoder=False, eval_metric="logloss")
    }

    results = {}
    print("\n🤖 Training models...")
    for name, model in models.items():
        model.fit(X_train_res, y_train_res)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        results[name] = {
            "accuracy": round(accuracy_score(y_test, y_pred) * 100, 2),
            "roc_auc": round(roc_auc_score(y_test, y_prob), 4),
            "fpr": fpr.tolist(),
            "tpr": tpr.tolist(),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist()
        }
        print(f"  ✅ {name}: ACC={results[name]['accuracy']}%  AUC={results[name]['roc_auc']}")

    # Save best model (XGBoost)
    best_model = models["XGBoost"]
    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, "models/xgb_model.pkl")
    joblib.dump(encoders, "models/encoders.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(FEATURE_COLS, "models/feature_cols.pkl")

    with open("models/results.json", "w") as f:
        json.dump(results, f)

    # Save feature names for SHAP
    feature_names = [c for c in FEATURE_COLS if c in df.columns]
    joblib.dump(feature_names, "models/feature_names.pkl")

    print("\n✅ All models saved to models/")
    return results


if __name__ == "__main__":
    train()

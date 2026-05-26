import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import json
import shap
import os
import sys

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0f1117; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1f2e 0%, #0f1117 100%);
        border-right: 1px solid #2d3748;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #1a1f2e, #252d3d);
        border: 1px solid #2d3748;
        border-radius: 12px;
        padding: 20px 24px;
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover { transform: translateY(-2px); }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 700;
        margin: 8px 0 4px;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #8892a4;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Risk badges */
    .badge-high {
        background: rgba(239,68,68,0.15);
        color: #f87171;
        border: 1px solid rgba(239,68,68,0.3);
        border-radius: 20px; padding: 3px 12px; font-size: 0.8rem; font-weight: 600;
    }
    .badge-medium {
        background: rgba(245,158,11,0.15);
        color: #fbbf24;
        border: 1px solid rgba(245,158,11,0.3);
        border-radius: 20px; padding: 3px 12px; font-size: 0.8rem; font-weight: 600;
    }
    .badge-low {
        background: rgba(16,185,129,0.15);
        color: #34d399;
        border: 1px solid rgba(16,185,129,0.3);
        border-radius: 20px; padding: 3px 12px; font-size: 0.8rem; font-weight: 600;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.3rem; font-weight: 700;
        color: #e2e8f0;
        margin: 24px 0 16px;
        padding-bottom: 8px;
        border-bottom: 2px solid #3b82f6;
        display: inline-block;
    }
    
    /* Info box */
    .info-box {
        background: rgba(59,130,246,0.1);
        border: 1px solid rgba(59,130,246,0.3);
        border-radius: 10px;
        padding: 14px 18px;
        margin: 12px 0;
    }
    
    /* Cost box */
    .cost-box {
        background: linear-gradient(135deg, rgba(239,68,68,0.1), rgba(239,68,68,0.05));
        border: 1px solid rgba(239,68,68,0.3);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
    
    /* Hide default streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Plotly chart backgrounds */
    .js-plotly-plot { border-radius: 12px; overflow: hidden; }
</style>
""", unsafe_allow_html=True)

CHART_THEME = {
    "paper_bgcolor": "#1a1f2e",
    "plot_bgcolor": "#1a1f2e",
    "font_color": "#e2e8f0",
    "gridcolor": "#2d3748",
    "colors": ["#3b82f6", "#f87171", "#34d399", "#fbbf24", "#a78bfa", "#fb923c"]
}

# ─── Load Assets ────────────────────────────────────────────────────────────
@st.cache_resource
def load_model_assets():
    model = joblib.load("models/xgb_model.pkl")
    encoders = joblib.load("models/encoders.pkl")
    scaler = joblib.load("models/scaler.pkl")
    feature_cols = joblib.load("models/feature_cols.pkl")
    feature_names = joblib.load("models/feature_names.pkl")
    with open("models/results.json") as f:
        results = json.load(f)
    return model, encoders, scaler, feature_cols, feature_names, results


@st.cache_data
def load_data():
    return pd.read_csv("data/hr_data.csv")


# Preprocess for prediction
CATEGORICAL_COLS = [
    "BusinessTravel", "Department", "EducationField",
    "Gender", "JobRole", "MaritalStatus", "OverTime"
]

def preprocess_input(df, encoders, scaler, feature_cols):
    df = df.copy()
    for col in CATEGORICAL_COLS:
        if col not in df.columns:
            continue
        le = encoders[col]
        df[col] = df[col].astype(str).map(
            lambda x, le=le: le.transform([x])[0] if x in le.classes_ else 0
        )
    X = df[[c for c in feature_cols if c in df.columns]]
    return scaler.transform(X)


# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 20px 0 10px;'>
            <div style='font-size:2.5rem;'>👥</div>
            <div style='font-size:1.1rem; font-weight:700; color:#e2e8f0; margin-top:8px;'>
                Attrition Predictor
            </div>
            <div style='font-size:0.75rem; color:#8892a4; margin-top:4px;'>
                HR Intelligence Platform
            </div>
        </div>
        <hr style='border-color:#2d3748; margin: 16px 0;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["🏠  Home", "📊  EDA & Insights", "🤖  Model Performance", "🔮  Predict Attrition"],
        label_visibility="collapsed"
    )

    st.markdown("""
        <hr style='border-color:#2d3748; margin: 16px 0;'>
        <div style='font-size:0.75rem; color:#8892a4; text-align:center; padding-bottom:10px;'>
            Model: XGBoost &nbsp;|&nbsp; Dataset: IBM HR
        </div>
    """, unsafe_allow_html=True)


# ─── Load ───────────────────────────────────────────────────────────────────
try:
    model, encoders, scaler, feature_cols, feature_names, results = load_model_assets()
    df = load_data()
except Exception as e:
    st.error(f"⚠️ Could not load model. Run `python train_model.py` first.\n\n{e}")
    st.stop()


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — HOME
# ══════════════════════════════════════════════════════════════════════════════
if "Home" in page:
    st.markdown("<h1 style='color:#e2e8f0; margin-bottom:4px;'>Employee Attrition Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892a4; font-size:1rem; margin-bottom:32px;'>Identify at-risk employees early. Retain talent. Reduce costs.</p>", unsafe_allow_html=True)

    attrition_rate = (df["Attrition"] == "Yes").mean()
    avg_income = df["MonthlyIncome"].mean()
    high_risk = (df["Attrition"] == "Yes").sum()
    dept_most = df[df["Attrition"] == "Yes"]["Department"].value_counts().idxmax()

    c1, c2, c3, c4 = st.columns(4)
    cards = [
        (c1, f"{attrition_rate:.1%}", "Overall Attrition Rate", "#f87171"),
        (c2, f"{high_risk}", "Employees Churned", "#fbbf24"),
        (c3, f"₹{avg_income:,.0f}", "Avg Monthly Income", "#34d399"),
        (c4, dept_most.split(" ")[0], "Highest Attrition Dept", "#a78bfa"),
    ]
    for col, val, label, color in cards:
        col.markdown(f"""
            <div class='metric-card'>
                <div class='metric-value' style='color:{color}'>{val}</div>
                <div class='metric-label'>{label}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, 1])

    with c1:
        st.markdown("<div class='section-header'>What This App Does</div>", unsafe_allow_html=True)
        features = [
            ("📊", "EDA & Insights", "Visual analysis of who's leaving and why"),
            ("🤖", "ML Model", "XGBoost trained on 1,470 employee records"),
            ("🔮", "Predict", "Upload employee data → get attrition risk scores"),
            ("💸", "Cost Analysis", "Estimate turnover cost impact on the business"),
        ]
        for icon, title, desc in features:
            st.markdown(f"""
                <div class='info-box'>
                    <span style='font-size:1.2rem;'>{icon}</span>
                    <strong style='color:#e2e8f0; margin-left:8px;'>{title}</strong>
                    <br><span style='color:#8892a4; font-size:0.85rem; margin-left:28px;'>{desc}</span>
                </div>
            """, unsafe_allow_html=True)

    with c2:
        att_counts = df["Attrition"].value_counts()
        fig = go.Figure(go.Pie(
            labels=["Stayed", "Left"],
            values=[att_counts.get("No", 0), att_counts.get("Yes", 0)],
            hole=0.65,
            marker_colors=["#3b82f6", "#f87171"],
            textinfo="percent",
            textfont_size=14,
        ))
        fig.update_layout(
            paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
            font_color="#e2e8f0",
            showlegend=True,
            legend=dict(orientation="h", y=-0.05),
            margin=dict(t=30, b=10, l=10, r=10),
            title=dict(text="Attrition Distribution", font_size=15, x=0.5)
        )
        fig.add_annotation(text=f"{attrition_rate:.1%}<br><span style='font-size:10px'>Attrition</span>",
                          x=0.5, y=0.5, showarrow=False,
                          font=dict(size=20, color="#f87171"))
        st.plotly_chart(fig, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — EDA & INSIGHTS
# ══════════════════════════════════════════════════════════════════════════════
elif "EDA" in page:
    st.markdown("<h1 style='color:#e2e8f0;'>📊 EDA & Business Insights</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892a4;'>Explore patterns in the HR data — who's leaving and what's driving it.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Row 1
    c1, c2 = st.columns(2)
    with c1:
        dept_att = df.groupby("Department")["Attrition"].apply(
            lambda x: (x == "Yes").mean() * 100
        ).reset_index()
        dept_att.columns = ["Department", "Attrition Rate (%)"]
        fig = px.bar(dept_att, x="Department", y="Attrition Rate (%)",
                     color="Attrition Rate (%)", color_continuous_scale="Reds",
                     title="Attrition Rate by Department")
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0", showlegend=False,
                         coloraxis_showscale=False,
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        ot_att = df.groupby("OverTime")["Attrition"].apply(
            lambda x: (x == "Yes").mean() * 100
        ).reset_index()
        ot_att.columns = ["OverTime", "Attrition Rate (%)"]
        fig = px.bar(ot_att, x="OverTime", y="Attrition Rate (%)",
                     color="OverTime", color_discrete_map={"Yes": "#f87171", "No": "#34d399"},
                     title="Overtime vs Attrition Rate")
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0", showlegend=False,
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"))
        st.plotly_chart(fig, use_container_width=True)

    # Row 2
    c1, c2 = st.columns(2)
    with c1:
        fig = px.box(df, x="Attrition", y="MonthlyIncome",
                     color="Attrition", color_discrete_map={"Yes": "#f87171", "No": "#3b82f6"},
                     title="Monthly Income vs Attrition",
                     labels={"MonthlyIncome": "Monthly Income (₹)"})
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0", showlegend=False,
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        sat_att = df.groupby("JobSatisfaction")["Attrition"].apply(
            lambda x: (x == "Yes").mean() * 100
        ).reset_index()
        sat_att.columns = ["Job Satisfaction", "Attrition Rate (%)"]
        sat_att["Label"] = sat_att["Job Satisfaction"].map(
            {1: "1 - Low", 2: "2 - Medium", 3: "3 - High", 4: "4 - Very High"}
        )
        fig = px.line(sat_att, x="Label", y="Attrition Rate (%)",
                      markers=True, title="Job Satisfaction vs Attrition",
                      color_discrete_sequence=["#3b82f6"])
        fig.update_traces(marker_size=10, line_width=3)
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0",
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"))
        st.plotly_chart(fig, use_container_width=True)

    # Row 3
    c1, c2 = st.columns(2)
    with c1:
        fig = px.histogram(df, x="Age", color="Attrition",
                           color_discrete_map={"Yes": "#f87171", "No": "#3b82f6"},
                           barmode="overlay", opacity=0.7,
                           title="Age Distribution by Attrition",
                           nbins=20)
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0",
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"),
                         legend=dict(title="Attrition"))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        wlb_att = df.groupby("WorkLifeBalance")["Attrition"].apply(
            lambda x: (x == "Yes").mean() * 100
        ).reset_index()
        wlb_att.columns = ["Work-Life Balance", "Attrition Rate (%)"]
        wlb_att["Label"] = wlb_att["Work-Life Balance"].map(
            {1: "1 - Bad", 2: "2 - Good", 3: "3 - Better", 4: "4 - Best"}
        )
        fig = px.bar(wlb_att, x="Label", y="Attrition Rate (%)",
                     color="Attrition Rate (%)", color_continuous_scale="RdYlGn_r",
                     title="Work-Life Balance vs Attrition")
        fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                         font_color="#e2e8f0", showlegend=False,
                         coloraxis_showscale=False,
                         xaxis=dict(gridcolor="#2d3748"),
                         yaxis=dict(gridcolor="#2d3748"))
        st.plotly_chart(fig, use_container_width=True)

    # Row 4 — Heatmap
    st.markdown("<div class='section-header'>Correlation Heatmap</div>", unsafe_allow_html=True)
    num_cols = ["Age", "MonthlyIncome", "YearsAtCompany", "JobSatisfaction",
                "WorkLifeBalance", "EnvironmentSatisfaction", "DistanceFromHome",
                "TotalWorkingYears", "NumCompaniesWorked"]
    corr = df[num_cols].corr().round(2)
    fig = px.imshow(corr, color_continuous_scale="RdBu_r", zmin=-1, zmax=1,
                    text_auto=True, aspect="auto",
                    title="Feature Correlation Matrix")
    fig.update_layout(paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                     font_color="#e2e8f0", height=420,
                     margin=dict(t=50))
    st.plotly_chart(fig, use_container_width=True)

    # Key Insights Box
    st.markdown("<div class='section-header'>🔍 Key Business Insights</div>", unsafe_allow_html=True)
    ot_rate = df[df["OverTime"] == "Yes"]["Attrition"].apply(lambda x: x == "Yes").mean()
    no_ot_rate = df[df["OverTime"] == "No"]["Attrition"].apply(lambda x: x == "Yes").mean()
    insights = [
        f"⏰ Employees doing overtime are **{ot_rate/no_ot_rate:.1f}x more likely** to leave than those who don't.",
        f"💰 Employees who left had an average income of ₹{df[df['Attrition']=='Yes']['MonthlyIncome'].mean():,.0f} vs ₹{df[df['Attrition']=='No']['MonthlyIncome'].mean():,.0f} for those who stayed.",
        f"📅 **{(df[df['Attrition']=='Yes']['YearsAtCompany'] < 3).mean():.0%} of churned employees** had less than 3 years of tenure.",
        f"😔 Employees with Job Satisfaction score 1 (Low) have the highest attrition risk.",
    ]
    for insight in insights:
        st.markdown(f"<div class='info-box'>{insight}</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — MODEL PERFORMANCE
# ══════════════════════════════════════════════════════════════════════════════
elif "Model" in page:
    st.markdown("<h1 style='color:#e2e8f0;'>🤖 Model Performance</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892a4;'>Evaluation metrics for all trained models. XGBoost is selected as the final model.</p>", unsafe_allow_html=True)
    st.markdown("---")

    # Model Comparison Table
    st.markdown("<div class='section-header'>Model Comparison</div>", unsafe_allow_html=True)
    compare_df = pd.DataFrame([
        {"Model": name, "Accuracy (%)": v["accuracy"], "ROC-AUC": v["roc_auc"],
         "Status": "✅ Selected" if name == "XGBoost" else ""}
        for name, v in results.items()
    ])
    st.dataframe(
        compare_df.style.highlight_max(subset=["ROC-AUC", "Accuracy (%)"],
                                        color="#1e3a5f"),
        use_container_width=True, hide_index=True
    )

    # ROC Curves + Confusion Matrix
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure()
        colors = ["#3b82f6", "#34d399", "#f87171"]
        for (name, v), color in zip(results.items(), colors):
            fig.add_trace(go.Scatter(
                x=v["fpr"], y=v["tpr"], mode="lines",
                name=f"{name} (AUC={v['roc_auc']})",
                line=dict(width=2.5, color=color)
            ))
        fig.add_trace(go.Scatter(x=[0,1], y=[0,1], mode="lines",
                                  line=dict(dash="dash", color="#4a5568"),
                                  name="Random Baseline", showlegend=True))
        fig.update_layout(
            title="ROC Curves — All Models",
            xaxis_title="False Positive Rate",
            yaxis_title="True Positive Rate",
            paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
            font_color="#e2e8f0",
            xaxis=dict(gridcolor="#2d3748"),
            yaxis=dict(gridcolor="#2d3748"),
            legend=dict(bgcolor="rgba(0,0,0,0)", x=0.4, y=0.1)
        )
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        cm = results["XGBoost"]["confusion_matrix"]
        labels = ["Stayed", "Left"]
        fig = px.imshow(
            cm, x=labels, y=labels,
            color_continuous_scale="Blues",
            text_auto=True,
            title="XGBoost Confusion Matrix",
            labels=dict(x="Predicted", y="Actual")
        )
        fig.update_layout(
            paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
            font_color="#e2e8f0", coloraxis_showscale=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # SHAP Feature Importance
    st.markdown("<div class='section-header'>🔍 SHAP Feature Importance — Why Does the Model Decide?</div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892a4; font-size:0.9rem;'>SHAP shows which features push employees toward or away from attrition.</p>", unsafe_allow_html=True)

    with st.spinner("Calculating SHAP values..."):
        try:
            sample = df.sample(200, random_state=42)
            X_sample_raw = sample.copy()
            for col in CATEGORICAL_COLS:
                if col in X_sample_raw.columns:
                    le = encoders[col]
                    X_sample_raw[col] = X_sample_raw[col].astype(str).map(
                        lambda x, le=le: le.transform([x])[0] if x in le.classes_ else 0
                    )
            X_sample = X_sample_raw[[c for c in feature_cols if c in X_sample_raw.columns]]
            X_scaled = scaler.transform(X_sample)

            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X_scaled)

            mean_shap = np.abs(shap_values).mean(axis=0)
            feat_imp = pd.DataFrame({
                "Feature": feature_names,
                "SHAP Importance": mean_shap
            }).sort_values("SHAP Importance", ascending=True).tail(15)

            fig = px.bar(feat_imp, x="SHAP Importance", y="Feature",
                         orientation="h", color="SHAP Importance",
                         color_continuous_scale="Blues",
                         title="Top 15 Features by SHAP Importance")
            fig.update_layout(
                paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                font_color="#e2e8f0", showlegend=False,
                coloraxis_showscale=False, height=500,
                xaxis=dict(gridcolor="#2d3748"),
                yaxis=dict(gridcolor="#2d3748"),
            )
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning(f"SHAP visualization unavailable: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — PREDICT
# ══════════════════════════════════════════════════════════════════════════════
elif "Predict" in page:
    st.markdown("<h1 style='color:#e2e8f0;'>🔮 Predict Employee Attrition</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#8892a4;'>Upload your employee CSV and get instant attrition risk scores.</p>", unsafe_allow_html=True)
    st.markdown("---")

    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.markdown("<div class='section-header'>Upload Employee Data</div>", unsafe_allow_html=True)
        st.markdown("""
            <div class='info-box'>
                📋 Upload a CSV with employee details. Must include columns like Age, Department,
                MonthlyIncome, OverTime, JobSatisfaction, etc.
                <br><br>
                💡 <strong>Don't have a file?</strong> Use the sample file below to try the app.
            </div>
        """, unsafe_allow_html=True)

        # Sample download
        from data.generate_data import generate_sample_upload
        sample_df = generate_sample_upload(20)
        st.download_button(
            "📥 Download Sample CSV",
            data=sample_df.to_csv(index=False),
            file_name="sample_employees.csv",
            mime="text/csv",
            use_container_width=True
        )

        uploaded = st.file_uploader("Upload Employee CSV", type=["csv"],
                                     label_visibility="collapsed")

    with c2:
        st.markdown("<div class='section-header'>Risk Level Guide</div>", unsafe_allow_html=True)
        guide = [
            ("🔴 High Risk", "badge-high", "> 65% chance of leaving. Immediate action needed."),
            ("🟡 Medium Risk", "badge-medium", "35–65% chance. Monitor and engage."),
            ("🟢 Low Risk", "badge-low", "< 35% chance. Employee is stable."),
        ]
        for label, badge, desc in guide:
            st.markdown(f"""
                <div class='info-box'>
                    <span class='{badge}'>{label}</span>
                    <br><span style='color:#8892a4; font-size:0.85rem; margin-top:6px; display:block;'>{desc}</span>
                </div>
            """, unsafe_allow_html=True)

    if uploaded:
        input_df = pd.read_csv(uploaded)
        id_col = "EmployeeID" if "EmployeeID" in input_df.columns else None
        name_col = "EmployeeName" if "EmployeeName" in input_df.columns else None

        meta_cols = [c for c in [id_col, name_col] if c]
        meta = input_df[meta_cols].copy() if meta_cols else pd.DataFrame()
        proc_df = input_df.drop(columns=meta_cols, errors="ignore")

        try:
            X = preprocess_input(proc_df, encoders, scaler, feature_cols)
            probs = model.predict_proba(X)[:, 1]

            def risk_label(p):
                if p >= 0.65: return "🔴 High", "badge-high"
                elif p >= 0.35: return "🟡 Medium", "badge-medium"
                else: return "🟢 Low", "badge-low"

            results_df = meta.copy() if not meta.empty else pd.DataFrame()
            results_df["Risk Score (%)"] = (probs * 100).round(1)
            results_df["Risk Level"] = [risk_label(p)[0] for p in probs]

            # Add key input cols for context
            for col in ["Department", "MonthlyIncome", "OverTime", "JobSatisfaction"]:
                if col in input_df.columns:
                    results_df[col] = input_df[col].values

            st.markdown("---")
            st.markdown("<div class='section-header'>📋 Prediction Results</div>", unsafe_allow_html=True)

            # Summary metrics
            high = (probs >= 0.65).sum()
            med = ((probs >= 0.35) & (probs < 0.65)).sum()
            low = (probs < 0.35).sum()
            total = len(probs)

            m1, m2, m3, m4 = st.columns(4)
            m1.markdown(f"<div class='metric-card'><div class='metric-value' style='color:#e2e8f0'>{total}</div><div class='metric-label'>Total Employees</div></div>", unsafe_allow_html=True)
            m2.markdown(f"<div class='metric-card'><div class='metric-value' style='color:#f87171'>{high}</div><div class='metric-label'>High Risk</div></div>", unsafe_allow_html=True)
            m3.markdown(f"<div class='metric-card'><div class='metric-value' style='color:#fbbf24'>{med}</div><div class='metric-label'>Medium Risk</div></div>", unsafe_allow_html=True)
            m4.markdown(f"<div class='metric-card'><div class='metric-value' style='color:#34d399'>{low}</div><div class='metric-label'>Low Risk</div></div>", unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Filter
            filter_risk = st.selectbox("Filter by Risk Level", ["All", "🔴 High", "🟡 Medium", "🟢 Low"])
            display_df = results_df.copy()
            if filter_risk != "All":
                display_df = display_df[display_df["Risk Level"] == filter_risk]

            # Style table
            def color_risk(val):
                if "High" in str(val): return "color: #f87171; font-weight: 600"
                elif "Medium" in str(val): return "color: #fbbf24; font-weight: 600"
                elif "Low" in str(val): return "color: #34d399; font-weight: 600"
                return ""

            st.dataframe(
                display_df.style.applymap(color_risk, subset=["Risk Level"]),
                use_container_width=True, hide_index=True, height=350
            )

            # Download predictions
            st.download_button(
                "📥 Download Full Report",
                data=results_df.to_csv(index=False),
                file_name="attrition_predictions.csv",
                mime="text/csv"
            )

            # Cost Calculator
            st.markdown("---")
            st.markdown("<div class='section-header'>💸 Turnover Cost Calculator</div>", unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            with c1:
                avg_salary = st.number_input(
                    "Average Monthly Salary (₹)", min_value=5000,
                    max_value=100000, value=50000, step=1000
                )
                multiplier = st.slider(
                    "Cost multiplier (industry avg: 1.5–2x annual salary)",
                    1.0, 3.0, 1.5, 0.1
                )
            with c2:
                annual = avg_salary * 12
                cost_per_person = annual * multiplier
                total_cost = high * cost_per_person

                st.markdown(f"""
                    <div class='cost-box'>
                        <div style='color:#8892a4; font-size:0.9rem;'>Estimated Turnover Cost</div>
                        <div style='font-size:2.5rem; font-weight:800; color:#f87171; margin:12px 0;'>
                            ₹{total_cost:,.0f}
                        </div>
                        <div style='color:#8892a4; font-size:0.85rem;'>
                            {high} high-risk employees × ₹{cost_per_person:,.0f}/person
                        </div>
                        <div style='color:#fbbf24; font-size:0.85rem; margin-top:8px;'>
                            💡 Retaining even 50% saves ₹{total_cost/2:,.0f}
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            # Risk Breakdown Chart
            st.markdown("<br>", unsafe_allow_html=True)
            risk_data = pd.DataFrame({
                "Risk": ["🔴 High", "🟡 Medium", "🟢 Low"],
                "Count": [high, med, low],
                "Color": ["#f87171", "#fbbf24", "#34d399"]
            })
            fig = px.bar(risk_data, x="Risk", y="Count",
                         color="Risk",
                         color_discrete_map={"🔴 High": "#f87171",
                                              "🟡 Medium": "#fbbf24",
                                              "🟢 Low": "#34d399"},
                         title="Employee Risk Distribution")
            fig.update_layout(
                paper_bgcolor="#1a1f2e", plot_bgcolor="#1a1f2e",
                font_color="#e2e8f0", showlegend=False,
                xaxis=dict(gridcolor="#2d3748"),
                yaxis=dict(gridcolor="#2d3748")
            )
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"⚠️ Error processing file: {e}\n\nMake sure the CSV has the correct columns.")
    else:
        st.markdown("""
            <div style='text-align:center; padding:60px; color:#4a5568;'>
                <div style='font-size:4rem;'>📂</div>
                <div style='font-size:1.1rem; margin-top:12px;'>Upload a CSV file to get predictions</div>
                <div style='font-size:0.9rem; margin-top:6px;'>or download the sample file above to try it out</div>
            </div>
        """, unsafe_allow_html=True)

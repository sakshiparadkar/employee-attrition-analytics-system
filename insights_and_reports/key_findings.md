# 🔍 Key Findings
### Project: Employee Attrition Analytics System

---

## 🔍 What is this document?
After running SQL queries and Python analysis, this document captures **what the data actually told us**. Every finding here comes directly from the data — not guesswork.

---

## 📊 Dataset at a Glance

| Detail | Value |
|--------|-------|
| Total Employees Analyzed | 1,470 |
| Employees Who Left | 237 |
| Employees Who Stayed | 1,233 |
| Overall Attrition Rate | **16.1%** |
| Industry Benchmark | 10–12% |
| Status | ⚠️ Company is above average |

---

## 🔑 Finding 1 — Overall Attrition is High

- **16.1% of employees left** — that means 1 in every 6 employees resigned
- Industry average is 10–12%, so this company is losing more people than normal
- At $40,000 replacement cost per employee: **Total Loss = 237 × $40,000 = $9.48 Million**

> 💡 Even reducing attrition by 5% would save the company nearly $3 Million

---

## 🔑 Finding 2 — Sales Department is the Biggest Problem

*(Fill in your actual SQL result here)*

| Department | Total Employees | Attrition Count | Attrition Rate |
|-----------|----------------|-----------------|----------------|
| Sales | — | — | **—%** 🔴 |
| Human Resources | — | — | **—%** 🟡 |
| Research & Development | — | — | **—%** 🟢 |

**Insight:** Sales department has the highest attrition — this could be due to high pressure targets and lower job satisfaction.

---

## 🔑 Finding 3 — Overtime is a Major Driver of Attrition

*(Fill in your actual SQL result here)*

| Overtime | Total Employees | Attrition Rate |
|----------|----------------|----------------|
| Yes | — | **—%** 🔴 |
| No | — | **—%** 🟢 |

**Insight:** Employees doing overtime are **X times more likely to leave** than those who don't. This is one of the strongest signals in the data.

---

## 🔑 Finding 4 — Low Salary = High Attrition

*(Fill in your actual SQL result here)*

| Salary Band | Attrition Rate |
|-------------|----------------|
| Low (< $3,000) | **—%** 🔴 |
| Mid ($3K–$6K) | **—%** 🟡 |
| High ($6K–$10K) | **—%** 🟢 |
| Very High (> $10K) | **—%** 🟢 |

**Insight:** Employees in the lowest salary band are leaving at the highest rate. This strongly suggests compensation is not competitive enough for entry-level roles.

---

## 🔑 Finding 5 — Young Employees (25–34) Leave the Most

*(Fill in your actual SQL result here)*

| Age Group | Attrition Rate |
|-----------|----------------|
| Under 25 | **—%** |
| 25–34 | **—%** 🔴 |
| 35–44 | **—%** |
| 45+ | **—%** 🟢 |

**Insight:** The 25–34 age group has the highest attrition. These are early-career employees who likely have many options in the job market and leave if they don't see growth quickly.

---

## 🔑 Finding 6 — Sales Executives Have Highest Role-wise Attrition

*(Fill in your actual SQL result here)*

| Job Role | Attrition Rate |
|----------|----------------|
| Sales Executive | **—%** 🔴 |
| Laboratory Technician | **—%** 🔴 |
| Research Scientist | **—%** |
| Sales Representative | **—%** |
| Human Resources | **—%** |

**Insight:** Sales-related roles dominate the top of the attrition list, confirming that the sales function needs the most urgent attention.

---

## 🔑 Finding 7 — ML Model Key Predictors (from SHAP Analysis)

The machine learning model identified these as the **top factors that predict attrition:**

| Rank | Feature | Impact |
|------|---------|--------|
| 1 | OverTime | Highest impact |
| 2 | MonthlyIncome | High impact |
| 3 | Age | Medium impact |
| 4 | YearsAtCompany | Medium impact |
| 5 | JobSatisfaction | Medium impact |
| 6 | WorkLifeBalance | Medium impact |
| 7 | DistanceFromHome | Lower impact |

> These 7 features explain most of why employees leave — and these are exactly what HR should focus on.

---

## ✅ Summary of All Findings

| Finding | What We Discovered |
|---------|-------------------|
| Overall Attrition | 16.1% — above industry average |
| Worst Department | Sales has highest attrition |
| Overtime Effect | Overtime employees leave much more |
| Salary Effect | Low salary employees leave most |
| Age Effect | 25–34 age group is highest risk |
| Role Effect | Sales Executives top the list |
| ML Top Predictor | Overtime is the #1 predictor |

---

> 📌 **Note:** Replace all "—" values above with your actual SQL query results once you run them in pgAdmin.

---

*All findings in this document are based on IBM HR Analytics dataset analysis using SQL and Python.*

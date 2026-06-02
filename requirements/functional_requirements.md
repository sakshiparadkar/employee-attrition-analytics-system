# ⚙️ Functional Requirements
### Project: Employee Attrition Analytics System

---

## 🔍 What are Functional Requirements?
Functional requirements describe **what the system should do** — like a checklist of features.

Think of it like ordering food:
- "I want a burger with cheese, no onions, extra sauce"
- That's your requirement — the kitchen (developer) follows it exactly

---

## 1. 📊 Dashboard Requirements (Power BI)

### FR-01 — Overall Attrition KPIs
**What it should do:**
The dashboard must show these 4 numbers at the top of Page 1:
- Total Employees
- Total Attrition Count
- Attrition Rate (%)
- Average Monthly Salary

**Why:** HR Head needs these numbers at a glance every morning

---

### FR-02 — Department-wise Attrition
**What it should do:**
Show a bar chart comparing attrition % across all departments:
- Sales
- Research & Development
- Human Resources

**Why:** HR needs to know which department needs most attention

---

### FR-03 — Overtime Impact View
**What it should do:**
Show a comparison between:
- Employees who do overtime → their attrition rate
- Employees who don't do overtime → their attrition rate

**Why:** If overtime is causing attrition, company should fix that first

---

### FR-04 — Salary vs Attrition
**What it should do:**
Group employees into salary bands and show attrition for each:
- Low (< $3,000)
- Mid ($3,000 – $6,000)
- High ($6,000 – $10,000)
- Very High (> $10,000)

**Why:** Helps HR decide if salary revision is needed

---

### FR-05 — Age Group Attrition
**What it should do:**
Show which age group has the most attrition:
- Under 25
- 25–34
- 35–44
- 45+

**Why:** Younger employees leaving = future talent pipeline at risk

---

### FR-06 — Job Role Attrition
**What it should do:**
Rank all job roles from highest to lowest attrition rate

**Why:** HR can target retention programs for specific roles

---

## 2. 🤖 ML Model Requirements

### FR-07 — Attrition Prediction
**What it should do:**
- Take employee details as input
- Output: Will this employee leave? Yes or No
- Also give a risk score: High / Medium / Low

**Why:** HR can proactively reach out to at-risk employees before they resign

---

### FR-08 — Explainability (SHAP)
**What it should do:**
For every prediction, show the top 3 reasons:

Example:
```
Employee E1042 — HIGH RISK
Reason 1: Works overtime (biggest factor)
Reason 2: Salary below market rate
Reason 3: No promotion in 3 years
```

**Why:** HR Manager needs to know WHY so they can take the right action

---

## 3. 🗃️ Data Requirements

### FR-09 — Data Source
- Dataset: IBM HR Analytics (1,470 employees, 35 columns)
- Must be cleaned before analysis (no nulls, correct data types)

### FR-10 — SQL Queries
System must have pre-written SQL queries to answer these business questions:
- Overall attrition rate
- Attrition by department
- Attrition by salary band
- Attrition by overtime status
- Attrition by age group
- Attrition by job role

---

## 4. 🌐 Application Requirements (Streamlit)

### FR-11 — Web App
**What it should do:**
- HR Manager enters employee details in a form
- App shows: Risk Level + Reasons for risk
- Should work in any browser

---

## 5. ✅ Requirements Summary Table

| ID | Requirement | Type | Priority | Status |
|----|-------------|------|----------|--------|
| FR-01 | KPI cards on dashboard | Dashboard | High | ✅ Done |
| FR-02 | Department attrition chart | Dashboard | High | ✅ Done |
| FR-03 | Overtime impact chart | Dashboard | High | ✅ Done |
| FR-04 | Salary vs attrition chart | Dashboard | High | ✅ Done |
| FR-05 | Age group attrition | Dashboard | Medium | ✅ Done |
| FR-06 | Job role ranking | Dashboard | Medium | ✅ Done |
| FR-07 | Attrition prediction | ML Model | High | ✅ Done |
| FR-08 | SHAP explanations | ML Model | High | ✅ Done |
| FR-09 | Clean dataset | Data | High | ✅ Done |
| FR-10 | SQL queries | Data | High | ✅ Done |
| FR-11 | Streamlit web app | App | Medium | ✅ Done |

---

*These requirements were defined before building the project to make sure we build exactly what the business needs.*

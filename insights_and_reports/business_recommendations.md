# 💡 Business Recommendations
### Project: Employee Attrition Analytics System

---

## 🔍 What is this document?
Based on everything we found in the data, this document tells the company **exactly what they should do** to reduce attrition. This is where the Business Analyst connects data to real business action.

> A data analyst finds patterns. A **Business Analyst** turns those patterns into decisions.

---

## 🚨 Priority Overview

| Priority | Recommendation | Expected Impact |
|----------|---------------|----------------|
| 🔴 HIGH | Fix Overtime Policy | Reduce attrition by 3–4% |
| 🔴 HIGH | Revise Salary for Low Band | Reduce attrition by 4–5% |
| 🟡 MEDIUM | Launch Early Career Program | Improve Year-1 retention by 8% |
| 🟡 MEDIUM | Sales Department Action Plan | Reduce Sales attrition by 5% |
| 🟢 LOW | Implement Risk Score Alerts | Proactive retention system |

---

## 🔴 Recommendation 1 — Fix the Overtime Problem (HIGH PRIORITY)

**What the data says:**
Employees who work overtime leave at a much higher rate than those who don't. Overtime is the #1 predictor in our ML model too.

**What is happening:**
Employees are being overworked. They feel burnt out and start looking for other jobs.

**What the company should do:**

| Action | Details |
|--------|---------|
| Cap overtime hours | Maximum 10 extra hours per week per employee |
| Introduce comp-off | For every overtime day, give 1 day off |
| Track overtime monthly | HR dashboard should flag anyone doing 20+ overtime hours |
| Manager accountability | Managers whose teams regularly overtime should be counselled |

**Expected Result:**
- Overtime-related attrition should drop significantly within 3–6 months
- Employee satisfaction scores will improve
- Estimated savings: If 30 employees are retained → $30 × $40,000 = **$1.2M saved**

---

## 🔴 Recommendation 2 — Revise Salary for Low Band Employees (HIGH PRIORITY)

**What the data says:**
Employees earning below $3,000/month have the highest attrition rate. They are likely getting better offers elsewhere.

**What is happening:**
Entry-level salaries are below market rate. Employees join, gain experience for 1–2 years, then leave for better pay.

**What the company should do:**

| Action | Details |
|--------|---------|
| Conduct market benchmarking | Compare current salaries with industry standards |
| Revise entry-level bands | Increase Low band salaries by 10–15% |
| Introduce annual hike guarantee | Minimum 8% hike for employees in Low salary band |
| Add performance bonus | Quarterly bonus for hitting targets (especially Sales) |

**Expected Result:**
- Low-band attrition should reduce by 4–5%
- Better talent attraction at entry level
- Estimated savings: If 40 employees retained → **$1.6M saved**

---

## 🟡 Recommendation 3 — Launch Early Career Retention Program (MEDIUM PRIORITY)

**What the data says:**
The 25–34 age group has the highest attrition. These are early-career professionals who leave if they don't see growth quickly.

**What is happening:**
Young employees join excited, but if they don't get clear career growth in 1–2 years, they look elsewhere.

**What the company should do:**

| Action | Details |
|--------|---------|
| 90-day onboarding plan | Structured plan for first 3 months so new joiners feel settled |
| Assign a mentor | Every new joiner gets a senior employee as mentor |
| 6-month career chat | Manager must have a formal career path discussion at 6 months |
| Learning budget | $500/year per employee for courses, certifications |
| Fast-track promotion track | Clear criteria for moving up — no ambiguity |

**Expected Result:**
- Year-1 retention should improve by 7–8%
- Employees feel valued and see a future at the company
- Reduces cost of constantly replacing junior talent

---

## 🟡 Recommendation 4 — Special Action Plan for Sales Department (MEDIUM PRIORITY)

**What the data says:**
Sales department has the highest attrition rate. Sales Executives and Representatives are leaving the most.

**What is happening:**
Sales is a high-pressure job. If incentives aren't good enough or targets are unrealistic, people leave fast.

**What the company should do:**

| Action | Details |
|--------|---------|
| Review sales targets | Are targets realistic? Consult with Sales Managers |
| Improve incentive structure | Better commission structure for hitting targets |
| Monthly 1-on-1s | Sales Managers must do monthly check-ins with each team member |
| Reduce field pressure | Balance remote vs field work for Sales Executives |
| Recognize top performers | Monthly recognition for top performers — public shoutouts, small rewards |

**Expected Result:**
- Sales attrition should reduce by 4–5%
- Better morale in Sales team
- Less time spent on constant hiring and training for Sales roles

---

## 🟢 Recommendation 5 — Implement Proactive Risk Score Alert System (LOW PRIORITY)

**What the data says:**
Our ML model can predict with 80%+ accuracy whether an employee will leave. But right now HR only knows after someone resigns.

**What is happening:**
HR is reactive — they find out too late. By the time someone gives notice, it's usually too late to retain them.

**What the company should do:**

| Action | Details |
|--------|---------|
| Use the Streamlit App | HR Managers enter employee details → get risk score instantly |
| Monthly risk report | Every month, HR gets a list of High-risk employees |
| Automatic flag | If an employee's score goes High, their manager gets notified |
| Retention conversation | HR to have a 1-on-1 with all High-risk employees within 2 weeks |

**Expected Result:**
- HR moves from reactive to proactive
- Can potentially retain 30–40% of High-risk employees
- Estimated savings: If 25 employees retained → **$1M saved**

---

## 📈 Total Expected Business Impact

If all recommendations are implemented:

| Metric | Before | Target |
|--------|--------|--------|
| Attrition Rate | 16.1% | < 11% |
| Employees Lost Per Year | 237 | < 160 |
| Replacement Cost Per Year | ~$9.5M | < $6.5M |
| **Annual Savings** | — | **~$3M+** |

---

## 🗓️ Implementation Roadmap

| Timeline | Action |
|----------|--------|
| Month 1 | Launch overtime tracking + cap policy |
| Month 1–2 | Conduct salary benchmarking |
| Month 2 | Begin salary revision for Low band |
| Month 2–3 | Launch 90-day onboarding program |
| Month 3 | Deploy Streamlit risk score app for HR |
| Month 3–6 | Monitor attrition rate monthly — check if trending down |
| Month 6 | Review all recommendations — adjust if needed |

---

*These recommendations are based on data analysis of 1,470 employee records using SQL, Python, and Machine Learning. All actions are designed to have measurable business impact.*

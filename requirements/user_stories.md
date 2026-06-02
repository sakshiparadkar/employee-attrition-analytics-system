# 📖 User Stories
### Project: Employee Attrition Analytics System

---

## 🔍 What is a User Story?
A user story is a simple way to write requirements **from the user's point of view**.

The format is always:
> **"As a [who], I want [what], so that [why]"**

Example:
> "As an HR Manager, I want to see which employees are at risk of leaving, so that I can talk to them before they resign."

User stories help us remember that we are building for **real people**, not just for data.

---

## 🏷️ Our User Types (Roles)

| Role | Who they are |
|------|-------------|
| **HR Head** | Senior HR leader, sees big picture |
| **HR Manager** | Manages a team, needs employee-level details |
| **CEO** | Wants cost and business impact summary |
| **Data Analyst** | Builds and maintains the system |

---

## 📋 User Stories

---

### 🟥 HIGH PRIORITY

---

**US-01 — Overall Attrition Rate**
> As an **HR Head**, I want to see the company's overall attrition rate on one screen, so that I can quickly report it to leadership every month.

**Acceptance Criteria:**
- ✅ Dashboard shows attrition % as a big KPI card
- ✅ Number updates when department filter is applied
- ✅ Shows total employees and total who left

---

**US-02 — Department Breakdown**
> As an **HR Head**, I want to see attrition broken down by department, so that I know which team needs urgent attention.

**Acceptance Criteria:**
- ✅ Bar chart shows all 3 departments
- ✅ Sorted from highest to lowest attrition
- ✅ Hover shows exact numbers

---

**US-03 — At-Risk Employee Prediction**
> As an **HR Manager**, I want to know which employees in my team are likely to leave, so that I can have a retention conversation with them before it is too late.

**Acceptance Criteria:**
- ✅ App shows employee risk as High / Medium / Low
- ✅ Shows top 3 reasons for the risk
- ✅ HR Manager can enter employee details and get instant result

---

**US-04 — Overtime Impact**
> As an **HR Head**, I want to see how overtime affects attrition, so that I can decide whether to change the overtime policy.

**Acceptance Criteria:**
- ✅ Dashboard shows attrition % for overtime vs non-overtime employees
- ✅ Difference is clearly visible (ideally with color coding)

---

**US-05 — Cost of Attrition**
> As a **CEO**, I want to understand how much money the company is losing due to attrition, so that I can approve budget for retention programs.

**Acceptance Criteria:**
- ✅ Dashboard or report shows estimated cost (no. of attrited × $40,000)
- ✅ Shown as a simple number on the executive summary page

---

### 🟨 MEDIUM PRIORITY

---

**US-06 — Salary Band Analysis**
> As an **HR Head**, I want to see attrition by salary range, so that I can decide if a salary revision is needed.

**Acceptance Criteria:**
- ✅ Shows 4 salary bands with attrition % for each
- ✅ Lowest salary band highlighted if attrition is highest there

---

**US-07 — Age Group Insight**
> As an **HR Manager**, I want to see which age group leaves the most, so that I can design the right retention program for that group.

**Acceptance Criteria:**
- ✅ Bar chart showing 4 age groups
- ✅ Highest attrition age group is clearly visible

---

**US-08 — Job Role Ranking**
> As an **HR Head**, I want to see which job roles have the highest attrition, so that I can focus hiring and retention on those roles.

**Acceptance Criteria:**
- ✅ All job roles listed with their attrition %
- ✅ Sorted from highest to lowest

---

### 🟩 LOW PRIORITY

---

**US-09 — SQL Data Access**
> As a **Data Analyst**, I want to have pre-written SQL queries for all key business questions, so that I can quickly pull data without writing from scratch every time.

**Acceptance Criteria:**
- ✅ At least 6 SQL queries saved in the project
- ✅ Each query has a comment explaining what it does

---

**US-10 — Documentation**
> As a **Data Analyst**, I want all business requirements and findings documented in markdown files, so that anyone who reads the GitHub repo understands the project without asking me.

**Acceptance Criteria:**
- ✅ BRD, User Stories, Functional Requirements all present
- ✅ Key Findings and Recommendations written clearly
- ✅ README explains the full project in simple language

---

## 📊 User Story Summary

| ID | User Story | Priority | Status |
|----|-----------|----------|--------|
| US-01 | Overall attrition rate | High | ✅ Done |
| US-02 | Department breakdown | High | ✅ Done |
| US-03 | At-risk employee prediction | High | ✅ Done |
| US-04 | Overtime impact | High | ✅ Done |
| US-05 | Cost of attrition for CEO | High | ✅ Done |
| US-06 | Salary band analysis | Medium | ✅ Done |
| US-07 | Age group insight | Medium | ✅ Done |
| US-08 | Job role ranking | Medium | ✅ Done |
| US-09 | SQL query library | Low | ✅ Done |
| US-10 | Full documentation | Low | ✅ Done |

---

*User stories keep the team focused on building what users actually need, not just what seems technically interesting.*

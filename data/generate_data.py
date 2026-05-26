import pandas as pd
import numpy as np

def generate_hr_data(n=1470, random_state=42):
    """Generate synthetic IBM HR Analytics-like dataset"""
    np.random.seed(random_state)

    departments = ["Sales", "Research & Development", "Human Resources"]
    job_roles = ["Sales Executive", "Research Scientist", "Laboratory Technician",
                 "Manufacturing Director", "Healthcare Representative", "Manager",
                 "Sales Representative", "Research Director", "Human Resources"]
    education_fields = ["Life Sciences", "Other", "Medical", "Marketing",
                        "Technical Degree", "Human Resources"]
    business_travel = ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    marital_status = ["Single", "Married", "Divorced"]

    age = np.random.randint(18, 60, n)
    monthly_income = np.random.randint(1000, 20000, n)
    years_at_company = np.random.randint(0, 40, n)
    overtime = np.random.choice(["Yes", "No"], n, p=[0.28, 0.72])
    job_satisfaction = np.random.randint(1, 5, n)
    work_life_balance = np.random.randint(1, 5, n)
    environment_satisfaction = np.random.randint(1, 5, n)
    relationship_satisfaction = np.random.randint(1, 5, n)
    job_involvement = np.random.randint(1, 5, n)
    num_companies = np.random.randint(0, 10, n)
    distance_from_home = np.random.randint(1, 30, n)
    total_working_years = np.random.randint(0, 40, n)
    years_since_promotion = np.random.randint(0, 15, n)
    training_times = np.random.randint(0, 6, n)
    stock_option = np.random.randint(0, 4, n)
    job_level = np.random.randint(1, 6, n)
    percent_salary_hike = np.random.randint(11, 25, n)
    performance_rating = np.random.choice([3, 4], n, p=[0.85, 0.15])
    education = np.random.randint(1, 6, n)

    dept = np.random.choice(departments, n, p=[0.30, 0.65, 0.05])
    role = np.random.choice(job_roles, n)
    edu_field = np.random.choice(education_fields, n)
    travel = np.random.choice(business_travel, n, p=[0.71, 0.19, 0.10])
    marital = np.random.choice(marital_status, n, p=[0.32, 0.46, 0.22])
    gender = np.random.choice(["Male", "Female"], n, p=[0.60, 0.40])

    # Attrition logic (realistic probabilities)
    attrition_prob = (
        0.05
        + 0.15 * (overtime == "Yes")
        + 0.10 * (job_satisfaction <= 2)
        + 0.08 * (work_life_balance <= 2)
        + 0.08 * (monthly_income < 3000)
        + 0.06 * (years_at_company < 3)
        + 0.05 * (marital == "Single")
        + 0.04 * (travel == "Travel_Frequently")
        - 0.05 * (stock_option >= 2)
        - 0.03 * (job_level >= 4)
    )
    attrition_prob = np.clip(attrition_prob, 0.02, 0.90)
    attrition = np.random.binomial(1, attrition_prob, n)
    attrition_label = np.where(attrition == 1, "Yes", "No")

    df = pd.DataFrame({
        "Age": age,
        "Attrition": attrition_label,
        "BusinessTravel": travel,
        "Department": dept,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EducationField": edu_field,
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital,
        "MonthlyIncome": monthly_income,
        "NumCompaniesWorked": num_companies,
        "OverTime": overtime,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": performance_rating,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": training_times,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": np.clip(years_at_company - np.random.randint(0, 5, n), 0, None),
        "YearsSinceLastPromotion": years_since_promotion,
        "YearsWithCurrManager": np.random.randint(0, 18, n),
    })

    return df


def generate_sample_upload(n=20):
    """Generate a small sample CSV for demo upload (no Attrition column)"""
    df = generate_hr_data(n=n, random_state=99)
    df = df.drop(columns=["Attrition"])
    employee_ids = [f"EMP{str(i).zfill(4)}" for i in range(1, n + 1)]
    names = [
        "Arjun Mehta", "Priya Sharma", "Ravi Kumar", "Sneha Iyer", "Amit Shah",
        "Divya Nair", "Rohit Verma", "Ananya Pillai", "Karan Malhotra", "Neha Joshi",
        "Suresh Patel", "Pooja Reddy", "Vikram Singh", "Aarti Gupta", "Manish Tiwari",
        "Sonal Desai", "Aditya Rao", "Kavita Saxena", "Deepak Chawla", "Ritika Bose"
    ]
    df.insert(0, "EmployeeID", employee_ids[:n])
    df.insert(1, "EmployeeName", names[:n])
    return df


if __name__ == "__main__":
    df = generate_hr_data()
    df.to_csv("data/hr_data.csv", index=False)
    sample = generate_sample_upload()
    sample.to_csv("data/sample_upload.csv", index=False)
    print(f"✅ Generated {len(df)} employee records")
    print(f"✅ Attrition rate: {(df['Attrition']=='Yes').mean():.1%}")
    print(f"✅ Sample upload file: {len(sample)} employees")

SELECT 
    CASE 
        WHEN MonthlyIncome < 3000 THEN 'Low (< 3K)'
        WHEN MonthlyIncome BETWEEN 3000 AND 6000 THEN 'Mid (3K-6K)'
        WHEN MonthlyIncome BETWEEN 6001 AND 10000 THEN 'High (6K-10K)'
        ELSE 'Very High (> 10K)'
    END AS salary_band,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS attrited,
    ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS attrition_rate
FROM hr_attrition
GROUP BY salary_band
ORDER BY attrition_rate DESC;
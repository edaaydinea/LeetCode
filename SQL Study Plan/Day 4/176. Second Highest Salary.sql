# Write your MySQL query statement below
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY 1 DESC
    LIMIT 1,1
) SecondHighestSalary;
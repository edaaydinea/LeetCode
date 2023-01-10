# Write an SQL query to report the IDs of all the employees with missing information.
# The information of an employee is missing if:
# The employee's name is missing, or
# The employee's salary is missing.
# Return the result table ordered by employee_id in ascending order.


SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (
    SELECT employee_id
    FROM Employees
)
ORDER BY employee_id ASC
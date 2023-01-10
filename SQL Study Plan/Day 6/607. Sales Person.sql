# Write your MySQL query statement below

# Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".

# Return the result table in any order.

SELECT name
FROM SalesPerson
WHERE sales_id not in (
    SELECT sales_id
    FROM orders
    JOIN company
    USING(com_id)
    WHERE name = 'red'
);
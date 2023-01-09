# Write your MySQL query statement below

# Write an SQL query that reports the products that were only sold in the first quarter of 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.

# Return the result table in any order

SELECT p.product_id, p.product_name
FROM Product p, Sales s
WHERE p.product_id = s.product_id
GROUP BY s.product_id
HAVING MIN(s.sales_date) >= '2019-01-01' AND MAX(s.sales_date) <= '2019-03-31';
# Write your MySQL query statement below

# Write an SQL query to find the IDs of the users who visited without making any transaction and
# the number of times they made these types of visits.
# Return the result table sorted in any order

SELECT customer_id, SUM(transaction_id is null) count_no_trans
FROM Visits
LEFT JOIN Transactions USING(visit_id)
GROUP BY 1
HAVING count_no_trans > 0
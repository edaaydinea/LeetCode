# Write your MySQL query statement below

# Write an SQL query to report all the duplicate emails.
# Return the result in any order.

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(id) >= 2;
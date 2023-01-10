# Write your MySQL query statement below

# Write an SQL query to find all dates' id with higher temperatures compared to its previous
# dates (yesterday).
# Return the result table in any order.

SELECT w1.id
FROM Weather w1, Weather w2
WHERE w1.Temperature > w2.Temperature AND DATEDIFF(w1.recordDate, w2.recordDate) = 1;
# Write your MySQL query statement below

# Write an SQL query to report the latest login for all users in the year 2020.
# D not include the users who did no login in 2020.
# Return the result table in any order

SELECT user_id, max(time_stamp) AS last_stamp
FROM Logins
WHERE DATE(time_stamp) BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY user_id;
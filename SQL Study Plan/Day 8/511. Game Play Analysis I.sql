# Write your MySQL query statement below

# Write an SQL query to report the first login date fore each player.
# Return the result table in any order.

SELECT player_id, min(event_date) first_login
FROM Activity
GROUP BY player_id;
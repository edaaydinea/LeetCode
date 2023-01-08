# Write your MySQL query statement below

# Write an SQL query to report the distance traveled by each user.

# Return the result table ordered by travelled_distance in descending order, if two or more users traveled the same distance, order them by their name in ascending order.

SELECT u.name, IFNULL(tb.travelled_distance, 0) AS travelled_distance
FROM (
    SELECT user_id, SUM(distance) AS travelled_distance
    FROM rides
    GROUP BY user_id) AS tb
RIGHT JOIN users u ON tb.user_id = u.id
ORDER BY tb.travelled_distance DESC, u.name ASC;

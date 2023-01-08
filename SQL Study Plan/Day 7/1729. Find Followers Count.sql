# Write your MySQL query statement below

# Write an SQL query that will, for each user, return the number of followers.
# Return the result table ordered by user_id in ascending order.

SELECT user_id, COUNT(DISTINCT follower_id) followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
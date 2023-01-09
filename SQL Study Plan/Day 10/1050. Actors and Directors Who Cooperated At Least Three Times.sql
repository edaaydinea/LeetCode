# Write your MySQL query statement below

# Write an SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

# Return the result table in any order.

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY 1,2
HAVING COUNT(timestamp) >= 3;
# Write your MySQL query statement below
SELECT id,
    CASE WHEN p_id IS NULL THEN "Root"
         WHEN id IN (
             SELECT p_id FROM tree
         ) THEN "Inner"
         ELSE "Leaf"
    END AS Type
FROM tree
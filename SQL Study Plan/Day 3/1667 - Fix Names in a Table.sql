# Write an SQL query to fix the names so that only the first character is uppercase and the rest are lowercase.
# Return the result table ordered by user_id

SELECT user_id,
CONCAT(UPPER(SUBSTRING(name, 1,1)), LOWER(SUBSTRING(name,2))) AS name
FROM Users
ORDER BY user_id;
# Write your MySQL query statement below

# Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's

# Return the result table in any order.

SELECT date_id, make_name, COUNT(DISTINCT lead_id) unique_leads, COUNT(DISTINCT partner_id) unique_partners
FROM DailySales
GROUP BY 1,2;
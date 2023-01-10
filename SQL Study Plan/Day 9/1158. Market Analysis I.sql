# Write your MySQL query statement below

# Write an SQL query to find for each user, the join date and the number of orders they made as a buyer in 2019.

# Return the result table in any order.

SELECT u.user_id AS buyer_id, u.join_date, IFNULL(tb.cnt, 0) AS orders_in_2019
FROM (
    SELECT buyer_id, COUNT(order_id) AS cnt
    FROM Orders
    WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31'
    GROUP BY buyer_id ) tb
RIGHT JOIN users u ON tb.buyer_id = u.user_id;

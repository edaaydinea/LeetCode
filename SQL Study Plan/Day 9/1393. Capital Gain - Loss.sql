# Write your MySQL query statement below

# Write an SQL query to report the Capital gain / loss for each stock.

# The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

#Return the result table in any order.

SELECT tb.stock_name, SUM(price) AS capital_gain_loss
FROM (
    SELECT stock_name, IF(operation = 'Buy', price * (-1), price) AS price
    FROM Stocks) tb
GROUP BY stock_name;
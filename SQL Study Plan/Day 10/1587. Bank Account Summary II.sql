# Write your MySQL query statement below

# Write an SQL query to report the name and balance of users with a balance higher than 10000. The balance of an account is equal to the sum of the amounts of all transactions involving that account.

# Return the result table in any order.

SELECT u.name, tb.sum AS balance
FROM (
    SELECT account, SUM(amount) AS sum
    FROM Transactions
    GROUP BY account
    HAVING SUM(amount) > 10000) tb
JOIN Users AS u
ON u.account = tb.account;
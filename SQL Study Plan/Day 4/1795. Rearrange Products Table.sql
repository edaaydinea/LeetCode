# Write an SQL query to rearrange the Products table so that each row has
# (product_id, store, price). If a product is not available in a store,
# do not include a row with that product_id and store combination in the result table.
# Return the result table in any order.

SELECT * FROM
(
    SELECT product_id, "store1" store, store1 price
    FROM Products
    UNION
    SELECT product_id, "store2" store, store2 price
    FROM Products
    UNION
    SELECT product_id, "store3" store, store3 price
    FROM Products
)t
WHERE price is not null;
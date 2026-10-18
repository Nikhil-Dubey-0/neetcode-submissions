-- Write your query below

-- SELECT c.customer_id, c.customer_name
-- FROM customers c
-- INNER JOIN orders o 
-- ON c.customer_id = o.customer_id
-- GROUP BY c.customer_id, c.customer_name
-- HAVING SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) > 0
--    AND SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) > 0
--    AND SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) = 0
-- ORDER BY c.customer_name;



SELECT customer_id, customer_name 
FROM customers 
WHERE customer_id IN (
    SELECT customer_id FROM orders WHERE product_name = 'A'
    INTERSECT
    SELECT customer_id FROM orders WHERE product_name = 'B'
    EXCEPT
    SELECT customer_id FROM orders WHERE product_name = 'C'
)
ORDER BY customer_name;



-- SELECT c.customer_id, c.customer_name
-- FROM customers c
-- WHERE c.customer_id IN (
--     SELECT customer_id FROM orders WHERE product_name = 'A'
-- )
-- AND c.customer_id IN (
--     SELECT customer_id FROM orders WHERE product_name = 'B'
-- )
-- AND c.customer_id NOT IN (
--     SELECT customer_id FROM orders WHERE product_name = 'C'
-- )
-- ORDER BY c.customer_name;

-- Write your query below
-- select name
-- from customers c
-- join orders o
-- on c.id = o.customer_id

select name
from customers
where id not in (
    select customer_id
    from orders
)
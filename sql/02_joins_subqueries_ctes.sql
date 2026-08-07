SELECT o.order_id, c.customer_name, c.city, p.product_name, p.category, o.sales
FROM analytics_project.orders o
INNER JOIN analytics_project.customers c ON o.customer_id = c.customer_id
INNER JOIN analytics_project.products p ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
LIMIT 10;

SELECT c.customer_id, c.customer_name
FROM analytics_project.customers c
LEFT JOIN analytics_project.orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

SELECT customer_id, ROUND(SUM(sales), 2) AS customer_total_spend
FROM analytics_project.orders
WHERE order_status = 'Delivered'
GROUP BY customer_id
HAVING SUM(sales) > (
    SELECT AVG(customer_sales)
    FROM (
        SELECT SUM(sales) AS customer_sales
        FROM analytics_project.orders
        WHERE order_status = 'Delivered'
        GROUP BY customer_id
    ) AS customer_totals
)
ORDER BY customer_total_spend DESC;

WITH customer_totals AS (
    SELECT customer_id, SUM(sales) AS customer_sales
    FROM analytics_project.orders
    WHERE order_status = 'Delivered'
    GROUP BY customer_id
),
overall_avg AS (
    SELECT AVG(customer_sales) AS avg_spend
    FROM customer_totals
)
SELECT ct.customer_id, ROUND(ct.customer_sales, 2) AS total_spend
FROM customer_totals ct, overall_avg oa
WHERE ct.customer_sales > oa.avg_spend
ORDER BY total_spend DESC;
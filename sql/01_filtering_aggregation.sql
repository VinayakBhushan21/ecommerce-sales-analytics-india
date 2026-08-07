-- Query 1: Basic filter + sort
SELECT order_id, city, sales, order_status
FROM analytics_project.orders
WHERE order_status = 'Delivered'
ORDER BY sales DESC
LIMIT 10;

-- Query 2: Total revenue and profit
SELECT
    ROUND(SUM(sales), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM analytics_project.orders
WHERE order_status = 'Delivered';

-- Query 3: Revenue by category (JOIN)
SELECT
    p.category,
    ROUND(SUM(o.sales), 2) AS category_revenue,
    COUNT(*) AS orders_count
FROM analytics_project.orders o
JOIN analytics_project.products p ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.category
ORDER BY category_revenue DESC;

-- Query 4: Cities with above-average order count (HAVING)
SELECT city, COUNT(*) AS order_count
FROM analytics_project.orders
GROUP BY city
HAVING order_count > 300
ORDER BY order_count DESC;

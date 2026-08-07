SELECT
    p.category,
    p.product_name,
    ROUND(SUM(o.sales), 2) AS product_revenue,
    RANK() OVER (
        PARTITION BY p.category
        ORDER BY SUM(o.sales) DESC
    ) AS revenue_rank
FROM analytics_project.orders o
JOIN analytics_project.products p ON o.product_id = p.product_id
WHERE o.order_status = 'Delivered'
GROUP BY p.category, p.product_name
ORDER BY p.category, revenue_rank;

WITH ranked_products AS (
    SELECT
        p.category,
        p.product_name,
        ROUND(SUM(o.sales), 2) AS product_revenue,
        RANK() OVER (
            PARTITION BY p.category
            ORDER BY SUM(o.sales) DESC
        ) AS revenue_rank
    FROM analytics_project.orders o
    JOIN analytics_project.products p ON o.product_id = p.product_id
    WHERE o.order_status = 'Delivered'
    GROUP BY p.category, p.product_name
)
SELECT * FROM ranked_products
WHERE revenue_rank <= 3
ORDER BY category, revenue_rank;

WITH monthly_revenue AS (
    SELECT
        DATE_FORMAT(order_date, '%Y-%m') AS order_month,
        ROUND(SUM(sales), 2) AS monthly_sales
    FROM analytics_project.orders
    WHERE order_status = 'Delivered'
    GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT
    order_month,
    monthly_sales,
    SUM(monthly_sales) OVER (ORDER BY order_month) AS running_total
FROM monthly_revenue
ORDER BY order_month;
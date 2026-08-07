CREATE VIEW analytics_project.vw_order_details AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.customer_name,
    c.city,
    c.state,
    c.customer_segment,
    p.product_id,
    p.product_name,
    p.category,
    o.quantity,
    o.discount_pct,
    o.sales,
    o.profit,
    o.payment_mode,
    o.order_status
FROM analytics_project.orders o
JOIN analytics_project.customers c ON o.customer_id = c.customer_id
JOIN analytics_project.products p ON o.product_id = p.product_id;
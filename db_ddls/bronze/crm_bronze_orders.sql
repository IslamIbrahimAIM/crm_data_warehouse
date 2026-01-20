DROP TABLE IF EXISTS crm_bronze_orders;
CREATE TABLE IF NOT EXISTS crm_bronze_orders (
    order_id VARCHAR(255),
    user_id VARCHAR(255),
    created_at VARCHAR(255),
    order_status VARCHAR(255),
    payment_provider VARCHAR(255),
    line_total VARCHAR(255)
);

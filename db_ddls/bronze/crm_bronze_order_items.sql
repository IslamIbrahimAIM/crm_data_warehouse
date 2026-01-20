DROP TABLE IF EXISTS crm_bronze_order_items;
CREATE TABLE IF NOT EXISTS crm_bronze_order_items (
    order_item_id VARCHAR(255),
    order_id VARCHAR(255),
    product_name VARCHAR(255),
    qty VARCHAR(255),
    unit_price VARCHAR(255),
    line_total VARCHAR(255)
);

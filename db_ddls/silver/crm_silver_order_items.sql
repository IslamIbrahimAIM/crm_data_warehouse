DROP TABLE IF EXISTS crm_silver_order_items;
CREATE TABLE IF NOT EXISTS crm_silver_order_items (
    order_item_sk CHAR(26) NOT NULL,
    order_sk    CHAR(26) NOT NULL,
    order_item_id VARCHAR(50),
    order_id VARCHAR(50),
    product_name VARCHAR(255),
    qty INT,
    unit_price DECIMAL(10,2),
    line_total DECIMAL(10,2),
    is_total_valid TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (order_item_sk),
KEY idx_crm_silver_order_items_order_item_id (order_item_id),
KEY idx_crm_silver_order_items_order_id (order_id)
)
ENGINE=InnoDB;

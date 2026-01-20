DROP TABLE IF EXISTS crm_silver_orders;
CREATE TABLE IF NOT EXISTS crm_silver_orders (
    order_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    provider_sk CHAR(26) NOT NULL,
    order_id VARCHAR(50),
    user_id VARCHAR(50),
    created_at DATETIME NOT NULL,
    order_status VARCHAR(255),
    payment_provider VARCHAR(255),
    payment_method  VARCHAR(255),
    line_total DECIMAL(10,2),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (order_sk),
KEY idx_crm_silver_orders_order_id (order_id),
KEY idx_crm_silver_orders_user_id (user_id)
)
ENGINE=InnoDB;

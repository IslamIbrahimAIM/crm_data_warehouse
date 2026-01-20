DROP TABLE IF EXISTS crm_silver_order_status_history;
CREATE TABLE IF NOT EXISTS crm_silver_order_status_history (
    order_status_history_sk CHAR(26) NOT NULL,
    order_sk CHAR(26) NOT NULL,
    change_id VARCHAR(255),
    order_id VARCHAR(50),
    order_status VARCHAR(255),
    changed_ts DATETIME,
    has_terminal_before TINYINT(1) NULL,
    is_invalid_stage  TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (order_status_history_sk),
KEY idx_crm_silver_order_status_history_order_id (order_id)
)
ENGINE=InnoDB;

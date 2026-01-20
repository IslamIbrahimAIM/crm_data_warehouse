DROP TABLE IF EXISTS crm_silver_payment_attempts;
CREATE TABLE IF NOT EXISTS crm_silver_payment_attempts (
    payment_attempt_sk CHAR(26) NOT NULL,
    order_sk CHAR(26) NOT NULL,
    attempt_id VARCHAR(50),
    order_id VARCHAR(50),
    payment_provider VARCHAR(255),
    payment_method VARCHAR(255),
    amount_attempted DECIMAL(10,2),
    is_success TINYINT(1),
    attempt_ts DATETIME,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (payment_attempt_sk),
KEY idx_crm_silver_payment_attempts_attempt_id (attempt_id),
KEY idx_crm_silver_payment_attempts_order_id (order_id)
)
ENGINE=InnoDB;

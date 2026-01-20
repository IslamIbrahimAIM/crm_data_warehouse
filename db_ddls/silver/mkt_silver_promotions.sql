DROP TABLE IF EXISTS mkt_silver_promotions;
CREATE TABLE IF NOT EXISTS mkt_silver_promotions (
    promotion_sk CHAR(26) NOT NULL,
    promotion_code VARCHAR(255),
    discount_pct INT,
    valid_from VARCHAR(255),
    valid_to VARCHAR(255),
    valid_days INT,
    promotion_status VARCHAR(255),
    is_invalid_window TINYINT(1) NOT NULL,
    is_active   TINYINT(1) NOT NULL,
    is_scheduled TINYINT(1) NOT NULL,
    is_expired TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (promotion_sk),
KEY idx_promotion_code (promotion_code)
)
ENGINE=InnoDB;

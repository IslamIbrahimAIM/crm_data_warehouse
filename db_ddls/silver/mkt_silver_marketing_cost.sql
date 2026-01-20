DROP TABLE IF EXISTS mkt_silver_marketing_cost;
CREATE TABLE IF NOT EXISTS mkt_silver_marketing_cost (
    marketing_cost_sk CHAR(26) NOT NULL,
    spend_id VARCHAR(50),
    channel VARCHAR(255),
    spend VARCHAR(255),
    spend_date DATE,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (marketing_cost_sk),
KEY idx_mkt_silver_marketing_cost_spend_id (spend_id)
)
ENGINE=InnoDB;

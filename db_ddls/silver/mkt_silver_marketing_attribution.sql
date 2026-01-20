DROP TABLE IF EXISTS mkt_silver_marketing_attribution;
CREATE TABLE IF NOT EXISTS mkt_silver_marketing_attribution (
    marketing_attribution_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    attrib_id VARCHAR(50),
    user_id VARCHAR(50),
    channel VARCHAR(255),
    campaign VARCHAR(255),
    medium VARCHAR(255),
    source VARCHAR(255),
    is_first_touch TINYINT(1),
    touch_ts DATETIME,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (marketing_attribution_sk),
KEY idx_mkt_silver_marketing_attribution_attrib_id (attrib_id),
KEY idx_mkt_silver_marketing_attribution_user_id (user_id)
)
ENGINE=InnoDB;

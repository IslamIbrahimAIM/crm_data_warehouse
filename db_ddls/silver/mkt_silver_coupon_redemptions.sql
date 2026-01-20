DROP TABLE IF EXISTS mkt_silver_coupon_redemptions;
CREATE TABLE IF NOT EXISTS mkt_silver_coupon_redemptions (
    coupon_redemption_sk CHAR(26) NOT NULL,
    user_sk  CHAR(26) NOT NULL,
    order_sk CHAR(26) NOT NULL,
    promotion_sk CHAR(26) NOT NULL,
    redemption_id VARCHAR(50),
    user_id VARCHAR(50),
    promotion_code VARCHAR(255),
    order_id VARCHAR(50),
    redeemed_ts DATETIME,
    is_valid_redeem TINYINT(1) NOT NULL,
    has_multiple_promos TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (coupon_redemption_sk),
KEY idx_mkt_silver_coupon_redemptions_redemption_id (redemption_id),
KEY idx_mkt_silver_coupon_redemptions_user_id (user_id),
KEY idx_mkt_silver_coupon_redemptions_order_id (order_id)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS mkt_bronze_coupon_redemptions;
CREATE TABLE IF NOT EXISTS mkt_bronze_coupon_redemptions (
    redemption_id VARCHAR(255),
    user_id VARCHAR(255),
    promotion_code VARCHAR(255),
    order_id VARCHAR(255),
    redeemed_ts VARCHAR(255)
);

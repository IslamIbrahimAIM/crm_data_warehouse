USE washit_dw;

DROP TABLE IF EXISTS mkt_bronze_coupon_redemptions;
CREATE TABLE IF NOT EXISTS mkt_bronze_coupon_redemptions (
    redemption_id VARCHAR(255),
    user_id VARCHAR(255),
    promotion_code VARCHAR(255),
    order_id VARCHAR(255),
    redeemed_ts VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_devices;
CREATE TABLE IF NOT EXISTS crm_bronze_devices (
    device_id VARCHAR(255),
    user_id VARCHAR(255),
    platform VARCHAR(255),
    device_model VARCHAR(255),
    mac_addr VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_events;
CREATE TABLE IF NOT EXISTS crm_bronze_events (
    event_id VARCHAR(255),
    user_id VARCHAR(255),
    event_type VARCHAR(255),
    event_ts VARCHAR(255),
    device_id VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_geo;
CREATE TABLE IF NOT EXISTS crm_bronze_geo (
    city_raw VARCHAR(255),
    country_raw VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255)
);

DROP TABLE IF EXISTS mkt_bronze_marketing_attribution;
CREATE TABLE IF NOT EXISTS mkt_bronze_marketing_attribution (
    attrib_id VARCHAR(255),
    user_id VARCHAR(255),
    channel VARCHAR(255),
    campaign VARCHAR(255),
    medium VARCHAR(255),
    source VARCHAR(255),
    touch_ts VARCHAR(255)
);

DROP TABLE IF EXISTS mkt_bronze_marketing_cost;
CREATE TABLE IF NOT EXISTS mkt_bronze_marketing_cost (
    spend_id VARCHAR(255),
    channel VARCHAR(255),
    spend VARCHAR(255),
    spend_date VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_order_items;
CREATE TABLE IF NOT EXISTS crm_bronze_order_items (
    order_item_id VARCHAR(255),
    order_id VARCHAR(255),
    product_name VARCHAR(255),
    qty VARCHAR(255),
    unit_price VARCHAR(255),
    line_total VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_order_status_history;
CREATE TABLE IF NOT EXISTS crm_bronze_order_status_history (
    id VARCHAR(255),
    order_id VARCHAR(255),
    status VARCHAR(255),
    changed_ts VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_orders;
CREATE TABLE IF NOT EXISTS crm_bronze_orders (
    order_id VARCHAR(255),
    user_id VARCHAR(255),
    created_at VARCHAR(255),
    order_status VARCHAR(255),
    payment_provider VARCHAR(255),
    line_total VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_payment_attempts;
CREATE TABLE IF NOT EXISTS crm_bronze_payment_attempts (
    attempt_id VARCHAR(255),
    order_id VARCHAR(255),
    provider VARCHAR(255),
    amount_attempted VARCHAR(255),
    success VARCHAR(255),
    attempt_ts VARCHAR(255)
);

DROP TABLE IF EXISTS mkt_bronze_promotions;
CREATE TABLE IF NOT EXISTS mkt_bronze_promotions (
    promotion_code VARCHAR(255),
    discount_pct VARCHAR(255),
    valid_from VARCHAR(255),
    valid_to VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_referrals;
CREATE TABLE IF NOT EXISTS crm_bronze_referrals (
    referral_id VARCHAR(255),
    referrer_user_id VARCHAR(255),
    referred_user_id VARCHAR(255),
    referral_ts VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_user_preferences;
CREATE TABLE IF NOT EXISTS crm_bronze_user_preferences (
    pref_id VARCHAR(255),
    user_id VARCHAR(255),
    pref_key VARCHAR(255),
    pref_value VARCHAR(255),
    updated_ts VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_users;
CREATE TABLE IF NOT EXISTS crm_bronze_users (
    user_id VARCHAR(255),
    full_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    signup_date VARCHAR(255),
    status VARCHAR(255),
    city_raw VARCHAR(255),
    address_raw VARCHAR(255)
);

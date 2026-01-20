USE washit_dw;

DROP TABLE IF EXISTS crm_silver_devices;
CREATE TABLE IF NOT EXISTS crm_silver_devices (
    device_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    device_id VARCHAR(50),
    user_id VARCHAR(50),
    platform VARCHAR(255),
    device_model VARCHAR(255),
    device_family VARCHAR(255),
    mac_addr VARCHAR(255),
    os_family VARCHAR(255),
    os_major_version INT,
    browser_family VARCHAR(255),
    browser_major_version INT,
    platform_os_mismatch TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (device_sk),
KEY idx_crm_silver_devices_device_id (device_id),
KEY idx_crm_silver_devices_user_id (user_id)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS crm_silver_events;
CREATE TABLE IF NOT EXISTS crm_silver_events (
    event_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    device_sk CHAR(26) NOT NULL,
    event_id VARCHAR(50),
    user_id VARCHAR(50),
    event_type VARCHAR(255),
    event_category VARCHAR(255),
    event_ts DATETIME,
    device_id VARCHAR(50),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (event_sk),
KEY idx_crm_silver_events_event_id (event_id),
KEY idx_crm_silver_events_user_id (user_id),
KEY idx_crm_silver_events_device_id (device_id)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS crm_silver_geo;
CREATE TABLE IF NOT EXISTS crm_silver_geo (
    geo_sk CHAR(26) NOT NULL,
    area_sk CHAR(26) NOT NULL,
    city_raw VARCHAR(255),
    city     VARCHAR(255),
    country_raw VARCHAR(255),
    country     VARCHAR(255),
    latitude DOUBLE NULL,
    longitude DOUBLE NULL,
    geo_percision   VARCHAR(20) NULL,
    is_city_resolved TINYINT(1) NOT NULL,
    is_country_resolved TINYINT(1) NOT NULL,
    is_geo_valid    TINYINT(1) NOT NULL,
    geo_quality_score   TINYINT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (area_sk),
UNIQUE KEY uk_city_lat_long (geo_sk, latitude, longitude),
KEY idx_city_sk (geo_sk),
KEY idx_lat_long (latitude, longitude),
KEY idx_geo_valid (is_geo_valid)
)
ENGINE=InnoDB;

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

DROP TABLE IF EXISTS crm_silver_referrals;
CREATE TABLE IF NOT EXISTS crm_silver_referrals (
    referral_sk CHAR(26) NOT NULL,
    referral_id VARCHAR(50),
    referrer_user_id VARCHAR(50),
    referrer_user_sk CHAR(26) NULL,
    referred_user_id VARCHAR(50),
    referred_user_sk CHAR(26) NULL,
    referral_ts DATETIME,
    is_self_referral TINYINT(1) NOT NULL DEFAULT 0,
    referral_ts_parse_status VARCHAR(20) NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (referral_sk),
KEY idx_crm_silver_referrals_referral_id (referral_id),
KEY idx_crm_silver_referrals_referrer_user_id (referrer_user_id),
KEY idx_crm_silver_referrals_referred_user_id (referred_user_id)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS crm_silver_user_preferences;
CREATE TABLE IF NOT EXISTS crm_silver_user_preferences (
    user_preference_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    pref_id VARCHAR(50),
    user_id VARCHAR(50),
    pref_key VARCHAR(255),
    pref_value VARCHAR(255),
    updated_ts DATETIME,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (user_preference_sk),
KEY idx_crm_silver_user_preferences_pref_id (pref_id),
KEY idx_crm_silver_user_preferences_user_id (user_id)
)
ENGINE=InnoDB;

DROP TABLE IF EXISTS crm_silver_users;
CREATE TABLE IF NOT EXISTS crm_silver_users (
    user_sk CHAR(26) NOT NULL,
    geo_sk CHAR(26) NOT NULL,
    user_id VARCHAR(50),
    full_name VARCHAR(255),
    initials VARCHAR(3),
    first_name VARCHAR(255),
    last_name  VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    signup_date DATE,
    status VARCHAR(255),
    city_raw VARCHAR(255),
    address_raw VARCHAR(255),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (user_sk),
KEY idx_crm_silver_users_user_id (user_id),
UNIQUE KEY (user_id)
)
ENGINE=InnoDB;

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


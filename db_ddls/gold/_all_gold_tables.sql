USE washit_dw;


-- CREATE TABLE IF NOT EXISTS gold_dim_date (
--     date_sk                 INT NOT NULL,
--     date_actual             DATE NOT NULL,
--     day_of_month            TINYINT NOT NULL,
--     month_num               TINYINT NOT NULL,
--     year_num                SMALLINT NOT NULL,
--     day_name                VARCHAR(20) NOT NULL,
--     calendar_week           TINYINT NOT NULL,
--     fiscal_year             SMALLINT NOT NULL,
--     fiscal_year_start_date  DATE NOT NULL,
--     fiscal_week             TINYINT NOT NULL,
--     salary_day              DATE NOT NULL,
--     is_salary_day           BOOLEAN NOT NULL,
--     is_black_friday         BOOLEAN NOT NULL,
--     dw_created_at           DATETIME NOT NULL,

--     PRIMARY KEY (date_sk),
--     UNIQUE KEY uk_date_actual (date_actual),
--     KEY idx_fiscal_year_week (fiscal_year, fiscal_week),
--     KEY idx_calendar_year_month (year_num, month_num)
-- ) ENGINE=InnoDB;

  
-- CREATE TABLE IF NOT EXISTS gold_dim_channel (
--     channel_sk      CHAR(26)     NOT NULL,
--     channel_name    VARCHAR(100) NOT NULL,
--     dw_created_at   DATETIME     NOT NULL,

--     PRIMARY KEY (channel_sk),
--     UNIQUE KEY uk_channel_name (channel_name)
-- ) ENGINE=InnoDB;



-- CREATE TABLE IF NOT EXISTS gold_dim_user (
--     user_sk     CHAR(26) NOT NULL,
--     full_name   VARCHAR(255),
--     first_name  VARCHAR(255),
--     last_name   VARCHAR(255),
--     email       VARCHAR(255),
--     phone       VARCHAR(255),
--     signup_date DATETIME,
--     user_status VARCHAR(255),
--     pref_language VARCHAR(255),
--     offers_enabled TINYINT(1),
--     notifications_enabled   TINYINT(1),
--     city        VARCHAR(255),
--     dw_created_at   DATETIME NOT NULL,

--     PRIMARY KEY (user_sk),
--     KEY idx_signup_date (signup_date),
--     KEY idx_status  (user_status)
-- )ENGINE=InnoDB;

-- CREATE TABLE IF NOT EXISTS gold_dim_device (
--     device_sk   CHAR(26) NOT NULL,
--     device_family    VARCHAR(255),
--     os_family        VARCHAR(255),
--     os_major_version VARCHAR(255),
--     browser_family   VARCHAR(255),
--     browser_major_version TINYINT,
--     dw_created_at    DATETIME NOT NULL,

--     PRIMARY KEY (device_sk),

--     KEY idx_device_family (device_family),
--     KEY idx_os (os_family, os_major_version),
--     KEY idx_browser (browser_family, browser_major_version)
-- ) ENGINE=InnoDB;


-- CREATE TABLE IF NOT EXISTS  gold_dim_geo (
--     geo_sk      CHAR(26) NOT NULL,
--     city        VARCHAR(255),
--     country     VARCHAR(255),
--     latitude    DOUBLE,
--     longitude   DOUBLE,
--     dw_created_at   DATETIME NOT NULL,

--     PRIMARY KEY (geo_sk),
--     KEY idx_country (country),
--     KEY idx_city (city)

-- ) ENGINE=InnoDB;



-- CREATE TABLE IF NOT EXISTS gold_fact_orders (
--     order_sk                      CHAR(26) NOT NULL,
--     user_sk                       CHAR(26) NOT NULL,
--     geo_sk                        CHAR(26) NOT NULL,
--     provider_sk                   CHAR(26) NOT NULL,
--     order_date_sk                 INT NOT NULL,
--     coupon_redemption_sk          CHAR(26),
--     promotion_sk                  CHAR(26),
--     order_status                  VARCHAR(50),
--     city                          VARCHAR(50),
--     order_total                   DECIMAL(10,2),
--     payment_provider              VARCHAR(50),
--     payment_method                VARCHAR(50),
--     order_date                    DATETIME NOT NULL,

--     dw_created_at                 DATETIME NOT NULL,

--     PRIMARY KEY (order_sk),

--     KEY idx_user_sk (user_sk),
--     KEY idx_geo_sk (geo_sk),
--     KEY idx_provider_sk (provider_sk),
--     KEY idx_coupon_redemption_sk (coupon_redemption_sk),
--     KEY idx_promotion_sk (promotion_sk),
--     KEY idx_order_date_sk (order_date_sk)
-- ) ENGINE=InnoDB;



CREATE TABLE IF NOT EXISTS gold_fact_events (
    event_sk                CHAR(26) NOT NULL,
    event_date_sk           INT NOT NULL,
    user_sk                 CHAR(26) NOT NULL,
    device_sk               CHAR(26) NOT NULL,
    geo_sk                  CHAR(26) NOT NULL,
    event_date              DATETIME NOT NULL,
    city                    VARCHAR(255) NOT NULL,
    event_type              VARCHAR(255) NOT NULL,
    event_category          VARCHAR(255) NOT NULL,
    device_family           VARCHAR(255) NOT NULL,
    os_family               VARCHAR(255) NOT NULL,
    os_major_version        INT,
    browser_family          VARCHAR(255),
    browser_major_version   INT,

    dw_created_at           DATETIME NOT NULL,

    PRIMARY KEY (event_sk),

    KEY idx_user_sk (user_sk),
    KEY idx_geo_sk  (geo_sk),
    KEY idx_device_sk (device_sk),    
    KEY idx_event_date_sk (event_date_sk)    

)ENGINE=InnoDB;
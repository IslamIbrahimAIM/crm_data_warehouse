DROP TABLE IF EXISTS gold_fact_orders;
CREATE TABLE IF NOT EXISTS gold_fact_orders (
    order_sk                      CHAR(26) NOT NULL,
    user_sk                       CHAR(26) NOT NULL,
    geo_sk                        CHAR(26) NOT NULL,
    provider_sk                   CHAR(26) NOT NULL,
    order_date_sk                 INT NOT NULL,
    coupon_redemption_sk          CHAR(26),
    promotion_sk                  CHAR(26),
    order_status                  VARCHAR(50),
    city                          VARCHAR(50),
    order_total                   DECIMAL(10,2),
    payment_provider              VARCHAR(50),
    payment_method                VARCHAR(50),
    order_date                    DATETIME NOT NULL,

    dw_created_at                 DATETIME NOT NULL,

    PRIMARY KEY (order_sk),

    KEY idx_user_sk (user_sk),
    KEY idx_geo_sk (geo_sk),
    KEY idx_provider_sk (provider_sk),
    KEY idx_coupon_redemption_sk (coupon_redemption_sk),
    KEY idx_promotion_sk (promotion_sk),
    KEY idx_order_date_sk (order_date_sk)
) ENGINE=InnoDB;

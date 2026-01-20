DROP TABLE IF EXISTS mkt_bronze_promotions;
CREATE TABLE IF NOT EXISTS mkt_bronze_promotions (
    promotion_code VARCHAR(255),
    discount_pct VARCHAR(255),
    valid_from VARCHAR(255),
    valid_to VARCHAR(255)
);

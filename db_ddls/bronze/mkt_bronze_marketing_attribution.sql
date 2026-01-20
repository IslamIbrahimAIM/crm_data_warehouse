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

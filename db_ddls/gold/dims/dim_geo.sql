DROP TABLE IF EXISTS gold_dim_geo;
CREATE TABLE IF NOT EXISTS  gold_dim_geo (
    geo_sk      CHAR(26) NOT NULL,
    city        VARCHAR(255),
    country     VARCHAR(255),
    latitude    DOUBLE,
    longitude   DOUBLE,
    dw_created_at   DATETIME NOT NULL,

    PRIMARY KEY (geo_sk),
    KEY idx_country (country),
    KEY idx_city (city)

) ENGINE=InnoDB;
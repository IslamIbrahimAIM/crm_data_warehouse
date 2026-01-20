DROP TABLE IF EXISTS crm_silver_geo;
CREATE TABLE IF NOT EXISTS crm_silver_geo (
    geo_sk CHAR(26) NOT NULL,
    city_raw VARCHAR(255),
    country_raw VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (geo_sk)
)
ENGINE=InnoDB;

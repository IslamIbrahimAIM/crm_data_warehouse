DROP TABLE IF EXISTS crm_bronze_geo;
CREATE TABLE IF NOT EXISTS crm_bronze_geo (
    city_raw VARCHAR(255),
    country_raw VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255)
);

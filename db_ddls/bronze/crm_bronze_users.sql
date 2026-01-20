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

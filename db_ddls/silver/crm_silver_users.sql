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
    city     VARCHAR(255),
    address_raw VARCHAR(255),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (user_sk),
KEY idx_crm_silver_users_user_id (user_id),
UNIQUE KEY (user_id)
)
ENGINE=InnoDB;
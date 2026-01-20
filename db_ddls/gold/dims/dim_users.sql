DROP TABLE IF EXISTS gold_dim_user;
CREATE TABLE IF NOT EXISTS gold_dim_user (
    user_sk     CHAR(26) NOT NULL,
    full_name   VARCHAR(255),
    first_name  VARCHAR(255),
    last_name   VARCHAR(255),
    email       VARCHAR(255),
    phone       VARCHAR(255),
    signup_date DATETIME,
    user_status VARCHAR(255),
    pref_language VARCHAR(255),
    offers_enabled TINYINT(1),
    notifications_enabled   TINYINT(1),
    city        VARCHAR(255),
    dw_created_at   DATETIME NOT NULL,

    PRIMARY KEY (user_sk),
    KEY idx_signup_date (signup_date),
    KEY idx_status  (user_status)
)ENGINE=InnoDB;
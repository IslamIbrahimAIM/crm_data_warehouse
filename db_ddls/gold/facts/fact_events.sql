DROP TABLE IF EXISTS gold_fact_events;
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
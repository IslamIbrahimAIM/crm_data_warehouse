DROP TABLE IF EXISTS crm_silver_events;
CREATE TABLE IF NOT EXISTS crm_silver_events (
    event_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    device_sk CHAR(26) NOT NULL,
    event_id VARCHAR(50),
    user_id VARCHAR(50),
    event_type VARCHAR(255),
    event_category VARCHAR(255),
    event_ts DATETIME,
    device_id VARCHAR(50),
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (event_sk),
KEY idx_crm_silver_events_event_id (event_id),
KEY idx_crm_silver_events_user_id (user_id),
KEY idx_crm_silver_events_device_id (device_id)
)
ENGINE=InnoDB;

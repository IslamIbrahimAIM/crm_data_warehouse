DROP TABLE IF EXISTS crm_bronze_events;
CREATE TABLE IF NOT EXISTS crm_bronze_events (
    event_id VARCHAR(255),
    user_id VARCHAR(255),
    event_type VARCHAR(255),
    event_ts VARCHAR(255),
    device_id VARCHAR(255)
);

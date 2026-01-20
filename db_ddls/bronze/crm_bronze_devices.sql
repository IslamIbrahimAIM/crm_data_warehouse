DROP TABLE IF EXISTS crm_bronze_devices;
CREATE TABLE IF NOT EXISTS crm_bronze_devices (
    device_id VARCHAR(255),
    user_id VARCHAR(255),
    platform VARCHAR(255),
    device_model VARCHAR(255),
    mac_addr VARCHAR(255)
);

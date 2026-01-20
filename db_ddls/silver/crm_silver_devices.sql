DROP TABLE IF EXISTS crm_silver_devices;
CREATE TABLE IF NOT EXISTS crm_silver_devices (
    device_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    device_id VARCHAR(50),
    user_id VARCHAR(50),
    platform VARCHAR(255),
    device_model VARCHAR(255),
    device_family VARCHAR(255),
    mac_addr VARCHAR(255),
    os_family VARCHAR(255),
    os_major_version INT,
    browser_family VARCHAR(255),
    browser_major_version INT,
    platform_os_mismatch TINYINT(1) NOT NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (device_sk),
KEY idx_crm_silver_devices_device_id (device_id),
KEY idx_crm_silver_devices_user_id (user_id)
)
ENGINE=InnoDB;

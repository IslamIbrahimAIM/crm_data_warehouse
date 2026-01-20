DROP TABLE IF EXISTS gold_dim_device;
CREATE TABLE IF NOT EXISTS gold_dim_device (
    device_sk   CHAR(26) NOT NULL,
    device_family    VARCHAR(255),
    os_family        VARCHAR(255),
    os_major_version VARCHAR(255),
    browser_family   VARCHAR(255),
    brower_major_version TINYINT,
    dw_created_at    DATETIME NOT NULL,

    PRIMARY KEY (device_sk),

    KEY idx_device_family (device_family),
    KEY idx_os (os_family, os_major_version),
    KEY idx_browser (browser_family, brower_major_version)
) ENGINE=InnoDB;
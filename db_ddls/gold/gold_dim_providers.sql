DROP TABLE IF EXISTS gold_dim_providers;
CREATE TABLE IF NOT EXISTS gold_dim_providers (
    `provider_sk` VARCHAR(255),
    `payment_provider` VARCHAR(255),
    `dw_created_at` DATETIME NOT NULL,
    PRIMARY KEY (`provider_sk`)
) ENGINE=InnoDB;
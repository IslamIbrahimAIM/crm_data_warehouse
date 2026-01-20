DROP TABLE IF EXISTS gold_dim_promotion;
CREATE TABLE IF NOT EXISTS gold_dim_promotion (
    `promotion_sk` VARCHAR(255),
    `valid_from_date_sk` INT,
    `valid_to_date_sk` INT,
    `promotion_code` VARCHAR(255),
    `discount_pct` INT,
    `valid_from` VARCHAR(255),
    `valid_to` VARCHAR(255),
    `valid_days` INT,
    `promotion_status` VARCHAR(255),
    `is_invalid_window` BOOLEAN,
    `is_active` BOOLEAN,
    `is_scheduled` BOOLEAN,
    `is_expired` BOOLEAN,
    `dw_created_at` DATETIME NOT NULL,
    PRIMARY KEY (`promotion_sk`),
    KEY `idx_gold_dim_promotion_valid_from_date_sk` (`valid_from_date_sk`),
    KEY `idx_gold_dim_promotion_valid_to_date_sk` (`valid_to_date_sk`)
) ENGINE=InnoDB;
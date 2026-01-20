USE washit_dw;

DROP TABLE IF EXISTS gold_dim_date;
CREATE TABLE IF NOT EXISTS gold_dim_date (
    date_sk                 INT NOT NULL,
    date_actual             DATE NOT NULL,
    day_of_month            TINYINT NOT NULL,
    month_num               TINYINT NOT NULL,
    year_num                SMALLINT NOT NULL,
    day_name                VARCHAR(20) NOT NULL,
    calendar_week           TINYINT NOT NULL,
    fiscal_year             SMALLINT NOT NULL,
    fiscal_year_start_date  DATE NOT NULL,
    fiscal_week             TINYINT NOT NULL,
    salary_day              DATE NOT NULL,
    is_salary_day           BOOLEAN NOT NULL,
    is_black_friday         BOOLEAN NOT NULL,
    dw_created_at           DATETIME NOT NULL,

    PRIMARY KEY (date_sk),
    UNIQUE KEY uk_date_actual (date_actual),
    KEY idx_fiscal_year_week (fiscal_year, fiscal_week),
    KEY idx_calendar_year_month (year_num, month_num)
) ENGINE=InnoDB;
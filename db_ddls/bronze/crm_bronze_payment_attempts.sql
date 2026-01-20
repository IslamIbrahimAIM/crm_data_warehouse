DROP TABLE IF EXISTS crm_bronze_payment_attempts;
CREATE TABLE IF NOT EXISTS crm_bronze_payment_attempts (
    attempt_id VARCHAR(255),
    order_id VARCHAR(255),
    provider VARCHAR(255),
    amount_attempted VARCHAR(255),
    success VARCHAR(255),
    attempt_ts VARCHAR(255)
);

DROP TABLE IF EXISTS crm_bronze_order_status_history;
CREATE TABLE IF NOT EXISTS crm_bronze_order_status_history (
    id VARCHAR(255),
    order_id VARCHAR(255),
    status VARCHAR(255),
    changed_ts VARCHAR(255)
);

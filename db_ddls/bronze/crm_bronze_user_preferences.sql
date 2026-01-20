DROP TABLE IF EXISTS crm_bronze_user_preferences;
CREATE TABLE IF NOT EXISTS crm_bronze_user_preferences (
    pref_id VARCHAR(255),
    user_id VARCHAR(255),
    pref_key VARCHAR(255),
    pref_value VARCHAR(255),
    updated_ts VARCHAR(255)
);

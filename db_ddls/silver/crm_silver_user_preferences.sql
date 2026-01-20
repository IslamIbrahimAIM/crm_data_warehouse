DROP TABLE IF EXISTS crm_silver_user_preferences;
CREATE TABLE IF NOT EXISTS crm_silver_user_preferences (
    user_preference_sk CHAR(26) NOT NULL,
    user_sk CHAR(26) NOT NULL,
    pref_id VARCHAR(50),
    user_id VARCHAR(50),
    pref_key VARCHAR(255),
    pref_value VARCHAR(255),
    updated_ts DATETIME,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (user_preference_sk),
KEY idx_crm_silver_user_preferences_pref_id (pref_id),
KEY idx_crm_silver_user_preferences_user_id (user_id)
)
ENGINE=InnoDB;

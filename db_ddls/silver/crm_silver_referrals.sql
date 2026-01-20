DROP TABLE IF EXISTS crm_silver_referrals;
CREATE TABLE IF NOT EXISTS crm_silver_referrals (
    referral_sk CHAR(26) NOT NULL,
    referral_id VARCHAR(50),
    referrer_user_id VARCHAR(50),
    referrer_user_sk CHAR(26) NULL,
    referred_user_id VARCHAR(50),
    referred_user_sk CHAR(26) NULL,
    referral_ts DATETIME,
    is_self_referral TINYINT(1) NOT NULL DEFAULT 0,
    referral_ts_parse_status VARCHAR(20) NULL,
    dw_created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (referral_sk),
KEY idx_crm_silver_referrals_referral_id (referral_id),
KEY idx_crm_silver_referrals_referrer_user_id (referrer_user_id),
KEY idx_crm_silver_referrals_referred_user_id (referred_user_id)
)
ENGINE=InnoDB;
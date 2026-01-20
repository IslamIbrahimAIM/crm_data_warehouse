DROP TABLE IF EXISTS crm_bronze_referrals;
CREATE TABLE IF NOT EXISTS crm_bronze_referrals (
    referral_id VARCHAR(255),
    referrer_user_id VARCHAR(255),
    referred_user_id VARCHAR(255),
    referral_ts VARCHAR(255)
);

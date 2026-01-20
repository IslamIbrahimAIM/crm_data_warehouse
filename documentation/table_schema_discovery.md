# Table Schema Discovery Report

Database: washit_dw
Table pattern: %gold%
Generated: 2026-01-20 06:41:10 UTC

```text

====================================================================================================
 TABLE: gold_dim_channel
====================================================================================================
root
 |-- channel_sk: string (nullable = true)
 |-- channel_name: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_date
====================================================================================================
root
 |-- date_sk: integer (nullable = true)
 |-- date_actual: date (nullable = true)
 |-- day_of_month: byte (nullable = true)
 |-- month_num: byte (nullable = true)
 |-- year_num: short (nullable = true)
 |-- day_name: string (nullable = true)
 |-- calendar_week: byte (nullable = true)
 |-- fiscal_year: short (nullable = true)
 |-- fiscal_year_start_date: date (nullable = true)
 |-- fiscal_week: byte (nullable = true)
 |-- salary_day: date (nullable = true)
 |-- is_salary_day: boolean (nullable = true)
 |-- is_black_friday: boolean (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_device
====================================================================================================
root
 |-- device_sk: string (nullable = true)
 |-- device_family: string (nullable = true)
 |-- os_family: string (nullable = true)
 |-- os_major_version: string (nullable = true)
 |-- browser_family: string (nullable = true)
 |-- browser_major_version: integer (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_geo
====================================================================================================
root
 |-- geo_sk: string (nullable = true)
 |-- city: string (nullable = true)
 |-- country: string (nullable = true)
 |-- latitude: double (nullable = true)
 |-- longitude: double (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_promotion
====================================================================================================
root
 |-- promotion_sk: string (nullable = true)
 |-- valid_from_date_sk: integer (nullable = true)
 |-- valid_to_date_sk: integer (nullable = true)
 |-- promotion_code: string (nullable = true)
 |-- discount_pct: integer (nullable = true)
 |-- valid_from: string (nullable = true)
 |-- valid_to: string (nullable = true)
 |-- valid_days: integer (nullable = true)
 |-- promotion_status: string (nullable = true)
 |-- is_invalid_window: boolean (nullable = true)
 |-- is_active: boolean (nullable = true)
 |-- is_scheduled: boolean (nullable = true)
 |-- is_expired: boolean (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_providers
====================================================================================================
root
 |-- provider_sk: string (nullable = true)
 |-- payment_provider: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_dim_user
====================================================================================================
root
 |-- user_sk: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- signup_date: timestamp (nullable = true)
 |-- user_status: string (nullable = true)
 |-- pref_language: string (nullable = true)
 |-- offers_enabled: integer (nullable = true)
 |-- notifications_enabled: integer (nullable = true)
 |-- city: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_fact_events
====================================================================================================
root
 |-- event_sk: string (nullable = true)
 |-- event_date_sk: integer (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- device_sk: string (nullable = true)
 |-- geo_sk: string (nullable = true)
 |-- event_date: timestamp (nullable = true)
 |-- city: string (nullable = true)
 |-- event_type: string (nullable = true)
 |-- event_category: string (nullable = true)
 |-- device_family: string (nullable = true)
 |-- os_family: string (nullable = true)
 |-- os_major_version: string (nullable = true)
 |-- browser_family: string (nullable = true)
 |-- browser_major_version: integer (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_fact_orders
====================================================================================================
root
 |-- order_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- geo_sk: string (nullable = true)
 |-- provider_sk: string (nullable = true)
 |-- order_date_sk: integer (nullable = true)
 |-- coupon_redemption_sk: string (nullable = true)
 |-- promotion_sk: string (nullable = true)
 |-- order_status: string (nullable = true)
 |-- city: string (nullable = true)
 |-- order_total: decimal(10,2) (nullable = true)
 |-- payment_provider: string (nullable = true)
 |-- payment_method: string (nullable = true)
 |-- order_date: timestamp (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


====================================================================================================
 TABLE: gold_user_value_profile
====================================================================================================
root
 |-- device_sk: string (nullable = true)
 |-- geo_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- first_event_date: timestamp (nullable = true)
 |-- last_event_date: timestamp (nullable = true)
 |-- first_order_date: timestamp (nullable = true)
 |-- last_order_date: timestamp (nullable = true)
 |-- total_orders: long (nullable = true)
 |-- total_revenue: decimal(20,2) (nullable = true)
 |-- actual_revenue: decimal(22,2) (nullable = true)
 |-- expected_revenue: decimal(22,2) (nullable = true)
 |-- lost_revenue: decimal(22,2) (nullable = true)
 |-- primary_city: string (nullable = true)
 |-- abs: integer (nullable = true)
 |-- aov: decimal(10,2) (nullable = true)
 |-- is_repeat_customer: boolean (nullable = true)
 |-- days_to_first_order: integer (nullable = true)
 |-- conversion_type: string (nullable = true)
 |-- purchase_behavior: string (nullable = true)
 |-- value_segment: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- user_status: string (nullable = true)
 |-- pref_language: string (nullable = true)
 |-- latitude: double (nullable = true)
 |-- longitude: double (nullable = true)
 |-- device_family: string (nullable = true)
 |-- os_family: string (nullable = true)
 |-- browser_family: string (nullable = true)
 |-- realized_ltv: decimal(22,2) (nullable = true)
 |-- potential_ltv: decimal(23,2) (nullable = true)
 |-- revenue_efficiency_score: decimal(25,2) (nullable = true)
 |-- churn_risk: string (nullable = true)
 |-- tenure_days: integer (nullable = true)
 |-- tenure_bucket: string (nullable = true)
 |-- purchase_tenure_days: integer (nullable = true)
 |-- purchase_tenure_bucket: string (nullable = true)
 |-- recency_days: integer (nullable = true)
 |-- r_score: integer (nullable = true)
 |-- f_score: integer (nullable = true)
 |-- m_score: integer (nullable = true)
 |-- rfm_score: string (nullable = true)
 |-- clv_rank: string (nullable = true)

```

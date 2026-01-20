SELECT
    COUNT(DISTINCT e.device_id)                                  AS event_devices,
    COUNT(DISTINCT d.device_id)                                  AS total_devices,
    COUNT(DISTINCT e.device_id) * 1.0 /
    NULLIF(COUNT(DISTINCT d.device_id), 0)                       AS coverage_ratio
FROM crm_bronze_devices d
LEFT JOIN crm_bronze_events e
    ON d.device_id = e.device_id;

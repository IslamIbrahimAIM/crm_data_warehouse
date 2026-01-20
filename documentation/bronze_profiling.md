# Table Discovery Report

Database: washit_dw
Table pattern: %bronze%
Generated: 2026-01-07 07:12:46 UTC

```text

 Discovered 14 tables:
  - crm_bronze_devices
  - crm_bronze_events
  - crm_bronze_geo
  - crm_bronze_order_items
  - crm_bronze_order_status_history
  - crm_bronze_orders
  - crm_bronze_payment_attempts
  - crm_bronze_referrals
  - crm_bronze_user_preferences
  - crm_bronze_users
  - mkt_bronze_coupon_redemptions
  - mkt_bronze_marketing_attribution
  - mkt_bronze_marketing_cost
  - mkt_bronze_promotions

====================================================================================================
 DISCOVERING TABLE: crm_bronze_devices
====================================================================================================

 SCHEMA
root
 |-- device_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- platform: string (nullable = true)
 |-- device_model: string (nullable = true)
 |-- mac_addr: string (nullable = true)


 TOTAL ROWS: 20000

 NULL COUNTS
+---------+-------+--------+------------+--------+
|device_id|user_id|platform|device_model|mac_addr|
+---------+-------+--------+------------+--------+
|0        |0      |0       |0           |4024    |
+---------+-------+--------+------------+--------+


 VALUE SHAPES — device_id
+----------+-----+
|shape     |count|
+----------+-----+
|99999999-9|298  |
|9999999A-9|199  |
|99999A99-9|193  |
|99999999-A|188  |
|999A9999-9|185  |
|9A999999-9|179  |
|99A99999-9|173  |
|999999A9-9|166  |
|A9999999-9|166  |
|9999A999-9|163  |
+----------+-----+


 SAMPLE VALUES — device_id
+----------+------------+
|shape     |sample_value|
+----------+------------+
|99999999-9|00024980-7  |
|99999999-9|00437127-7  |
|99999999-9|00485546-2  |
|99999999-A|00071907-a  |
|99999999-A|01780208-a  |
|99999999-A|01877392-d  |
|9999999A-9|0009066d-6  |
|9999999A-9|0079045e-8  |
|9999999A-9|0138131d-5  |
|9999999A-A|0023892f-d  |
|9999999A-A|0383766d-e  |
|9999999A-A|0418666e-f  |
|999999A9-9|002797d8-4  |
|999999A9-9|010208e9-6  |
|999999A9-9|013722b4-3  |
|999999A9-A|015467b4-c  |
|999999A9-A|022239d5-f  |
|999999A9-A|038302b1-b  |
|999999AA-9|000760fd-7  |
|999999AA-9|008549cc-4  |
|999999AA-9|013889bc-2  |
|999999AA-A|019939af-d  |
|999999AA-A|040992aa-b  |
|999999AA-A|045681eb-e  |
|99999A99-9|00496c91-8  |
|99999A99-9|01631d67-3  |
|99999A99-9|02384a60-5  |
|99999A99-A|00166f67-c  |
|99999A99-A|01927e11-d  |
|99999A99-A|03551b86-f  |
|99999A9A-9|01022b3f-9  |
|99999A9A-9|01405c3a-9  |
|99999A9A-9|02656d3c-2  |
|99999A9A-A|00838d3b-d  |
|99999A9A-A|00880a0b-c  |
|99999A9A-A|01682e4b-e  |
|99999AA9-9|01729ff8-6  |
|99999AA9-9|02175da0-2  |
|99999AA9-9|03595af3-8  |
|99999AA9-A|00413ed5-b  |
|99999AA9-A|00433aa4-c  |
|99999AA9-A|01350bd9-b  |
|99999AAA-9|00824cfd-4  |
|99999AAA-9|06438cbb-5  |
|99999AAA-9|07307bca-0  |
|99999AAA-A|02584dba-b  |
|99999AAA-A|04766edf-e  |
|99999AAA-A|05129fba-a  |
|9999A999-9|0138f992-8  |
|9999A999-9|0191e915-1  |
+----------+------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|459  |
|99999A99|305  |
|999999A9|300  |
|9A999999|277  |
|9999A999|275  |
|A9999999|274  |
|999A9999|271  |
|99A99999|271  |
|9999999A|263  |
|A999A999|208  |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00490484    |
|99999999|00523225    |
|99999999|00559501    |
|9999999A|0021277e    |
|9999999A|0021277e    |
|9999999A|0036854b    |
|999999A9|002277b1    |
|999999A9|009274b4    |
|999999A9|009274b4    |
|999999AA|014281af    |
|999999AA|014330fe    |
|999999AA|018069fe    |
|99999A99|00697f39    |
|99999A99|00963d91    |
|99999A99|01138a37    |
|99999A9A|00596a6b    |
|99999A9A|00596a6b    |
|99999A9A|01307a4f    |
|99999AA9|01268ae8    |
|99999AA9|01268ae8    |
|99999AA9|02196dd6    |
|99999AAA|00051eae    |
|99999AAA|00051eae    |
|99999AAA|00205aab    |
|9999A999|0015a687    |
|9999A999|0112b853    |
|9999A999|0112b853    |
|9999A99A|0035e91f    |
|9999A99A|0044f95c    |
|9999A99A|0224f31c    |
|9999A9A9|0005d1c3    |
|9999A9A9|0063e6d4    |
|9999A9A9|0095b6d7    |
|9999A9AA|0029e1dd    |
|9999A9AA|0090a7cd    |
|9999A9AA|0325f6ea    |
|9999AA99|0049ff76    |
|9999AA99|0115da71    |
|9999AA99|0275ff27    |
|9999AA9A|0203bb1e    |
|9999AA9A|0276db9d    |
|9999AA9A|0319ae1b    |
|9999AAA9|0040ebe3    |
|9999AAA9|0284dce9    |
|9999AAA9|0284dce9    |
|9999AAAA|0099dfce    |
|9999AAAA|0109bbcf    |
|9999AAAA|0584cefc    |
|999A9999|001b3034    |
|999A9999|008a0514    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — platform
+----------+-----+
|shape     |count|
+----------+-----+
|AAA       |10918|
|AAAAA     |2147 |
|AAAAAAA   |2143 |
|AAAAAAAA  |2125 |
|AAAAAA    |2116 |
|AAA??     |310  |
|AAAAA??   |69   |
|AAAAAAA?? |64   |
|AAAAAA??  |57   |
|AAAAAAAA??|51   |
+----------+-----+


 SAMPLE VALUES — platform
+----------+------------+
|shape     |sample_value|
+----------+------------+
|AAA       |IOS         |
|AAA       |IOS         |
|AAA       |IOS         |
|AAA??     |WEB??       |
|AAA??     |WEB??       |
|AAA??     |WEB??       |
|AAAAA     |APPLE       |
|AAAAA     |APPLE       |
|AAAAA     |APPLE       |
|AAAAA??   |APPLE??     |
|AAAAA??   |APPLE??     |
|AAAAA??   |APPLE??     |
|AAAAAA    |IPHONE      |
|AAAAAA    |IPHONE      |
|AAAAAA    |IPHONE      |
|AAAAAA??  |Iphone??    |
|AAAAAA??  |Iphone??    |
|AAAAAA??  |Iphone??    |
|AAAAAAA   |ANDROID     |
|AAAAAAA   |ANDROID     |
|AAAAAAA   |ANDROID     |
|AAAAAAA?? |Android??   |
|AAAAAAA?? |Android??   |
|AAAAAAA?? |Android??   |
|AAAAAAAA  |ANDROIDD    |
|AAAAAAAA  |ANDROIDD    |
|AAAAAAAA  |ANDROIDD    |
|AAAAAAAA??|ANDROIDD??  |
|AAAAAAAA??|ANDROIDD??  |
|AAAAAAAA??|ANDROIDD??  |
+----------+------------+


 VALUE SHAPES — device_model
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+
|shape                                                                                                                                             |count|
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA AA 9.9; AAAAAAA/9.9)                                                                                   |1943 |
|AAAAAAA/9.9 (AAAA; A; AAA AAAAAA AA 9_9 AAAA AAA AA A; AA-AA) AAAAAAAAAAA/999.99.9 (AAAAA, AAAA AAAAA) AAAAAAA/9.9.9 AAAAAA/9A999 AAAAAA/9999.99.9|809  |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                  |739  |
|AAAAA/9.99.(AAAAAAA AA 9.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                   |723  |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                |690  |
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA AA 99.9; AAAAAAA/9.9)                                                                                  |589  |
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA 99; AAAAAAA/9.9)                                                                                       |557  |
|AAAAAAA/9.9 (AAAAA; AAAAAAA 9.9.9) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9                                           |463  |
|AAAAAAA/9.9 (AAAAAAA 9.9.9; AAAAAA; AA:99.9) AAAAA/99.9 AAAAAAA/99.9                                                                              |403  |
|AAAAAAA/9.9 (AAAAAAA AA 9.9) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9                                                 |392  |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+


 SAMPLE VALUES — device_model
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|shape                                                                      |sample_value                                                               |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/8.16.(X11; LINUX I686; GU-IN) PRESTO/2.9.187 VERSION/10.00           |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/8.20.(X11; LINUX I686; BE-BY) PRESTO/2.9.169 VERSION/11.00           |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/8.20.(X11; LINUX I686; CV-RU) PRESTO/2.9.167 VERSION/10.00           |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/8.12.(X11; Linux i686; gl-ES) Presto/2.9.184 Version/11.00??         |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/8.16.(X11; Linux i686; ro-RO) Presto/2.9.189 Version/12.00??         |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/8.20.(X11; Linux i686; de-DE) Presto/2.9.170 Version/12.00??         |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99          |OPERA/8.26.(X11; LINUX I686; MAI-IN) PRESTO/2.9.171 VERSION/12.00          |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99          |OPERA/8.31.(X11; LINUX I686; WAE-CH) PRESTO/2.9.165 VERSION/12.00          |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99          |OPERA/8.33.(X11; LINUX I686; AYC-PE) PRESTO/2.9.173 VERSION/10.00          |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??        |Opera/8.10.(X11; Linux i686; doi-IN) Presto/2.9.182 Version/11.00??        |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??        |Opera/8.52.(X11; Linux i686; shs-CA) Presto/2.9.189 Version/11.00??        |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??        |Opera/8.62.(X11; Linux i686; lzh-TW) Presto/2.9.174 Version/11.00??        |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99         |OPERA/8.10.(X11; LINUX X86_64; HR-HR) PRESTO/2.9.189 VERSION/10.00         |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99         |OPERA/8.13.(X11; LINUX X86_64; AS-IN) PRESTO/2.9.181 VERSION/11.00         |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99         |OPERA/8.15.(X11; LINUX X86_64; IW-IL) PRESTO/2.9.171 VERSION/12.00         |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??       |Opera/8.12.(X11; Linux x86_64; ru-UA) Presto/2.9.186 Version/11.00??       |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??       |Opera/8.15.(X11; Linux x86_64; sv-SE) Presto/2.9.189 Version/10.00??       |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??       |Opera/8.19.(X11; Linux x86_64; it-CH) Presto/2.9.172 Version/10.00??       |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99        |OPERA/8.26.(X11; LINUX X86_64; AST-ES) PRESTO/2.9.181 VERSION/11.00        |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99        |OPERA/8.52.(X11; LINUX X86_64; RAJ-IN) PRESTO/2.9.171 VERSION/11.00        |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99        |OPERA/8.52.(X11; LINUX X86_64; SID-ET) PRESTO/2.9.162 VERSION/12.00        |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??      |Opera/8.53.(X11; Linux x86_64; cmn-TW) Presto/2.9.166 Version/10.00??      |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??      |Opera/8.54.(X11; Linux x86_64; shs-CA) Presto/2.9.168 Version/10.00??      |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??      |Opera/8.85.(X11; Linux x86_64; fur-IT) Presto/2.9.187 Version/10.00??      |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                |OPERA/9.24.(WINDOWS 95; LV-LV) PRESTO/2.9.168 VERSION/10.00                |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                |OPERA/9.28.(WINDOWS 98; XH-ZA) PRESTO/2.9.165 VERSION/11.00                |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                |OPERA/9.37.(WINDOWS 95; EL-CY) PRESTO/2.9.185 VERSION/10.00                |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??              |Opera/8.46.(Windows 98; lb-LU) Presto/2.9.182 Version/12.00??              |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??              |Opera/8.49.(Windows 95; ga-IE) Presto/2.9.166 Version/11.00??              |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??              |Opera/8.58.(Windows 95; xh-ZA) Presto/2.9.180 Version/10.00??              |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99   |OPERA/8.34.(WINDOWS 98; WIN 9X 4.90; MS-MY) PRESTO/2.9.160 VERSION/12.00   |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99   |OPERA/8.69.(WINDOWS 98; WIN 9X 4.90; AF-ZA) PRESTO/2.9.177 VERSION/12.00   |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99   |OPERA/8.83.(WINDOWS 98; WIN 9X 4.90; SK-SK) PRESTO/2.9.185 VERSION/10.00   |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99?? |Opera/8.79.(Windows 98; Win 9x 4.90; dv-MV) Presto/2.9.185 Version/12.00?? |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99?? |Opera/9.67.(Windows 98; Win 9x 4.90; sw-TZ) Presto/2.9.162 Version/11.00?? |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99?? |Opera/9.72.(Windows 98; Win 9x 4.90; ca-ES) Presto/2.9.163 Version/11.00?? |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99  |OPERA/8.22.(WINDOWS 98; WIN 9X 4.90; BYN-ER) PRESTO/2.9.190 VERSION/10.00  |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99  |OPERA/8.27.(WINDOWS 98; WIN 9X 4.90; BEM-ZM) PRESTO/2.9.166 VERSION/10.00  |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99  |OPERA/9.80.(WINDOWS 98; WIN 9X 4.90; AST-ES) PRESTO/2.9.172 VERSION/12.00  |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??|Opera/8.30.(Windows 98; Win 9x 4.90; cmn-TW) Presto/2.9.181 Version/10.00??|
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99               |OPERA/8.28.(WINDOWS 98; QUZ-PE) PRESTO/2.9.162 VERSION/12.00               |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99               |OPERA/8.43.(WINDOWS 95; KOK-IN) PRESTO/2.9.180 VERSION/12.00               |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99               |OPERA/8.59.(WINDOWS 95; MHR-RU) PRESTO/2.9.163 VERSION/12.00               |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??             |Opera/9.91.(Windows 95; hak-TW) Presto/2.9.182 Version/10.00??             |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/8.34.(WINDOWS NT 5.01; XH-ZA) PRESTO/2.9.165 VERSION/11.00           |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/8.56.(WINDOWS NT 5.01; ZH-HK) PRESTO/2.9.163 VERSION/11.00           |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99           |OPERA/9.77.(WINDOWS NT 5.01; SC-IT) PRESTO/2.9.184 VERSION/10.00           |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/8.19.(Windows NT 5.01; ik-CA) Presto/2.9.168 Version/12.00??         |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/8.68.(Windows NT 5.01; se-NO) Presto/2.9.176 Version/10.00??         |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99??         |Opera/9.25.(Windows NT 5.01; be-BY) Presto/2.9.184 Version/12.00??         |
+---------------------------------------------------------------------------+---------------------------------------------------------------------------+
only showing top 50 rows

 VALUE SHAPES — mac_addr
+-----------------+-----+
|shape            |count|
+-----------------+-----+
|99:99:99:99:99:99|57   |
|99:A9:99:99:99:99|42   |
|99:99:99:99:99:A9|42   |
|99:99:99:99:A9:99|41   |
|99:99:99:A9:99:99|41   |
|99:99:99:9A:99:99|38   |
|99:99:9A:99:99:99|38   |
|99:9A:99:99:99:99|36   |
|99:99:A9:99:99:99|33   |
|9A:99:99:99:99:99|33   |
+-----------------+-----+


 SAMPLE VALUES — mac_addr
+-----------------+-----------------+
|shape            |sample_value     |
+-----------------+-----------------+
|99:99:99:99:99:99|00:61:84:05:83:57|
|99:99:99:99:99:99|02:03:63:09:36:61|
|99:99:99:99:99:99|06:56:73:49:44:04|
|99:99:99:99:99:9A|08:39:84:75:80:4d|
|99:99:99:99:99:9A|08:76:90:91:43:5e|
|99:99:99:99:99:9A|12:01:28:27:21:0d|
|99:99:99:99:99:A9|00:37:52:91:59:d2|
|99:99:99:99:99:A9|00:90:24:09:11:a8|
|99:99:99:99:99:A9|08:20:89:95:10:c4|
|99:99:99:99:99:AA|00:24:07:38:74:da|
|99:99:99:99:99:AA|06:56:59:65:61:ea|
|99:99:99:99:99:AA|12:66:52:74:23:ab|
|99:99:99:99:9A:99|00:11:14:87:1c:85|
|99:99:99:99:9A:99|08:37:13:14:9e:77|
|99:99:99:99:9A:99|14:35:20:71:9c:54|
|99:99:99:99:9A:9A|04:70:27:78:7c:5b|
|99:99:99:99:9A:9A|14:71:66:10:6b:2a|
|99:99:99:99:9A:9A|28:64:60:09:8f:1b|
|99:99:99:99:9A:A9|06:50:72:67:1f:e1|
|99:99:99:99:9A:A9|12:65:37:90:9b:e5|
|99:99:99:99:9A:A9|12:77:72:72:2b:b5|
|99:99:99:99:9A:AA|06:64:38:48:2e:fc|
|99:99:99:99:9A:AA|08:69:67:09:4a:ef|
|99:99:99:99:9A:AA|22:32:76:69:6a:bc|
|99:99:99:99:A9:99|02:66:12:80:b1:91|
|99:99:99:99:A9:99|12:67:14:01:c4:05|
|99:99:99:99:A9:99|14:23:16:35:b6:37|
|99:99:99:99:A9:9A|02:95:28:09:a6:7d|
|99:99:99:99:A9:9A|12:95:88:90:a9:4e|
|99:99:99:99:A9:9A|16:30:70:22:b1:5d|
|99:99:99:99:A9:A9|04:58:86:29:a4:f5|
|99:99:99:99:A9:A9|08:36:02:52:d3:e0|
|99:99:99:99:A9:A9|10:86:96:27:b6:e5|
|99:99:99:99:A9:AA|00:67:41:43:e5:ab|
|99:99:99:99:A9:AA|12:30:34:82:e2:fd|
|99:99:99:99:A9:AA|16:56:69:95:d7:df|
|99:99:99:99:AA:99|00:57:21:61:bb:08|
|99:99:99:99:AA:99|00:99:35:42:da:15|
|99:99:99:99:AA:99|10:73:15:22:cd:47|
|99:99:99:99:AA:9A|12:73:96:64:ef:1f|
|99:99:99:99:AA:9A|18:19:32:85:ba:9f|
|99:99:99:99:AA:9A|26:48:60:14:bc:2c|
|99:99:99:99:AA:A9|06:00:10:45:dd:e6|
|99:99:99:99:AA:A9|08:36:21:20:ff:c1|
|99:99:99:99:AA:A9|24:92:93:28:af:b1|
|99:99:99:99:AA:AA|04:87:57:69:bc:cf|
|99:99:99:99:AA:AA|46:23:26:71:be:df|
|99:99:99:99:AA:AA|48:70:08:85:ae:ff|
|99:99:99:9A:99:99|00:40:23:2d:13:43|
|99:99:99:9A:99:99|00:88:75:7f:14:63|
+-----------------+-----------------+
only showing top 50 rows

 Discovery complete for crm_bronze_devices — scanned 20000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_events
====================================================================================================

 SCHEMA
root
 |-- event_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- event_type: string (nullable = true)
 |-- event_ts: string (nullable = true)
 |-- device_id: string (nullable = true)


 TOTAL ROWS: 1000000

 NULL COUNTS
+--------+-------+----------+--------+---------+
|event_id|user_id|event_type|event_ts|device_id|
+--------+-------+----------+--------+---------+
|0       |0      |0         |0       |150001   |
+--------+-------+----------+--------+---------+


 VALUE SHAPES — event_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|9A99A999-999A-9A9A-AA99-A9999999999A|3    |
|9A999A99-9999-9999-AA99-9A999A999999|3    |
|99999999-9999-99A9-99A9-9999999999A9|3    |
|99999999-9999-999A-9A99-999999999999|3    |
|99999A99-9999-9A99-AA99-A999999AA999|3    |
|A9A99999-AA99-99AA-9999-AA9999999A99|3    |
|9A99999A-9AAA-9999-A999-999A999999A9|3    |
|9A99A999-9999-999A-A999-A9999A999999|3    |
|A9999A9A-9999-9999-9999-999999999999|3    |
|9A999999-9999-99A9-9A99-999A99999A9A|3    |
+------------------------------------+-----+


 SAMPLE VALUES — event_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-999999999999|32164039-1321-4584-8477-472352700892|
|99999999-9999-9999-9999-999999999A99|10916025-0037-4905-9041-277286899f66|
|99999999-9999-9999-9999-999999A9AA99|15565808-9084-4163-8056-610723b1ac81|
|99999999-9999-9999-9999-9999AA99AA9A|92895989-2447-4506-8417-2607ce54fa3e|
|99999999-9999-9999-9999-9999AAA9A9A9|60784346-7711-4736-9018-9245eab1b6c4|
|99999999-9999-9999-9999-999A99999A99|95681014-4166-4852-9515-170d08984f33|
|99999999-9999-9999-9999-999A999A9999|48864152-6595-4595-8963-599c832f7409|
|99999999-9999-9999-9999-999A9A9AA999|60525938-0411-4594-8620-552b7e4fa059|
|99999999-9999-9999-9999-999AAAA99999|40326821-5650-4088-9709-576eede07685|
|99999999-9999-9999-9999-99A999A99A99|54649455-3509-4233-8192-81b549d49b00|
|99999999-9999-9999-9999-99A99AAAA9AA|64358413-2382-4852-9287-65c85cefd6ea|
|99999999-9999-9999-9999-99AA999A999A|90687783-5032-4491-9942-44dd767e554d|
|99999999-9999-9999-9999-99AA99A9AAA9|13566887-3918-4211-8426-86cf56a8eac0|
|99999999-9999-9999-9999-9A999A9AA9A9|92517594-5527-4600-8362-1b396f7ba2e0|
|99999999-9999-9999-9999-9A999AAAA999|39314843-6289-4338-8386-7d267addd752|
|99999999-9999-9999-9999-9A99A999999A|97438263-8543-4679-9636-3c61c597132e|
|99999999-9999-9999-9999-9AA99A999999|95295975-8928-4798-9146-9ff25f438916|
|99999999-9999-9999-9999-9AAAA99AA9A9|24413119-3741-4408-8514-3cfdf04ff6b0|
|99999999-9999-9999-9999-A999999AA9AA|56199688-2049-4649-9758-a508262be9fc|
|99999999-9999-9999-9999-A99999A99999|05630770-2583-4046-8905-c70811b63396|
|99999999-9999-9999-9999-A99999A99999|16021457-0942-4152-9832-f32870a73689|
|99999999-9999-9999-9999-A999A99999AA|37464155-3308-4516-8495-e046e60987fd|
|99999999-9999-9999-9999-A99A99999A99|40392325-6008-4085-9390-f52e75384c38|
|99999999-9999-9999-9999-A9A99A9999A9|58580683-2153-4655-9769-e9f73a1715b5|
|99999999-9999-9999-9999-AA99A9A99A99|58250331-4291-4174-9170-dc01d1b21b36|
|99999999-9999-9999-9999-AA9A999A999A|65537059-7552-4385-8738-fb9f077c857e|
|99999999-9999-9999-9999-AAA99A999999|86983335-2594-4321-8409-ecd39f065996|
|99999999-9999-9999-9999-AAA9A999999A|05332767-0891-4144-9592-cba5a324629a|
|99999999-9999-9999-9999-AAA9AAAAA9AA|25456456-2365-4558-8792-fdf4deefd0cf|
|99999999-9999-9999-999A-99999999999A|08548723-8805-4419-873d-58642527086b|
|99999999-9999-9999-999A-9999999A9999|77616767-4954-4910-969f-6184510d9437|
|99999999-9999-9999-999A-999A999999AA|11278963-0535-4988-972f-913c714371ad|
|99999999-9999-9999-999A-999AA99999A9|37322274-5076-4508-951d-269aa03760e9|
|99999999-9999-9999-999A-999AA9A99A9A|56856028-1074-4248-928c-173fa3d54b4a|
|99999999-9999-9999-999A-999AAAA99999|52531641-9620-4436-881b-215abcc60088|
|99999999-9999-9999-999A-99A999999A99|05498721-2144-4212-836b-38d366641f10|
|99999999-9999-9999-999A-99A9999A9999|68462921-7033-4094-999c-15e9973e4540|
|99999999-9999-9999-999A-99AA9AA9AA99|07709447-9742-4995-834d-92df5fa3ea98|
|99999999-9999-9999-999A-99AAAA9999AA|86326447-0457-4478-887d-29fefe7338de|
|99999999-9999-9999-999A-A9A999999999|66775550-5704-4978-848c-d7a938705231|
|99999999-9999-9999-999A-A9A99A999999|97209974-8421-4712-912c-f6f53e580638|
|99999999-9999-9999-999A-A9AA99A99AAA|27782208-8501-4778-979d-c4bd42e28cff|
|99999999-9999-9999-999A-A9AA9A99A999|24176229-2805-4065-815c-b3cf3b77a172|
|99999999-9999-9999-999A-A9AA9A9AA99A|19236986-2646-4728-873a-b4eb8c4fc14d|
|99999999-9999-9999-999A-A9AAAAA9999A|31780875-9203-4948-895f-b3bdfff8314d|
|99999999-9999-9999-999A-AA999999999A|24795220-2148-4328-999a-bb867561022c|
|99999999-9999-9999-999A-AA99A9999AA9|23514948-5489-4881-924d-fe83a6910bf9|
|99999999-9999-9999-999A-AA9AAA9A99A9|74317227-5898-4666-943b-da8fcc0a29b5|
|99999999-9999-9999-999A-AAAA999999A9|87131121-2592-4561-992b-cddc790356f9|
|99999999-9999-9999-999A-AAAA9A9A999A|06508699-6362-4556-973d-bfcf1b9e748c|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|23220|
|9999A999|14798|
|999999A9|14365|
|99A99999|13989|
|9A999999|13941|
|A9999999|13891|
|99999A99|13877|
|9999999A|13192|
|999A9999|13065|
|A999A999|9629 |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00047613    |
|99999999|00047613    |
|99999999|00047613    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|999999A9|002277b1    |
|999999A9|002277b1    |
|999999A9|002277b1    |
|999999AA|007073eb    |
|999999AA|007073eb    |
|999999AA|007073eb    |
|99999A99|00378d65    |
|99999A99|00378d65    |
|99999A99|00378d65    |
|99999A9A|00596a6b    |
|99999A9A|00596a6b    |
|99999A9A|00596a6b    |
|99999AA9|00150ad6    |
|99999AA9|00150ad6    |
|99999AA9|00150ad6    |
|99999AAA|00051eae    |
|99999AAA|00051eae    |
|99999AAA|00051eae    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A99A|0030d89e    |
|9999A99A|0030d89e    |
|9999A99A|0030d89e    |
|9999A9A9|0005d1c3    |
|9999A9A9|0005d1c3    |
|9999A9A9|0005d1c3    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999AA99|0002bc78    |
|9999AA99|0002bc78    |
|9999AA99|0002bc78    |
|9999AA9A|0044ed8c    |
|9999AA9A|0044ed8c    |
|9999AA9A|0044ed8c    |
|9999AAA9|0009ebd5    |
|9999AAA9|0009ebd5    |
|9999AAA9|0009ebd5    |
|9999AAAA|0099dfce    |
|9999AAAA|0099dfce    |
|9999AAAA|0099dfce    |
|999A9999|001b3034    |
|999A9999|001b3034    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — event_type
+---------------+------+
|shape          |count |
+---------------+------+
|AAAA           |222094|
|AAAAA_AAAAA    |111426|
|AAAAAA         |111308|
|AAA_AAAA       |111252|
|AAAAA_AAAAAAAAA|111214|
|AAAA_AAAA      |111031|
|AAAAAA_AAAAAAA |110863|
|AAAA_AAA       |110812|
+---------------+------+


 SAMPLE VALUES — event_type
+---------------+---------------+
|shape          |sample_value   |
+---------------+---------------+
|AAAA           |open           |
|AAAA           |open           |
|AAAA           |open           |
|AAAAAA         |signup         |
|AAAAAA         |signup         |
|AAAAAA         |signup         |
|AAAAAA_AAAAAAA |signup_started |
|AAAAAA_AAAAAAA |signup_started |
|AAAAAA_AAAAAAA |signup_started |
|AAAAA_AAAAA    |order_start    |
|AAAAA_AAAAA    |order_start    |
|AAAAA_AAAAA    |order_start    |
|AAAAA_AAAAAAAAA|ORDER_COMPLETED|
|AAAAA_AAAAAAAAA|ORDER_COMPLETED|
|AAAAA_AAAAAAAAA|ORDER_COMPLETED|
|AAAA_AAA       |OPEN_APP       |
|AAAA_AAA       |OPEN_APP       |
|AAAA_AAA       |OPEN_APP       |
|AAAA_AAAA      |VIEW_PAGE      |
|AAAA_AAAA      |VIEW_PAGE      |
|AAAA_AAAA      |VIEW_PAGE      |
|AAA_AAAA       |app_open       |
|AAA_AAAA       |app_open       |
|AAA_AAAA       |app_open       |
+---------------+---------------+


 VALUE SHAPES — event_ts
+-------------------+------+
|shape              |count |
+-------------------+------+
|AAA 99 9999 99:99  |333618|
|9999-99-99 99:99:99|333443|
|99/99/9999 99:99   |332939|
+-------------------+------+


 SAMPLE VALUES — event_ts
+-------------------+-------------------+
|shape              |sample_value       |
+-------------------+-------------------+
|99/99/9999 99:99   |01/01/2026 00:03   |
|99/99/9999 99:99   |01/01/2026 00:03   |
|99/99/9999 99:99   |01/01/2026 00:04   |
|9999-99-99 99:99:99|2025-01-06 05:42:40|
|9999-99-99 99:99:99|2025-01-06 05:44:52|
|9999-99-99 99:99:99|2025-01-06 05:45:10|
|AAA 99 9999 99:99  |Apr 01 2025 00:01  |
|AAA 99 9999 99:99  |Apr 01 2025 00:02  |
|AAA 99 9999 99:99  |Apr 01 2025 00:05  |
+-------------------+-------------------+


 VALUE SHAPES — device_id
+----------+-----+
|shape     |count|
+----------+-----+
|99999999-9|12384|
|9999999A-9|8627 |
|99999A99-9|8178 |
|99999999-A|7964 |
|999A9999-9|7798 |
|9A999999-9|7685 |
|99A99999-9|7312 |
|A9999999-9|7125 |
|9999A999-9|6952 |
|999999A9-9|6923 |
+----------+-----+


 SAMPLE VALUES — device_id
+----------+------------+
|shape     |sample_value|
+----------+------------+
|99999999-9|00024980-7  |
|99999999-9|00024980-7  |
|99999999-9|00024980-7  |
|99999999-A|00071907-a  |
|99999999-A|00071907-a  |
|99999999-A|00071907-a  |
|9999999A-9|0009066d-6  |
|9999999A-9|0009066d-6  |
|9999999A-9|0009066d-6  |
|9999999A-A|0023892f-d  |
|9999999A-A|0023892f-d  |
|9999999A-A|0023892f-d  |
|999999A9-9|002797d8-4  |
|999999A9-9|002797d8-4  |
|999999A9-9|002797d8-4  |
|999999A9-A|015467b4-c  |
|999999A9-A|015467b4-c  |
|999999A9-A|015467b4-c  |
|999999AA-9|000760fd-7  |
|999999AA-9|000760fd-7  |
|999999AA-9|000760fd-7  |
|999999AA-A|019939af-d  |
|999999AA-A|019939af-d  |
|999999AA-A|019939af-d  |
|99999A99-9|00496c91-8  |
|99999A99-9|00496c91-8  |
|99999A99-9|00496c91-8  |
|99999A99-A|00166f67-c  |
|99999A99-A|00166f67-c  |
|99999A99-A|00166f67-c  |
|99999A9A-9|01022b3f-9  |
|99999A9A-9|01022b3f-9  |
|99999A9A-9|01022b3f-9  |
|99999A9A-A|00838d3b-d  |
|99999A9A-A|00838d3b-d  |
|99999A9A-A|00838d3b-d  |
|99999AA9-9|01729ff8-6  |
|99999AA9-9|01729ff8-6  |
|99999AA9-9|01729ff8-6  |
|99999AA9-A|00413ed5-b  |
|99999AA9-A|00413ed5-b  |
|99999AA9-A|00413ed5-b  |
|99999AAA-9|00824cfd-4  |
|99999AAA-9|00824cfd-4  |
|99999AAA-9|00824cfd-4  |
|99999AAA-A|02584dba-b  |
|99999AAA-A|02584dba-b  |
|99999AAA-A|02584dba-b  |
|9999A999-9|0138f992-8  |
|9999A999-9|0138f992-8  |
+----------+------------+
only showing top 50 rows

 Discovery complete for crm_bronze_events — scanned 1000000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_geo
====================================================================================================

 SCHEMA
root
 |-- city_raw: string (nullable = true)
 |-- country_raw: string (nullable = true)
 |-- latitude: string (nullable = true)
 |-- longitude: string (nullable = true)


 TOTAL ROWS: 10000

 NULL COUNTS
+--------+-----------+--------+---------+
|city_raw|country_raw|latitude|longitude|
+--------+-----------+--------+---------+
|0       |0          |473     |505      |
+--------+-----------+--------+---------+


 VALUE SHAPES — city_raw
+----------------+-----+
|shape           |count|
+----------------+-----+
|AAAAA           |2765 |
|AA AAA          |1447 |
|AAA AAAAA       |1391 |
|AAA AA AAAAAAA  |1375 |
|AAAAAAA         |1373 |
|AAAAAAAA        |1352 |
|AAAAA??         |70   |
|AAAAAAA??       |53   |
|AAA AA AAAAAAA??|47   |
|AAA AAAAA??     |45   |
+----------------+-----+


 SAMPLE VALUES — city_raw
+----------------+----------------+
|shape           |sample_value    |
+----------------+----------------+
|AA AAA          |AL AIN          |
|AA AAA          |AL AIN          |
|AA AAA          |AL AIN          |
|AA AAA??        |Al Ain??        |
|AA AAA??        |Al Ain??        |
|AA AAA??        |Al Ain??        |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA??     |Abu Dhabi??     |
|AAA AAAAA??     |Abu Dhabi??     |
|AAA AAAAA??     |Abu Dhabi??     |
|AAAAA           |AJMAN           |
|AAAAA           |AJMAN           |
|AAAAA           |AJMAN           |
|AAAAA??         |Ajman??         |
|AAAAA??         |Ajman??         |
|AAAAA??         |Ajman??         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA??       |Sharjah??       |
|AAAAAAA??       |Sharjah??       |
|AAAAAAA??       |Sharjah??       |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA??      |Fujairah??      |
|AAAAAAAA??      |Fujairah??      |
|AAAAAAAA??      |Fujairah??      |
+----------------+----------------+


 VALUE SHAPES — country_raw
+----------------------+-----+
|shape                 |count|
+----------------------+-----+
|AAA                   |4845 |
|AAAAAA AAAA AAAAAAAA  |2492 |
|A.A.A                 |2407 |
|AAA??                 |129  |
|AAAAAA AAAA AAAAAAAA??|69   |
|A.A.A??               |58   |
+----------------------+-----+


 SAMPLE VALUES — country_raw
+----------------------+----------------------+
|shape                 |sample_value          |
+----------------------+----------------------+
|A.A.A                 |U.A.E                 |
|A.A.A                 |U.A.E                 |
|A.A.A                 |U.A.E                 |
|A.A.A??               |U.A.E??               |
|A.A.A??               |U.A.E??               |
|A.A.A??               |U.A.E??               |
|AAA                   |UAE                   |
|AAA                   |UAE                   |
|AAA                   |UAE                   |
|AAA??                 |UAE??                 |
|AAA??                 |UAE??                 |
|AAA??                 |UAE??                 |
|AAAAAA AAAA AAAAAAAA  |UNITED ARAB EMIRATES  |
|AAAAAA AAAA AAAAAAAA  |UNITED ARAB EMIRATES  |
|AAAAAA AAAA AAAAAAAA  |UNITED ARAB EMIRATES  |
|AAAAAA AAAA AAAAAAAA??|United Arab Emirates??|
|AAAAAA AAAA AAAAAAAA??|United Arab Emirates??|
|AAAAAA AAAA AAAAAAAA??|United Arab Emirates??|
+----------------------+----------------------+


 VALUE SHAPES — latitude
+------------------+-----+
|shape             |count|
+------------------+-----+
|99.999999999999999|4652 |
|99.99999999999999 |2314 |
|99.999999         |1885 |
|99.99999          |352  |
|99.9999999999999  |234  |
|99.9999           |48   |
|99.999999999999   |29   |
|99.999            |8    |
|99.99999999999    |4    |
|99.99             |1    |
+------------------+-----+


 SAMPLE VALUES — latitude
+------------------+------------------+
|shape             |sample_value      |
+------------------+------------------+
|99.99             |25.32             |
|99.999            |24.275            |
|99.999            |24.539            |
|99.999            |25.289            |
|99.9999           |24.1264           |
|99.9999           |24.1482           |
|99.9999           |24.1999           |
|99.99999          |24.10919          |
|99.99999          |24.14363          |
|99.99999          |24.14426          |
|99.999999         |24.100208         |
|99.999999         |24.101472         |
|99.999999         |24.102644         |
|99.99999999999    |24.21540289085    |
|99.99999999999    |24.27199603203    |
|99.99999999999    |25.22145338478    |
|99.999999999999   |24.045078310518   |
|99.999999999999   |24.081900797322   |
|99.999999999999   |24.146523678711   |
|99.9999999999999  |24.0045641299745  |
|99.9999999999999  |24.0203337627786  |
|99.9999999999999  |24.0313844507201  |
|99.99999999999999 |24.00101132949417 |
|99.99999999999999 |24.00153449389542 |
|99.99999999999999 |24.00218808695603 |
|99.999999999999999|24.000948414072752|
|99.999999999999999|24.001111120642882|
|99.999999999999999|24.001720134017862|
+------------------+------------------+


 VALUE SHAPES — longitude
+------------------+-----+
|shape             |count|
+------------------+-----+
|99.99999999999999 |4160 |
|99.999999         |2486 |
|99.999999999999999|1822 |
|99.99999          |484  |
|99.9999999999999  |412  |
|99.9999           |81   |
|99.999999999999   |35   |
|99.999            |8    |
|99.99999999999    |5    |
|99.9              |1    |
+------------------+-----+


 SAMPLE VALUES — longitude
+------------------+------------------+
|shape             |sample_value      |
+------------------+------------------+
|99.9              |54.5              |
|99.99             |56.34             |
|99.999            |54.452            |
|99.999            |54.729            |
|99.999            |55.414            |
|99.9999           |54.3121           |
|99.9999           |54.3599           |
|99.9999           |54.3957           |
|99.99999          |54.30014          |
|99.99999          |54.30141          |
|99.99999          |54.30174          |
|99.999999         |54.301555         |
|99.999999         |54.303346         |
|99.999999         |54.304213         |
|99.99999999999    |55.10534475548    |
|99.99999999999    |55.38467050357    |
|99.99999999999    |55.53103370663    |
|99.999999999999   |54.322244385803   |
|99.999999999999   |54.426638185951   |
|99.999999999999   |54.445730594641   |
|99.9999999999999  |54.3089261333833  |
|99.9999999999999  |54.3198278471948  |
|99.9999999999999  |54.3296992581781  |
|99.99999999999999 |54.30076098632462 |
|99.99999999999999 |54.30078054861159 |
|99.99999999999999 |54.30124219736861 |
|99.999999999999999|54.300688131224184|
|99.999999999999999|54.301151817112704|
|99.999999999999999|54.306667158142524|
+------------------+------------------+


 Discovery complete for crm_bronze_geo — scanned 10000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_order_items
====================================================================================================

 SCHEMA
root
 |-- order_item_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- product_name: string (nullable = true)
 |-- qty: string (nullable = true)
 |-- unit_price: string (nullable = true)
 |-- line_total: string (nullable = true)


 TOTAL ROWS: 359798

 NULL COUNTS
+-------------+--------+------------+---+----------+----------+
|order_item_id|order_id|product_name|qty|unit_price|line_total|
+-------------+--------+------------+---+----------+----------+
|0            |0       |0           |0  |0         |0         |
+-------------+--------+------------+---+----------+----------+


 VALUE SHAPES — order_item_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|8326 |
|99A99999|5186 |
|999A9999|5073 |
|999999A9|5059 |
|9999999A|5044 |
|99999A99|5024 |
|9A999999|5009 |
|9999A999|4975 |
|A9999999|4951 |
|A99A9999|3133 |
+--------+-----+


 SAMPLE VALUES — order_item_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00008407    |
|99999999|00024038    |
|99999999|00035621    |
|9999999A|0002978b    |
|9999999A|0006957b    |
|9999999A|0006963d    |
|999999A9|000002d5    |
|999999A9|000090f7    |
|999999A9|000250f2    |
|999999AA|000119ad    |
|999999AA|000138ad    |
|999999AA|000177eb    |
|99999A99|00023a15    |
|99999A99|00023d12    |
|99999A99|00029e44    |
|99999A9A|00042a6a    |
|99999A9A|00049b5f    |
|99999A9A|00070b6f    |
|99999AA9|00049bb9    |
|99999AA9|00077ad2    |
|99999AA9|00077fa8    |
|99999AAA|00129fbe    |
|99999AAA|00132cac    |
|99999AAA|00251daf    |
|9999A999|0000d765    |
|9999A999|0002d931    |
|9999A999|0003e067    |
|9999A99A|0010e99a    |
|9999A99A|0013b55a    |
|9999A99A|0023d54f    |
|9999A9A9|0001b5d2    |
|9999A9A9|0009b7e1    |
|9999A9A9|0011a5f5    |
|9999A9AA|0007d4dd    |
|9999A9AA|0013b7bd    |
|9999A9AA|0014b4bf    |
|9999AA99|0001fa89    |
|9999AA99|0002ba38    |
|9999AA99|0008fd40    |
|9999AA9A|0002ec7f    |
|9999AA9A|0009fa9c    |
|9999AA9A|0015cf2a    |
|9999AAA9|0010dfa4    |
|9999AAA9|0012ddc9    |
|9999AAA9|0021ded5    |
|9999AAAA|0024cfbe    |
|9999AAAA|0026efbc    |
|9999AAAA|0033cdaa    |
|999A9999|000c4624    |
|999A9999|000c5197    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|8264 |
|99A99999|5197 |
|9999999A|5188 |
|9A999999|5116 |
|A9999999|5110 |
|999A9999|5098 |
|999999A9|5080 |
|99999A99|4935 |
|9999A999|4912 |
|9A9999A9|3294 |
+--------+-----+


 SAMPLE VALUES — order_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00011393    |
|99999999|00011393    |
|99999999|00011393    |
|9999999A|0002461d    |
|9999999A|0002461d    |
|9999999A|0002461d    |
|999999A9|001127d4    |
|999999A9|001127d4    |
|999999A9|001127d4    |
|999999AA|000648dd    |
|999999AA|000648dd    |
|999999AA|000648dd    |
|99999A99|00028b78    |
|99999A99|00028b78    |
|99999A99|00093f42    |
|99999A9A|00075a5c    |
|99999A9A|00075a5c    |
|99999A9A|00075a5c    |
|99999AA9|00144dc0    |
|99999AA9|00144dc0    |
|99999AA9|00144dc0    |
|99999AAA|00018bfe    |
|99999AAA|00018bfe    |
|99999AAA|00018bfe    |
|9999A999|0008a621    |
|9999A999|0008a621    |
|9999A999|0008a621    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A9A9|0025a0d9    |
|9999A9A9|0025a0d9    |
|9999A9A9|0025a0d9    |
|9999A9AA|0016b5ea    |
|9999A9AA|0016b5ea    |
|9999A9AA|0059c4de    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034fb6a    |
|9999AAA9|0002afd2    |
|9999AAA9|0002afd2    |
|9999AAA9|0052fac2    |
|9999AAAA|0009dbff    |
|9999AAAA|0009dbff    |
|9999AAAA|0009dbff    |
|999A9999|000f8535    |
|999A9999|000f8535    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — product_name
+---------+------+
|shape    |count |
+---------+------+
|AAAAA    |233353|
|AAAAAA   |77616 |
|AAAAAAA  |39074 |
|AAAAA??  |6488  |
|AAAAAA?? |2182  |
|AAAAAAA??|1085  |
+---------+------+


 SAMPLE VALUES — product_name
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAAAA    |ABAYA       |
|AAAAA    |ABAYA       |
|AAAAA    |ABAYA       |
|AAAAA??  |Abaya??     |
|AAAAA??  |Abaya??     |
|AAAAA??  |Abaya??     |
|AAAAAA   |HOODIE      |
|AAAAAA   |HOODIE      |
|AAAAAA   |HOODIE      |
|AAAAAA?? |Hoodie??    |
|AAAAAA?? |Hoodie??    |
|AAAAAA?? |Hoodie??    |
|AAAAAAA  |BLANKET     |
|AAAAAAA  |BLANKET     |
|AAAAAAA  |BLANKET     |
|AAAAAAA??|Blanket??   |
|AAAAAAA??|Blanket??   |
|AAAAAAA??|Blanket??   |
+---------+------------+


 VALUE SHAPES — qty
+-----+------+
|shape|count |
+-----+------+
|9    |359798|
+-----+------+


 SAMPLE VALUES — qty
+-----+------------+
|shape|sample_value|
+-----+------------+
|9    |1           |
|9    |1           |
|9    |1           |
+-----+------------+


 VALUE SHAPES — unit_price
+------+------+
|shape |count |
+------+------+
|999.99|226944|
|99.99 |96713 |
|999.9 |25304 |
|99.9  |10837 |
+------+------+


 SAMPLE VALUES — unit_price
+------+------------+
|shape |sample_value|
+------+------------+
|99.9  |15.0        |
|99.9  |15.0        |
|99.9  |15.0        |
|99.99 |15.01       |
|99.99 |15.01       |
|99.99 |15.01       |
|999.9 |100.0       |
|999.9 |100.0       |
|999.9 |100.0       |
|999.99|100.01      |
|999.99|100.01      |
|999.99|100.01      |
+------+------------+


 VALUE SHAPES — line_total
+------+------+
|shape |count |
+------+------+
|999.99|260649|
|99.99 |51167 |
|999.9 |40643 |
|99.9  |7339  |
+------+------+


 SAMPLE VALUES — line_total
+------+------------+
|shape |sample_value|
+------+------------+
|99.9  |15.0        |
|99.9  |15.0        |
|99.9  |15.0        |
|99.99 |15.01       |
|99.99 |15.01       |
|99.99 |15.01       |
|999.9 |100.0       |
|999.9 |100.0       |
|999.9 |100.0       |
|999.99|100.01      |
|999.99|100.01      |
|999.99|100.01      |
+------+------------+


 Discovery complete for crm_bronze_order_items — scanned 359798 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_order_status_history
====================================================================================================

 SCHEMA
root
 |-- id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- status: string (nullable = true)
 |-- changed_ts: string (nullable = true)


 TOTAL ROWS: 250000

 NULL COUNTS
+---+--------+------+----------+
|id |order_id|status|changed_ts|
+---+--------+------+----------+
|0  |0       |0     |0         |
+---+--------+------+----------+


 VALUE SHAPES — id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|999999A9-9999-99A9-A9A9-999A99A99999|3    |
|A9A9999A-9A99-9999-99A9-9A999A99A9A9|2    |
|9A999999-AAA9-9999-9999-9A999999A999|2    |
|99999999-9A99-9999-A9A9-9999999A9999|2    |
|999999A9-A99A-99A9-999A-A9999A9A9999|2    |
|AA99AA99-A9A9-999A-99A9-A99999AA999A|2    |
|999999AA-9999-999A-A999-999A9A9A99A9|2    |
|99999999-A9A9-9A9A-9999-A9A9999A999A|2    |
|9A999A99-9999-9999-9999-AA9999A9A999|2    |
|99999999-99A9-9999-99A9-99A99999A999|2    |
+------------------------------------+-----+


 SAMPLE VALUES — id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-999999999999|18865823-1765-4519-8131-323861508825|
|99999999-9999-9999-9999-99A9A99A9999|93193369-4907-4547-8931-96f9f14e1025|
|99999999-9999-9999-9999-99AA999A9999|05528930-1505-4059-8529-86ee246d9505|
|99999999-9999-9999-9999-9AA9AAAAAAA9|83504434-2566-4380-9737-4ee4dceccaf6|
|99999999-9999-9999-9999-A999AA99A9AA|94698507-2539-4114-9568-f745ac02e6fb|
|99999999-9999-9999-9999-A99A99A999A9|98757421-8360-4680-8017-e08a27a298a0|
|99999999-9999-9999-9999-A9A999A9AA9A|83616947-3697-4878-8573-b3c736c1ff8b|
|99999999-9999-9999-9999-A9AAA9A9AA99|87819253-1892-4895-8617-c5bca8b0cb99|
|99999999-9999-9999-99A9-A999A9AAA999|03910494-6813-4920-95c9-b073e5cbf346|
|99999999-9999-9999-99A9-A9AAA9A9A999|15010134-7116-4216-98d4-c5dac4d1a618|
|99999999-9999-9999-99AA-99A99A9999A9|14101339-1969-4506-93ed-70e60f5589c9|
|99999999-9999-9999-9A99-9999A99A99A9|30244660-2700-4624-9a94-0420c52d89c1|
|99999999-9999-9999-9A99-99AAA99999A9|35290595-5735-4967-8c58-61dfe53869e4|
|99999999-9999-9999-9A99-9A99A99A9A9A|85451739-6140-4163-8d86-7d22f62e9d9e|
|99999999-9999-9999-9A99-9AAA9A99A99A|39511149-2356-4809-9c35-2fae6b43c97f|
|99999999-9999-9999-9A99-A99A99999A99|52230175-4690-4604-8d34-b76b21428b40|
|99999999-9999-9999-9A9A-99999A9AAAA9|08631904-9825-4737-9e8d-79981a2fdbd8|
|99999999-9999-9999-9A9A-A9A9A999A999|68540463-2308-4807-9c1c-e7a5f157b790|
|99999999-9999-9999-9A9A-AAA99A99AAAA|30579670-2216-4925-9e4f-dca03d07fcab|
|99999999-9999-9999-9AA9-9999999A9999|73863362-3786-4690-9ea8-8189726b9894|
|99999999-9999-9999-9AA9-AA9A999A9A99|44540071-7901-4591-8ac3-aa5c596a3c94|
|99999999-9999-9999-A999-999A99A9A99A|41764070-2610-4886-a800-798f65d8f41e|
|99999999-9999-9999-A999-99A999999999|42990519-5108-4808-a169-96c467880819|
|99999999-9999-9999-A999-99A9AAA9A999|76686347-4411-4768-a411-62d6ecf2a694|
|99999999-9999-9999-A999-99AA99999999|36721360-1982-4349-b076-32be60351646|
|99999999-9999-9999-A999-9A9AA9A9A99A|57431778-6792-4086-a977-9d4cb0e1e54c|
|99999999-9999-9999-A999-9AA999999AA9|65234736-7808-4777-a627-2bb020237af3|
|99999999-9999-9999-A999-9AA99A9A999A|43955705-3074-4267-b147-3fd87d0f937c|
|99999999-9999-9999-A999-A99A99A999AA|12999970-6487-4857-b771-c96a09a121dd|
|99999999-9999-9999-A999-AA9999AAAA99|06181046-5028-4101-a440-ee5538cadc93|
|99999999-9999-9999-A999-AA9999AAAA99|62647729-4814-4530-b977-ab2433dbeb40|
|99999999-9999-9999-A99A-999A99A9999A|34727720-3373-4555-b31c-202b05a8278d|
|99999999-9999-9999-A99A-99A999999999|11140162-6675-4310-b53c-28d849413458|
|99999999-9999-9999-A99A-9A999A9AAA9A|78743895-1679-4206-a38e-5b298d0eda3e|
|99999999-9999-9999-A99A-A9999999A99A|31611887-2554-4138-b20f-d6996261b19e|
|99999999-9999-9999-A99A-AAAA99A9AAA9|46617993-6509-4761-b60a-bbeb87b0bab2|
|99999999-9999-9999-A99A-AAAAA9A9A999|36314485-5539-4709-b17a-aaabd2c3e625|
|99999999-9999-9999-A9A9-99AA9A99AAAA|46129972-1060-4460-a1e9-24dc3e84ddbb|
|99999999-9999-9999-A9A9-9A999A999A99|53757536-6255-4251-b7e6-2f053c823a57|
|99999999-9999-9999-A9A9-9A999AA99AA9|47944633-9863-4702-a5a8-3d607de40ea7|
|99999999-9999-9999-A9A9-A99A9AAA9999|83557181-8366-4248-b6e5-b55b1aac6493|
|99999999-9999-9999-A9A9-A9A99999A999|24945755-0701-4960-a2d5-d3b35680c916|
|99999999-9999-9999-A9AA-9A99AAA9A99A|33206534-6974-4701-a9cf-9d73ecb2f30a|
|99999999-9999-9999-A9AA-9A9A9A999A9A|25796284-3658-4643-b7ef-6f0d4b616d5c|
|99999999-9999-9999-A9AA-9AA99A999999|51828139-2314-4196-a6eb-9ee50f992032|
|99999999-9999-9999-A9AA-A99AAA9A9999|61739256-3115-4920-b5da-c38aad3d2492|
|99999999-9999-9999-A9AA-AA99A9AA9AAA|77545641-8481-4165-b2fd-ae15d8cc6bde|
|99999999-9999-9999-AA99-999999A9AAA9|39953817-8884-4489-be86-793337b3bef4|
|99999999-9999-9999-AA99-99A9AA999999|15259147-2097-4727-ba86-32e0aa279004|
|99999999-9999-9999-AA99-99AA9AA9AA99|89341227-3018-4194-ae64-61cf1fb0ff13|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|5744 |
|999999A9|3604 |
|99A99999|3594 |
|9999999A|3579 |
|A9999999|3456 |
|999A9999|3413 |
|9A999999|3403 |
|99999A99|3389 |
|9999A999|3386 |
|9AA99999|2316 |
+--------+-----+


 SAMPLE VALUES — order_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00011393    |
|99999999|00049892    |
|99999999|00049892    |
|9999999A|0002461d    |
|9999999A|0002461d    |
|9999999A|0002461d    |
|999999A9|001127d4    |
|999999A9|001127d4    |
|999999A9|001127d4    |
|999999AA|001847de    |
|999999AA|001847de    |
|999999AA|002763ad    |
|99999A99|00028b78    |
|99999A99|00028b78    |
|99999A99|00028b78    |
|99999A9A|00075a5c    |
|99999A9A|00075a5c    |
|99999A9A|00075a5c    |
|99999AA9|00144dc0    |
|99999AA9|00144dc0    |
|99999AA9|00144dc0    |
|99999AAA|00018bfe    |
|99999AAA|00018bfe    |
|99999AAA|00018bfe    |
|9999A999|0008a621    |
|9999A999|0008a621    |
|9999A999|0012c603    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A99A|0026a33e    |
|9999A9A9|0025a0d9    |
|9999A9A9|0025a0d9    |
|9999A9A9|0025a0d9    |
|9999A9AA|0016b5ea    |
|9999A9AA|0016b5ea    |
|9999A9AA|0067d9ce    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034ac4e    |
|9999AAA9|0002afd2    |
|9999AAA9|0002afd2    |
|9999AAA9|0002afd2    |
|9999AAAA|0009dbff    |
|9999AAAA|0009dbff    |
|9999AAAA|0009dbff    |
|999A9999|000f8535    |
|999A9999|000f8535    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — status
+-----------+-----+
|shape      |count|
+-----------+-----+
|AAAAAAAAA  |93907|
|AAAAAAAA   |62419|
|AA_AAAAAAAA|62320|
|AAAAAAA    |31354|
+-----------+-----+


 SAMPLE VALUES — status
+-----------+------------+
|shape      |sample_value|
+-----------+------------+
|AAAAAAA    |pending     |
|AAAAAAA    |pending     |
|AAAAAAA    |pending     |
|AAAAAAAA   |COMPLETE    |
|AAAAAAAA   |COMPLETE    |
|AAAAAAAA   |COMPLETE    |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
|AA_AAAAAAAA|IN_PROGRESS |
|AA_AAAAAAAA|IN_PROGRESS |
|AA_AAAAAAAA|IN_PROGRESS |
+-----------+------------+


 VALUE SHAPES — changed_ts
+--------------------------+------+
|shape                     |count |
+--------------------------+------+
|9999-99-99 99:99:99.999999|250000|
+--------------------------+------+


 SAMPLE VALUES — changed_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2024-01-07 05:44:15.153523|
|9999-99-99 99:99:99.999999|2024-01-07 05:44:49.835555|
|9999-99-99 99:99:99.999999|2024-01-07 05:49:58.553785|
+--------------------------+--------------------------+


 Discovery complete for crm_bronze_order_status_history — scanned 250000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_orders
====================================================================================================

 SCHEMA
root
 |-- order_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- created_at: string (nullable = true)
 |-- order_status: string (nullable = true)
 |-- payment_provider: string (nullable = true)
 |-- line_total: string (nullable = true)


 TOTAL ROWS: 120000

 NULL COUNTS
+--------+-------+----------+------------+----------------+----------+
|order_id|user_id|created_at|order_status|payment_provider|line_total|
+--------+-------+----------+------------+----------------+----------+
|0       |0      |0         |0           |0               |0         |
+--------+-------+----------+------------+----------------+----------+


 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|2743 |
|99A99999|1762 |
|9999999A|1718 |
|999999A9|1696 |
|A9999999|1683 |
|9A999999|1681 |
|999A9999|1664 |
|9999A999|1631 |
|99999A99|1628 |
|9A9999A9|1089 |
+--------+-----+


 SAMPLE VALUES — order_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00011393    |
|99999999|00049892    |
|99999999|00070293    |
|9999999A|0002461d    |
|9999999A|0004751d    |
|9999999A|0013928e    |
|999999A9|001127d4    |
|999999A9|001223a8    |
|999999A9|002393c0    |
|999999AA|000648dd    |
|999999AA|001847de    |
|999999AA|002763ad    |
|99999A99|00028b78    |
|99999A99|00093f42    |
|99999A99|00139b68    |
|99999A9A|00075a5c    |
|99999A9A|00139f1b    |
|99999A9A|00168d9b    |
|99999AA9|00144dc0    |
|99999AA9|00197cf1    |
|99999AA9|00217aa1    |
|99999AAA|00018bfe    |
|99999AAA|00035aaa    |
|99999AAA|00068ffc    |
|9999A999|0008a621    |
|9999A999|0012c603    |
|9999A999|0012d106    |
|9999A99A|0013f04a    |
|9999A99A|0026a33e    |
|9999A99A|0030d61e    |
|9999A9A9|0025a0d9    |
|9999A9A9|0035a4c7    |
|9999A9A9|0057c5d5    |
|9999A9AA|0016b5ea    |
|9999A9AA|0059c4de    |
|9999A9AA|0067d9ce    |
|9999AA99|0008fd91    |
|9999AA99|0036dc35    |
|9999AA99|0040cb93    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034fb6a    |
|9999AA9A|0046ae7d    |
|9999AAA9|0002afd2    |
|9999AAA9|0052fac2    |
|9999AAA9|0053aaa5    |
|9999AAAA|0009dbff    |
|9999AAAA|0090bbfc    |
|9999AAAA|0144ecab    |
|999A9999|000f8535    |
|999A9999|001b8590    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|2788 |
|9999A999|1791 |
|999999A9|1760 |
|99A99999|1725 |
|9A999999|1650 |
|9999999A|1647 |
|99999A99|1616 |
|A9999999|1612 |
|999A9999|1611 |
|A999A999|1134 |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00047613    |
|99999999|00047613    |
|99999999|00057737    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|999999A9|002277b1    |
|999999A9|002277b1    |
|999999A9|002277b1    |
|999999AA|007073eb    |
|999999AA|007073eb    |
|999999AA|007073eb    |
|99999A99|00378d65    |
|99999A99|00697f39    |
|99999A99|00697f39    |
|99999A9A|00596a6b    |
|99999A9A|00596a6b    |
|99999A9A|00596a6b    |
|99999AA9|00150ad6    |
|99999AA9|00150ad6    |
|99999AA9|00150ad6    |
|99999AAA|00051eae    |
|99999AAA|00051eae    |
|99999AAA|00056dbd    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A99A|0030d89e    |
|9999A99A|0035e91f    |
|9999A99A|0035e91f    |
|9999A9A9|0005d1c3    |
|9999A9A9|0005d1c3    |
|9999A9A9|0005d1c3    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999AA99|0002bc78    |
|9999AA99|0002bc78    |
|9999AA99|0034cd97    |
|9999AA9A|0044ed8c    |
|9999AA9A|0044ed8c    |
|9999AA9A|0044ed8c    |
|9999AAA9|0009ebd5    |
|9999AAA9|0009ebd5    |
|9999AAA9|0040ebe3    |
|9999AAAA|0099dfce    |
|9999AAAA|0109bbcf    |
|9999AAAA|0109bbcf    |
|999A9999|001b3034    |
|999A9999|001b3034    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — created_at
+-------------------+-----+
|shape              |count|
+-------------------+-----+
|AAA 99 9999 99:99  |40314|
|9999-99-99 99:99:99|39932|
|99/99/9999 99:99   |39754|
+-------------------+-----+


 SAMPLE VALUES — created_at
+-------------------+-------------------+
|shape              |sample_value       |
+-------------------+-------------------+
|99/99/9999 99:99   |01/01/2025 00:20   |
|99/99/9999 99:99   |01/01/2025 00:29   |
|99/99/9999 99:99   |01/01/2025 00:35   |
|9999-99-99 99:99:99|2024-01-07 05:43:10|
|9999-99-99 99:99:99|2024-01-07 05:56:18|
|9999-99-99 99:99:99|2024-01-07 06:01:04|
|AAA 99 9999 99:99  |Apr 01 2024 00:13  |
|AAA 99 9999 99:99  |Apr 01 2024 00:16  |
|AAA 99 9999 99:99  |Apr 01 2024 00:26  |
+-------------------+-------------------+


 VALUE SHAPES — order_status
+-----------+-----+
|shape      |count|
+-----------+-----+
|AAAAAAAA   |34395|
|AAAAAAAAA  |34250|
|AAAA       |17167|
|AA_AAAAAAAA|17120|
|AAAAAAA    |17068|
+-----------+-----+


 SAMPLE VALUES — order_status
+-----------+------------+
|shape      |sample_value|
+-----------+------------+
|AAAA       |done        |
|AAAA       |done        |
|AAAA       |done        |
|AAAAAAA    |pending     |
|AAAAAAA    |pending     |
|AAAAAAA    |pending     |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
|AA_AAAAAAAA|in_progress |
|AA_AAAAAAAA|in_progress |
|AA_AAAAAAAA|in_progress |
+-----------+------------+


 VALUE SHAPES — payment_provider
+---------+-----+
|shape    |count|
+---------+-----+
|AAAAAA   |34263|
|AAA      |34145|
|AAAAA_AAA|17286|
|AAAAAAA  |17207|
|AAAA     |17099|
+---------+-----+


 SAMPLE VALUES — payment_provider
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAA      |Tap         |
|AAA      |Tap         |
|AAA      |Tap         |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAAAA   |STRIPE      |
|AAAAAA   |STRIPE      |
|AAAAAA   |STRIPE      |
|AAAAAAA  |stripee     |
|AAAAAAA  |stripee     |
|AAAAAAA  |stripee     |
|AAAAA_AAA|apple_pay   |
|AAAAA_AAA|apple_pay   |
|AAAAA_AAA|apple_pay   |
+---------+------------+


 VALUE SHAPES — line_total
+------------------+-----+
|shape             |count|
+------------------+-----+
|999.99            |48321|
|9999.99           |37343|
|9999.9999999999999|9148 |
|999.9999999999999 |6806 |
|999.9             |6680 |
|9999.9            |4510 |
|99.99             |3579 |
|999.99999999999999|3068 |
|99.9              |513  |
|99.99999999999999 |30   |
+------------------+-----+


 SAMPLE VALUES — line_total
+------------------+------------------+
|shape             |sample_value      |
+------------------+------------------+
|99.9              |15.7              |
|99.9              |15.8              |
|99.9              |16.2              |
|99.99             |15.02             |
|99.99             |15.05             |
|99.99             |15.05             |
|99.99999999999999 |61.82000000000001 |
|99.99999999999999 |62.18000000000001 |
|99.99999999999999 |65.21000000000001 |
|99.999999999999999|56.739999999999995|
|99.999999999999999|60.989999999999995|
|999.9             |100.2             |
|999.9             |100.3             |
|999.9             |100.3             |
|999.99            |100.03            |
|999.99            |100.03            |
|999.99            |100.04            |
|999.9999999999999 |405.6700000000001 |
|999.9999999999999 |433.5899999999999 |
|999.9999999999999 |458.2099999999999 |
|999.99999999999999|100.52000000000001|
|999.99999999999999|100.80000000000001|
|999.99999999999999|101.05000000000001|
|9999.9            |1000.2            |
|9999.9            |1000.2            |
|9999.9            |1000.3            |
|9999.99           |1000.01           |
|9999.99           |1000.04           |
|9999.99           |1000.11           |
|9999.9999999999999|1000.0699999999999|
|9999.9999999999999|1000.0699999999999|
|9999.9999999999999|1000.0799999999999|
+------------------+------------------+


 Discovery complete for crm_bronze_orders — scanned 120000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_payment_attempts
====================================================================================================

 SCHEMA
root
 |-- attempt_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- provider: string (nullable = true)
 |-- amount_attempted: string (nullable = true)
 |-- success: string (nullable = true)
 |-- attempt_ts: string (nullable = true)


 TOTAL ROWS: 80000

 NULL COUNTS
+----------+--------+--------+----------------+-------+----------+
|attempt_id|order_id|provider|amount_attempted|success|attempt_ts|
+----------+--------+--------+----------------+-------+----------+
|0         |0       |0       |0               |0      |0         |
+----------+--------+--------+----------------+-------+----------+


 VALUE SHAPES — attempt_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|999A9A99-9999-9999-A999-999A9A99A9AA|2    |
|A9999999-9999-99AA-999A-9AA9A99999A9|2    |
|99999999-999A-9A99-9999-A999999999A9|2    |
|999A999A-9999-9999-9999-A9A9999999A9|2    |
|A999A999-9AA9-9999-99AA-9999999A9A99|2    |
|9AA99AA9-999A-9999-A9A9-999A99AAAAA9|2    |
|AA9A9A99-99A9-9999-A999-99A9A9AAAA99|2    |
|9AA99AAA-A9A9-9999-9999-A9A999999A99|2    |
|AAA99999-AAA9-9A99-AA99-9A9A9999999A|1    |
|AA9A99A9-9999-9999-A9AA-A99A9A99A99A|1    |
+------------------------------------+-----+


 SAMPLE VALUES — attempt_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-99A9-99999A99AA9A|06543938-3166-4786-91a1-90728d02fa9c|
|99999999-9999-9999-99A9-9A9A9999999A|03635320-2451-4508-86a2-2b8e4361968a|
|99999999-9999-9999-99A9-A99A9999A999|95132126-6965-4145-96b8-b58a8457c678|
|99999999-9999-9999-99AA-A999A99AA99A|58252748-4200-4058-99aa-f255c14ff06e|
|99999999-9999-9999-9A99-A9A9A99999A9|87100750-5253-4936-9f30-e7f1e49172d2|
|99999999-9999-9999-9A9A-9AA99999AA99|76098950-6352-4107-9e7b-2bd45252aa05|
|99999999-9999-9999-9A9A-A999999999A9|25359156-0811-4262-8e7d-d334945517f9|
|99999999-9999-9999-A999-9999A9AA9A99|63957384-2158-4938-b947-4153f6aa4d81|
|99999999-9999-9999-A99A-A999A9AAA999|08411103-2868-4816-a39f-d148d2fbe281|
|99999999-9999-9999-A9A9-A99999A99A99|88166041-6952-4389-a9d2-b51181d65d13|
|99999999-9999-9999-A9A9-A999A9A9A9A9|38524101-8762-4562-a8e9-a655c8e3f5b0|
|99999999-9999-9999-A9A9-A9A9A9AA9999|85300255-7254-4415-b2d1-b8c1b6db9328|
|99999999-9999-9999-AA99-99A9999A99AA|01874984-8834-4378-ad27-75e0368c13ad|
|99999999-9999-9999-AA99-A999A9AAA999|12150529-1271-4708-ad41-b377f6aed048|
|99999999-9999-9999-AA9A-999999999AA9|14660881-7612-4681-af4c-898252666db7|
|99999999-9999-9999-AAA9-99AA999A99A9|62226069-4886-4519-bed4-68cc783f52f6|
|99999999-9999-999A-9999-99A99999A999|40905623-9354-490e-8179-86b15801a895|
|99999999-9999-999A-9999-AA9A9999AA99|74265551-0281-434b-9397-eb0c5077ab24|
|99999999-9999-999A-999A-999A999AAAAA|73380612-2648-443a-984e-930b653ddfdf|
|99999999-9999-999A-9A99-999999AA99AA|29372645-9520-429a-8e12-858504df78eb|
|99999999-9999-999A-A999-9A9AA99A9A9A|11181530-4233-430d-b521-3d7da95f3e5f|
|99999999-9999-999A-A999-A99999A9A99A|02499255-3465-405e-a230-a07350c7a74a|
|99999999-9999-999A-A999-A99A999999AA|58008854-5009-481f-a109-e88a265562ea|
|99999999-9999-999A-A999-AA9A9AA9AA99|32743859-8925-467f-a777-ba6e2ed3fa78|
|99999999-9999-999A-A9A9-A99A99999A99|53881678-5026-406f-b1d3-b38c90281e38|
|99999999-9999-999A-AAA9-99999999999A|01861107-4555-457d-afa3-97802993655c|
|99999999-9999-999A-AAA9-99A9A99999AA|53110345-7836-434c-aaf4-91f2c56851ca|
|99999999-9999-999A-AAA9-99A9A9A9999A|99735983-5496-437f-aff2-76f6a7d4637e|
|99999999-9999-99A9-9999-99AAAAAA9999|03336588-5671-47b4-8925-52bacdab3160|
|99999999-9999-99A9-9999-A99999AAA999|96453271-7887-46e8-8541-a73105aab568|
|99999999-9999-99A9-99A9-999999A9AAA9|18365635-0826-48c1-87a3-797714b6cbf6|
|99999999-9999-99A9-99A9-AAA99A9999A9|01593303-3859-48e1-80b2-efd55e3111d4|
|99999999-9999-99A9-A999-AA999999A999|00172465-9046-43c2-a470-ee167434b115|
|99999999-9999-99A9-A999-AA9A99999A9A|00339418-6720-49c7-b049-fc7c68778f3d|
|99999999-9999-99A9-A9A9-AAA99A999AA9|41348240-5150-46f2-a3b2-bbd74f629af5|
|99999999-9999-99A9-A9AA-A999AA9AA999|35127184-4877-45e7-b2de-c366ef9ae649|
|99999999-9999-99A9-AA9A-9A999999999A|06373284-1558-43d8-ab7c-2d251490915c|
|99999999-9999-99A9-AA9A-9A9999A9A9A9|92644107-8731-48a7-ae8a-8c6488c0f1b2|
|99999999-9999-99AA-9999-A99999999999|40274030-1218-44ac-8551-b36945623921|
|99999999-9999-99AA-999A-999AA9AA9999|06464099-8098-48fd-831e-400bf5bc5065|
|99999999-9999-99AA-99A9-9A9999999999|03487560-2753-49dc-99e3-8d9251010918|
|99999999-9999-99AA-9AA9-999999A99999|04045925-1564-44ee-9ce7-188656a25377|
|99999999-9999-99AA-A999-9999AAA9AAAA|14678935-3478-42bf-b579-1735dff5dcef|
|99999999-9999-99AA-A99A-999AA99AAAA9|93855723-9367-43ec-a79a-843ef41bfbf3|
|99999999-9999-99AA-AAA9-999AAAAAA999|78746352-9453-40af-bac6-008aadbaa920|
|99999999-9999-9A99-99AA-999AA99A99A9|26953218-1348-4a64-93bc-943ed66e04c0|
|99999999-9999-9A99-9A99-9A999A99A999|05412047-0345-4f92-9d67-8d140b66a680|
|99999999-9999-9A99-9A99-A9A99A99A99A|49873223-8197-4d30-9c27-e7e86d26d14b|
|99999999-9999-9A99-A999-999999999AA9|32916453-3850-4a71-a652-461300152ed4|
|99999999-9999-9A99-AA9A-9A99A999AAAA|73166033-4569-4d91-ac0a-5a46d917acef|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|1782 |
|9999999A|1168 |
|A9999999|1159 |
|99A99999|1153 |
|999999A9|1143 |
|999A9999|1127 |
|9999A999|1093 |
|9A999999|1086 |
|99999A99|1065 |
|9AA99999|738  |
+--------+-----+


 SAMPLE VALUES — order_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00049892    |
|99999999|00070293    |
|99999999|00186870    |
|9999999A|0004751d    |
|9999999A|0013928e    |
|9999999A|0019442f    |
|999999A9|004008d5    |
|999999A9|004008d5    |
|999999A9|004008d5    |
|999999AA|001847de    |
|999999AA|002763ad    |
|999999AA|002936cb    |
|99999A99|00216c03    |
|99999A99|00315f93    |
|99999A99|00429a00    |
|99999A9A|00168d9b    |
|99999A9A|00536a0c    |
|99999A9A|00744a6a    |
|99999AA9|00144dc0    |
|99999AA9|00432da4    |
|99999AA9|00432da4    |
|99999AAA|00035aaa    |
|99999AAA|00068ffc    |
|99999AAA|00314ebd    |
|9999A999|0008a621    |
|9999A999|0012c603    |
|9999A999|0026b190    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A9A9|0057c5d5    |
|9999A9A9|0067a0f5    |
|9999A9A9|0086e7e9    |
|9999A9AA|0016b5ea    |
|9999A9AA|0067d9ce    |
|9999A9AA|0069e0cd    |
|9999AA99|0040cb93    |
|9999AA99|0049dd67    |
|9999AA99|0049dd67    |
|9999AA9A|0034ac4e    |
|9999AA9A|0046ae7d    |
|9999AA9A|0051ea4b    |
|9999AAA9|0002afd2    |
|9999AAA9|0052fac2    |
|9999AAA9|0062dfa9    |
|9999AAAA|0214afcb    |
|9999AAAA|0331cbdf    |
|9999AAAA|0331cbdf    |
|999A9999|000f8535    |
|999A9999|001b8590    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — provider
+---------+-----+
|shape    |count|
+---------+-----+
|AAA      |23046|
|AAAAAA   |22832|
|AAAAAAA  |11444|
|AAAA     |11419|
|AAAAA_AAA|11259|
+---------+-----+


 SAMPLE VALUES — provider
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAA      |Tap         |
|AAA      |Tap         |
|AAA      |Tap         |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAAAA   |STRIPE      |
|AAAAAA   |STRIPE      |
|AAAAAA   |STRIPE      |
|AAAAAAA  |stripee     |
|AAAAAAA  |stripee     |
|AAAAAAA  |stripee     |
|AAAAA_AAA|apple_pay   |
|AAAAA_AAA|apple_pay   |
|AAAAA_AAA|apple_pay   |
+---------+------------+


 VALUE SHAPES — amount_attempted
+------+-----+
|shape |count|
+------+-----+
|999.99|59837|
|99.99 |12180|
|999.9 |6699 |
|99.9  |1284 |
+------+-----+


 SAMPLE VALUES — amount_attempted
+------+------------+
|shape |sample_value|
+------+------------+
|99.9  |20.0        |
|99.9  |20.1        |
|99.9  |20.1        |
|99.99 |20.01       |
|99.99 |20.02       |
|99.99 |20.02       |
|999.9 |100.2       |
|999.9 |100.2       |
|999.9 |100.3       |
|999.99|100.01      |
|999.99|100.01      |
|999.99|100.01      |
+------+------------+


 VALUE SHAPES — success
+-----+-----+
|shape|count|
+-----+-----+
|9    |80000|
+-----+-----+


 SAMPLE VALUES — success
+-----+------------+
|shape|sample_value|
+-----+------------+
|9    |0           |
|9    |0           |
|9    |0           |
+-----+------------+


 VALUE SHAPES — attempt_ts
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|80000|
+--------------------------+-----+


 SAMPLE VALUES — attempt_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2024-07-15 05:55:43.139122|
|9999-99-99 99:99:99.999999|2024-07-15 05:58:26.672463|
|9999-99-99 99:99:99.999999|2024-07-15 06:01:35.277973|
+--------------------------+--------------------------+


 Discovery complete for crm_bronze_payment_attempts — scanned 80000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_referrals
====================================================================================================

 SCHEMA
root
 |-- referral_id: string (nullable = true)
 |-- referrer_user_id: string (nullable = true)
 |-- referred_user_id: string (nullable = true)
 |-- referral_ts: string (nullable = true)


 TOTAL ROWS: 3000

 NULL COUNTS
+-----------+----------------+----------------+-----------+
|referral_id|referrer_user_id|referred_user_id|referral_ts|
+-----------+----------------+----------------+-----------+
|0          |0               |0               |0          |
+-----------+----------------+----------------+-----------+


 VALUE SHAPES — referral_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|9A9A9999-9A9A-9A9A-9A9A-A9AA9A999999|1    |
|99999999-99A9-9A9A-A99A-A999999999AA|1    |
|9A9999A9-999A-9A9A-A9AA-99999999999A|1    |
|9A99A99A-9A9A-9AA9-A999-A9AA9999A999|1    |
|99999999-A9A9-99A9-A999-9AA9999AA999|1    |
|9A9AA9AA-9999-9999-AAAA-99999A9A999A|1    |
|AA99AAA9-999A-99A9-AAA9-99AA9A9AAA99|1    |
|9A9A9999-9999-9A99-99AA-A9A999A99999|1    |
|A99A9999-99AA-9999-999A-99A999999AAA|1    |
|AAA99A9A-AAA9-99AA-999A-A99A9999AA9A|1    |
+------------------------------------+-----+


 SAMPLE VALUES — referral_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-99A9-9999-AAA9AA999A9A|47422145-1362-40a6-9617-dde5ff900b1b|
|99999999-9999-99A9-99AA-99A999AAA999|49188229-1679-45a4-80ba-67a196bad417|
|99999999-9999-99A9-A99A-A9A9AAAA9A9A|50153966-0855-45d5-b90b-a0c5fcfc3a3a|
|99999999-9999-99AA-A9AA-A9A9A999A9A9|02712661-1196-40ba-a2bf-b1e6b519a0d4|
|99999999-9999-9A99-9999-99A9AA9AA9AA|44691372-1249-4e14-8076-09e2cc2eb2ef|
|99999999-9999-9A99-A9A9-999AA9AA999A|83605536-7783-4d55-b0f3-501ba4bc606b|
|99999999-9999-9A99-A9A9-9A9999A99A99|24040071-9048-4a47-a8e9-9d0046e74a38|
|99999999-9999-9A99-A9AA-9AA9AA9A9A99|44104447-4394-4f49-b0ec-5af5ec1f7f27|
|99999999-9999-9A9A-9A99-99A9A9AA9A99|87439366-4428-4d5b-8c96-41e3f2db1d62|
|99999999-9999-9A9A-A999-A9A99AA9AAA9|86504816-2199-4c6b-a174-d4c14da1cae1|
|99999999-9999-9AA9-9AA9-A9A99A99AAAA|79022752-9587-4fb9-8fe6-e6a64a91edbb|
|99999999-999A-9999-A9A9-9A9AAA99999A|37594245-444a-4763-a3c0-1b7baa28174e|
|99999999-999A-99A9-9AA9-99A99A9AA999|93904612-207c-45f5-8ce0-36f04e8ec733|
|99999999-999A-99AA-9A9A-A9AAA9A9AAA9|91990804-780d-41ca-9b7a-b7ccd4e4def5|
|99999999-999A-9A99-9999-9999A9AA999A|46168125-815a-4e45-8426-1596b1bf343e|
|99999999-999A-9A9A-9A99-AAAAA9A99999|74935005-416b-4a9e-9f65-beaeb3b83385|
|99999999-99A9-9999-9A9A-99AA99AAA9AA|28539969-43a6-4486-9b6a-50ea46cad4eb|
|99999999-99A9-999A-A999-A9AAA999AA99|66727134-78c3-430b-a099-f2ebd349cd57|
|99999999-99A9-99A9-AA99-99A9A99A9A9A|82062406-90a8-40e8-ab08-08c4c55e3d6d|
|99999999-99A9-99AA-9999-999A9A9A99A9|19124047-53a3-41ab-8379-967a6e2c76f2|
|99999999-99A9-9A99-9A99-9999AA999AA9|98926257-16a5-4e55-8c48-9633cc817bb8|
|99999999-99A9-9A99-A9A9-9AA999A9A999|31166583-07a3-4a32-a1b3-0ac837b1c665|
|99999999-99A9-9A9A-A99A-A999999999AA|96309957-34d9-4d5c-b24d-d072969311ec|
|99999999-99AA-9999-A99A-A9A999A9AA99|76713361-47ac-4954-a78b-a5c092e9de96|
|99999999-99AA-99A9-AAA9-9A9AA99A9A9A|58367822-11bf-48c9-aae3-1f1cc77b5d1f|
|99999999-99AA-9AA9-9A9A-99A9A9AA9AAA|45266158-83bc-4fe0-9c2b-04f8f9ab7aee|
|99999999-9A99-9999-99AA-AA99AAA99A99|07557631-2e08-4308-92db-ae86dcc78e17|
|99999999-9A99-99A9-AA9A-A9AA999AA999|58292045-8b03-44f5-ab5e-f2bb514bb819|
|99999999-9A99-99AA-A999-99A99999999A|21302890-1c03-46be-a743-82f32501539c|
|99999999-9A99-9AA9-9999-99AAA9A999AA|81120450-0e73-4af3-8843-98bfa0a443cf|
|99999999-9A99-9AAA-A999-9AAA99AA999A|90117548-0c22-4ecf-b278-1ddc16dc264f|
|99999999-9A9A-9999-AA99-99999AAA9A9A|80562194-5d1b-4227-ba88-74308eae7f5c|
|99999999-9A9A-9A9A-A99A-AAAA99A99A99|74729002-0e2f-4e8b-b28e-bcaa51c66c75|
|99999999-9AA9-9999-AAA9-A9A9A9A99A99|94445258-6ca8-4250-aef2-e6f3f8e27f77|
|99999999-9AA9-9999-AAAA-99AAA9A9999A|71095810-9db4-4393-adcc-35cad4a3306e|
|99999999-9AA9-99AA-A9AA-AAA99A999999|14145926-0af4-44ca-a3cc-fbe30c641603|
|99999999-9AAA-999A-A99A-9A9AAAA999A9|45443065-6ecb-479d-a11f-7f0cdba969d1|
|99999999-9AAA-99A9-A999-999AA9AA9999|82804553-6feb-44d8-b592-876eb4dc5237|
|99999999-A999-9999-A9AA-AA99999999AA|45517932-e934-4725-b8fc-ef85953536dd|
|99999999-A999-9999-AA99-999A999AA999|08559565-d483-4702-af97-496f436bc552|
|99999999-A999-999A-AA99-A999A99999A9|87129377-e711-479b-ad44-a154c28642b0|
|99999999-A999-99AA-99A9-9AAAAAA99A9A|63355419-a820-47af-90e4-3ccbdae45b5c|
|99999999-A999-9A99-AA9A-9AA9999999A9|24436492-d816-4b14-aa9b-9ef7655691d7|
|99999999-A999-9A9A-A9A9-999A9999AA99|97958204-a181-4a0d-a3e8-265a8158fe86|
|99999999-A99A-9999-A999-A99A9A99AA99|71210773-a05e-4747-b314-d22d9f80ca74|
|99999999-A99A-99A9-9A99-99A999A9A99A|51955535-b22e-40f0-8a49-53b498e0b11f|
|99999999-A99A-9AAA-A999-999A99999A99|16950605-e10d-4adc-b910-529f51787d41|
|99999999-A9A9-9999-999A-A9A99A9A99A9|65752852-d1b6-4640-800b-f5f19c1e43e4|
|99999999-A9A9-9999-AA99-999A99999A99|71824283-f3f4-4477-bf95-952b22241d17|
|99999999-A9A9-999A-9AAA-AA9AA999A99A|73874234-b3e2-478e-9bdf-de9db806a31b|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — referrer_user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|86   |
|9999A999|58   |
|99999A99|56   |
|999A9999|52   |
|A9999999|52   |
|99A99999|44   |
|9A999999|42   |
|9999999A|39   |
|999999A9|38   |
|99A9999A|35   |
+--------+-----+


 SAMPLE VALUES — referrer_user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|02325011    |
|99999999|05066010    |
|99999999|06706532    |
|9999999A|0021277e    |
|9999999A|0039640b    |
|9999999A|0462994e    |
|999999A9|033954b2    |
|999999A9|058036a2    |
|999999A9|069293f3    |
|999999AA|036826de    |
|999999AA|054293bf    |
|999999AA|108955be    |
|99999A99|03351c46    |
|99999A99|03415e87    |
|99999A99|06153c49    |
|99999A9A|05688a5a    |
|99999A9A|09123e4f    |
|99999A9A|09779c3f    |
|99999AA9|01078db6    |
|99999AA9|04321dd7    |
|99999AA9|09939ef8    |
|99999AAA|07993def    |
|99999AAA|09952dab    |
|99999AAA|15284bcb    |
|9999A999|0513d432    |
|9999A999|0547e179    |
|9999A999|0605b819    |
|9999A99A|0044f95c    |
|9999A99A|0110e11e    |
|9999A99A|0224f31c    |
|9999A9A9|0165f8f7    |
|9999A9A9|0263e9d9    |
|9999A9A9|0541e5c0    |
|9999A9AA|0493d4da    |
|9999A9AA|0525a6ae    |
|9999A9AA|2026a4ef    |
|9999AA99|0027ce61    |
|9999AA99|0027ce61    |
|9999AA99|0187ad35    |
|9999AA9A|0044ed8c    |
|9999AA9A|0070df5a    |
|9999AA9A|0356ad1b    |
|9999AAA9|0009ebd5    |
|9999AAA9|0070abc0    |
|9999AAA9|0795eec0    |
|9999AAAA|2415bdda    |
|9999AAAA|2556dcfe    |
|9999AAAA|2556dcfe    |
|999A9999|050a8032    |
|999A9999|078d5872    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — referred_user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|65   |
|99A99999|47   |
|9A999999|44   |
|99AA9999|44   |
|99999A99|42   |
|9999A999|41   |
|9AA99999|39   |
|A9999999|36   |
|9999999A|35   |
|A999A999|35   |
+--------+-----+


 SAMPLE VALUES — referred_user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|02878033    |
|99999999|05000731    |
|99999999|08507420    |
|9999999A|0168790f    |
|9999999A|0839341b    |
|9999999A|0843049d    |
|999999A9|016776c5    |
|999999A9|023670a4    |
|999999A9|029367a9    |
|999999AA|028346dd    |
|999999AA|085260fd    |
|999999AA|085260fd    |
|99999A99|01138a37    |
|99999A99|06921c45    |
|99999A99|12031a50    |
|99999A9A|01565e8e    |
|99999A9A|05688a5a    |
|99999A9A|05853e2c    |
|99999AA9|02312ca5    |
|99999AA9|02866ee0    |
|99999AA9|04262ea0    |
|99999AAA|00205aab    |
|99999AAA|08214bbf    |
|99999AAA|23970dfe    |
|9999A999|0111c443    |
|9999A999|0317b748    |
|9999A999|0525a834    |
|9999A99A|0571e92f    |
|9999A99A|0696b82c    |
|9999A99A|1071c78c    |
|9999A9A9|0467c5e5    |
|9999A9A9|0665a4b2    |
|9999A9A9|0707a9e7    |
|9999A9AA|0732a8ba    |
|9999A9AA|0929d5cd    |
|9999A9AA|1186b9ab    |
|9999AA99|0303fd42    |
|9999AA99|0846de76    |
|9999AA99|1306aa22    |
|9999AA9A|0558aa9d    |
|9999AA9A|1919dd0b    |
|9999AA9A|2751df4e    |
|9999AAA9|0284dce9    |
|9999AAA9|0574bed9    |
|9999AAA9|0656bdb2    |
|9999AAAA|1944afad    |
|9999AAAA|2381face    |
|9999AAAA|2575ffdd    |
|999A9999|110a1404    |
|999A9999|110a1404    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — referral_ts
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|3000 |
+--------------------------+-----+


 SAMPLE VALUES — referral_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-01-06 05:45:48.999759|
|9999-99-99 99:99:99.999999|2025-01-06 06:19:39.019571|
|9999-99-99 99:99:99.999999|2025-01-06 09:10:17.027080|
+--------------------------+--------------------------+


 Discovery complete for crm_bronze_referrals — scanned 3000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_user_preferences
====================================================================================================

 SCHEMA
root
 |-- pref_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- pref_key: string (nullable = true)
 |-- pref_value: string (nullable = true)
 |-- updated_ts: string (nullable = true)


 TOTAL ROWS: 20000

 NULL COUNTS
+-------+-------+--------+----------+----------+
|pref_id|user_id|pref_key|pref_value|updated_ts|
+-------+-------+--------+----------+----------+
|0      |0      |0       |0         |0         |
+-------+-------+--------+----------+----------+


 VALUE SHAPES — pref_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|9999AA99-99AA-999A-AA9A-99AA999999A9|2    |
|A99AAA99-99A9-9A99-A9A9-A999A9AAA999|1    |
|AAA999A9-A999-99AA-99A9-99AA99999999|1    |
|99AA99AA-A9A9-999A-AAA9-9999AAAAA9AA|1    |
|9AA9A9AA-A9A9-9999-A99A-99A999999A99|1    |
|AA9A9999-99A9-9A9A-AAAA-99A99A9999A9|1    |
|99A9A99A-999A-9A99-99AA-9A999AA9A999|1    |
|999A9AA9-9999-9999-AA99-9999A9AA9999|1    |
|AAA99999-9A9A-99AA-A9AA-99A9AAA9AAA9|1    |
|AAA9999A-A99A-999A-A9A9-99999A9999AA|1    |
+------------------------------------+-----+


 SAMPLE VALUES — pref_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-9A9A99A9AA99|31110295-1522-4808-8418-5a7a55c2ec34|
|99999999-9999-9999-9999-9A9AA9AAAA99|32146041-3767-4738-9483-6e6cf3adcd67|
|99999999-9999-9999-9999-9AA9AAA99A9A|91256728-9366-4483-8863-7fb4dbd15c7e|
|99999999-9999-9999-999A-999AA9999AA9|36090065-1544-4534-891a-037fe6179be8|
|99999999-9999-9999-999A-9A99A9999999|43696091-7271-4735-877f-7f98b4484453|
|99999999-9999-9999-999A-AA9A9A9A9A99|55642353-0864-4271-970b-ea4b1b0b2c55|
|99999999-9999-9999-99A9-99AAA99AA99A|56643949-3634-4124-99c8-75cbc27ff54d|
|99999999-9999-9999-9A99-9999AA9999A9|75833067-3579-4296-9c35-5418ed9734b7|
|99999999-9999-9999-9A99-99AAAAAA9AAA|51546261-5138-4525-8c81-20dfcfbd5bff|
|99999999-9999-9999-9A99-A9A9AA9AAA99|62407409-9271-4896-8b54-f4c4ba2aeb41|
|99999999-9999-9999-9A99-AAA9A9AA99AA|35545563-0573-4741-9b05-fee9d6db16bd|
|99999999-9999-9999-9A9A-99A9A9999999|59767485-1978-4289-8f7d-69c3b2529020|
|99999999-9999-9999-9AAA-99999999999A|13768249-5629-4358-9cea-27166138792a|
|99999999-9999-9999-A999-999A99A99AA9|97812188-9130-4817-a554-256c44a18ce8|
|99999999-9999-9999-A9A9-99A99999A9AA|47096124-1228-4489-a3d3-24b57582c8dd|
|99999999-9999-9999-A9A9-99A99A99A9AA|19336464-2720-4414-b8c1-29a28b70b6da|
|99999999-9999-999A-9999-AA9A9A999A9A|26542582-2436-460c-9099-ae6d8b389e0d|
|99999999-9999-999A-9999-AA9A9A9A9A99|60585898-7265-425a-8722-af6d3d2b4b66|
|99999999-9999-999A-999A-A99AA9AA9A9A|88215366-9647-430a-884b-f73ef0bb4c9a|
|99999999-9999-999A-99A9-A9AAA999AAAA|00836084-7377-474d-83c0-a0efd338dada|
|99999999-9999-999A-99A9-AAA99999A999|63217611-3385-444b-80d5-faf66081c713|
|99999999-9999-999A-99AA-99AAAAA99AA9|79552855-9425-425c-98fe-21fbeef67fb1|
|99999999-9999-999A-9A99-99999AAA9A9A|45709552-6759-481d-9f68-17035cfc4b5f|
|99999999-9999-999A-9A99-99AA9999AA99|95080761-1256-420e-9c54-85ad3532cd06|
|99999999-9999-999A-9A9A-99A99AA99999|68730748-1419-492a-8c9e-98d98ae58753|
|99999999-9999-999A-9A9A-A9AAAA9A99AA|50388265-0087-450b-8f9c-f0daca7e30ef|
|99999999-9999-999A-9A9A-AAAAAA99A9AA|42137981-1200-426c-9b5e-accabd94b8ec|
|99999999-9999-999A-9AA9-AA99AAA9A999|25171355-1208-428b-8cd1-ae43afc2a566|
|99999999-9999-999A-A999-999A9AAA9A9A|36721871-0040-491e-b962-126d0ecd8c4d|
|99999999-9999-999A-A99A-AA99A9999A99|44105391-3140-434f-b16e-dc93c6229b91|
|99999999-9999-999A-A99A-AAA9AA9A9999|80473397-4608-473b-a95b-cbe3ab9a6065|
|99999999-9999-999A-AAA9-99999A999AAA|29875872-5597-492c-bce0-55044f397dfe|
|99999999-9999-999A-AAAA-9999AA9A9AA9|18670060-9264-443a-bfed-3898ff5c2cb9|
|99999999-9999-99A9-9999-9A999A99A99A|52680174-4591-47c1-8379-3b097f02f84b|
|99999999-9999-99A9-9A99-9999AA99A9A9|67702953-6155-41c5-9b53-7368ac99e9d6|
|99999999-9999-99A9-9A99-99AA9999A999|45103126-3102-42c2-8d41-46cc0870c556|
|99999999-9999-99A9-9AA9-9A999AA9999A|62958459-6193-42a2-9eb1-9f737dc6887f|
|99999999-9999-99A9-A9A9-9A999AA99A99|36549356-8266-44b7-b0f6-5f915dc82d13|
|99999999-9999-99A9-AA99-9A9AA9A9AA99|58731628-1506-41f1-af06-3d0df3d8cd66|
|99999999-9999-99A9-AAA9-99999AAA99AA|02695725-5486-44d0-bde4-90285eac62cf|
|99999999-9999-99AA-A999-AA9999A99A99|95594500-1482-47ce-a889-db0934c80d79|
|99999999-9999-99AA-A999-AA9AAAA99999|67702250-6372-43da-b829-fd0eefb32467|
|99999999-9999-99AA-A99A-9999A9999A9A|86936702-5714-43bb-a36f-5487f9540a5b|
|99999999-9999-99AA-A99A-99A9A9999999|24475880-3277-40cf-a93b-23b0c4461793|
|99999999-9999-99AA-AA99-99A99A9A9999|13511320-8713-48bf-ab83-71d90f8f0524|
|99999999-9999-99AA-AA99-A99AA9A999AA|87995330-7857-40fc-bd05-d80ff6d576db|
|99999999-9999-9A99-9999-A9A99999A9AA|01354723-4178-4e24-9667-b5a48260a3dc|
|99999999-9999-9A99-99A9-999A9999A999|25563998-7392-4d77-85b0-648d6904f672|
|99999999-9999-9A99-99A9-9A9AA9A9A999|95026621-8687-4d42-93b6-8e1ac9a1f796|
|99999999-9999-9A99-9A99-9999A9A9A999|62676843-5942-4d82-9a15-7047d4c4d747|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|503  |
|9999A999|316  |
|99A99999|298  |
|999A9999|288  |
|999999A9|283  |
|99999A99|279  |
|9A999999|267  |
|9999999A|260  |
|A9999999|250  |
|99A999A9|196  |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00047613    |
|99999999|00057737    |
|99999999|00559501    |
|9999999A|0000452f    |
|9999999A|0021277e    |
|9999999A|0034278a    |
|999999A9|009274b4    |
|999999A9|023670a4    |
|999999A9|023670a4    |
|999999AA|014330fe    |
|999999AA|018069fe    |
|999999AA|038138fc    |
|99999A99|00985c97    |
|99999A99|00985c97    |
|99999A99|01430e51    |
|99999A9A|01026c1c    |
|99999A9A|01434a5a    |
|99999A9A|01565e8e    |
|99999AA9|00733be5    |
|99999AA9|01078db6    |
|99999AA9|01078db6    |
|99999AAA|01143cbc    |
|99999AAA|01143cbc    |
|99999AAA|01597ede    |
|9999A999|0042e503    |
|9999A999|0072d454    |
|9999A999|0112b853    |
|9999A99A|0030d89e    |
|9999A99A|0079f71b    |
|9999A99A|0275b90d    |
|9999A9A9|0055b8b6    |
|9999A9A9|0055b8b6    |
|9999A9A9|0095b6d7    |
|9999A9AA|0081c4ad    |
|9999A9AA|0081c4ad    |
|9999A9AA|0104c3ff    |
|9999AA99|0002bc78    |
|9999AA99|0115da71    |
|9999AA99|0187ad35    |
|9999AA9A|0162da6d    |
|9999AA9A|0321fd0e    |
|9999AA9A|0354be1c    |
|9999AAA9|0345abb8    |
|9999AAA9|0372dfc8    |
|9999AAA9|0495dde7    |
|9999AAAA|0099dfce    |
|9999AAAA|0277adfe    |
|9999AAAA|0376abbc    |
|999A9999|004d3249    |
|999A9999|011c4142    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — pref_key
+-------------+-----+
|shape        |count|
+-------------+-----+
|AAAAAAAAAAAAA|6673 |
|AAAAAAAA     |6671 |
|AAAAAA       |6656 |
+-------------+-----+


 SAMPLE VALUES — pref_key
+-------------+-------------+
|shape        |sample_value |
+-------------+-------------+
|AAAAAA       |offers       |
|AAAAAA       |offers       |
|AAAAAA       |offers       |
|AAAAAAAA     |language     |
|AAAAAAAA     |language     |
|AAAAAAAA     |language     |
|AAAAAAAAAAAAA|notifications|
|AAAAAAAAAAAAA|notifications|
|AAAAAAAAAAAAA|notifications|
+-------------+-------------+


 VALUE SHAPES — pref_value
+-----+-----+
|shape|count|
+-----+-----+
|AA   |16037|
|AAA  |3963 |
+-----+-----+


 SAMPLE VALUES — pref_value
+-----+------------+
|shape|sample_value|
+-----+------------+
|AA   |EN          |
|AA   |EN          |
|AA   |EN          |
|AAA  |yes         |
|AAA  |yes         |
|AAA  |yes         |
+-----+------------+


 VALUE SHAPES — updated_ts
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|20000|
+--------------------------+-----+


 SAMPLE VALUES — updated_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-01-06 06:57:02.542554|
|9999-99-99 99:99:99.999999|2025-01-06 07:19:08.443867|
|9999-99-99 99:99:99.999999|2025-01-06 07:40:53.353374|
+--------------------------+--------------------------+


 Discovery complete for crm_bronze_user_preferences — scanned 20000 rows

====================================================================================================
 DISCOVERING TABLE: crm_bronze_users
====================================================================================================

 SCHEMA
root
 |-- user_id: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- signup_date: string (nullable = true)
 |-- status: string (nullable = true)
 |-- city_raw: string (nullable = true)
 |-- address_raw: string (nullable = true)


 TOTAL ROWS: 50000

 NULL COUNTS
+-------+---------+-----+-----+-----------+------+--------+-----------+
|user_id|full_name|email|phone|signup_date|status|city_raw|address_raw|
+-------+---------+-----+-----+-----------+------+--------+-----------+
|0      |0        |3498 |0    |0          |0     |0       |7547       |
+-------+---------+-----+-----+-----------+------+--------+-----------+


 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|1164 |
|9999A999|736  |
|999999A9|721  |
|99A99999|705  |
|A9999999|699  |
|99999A99|698  |
|9A999999|696  |
|999A9999|658  |
|9999999A|650  |
|A999A999|480  |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00047613    |
|99999999|00057737    |
|99999999|00264356    |
|9999999A|0000452f    |
|9999999A|0001711a    |
|9999999A|0021277e    |
|999999A9|002277b1    |
|999999A9|003069d7    |
|999999A9|003657c3    |
|999999AA|007073eb    |
|999999AA|013838da    |
|999999AA|014281af    |
|99999A99|00378d65    |
|99999A99|00697f39    |
|99999A99|00763a96    |
|99999A9A|00596a6b    |
|99999A9A|00625a9d    |
|99999A9A|00749e6f    |
|99999AA9|00150ad6    |
|99999AA9|00178ef0    |
|99999AA9|00430da3    |
|99999AAA|00051eae    |
|99999AAA|00056dbd    |
|99999AAA|00205aab    |
|9999A999|0015a687    |
|9999A999|0037b561    |
|9999A999|0042e503    |
|9999A99A|0030d89e    |
|9999A99A|0035e91f    |
|9999A99A|0044f95c    |
|9999A9A9|0005d1c3    |
|9999A9A9|0055b8b6    |
|9999A9A9|0063e6d4    |
|9999A9AA|0029e1dd    |
|9999A9AA|0081c4ad    |
|9999A9AA|0090a7cd    |
|9999AA99|0002bc78    |
|9999AA99|0027ce61    |
|9999AA99|0034cd97    |
|9999AA9A|0044ed8c    |
|9999AA9A|0070df5a    |
|9999AA9A|0102ac8b    |
|9999AAA9|0009ebd5    |
|9999AAA9|0040ebe3    |
|9999AAA9|0048aec0    |
|9999AAAA|0099dfce    |
|9999AAAA|0109bbcf    |
|9999AAAA|0183aece    |
|999A9999|001b3034    |
|999A9999|003d2384    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — full_name
+---------------+-----+
|shape          |count|
+---------------+-----+
|AAAAA AAAAAA   |3138 |
|AAAAA AAAAA    |2995 |
|AAAAAA AAAAAA  |2928 |
|AAAAAA AAAAA   |2819 |
|AAAAAAA AAAAAA |2728 |
|AAAAAAA AAAAA  |2582 |
|AAAAA AAAAAAA  |2034 |
|AAAAAA AAAAAAA |1945 |
|AAAAAAA AAAAAAA|1893 |
|AAAA AAAAAA    |1652 |
+---------------+-----+


 SAMPLE VALUES — full_name
+--------------------+--------------------+
|shape               |sample_value        |
+--------------------+--------------------+
|AA AAAA             |Jo Ruiz             |
|AA AAAAA            |Jo Berry            |
|AA AAAAAA           |Jo Keller           |
|AA AAAAAA           |Jo Miller           |
|AA AAAAAAA??        |Jo Leblanc??        |
|AA AAAAAAAA         |Jo Anderson         |
|AA. AAA AAAA        |Dr. Amy Paul        |
|AA. AAA AAAA        |Dr. Amy Tate        |
|AA. AAA AAAA AA     |Mr. Dan Ruiz MD     |
|AA. AAA AAAAA       |Ms. Joy Ellis       |
|AA. AAA AAAAAA      |Dr. Amy Nguyen      |
|AA. AAA AAAAAA      |Dr. Ana Foster      |
|AA. AAA AAAAAA      |Mr. Don Larson      |
|AA. AAA AAAAAA AA.  |Mr. Joe Nelson Jr.  |
|AA. AAA AAAAAAA     |Mr. Ray Hampton     |
|AA. AAAA AAA        |Mr. Troy Fry        |
|AA. AAAA AAAA       |Dr. Alan Wade       |
|AA. AAAA AAAA       |Dr. Jill Bush       |
|AA. AAAA AAAA       |Dr. Sean Cruz       |
|AA. AAAA AAAA AA    |Dr. Lisa Todd MD    |
|AA. AAAA AAAA AA.   |Dr. John Ward Jr.   |
|AA. AAAA AAAA AA.   |Dr. Todd Gray Jr.   |
|AA. AAAA AAAA AAA   |Mr. Ryan Boyd DDS   |
|AA. AAAA AAAAA      |Dr. Jodi Smith      |
|AA. AAAA AAAAA      |Dr. John Berry      |
|AA. AAAA AAAAA      |Dr. Jose Smith      |
|AA. AAAA AAAAA AA   |Mr. Ryan Allen MD   |
|AA. AAAA AAAAA AAA  |Dr. John Smith DVM  |
|AA. AAAA AAAAA??    |Mr. Paul Casey??    |
|AA. AAAA AAAAAA     |Dr. Adam Miller     |
|AA. AAAA AAAAAA     |Dr. Eric Torres     |
|AA. AAAA AAAAAA     |Dr. Joel Haynes     |
|AA. AAAA AAAAAA AA  |Dr. Erin Castro MD  |
|AA. AAAA AAAAAA AA  |Mr. Jack Porter II  |
|AA. AAAA AAAAAA AA  |Mr. Ryan Rivera MD  |
|AA. AAAA AAAAAA AA. |Dr. Cody Hunter Jr. |
|AA. AAAA AAAAAA AA. |MR. SEAN ARNOLD JR. |
|AA. AAAA AAAAAA AAA |Dr. Dana Torres DVM |
|AA. AAAA AAAAAA AAA |Dr. Jodi Martin PhD |
|AA. AAAA AAAAAA AAA |Mr. Dale Bailey DVM |
|AA. AAAA AAAAAA??   |Mr. John Little??   |
|AA. AAAA AAAAAAA    |DR. GINA OCONNOR    |
|AA. AAAA AAAAAAA    |DR. MARY FLEMING    |
|AA. AAAA AAAAAAA    |Dr. Joel Johnson    |
|AA. AAAA AAAAAAA AA |Mr. Mark Jackson MD |
|AA. AAAA AAAAAAA AAA|Mr. Mark Leonard III|
|AA. AAAA AAAAAAA AAA|Mr. Sean Benitez DDS|
|AA. AAAA AAAAAAA??  |Mr. Joel Montoya??  |
|AA. AAAA AAAAAAAA   |Dr. Chad Martinez   |
|AA. AAAA AAAAAAAA   |Dr. John Johnston   |
+--------------------+--------------------+
only showing top 50 rows

 VALUE SHAPES — email
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAA@AAAAAAA.AAA  |4359 |
|AAAAAAAAAAA@AAAAAAA.AAA   |4117 |
|AAAAAAAAAAAAA@AAAAAAA.AAA |3787 |
|AAAAAAAAAA@AAAAAAA.AAA    |3519 |
|AAAAAAA@AAAAAAA.AAA       |3208 |
|AAAAAAAAA@AAAAAAA.AAA     |2970 |
|AAAAA99@AAAAAAA.AAA       |2951 |
|AAAAAA@AAAAAAA.AAA        |2925 |
|AAAAAA99@AAAAAAA.AAA      |2765 |
|AAAAAAAAAAAAAA@AAAAAAA.AAA|2723 |
+--------------------------+-----+


 SAMPLE VALUES — email
+------------------------+------------------------+
|shape                   |sample_value            |
+------------------------+------------------------+
|AA99@AAAAAAA.AAA        |jo15@example.com        |
|AA99@AAAAAAA.AAA        |jo18@example.com        |
|AA99@AAAAAAA.AAA        |jo34@example.net        |
|AAA99@AAAAAAA.AAA       |amy02@example.com       |
|AAA99@AAAAAAA.AAA       |amy03@example.com       |
|AAA99@AAAAAAA.AAA       |amy03@example.org       |
|AAA@AAAAAAA.AAA         |ble@example.org         |
|AAA@AAAAAAA.AAA         |cli@example.net         |
|AAA@AAAAAAA.AAA         |fli@example.net         |
|AAAA99@AAAAAAA.AAA      |adam02@example.org      |
|AAAA99@AAAAAAA.AAA      |adam04@example.com      |
|AAAA99@AAAAAAA.AAA      |adam05@example.com      |
|AAAA@AAAAAAA.AAA        |acox@example.net        |
|AAAA@AAAAAAA.AAA        |acox@example.net        |
|AAAA@AAAAAAA.AAA        |aday@example.net        |
|AAAAA99@AAAAAAA.AAA     |aaron00@example.net     |
|AAAAA99@AAAAAAA.AAA     |aaron01@example.net     |
|AAAAA99@AAAAAAA.AAA     |aaron02@example.org     |
|AAAAA@AAAAAAA.AAA       |abass@example.com       |
|AAAAA@AAAAAAA.AAA       |abeck@example.org       |
|AAAAA@AAAAAAA.AAA       |abell@example.net       |
|AAAAAA99@AAAAAAA.AAA    |adrian05@example.com    |
|AAAAAA99@AAAAAAA.AAA    |adrian09@example.org    |
|AAAAAA99@AAAAAAA.AAA    |adrian72@example.org    |
|AAAAAA@AAAAAAA.AAA      |aadams@example.net      |
|AAAAAA@AAAAAAA.AAA      |aadams@example.net      |
|AAAAAA@AAAAAAA.AAA      |aadams@example.net      |
|AAAAAAA99@AAAAAAA.AAA   |abigail06@example.org   |
|AAAAAAA99@AAAAAAA.AAA   |abigail08@example.net   |
|AAAAAAA99@AAAAAAA.AAA   |abigail08@example.org   |
|AAAAAAA@AAAAAAA.AAA     |abailey@example.net     |
|AAAAAAA@AAAAAAA.AAA     |abarnes@example.net     |
|AAAAAAA@AAAAAAA.AAA     |abender@example.org     |
|AAAAAAAA99@AAAAAAA.AAA  |adrienne06@example.com  |
|AAAAAAAA99@AAAAAAA.AAA  |adrienne07@example.net  |
|AAAAAAAA99@AAAAAAA.AAA  |adrienne11@example.org  |
|AAAAAAAA@AAAAAAA.AAA    |aalvarez@example.com    |
|AAAAAAAA@AAAAAAA.AAA    |aanthony@example.com    |
|AAAAAAAA@AAAAAAA.AAA    |aaronlee@example.com    |
|AAAAAAAAA99@AAAAAAA.AAA |alejandra17@example.org |
|AAAAAAAAA99@AAAAAAA.AAA |alejandra71@example.com |
|AAAAAAAAA99@AAAAAAA.AAA |alejandra89@example.net |
|AAAAAAAAA@AAAAAAA.AAA   |aalvarado@example.net   |
|AAAAAAAAA@AAAAAAA.AAA   |aanderson@example.com   |
|AAAAAAAAA@AAAAAAA.AAA   |aanderson@example.com   |
|AAAAAAAAAA99@AAAAAAA.AAA|alexandria16@example.net|
|AAAAAAAAAA99@AAAAAAA.AAA|alexandria22@example.com|
|AAAAAAAAAA99@AAAAAAA.AAA|alexandria55@example.org|
|AAAAAAAAAA@AAAAAAA.AAA  |aalexander@example.com  |
|AAAAAAAAAA@AAAAAAA.AAA  |aaronbaker@example.net  |
+------------------------+------------------------+
only showing top 50 rows

 VALUE SHAPES — phone
+---------------+-----+
|shape          |count|
+---------------+-----+
|+999999999999  |48637|
|+999999999999??|1363 |
+---------------+-----+


 SAMPLE VALUES — phone
+---------------+---------------+
|shape          |sample_value   |
+---------------+---------------+
|+999999999999  |+971510000475  |
|+999999999999  |+971510001272  |
|+999999999999  |+971510004458  |
|+999999999999??|+971510264058??|
|+999999999999??|+971510326177??|
|+999999999999??|+971510353858??|
+---------------+---------------+


 VALUE SHAPES — signup_date
+----------+-----+
|shape     |count|
+----------+-----+
|9999-99-99|50000|
+----------+-----+


 SAMPLE VALUES — signup_date
+----------+------------+
|shape     |sample_value|
+----------+------------+
|9999-99-99|2023-01-07  |
|9999-99-99|2023-01-07  |
|9999-99-99|2023-01-07  |
+----------+------------+


 VALUE SHAPES — status
+--------+-----+
|shape   |count|
+--------+-----+
|AAAAAAA |25121|
|AAAAAA  |12500|
|AAAAAAAA|12379|
+--------+-----+


 SAMPLE VALUES — status
+--------+------------+
|shape   |sample_value|
+--------+------------+
|AAAAAA  |active      |
|AAAAAA  |active      |
|AAAAAA  |active      |
|AAAAAAA |BLOCKED     |
|AAAAAAA |BLOCKED     |
|AAAAAAA |BLOCKED     |
|AAAAAAAA|inactive    |
|AAAAAAAA|inactive    |
|AAAAAAAA|inactive    |
+--------+------------+


 VALUE SHAPES — city_raw
+--------------+-----+
|shape         |count|
+--------------+-----+
|AAAAA         |13817|
|AAAAAAA       |7044 |
|AAAAAAAA      |6950 |
|AAA AAAAA     |6946 |
|AA AAA        |6939 |
|AAA AA AAAAAAA|6906 |
|AAAAA??       |377  |
|AAAAAAAA??    |242  |
|AAAAAAA??     |204  |
|AA AAA??      |193  |
+--------------+-----+


 SAMPLE VALUES — city_raw
+----------------+----------------+
|shape           |sample_value    |
+----------------+----------------+
|AA AAA          |AL AIN          |
|AA AAA          |AL AIN          |
|AA AAA          |AL AIN          |
|AA AAA??        |Al Ain??        |
|AA AAA??        |Al Ain??        |
|AA AAA??        |Al Ain??        |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA  |RAS AL KHAIMAH  |
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AA AAAAAAA??|Ras Al Khaimah??|
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA       |ABU DHABI       |
|AAA AAAAA??     |Abu Dhabi??     |
|AAA AAAAA??     |Abu Dhabi??     |
|AAA AAAAA??     |Abu Dhabi??     |
|AAAAA           |AJMAN           |
|AAAAA           |AJMAN           |
|AAAAA           |AJMAN           |
|AAAAA??         |Ajman??         |
|AAAAA??         |Ajman??         |
|AAAAA??         |Ajman??         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA         |SHARJAH         |
|AAAAAAA??       |Sharjah??       |
|AAAAAAA??       |Sharjah??       |
|AAAAAAA??       |Sharjah??       |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA        |FUJAIRAH        |
|AAAAAAAA??      |Fujairah??      |
|AAAAAAAA??      |Fujairah??      |
|AAAAAAAA??      |Fujairah??      |
+----------------+----------------+


 VALUE SHAPES — address_raw
+-------------------+-----+
|shape              |count|
+-------------------+-----+
|999 AAAAAA AAAAA   |556  |
|9999 AAAAA AAAAA   |505  |
|99999 AAAAAA AAAAA |494  |
|999 AAAAA AAAAA    |493  |
|9999 AAAAAA AAAAA  |487  |
|99999 AAAAA AAAAA  |481  |
|99999 AAAAAAA AAAAA|424  |
|9999 AAAAA AAAAAA  |422  |
|9999 AAAAAA AAAAAA |420  |
|999 AAAAAA AAAAAA  |419  |
+-------------------+-----+


 SAMPLE VALUES — address_raw
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|999 AA AAAA               |483 Wu Road               |
|999 AA AAAA               |512 Wu Road               |
|999 AA AAAA               |831 Li Burg               |
|999 AA AAAAA              |285 Wu Field              |
|999 AA AAAAA              |629 Yu Cliff              |
|999 AA AAAAA              |652 Li Curve              |
|999 AA AAAAA AAA. 999     |516 Ho Lodge Apt. 341     |
|999 AA AAAAA AAA. 999     |923 Yu Creek Apt. 281     |
|999 AA AAAAA AAAAA 999    |472 Le Curve Suite 919    |
|999 AA AAAAA AAAAA 999    |941 Wu Green Suite 539    |
|999 AA AAAAAA             |377 Le Hollow             |
|999 AA AAAAAA AAA. 999    |073 Le Shores Apt. 890    |
|999 AA AAAAAA AAA. 999    |728 Yu Divide Apt. 449    |
|999 AA AAAAAA AAAAA 999   |406 Li Lights Suite 063   |
|999 AA AAAAAAA            |236 Le Viaduct            |
|999 AA AAAAAAA AAAAA 999  |173 Le Heights Suite 996  |
|999 AA AAAAAAAAA AAA. 999 |205 Yu Mountains Apt. 219 |
|999 AA AAAAAAAAA AAA. 999 |549 Jo Junctions Apt. 920 |
|999 AA AAAAAAAAA AAAAA 999|750 Wu Stravenue Suite 444|
|999 AA AAAAAAAAAA         |787 Wu Extensions         |
|999 AAA AAA               |742 Ann Row               |
|999 AAA AAA AAA. 999      |353 Day Via Apt. 280      |
|999 AAA AAA AAA. 999      |729 Orr Dam Apt. 022      |
|999 AAA AAAA              |014 Joy Pine              |
|999 AAA AAAA              |095 May Burg              |
|999 AAA AAAA              |185 Lee Club              |
|999 AAA AAAA AAA. 999     |008 Dan Loop Apt. 453     |
|999 AAA AAAA AAA. 999     |018 Amy Mill Apt. 902     |
|999 AAA AAAA AAA. 999     |082 Lee Mill Apt. 014     |
|999 AAA AAAA AAAAA 999    |186 Cox Glen Suite 716    |
|999 AAA AAAA AAAAA 999    |280 Lin Ways Suite 451    |
|999 AAA AAAA AAAAA 999    |473 Mia Road Suite 777    |
|999 AAA AAAAA             |056 Amy Inlet             |
|999 AAA AAAAA             |080 Amy Brook             |
|999 AAA AAAAA             |094 Amy Flats             |
|999 AAA AAAAA AAA. 999    |039 Key Light Apt. 196    |
|999 AAA AAAAA AAA. 999    |129 Ray Burgs Apt. 350    |
|999 AAA AAAAA AAA. 999    |264 Gay Lodge Apt. 015    |
|999 AAA AAAAA AAAAA 999   |160 Joy Curve Suite 460   |
|999 AAA AAAAA AAAAA 999   |410 Lee Field Suite 492   |
|999 AAA AAAAA AAAAA 999   |504 Don Crest Suite 048   |
|999 AAA AAAAAA            |012 Lin Tunnel            |
|999 AAA AAAAAA            |062 Ana Garden            |
|999 AAA AAAAAA            |082 Amy Forges            |
|999 AAA AAAAAA AAA. 999   |114 Cox Groves Apt. 821   |
|999 AAA AAAAAA AAA. 999   |326 Day Common Apt. 987   |
|999 AAA AAAAAA AAA. 999   |530 Ann Brooks Apt. 609   |
|999 AAA AAAAAA AAAAA 999  |074 Gay Cliffs Suite 163  |
|999 AAA AAAAAA AAAAA 999  |212 Day Groves Suite 284  |
|999 AAA AAAAAA AAAAA 999  |212 Orr Points Suite 414  |
+--------------------------+--------------------------+
only showing top 50 rows

 Discovery complete for crm_bronze_users — scanned 50000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_bronze_coupon_redemptions
====================================================================================================

 SCHEMA
root
 |-- redemption_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- promotion_code: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- redeemed_ts: string (nullable = true)


 TOTAL ROWS: 4000

 NULL COUNTS
+-------------+-------+--------------+--------+-----------+
|redemption_id|user_id|promotion_code|order_id|redeemed_ts|
+-------------+-------+--------------+--------+-----------+
|0            |0      |0             |0       |0          |
+-------------+-------+--------------+--------+-----------+


 VALUE SHAPES — redemption_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|AA999AA9-AA9A-9999-99A9-A9A99AAAAA99|1    |
|AAAA999A-9A99-999A-A999-9A99AA99AA99|1    |
|A999AAAA-A999-999A-999A-9A999AAAAA99|1    |
|A9A99999-999A-9A9A-A999-99999AA99999|1    |
|9AA999A9-99A9-9A9A-AAAA-9A99A999A9A9|1    |
|9AA99999-9999-99AA-A999-A99A9A9AA999|1    |
|A9A99999-AAA9-9999-A999-A9A99A99A9A9|1    |
|999999A9-999A-999A-9999-999999A99AA9|1    |
|999AAAA9-AA99-9A99-A999-99A999A999AA|1    |
|AAAAA9A9-AA99-9AA9-AA99-99999999999A|1    |
+------------------------------------+-----+


 SAMPLE VALUES — redemption_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-99999999A9AA|43679831-9490-4798-9626-43195960c7be|
|99999999-9999-999A-9999-99A99A9999A9|11834351-0193-498c-8502-19f35d9811a9|
|99999999-9999-999A-999A-99999999999A|56508144-4776-411c-938a-72558921983c|
|99999999-9999-999A-9AA9-A9AA9AA99A9A|55267405-2802-440f-8fa9-f0de4cc32c4b|
|99999999-9999-999A-A99A-9A9A9A99999A|31045632-9956-419c-a43e-1b8c2a98302a|
|99999999-9999-99AA-AA99-99A999A999A9|52203343-1222-43bc-ad92-92f268a772a5|
|99999999-9999-99AA-AA99-AA9AA9A9999A|98390412-4471-40fa-ab64-be4bf6e5351d|
|99999999-9999-9A99-A9AA-9AA9A999999A|32927183-9571-4c49-b9fc-3ea6e242309d|
|99999999-9999-9AA9-9A99-99A99A9A999A|54688010-9458-4ae1-9c53-77b41d6f765c|
|99999999-9999-9AA9-A999-AA9999AA99A9|65192316-4249-4bf2-a738-cf2364ab26b8|
|99999999-9999-9AA9-AA99-AA9A99A99A9A|48004822-7888-4df8-ba47-aa7f72d80e9d|
|99999999-999A-999A-99A9-A999999A9999|15292781-716d-416b-89c0-d778388d3709|
|99999999-999A-999A-99A9-A99A9AA9AA9A|62926881-327b-477b-86d4-e33e2ed6fb5c|
|99999999-999A-999A-A999-9AAA9A999A99|29233144-657d-405a-a141-7eae7b599f10|
|99999999-999A-99A9-9999-9AAAA9999A9A|61338885-932a-44d5-8355-2dcff9359a4e|
|99999999-999A-99A9-9A99-AAA9999AA9A9|31323980-920e-42b4-9c16-bfc4559af5f3|
|99999999-999A-99AA-99A9-A9999AA9999A|04765013-819d-49ba-89c5-c3736cb4016a|
|99999999-999A-9A9A-AA9A-9999999AA9AA|33197871-593c-4d2d-ba0d-3994579dc5ef|
|99999999-99A9-9999-99A9-999A99A9AA9A|86255381-32f7-4591-86f0-296e45b0ba7c|
|99999999-99A9-999A-A9A9-99AA9A9A99A9|82023529-20d1-487f-a1c5-19ea9b9b50b5|
|99999999-99A9-99A9-A999-9A9A9999A9AA|58315929-65b4-45f0-a042-0f3b3601b3fb|
|99999999-99A9-9A99-AA99-A99A999A9AA9|98408471-61b2-4a13-bb72-a22c514b7fc5|
|99999999-99A9-9A99-AAA9-A99A99A9A999|51017164-18b1-4d29-bbf8-d30a66e9e749|
|99999999-99A9-9AA9-99A9-9AAAA99A999A|30909637-81e3-4cb8-89e6-9fbed10b474b|
|99999999-99A9-9AA9-A999-999AA9AA9AA9|45575677-24f8-4ad1-a879-974ac6ae9ee0|
|99999999-99AA-9999-A9A9-9999999A999A|61490467-68fe-4424-a2c8-8892721e209e|
|99999999-99AA-99A9-9A99-99A9A9A999A9|29564878-45fe-42c1-8b28-97a4d7c897c5|
|99999999-99AA-99A9-AAAA-999AA999AA99|90544474-71dd-42b2-bbea-554cd433ec24|
|99999999-99AA-9A9A-999A-A99A99A99999|79603305-46ef-4d5a-827d-d22b82a35063|
|99999999-9A99-9999-99AA-9AAAA9A99999|24786909-2d80-4939-81af-7eeaa4c71631|
|99999999-9A99-9999-9A99-A9999A9999A9|89383480-3d51-4707-9f85-a6201a0749d7|
|99999999-9A99-9999-A999-9AAA999A99A9|48859594-6b58-4617-b044-5fcd582d63b2|
|99999999-9A99-9999-A999-A99AAA999999|15293113-5b50-4980-b371-d82fff459178|
|99999999-9A99-999A-99A9-999A99999A99|86551032-5d96-408a-80c0-199f27191e33|
|99999999-9A99-999A-99A9-A99A999AAAA9|51557418-7f89-417e-87e9-c32f825dafc3|
|99999999-9A99-999A-AAA9-AA9AAAA99AAA|54916437-3f23-480f-aae6-fb2ffee13acf|
|99999999-9A99-99A9-99A9-99AA9A999AA9|72167787-1c60-45c2-88a5-86cb9f881be7|
|99999999-9A99-99A9-9A99-99AAA999A99A|30282632-2e14-42d0-8d21-83dfc174a73e|
|99999999-9A99-9A9A-9999-AAA99AAA9999|57924095-7c10-4f8a-9913-dff72bed7421|
|99999999-9A99-9AA9-99AA-99999AA99AA9|72728812-2d89-4fb4-83bf-31945cc77bd7|
|99999999-9A99-9AAA-AA9A-999A99A999AA|52398055-2a11-4bfc-ae8e-362a18b073cb|
|99999999-9A9A-99A9-999A-9999AA9AA9A9|87045499-7e3d-41d0-903e-1099eb5ce4f9|
|99999999-9A9A-9A9A-9A99-9A9AA99AA9A9|53078654-7d5c-4e8f-8d96-9d0de03bb0e6|
|99999999-9A9A-9AA9-9999-99A9AA9A9AA9|34738936-9d8c-4cf5-8107-78e8bd8c4da9|
|99999999-9AA9-9999-A999-A99A9A9999A9|61000048-4cb3-4804-b663-c44c8f6274b0|
|99999999-9AA9-9999-A9A9-AA9AA99999AA|29196670-7be0-4354-b8f9-ae5bb16094bf|
|99999999-9AA9-9999-AA9A-9A999999AA9A|28197731-9cc4-4165-ae8e-8f523686ba9e|
|99999999-9AA9-999A-A999-99AA9AAA9AA9|03484481-1ce4-441a-a389-00fd0ffd6ac9|
|99999999-9AA9-99A9-A999-999A99AAA999|03807760-9ce3-41e4-b435-375f90dfb051|
|99999999-9AA9-9A99-A9A9-99AA99AAAAA9|50481828-0db0-4a49-b2a6-77cd71fdebd8|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|102  |
|9999A999|63   |
|999999A9|58   |
|A9999999|54   |
|99999A99|54   |
|99A99999|54   |
|9A999999|50   |
|999A9999|46   |
|9999999A|46   |
|99AA9999|44   |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00490484    |
|99999999|02534218    |
|99999999|03109354    |
|9999999A|0074313b    |
|9999999A|0113870f    |
|9999999A|0348016e    |
|999999A9|016195d9    |
|999999A9|023670a4    |
|999999A9|025459f5    |
|999999AA|036826de    |
|999999AA|059398bb    |
|999999AA|065256bf    |
|99999A99|02800d25    |
|99999A99|04269d29    |
|99999A99|04863f86    |
|99999A9A|00625a9d    |
|99999A9A|01434a5a    |
|99999A9A|11283c0e    |
|99999AA9|01078db6    |
|99999AA9|02312ca5    |
|99999AA9|02312ca5    |
|99999AAA|00051eae    |
|99999AAA|00056dbd    |
|99999AAA|01683adf    |
|9999A999|0037b561    |
|9999A999|0431a948    |
|9999A999|0809d070    |
|9999A99A|0249a09a    |
|9999A99A|0571e92f    |
|9999A99A|0608f79b    |
|9999A9A9|0165f8f7    |
|9999A9A9|0397d7f0    |
|9999A9A9|1928a4e3    |
|9999A9AA|0387a1bb    |
|9999A9AA|2599b6ee    |
|9999A9AA|2835c7db    |
|9999AA99|1118cb40    |
|9999AA99|1479cd74    |
|9999AA99|1740bd02    |
|9999AA9A|0276db9d    |
|9999AA9A|0319ae1b    |
|9999AA9A|1010ec2e    |
|9999AAA9|1902fed2    |
|9999AAA9|4068ffd1    |
|9999AAA9|4462bbf1    |
|9999AAAA|0474edff    |
|9999AAAA|0794fabb    |
|9999AAAA|0843ceec    |
|999A9999|022f0905    |
|999A9999|086d8965    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — promotion_code
+---------+-----+
|shape    |count|
+---------+-----+
|AAAAA9999|4000 |
+---------+-----+


 SAMPLE VALUES — promotion_code
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAAAA9999|PROMO0000   |
|AAAAA9999|PROMO0000   |
|AAAAA9999|PROMO0000   |
+---------+------------+


 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|85   |
|9999A999|65   |
|9999999A|59   |
|99A99999|59   |
|9A999999|57   |
|999A9999|55   |
|99999A99|55   |
|999999A9|53   |
|A9999999|46   |
|9999A99A|46   |
+--------+-----+


 SAMPLE VALUES — order_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|01434851    |
|99999999|04444192    |
|99999999|05633841    |
|9999999A|0300173e    |
|9999999A|0363985f    |
|9999999A|0474291b    |
|999999A9|033217e4    |
|999999A9|034786b7    |
|999999A9|075185f3    |
|999999AA|021190da    |
|999999AA|144411cb    |
|999999AA|148956dd    |
|99999A99|00315f93    |
|99999A99|02683c89    |
|99999A99|03083d46    |
|99999A9A|02244b3b    |
|99999A9A|04596a7d    |
|99999A9A|04938c4c    |
|99999AA9|00857ad1    |
|99999AA9|01096fe2    |
|99999AA9|01907ad5    |
|99999AAA|00314ebd    |
|99999AAA|04548cdc    |
|99999AAA|05681cda    |
|9999A999|0163e163    |
|9999A999|0220b090    |
|9999A999|0344a738    |
|9999A99A|0013f04a    |
|9999A99A|0309d41a    |
|9999A99A|0396a39e    |
|9999A9A9|0091f4f8    |
|9999A9A9|0256f2c2    |
|9999A9A9|0285d6e9    |
|9999A9AA|0138a2ad    |
|9999A9AA|0562d4bd    |
|9999A9AA|0707d2ac    |
|9999AA99|0476fc81    |
|9999AA99|1042be19    |
|9999AA99|1150cb22    |
|9999AA9A|0342db3e    |
|9999AA9A|0681cf6e    |
|9999AA9A|0696af7d    |
|9999AAA9|0201dfe4    |
|9999AAA9|1329cdf9    |
|9999AAA9|1612adf7    |
|9999AAAA|0901acbb    |
|9999AAAA|1003adad    |
|9999AAAA|1208bbdf    |
|999A9999|007e7765    |
|999A9999|017a5856    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — redeemed_ts
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|4000 |
+--------------------------+-----+


 SAMPLE VALUES — redeemed_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-01-06 08:07:56.841333|
|9999-99-99 99:99:99.999999|2025-01-06 10:32:33.771227|
|9999-99-99 99:99:99.999999|2025-01-06 11:43:29.842640|
+--------------------------+--------------------------+


 Discovery complete for mkt_bronze_coupon_redemptions — scanned 4000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_bronze_marketing_attribution
====================================================================================================

 SCHEMA
root
 |-- attrib_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- channel: string (nullable = true)
 |-- campaign: string (nullable = true)
 |-- medium: string (nullable = true)
 |-- source: string (nullable = true)
 |-- touch_ts: string (nullable = true)


 TOTAL ROWS: 80000

 NULL COUNTS
+---------+-------+-------+--------+------+------+--------+
|attrib_id|user_id|channel|campaign|medium|source|touch_ts|
+---------+-------+-------+--------+------+------+--------+
|0        |0      |0      |0       |0     |0     |0       |
+---------+-------+-------+--------+------+------+--------+


 VALUE SHAPES — attrib_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|9AA99A99-9999-9AAA-AA9A-9A9A999999A9|2    |
|99999999-9A99-99A9-99A9-999A9A9AAA99|2    |
|99A999AA-9999-99A9-9A99-9A9AA9AA9999|2    |
|99999999-9999-9AA9-9999-A9A99AAA9999|2    |
|999A99A9-A99A-9999-9999-9999999A9999|2    |
|9999A999-99A9-9999-9999-999A9A9999A9|2    |
|9A999999-999A-9A99-99A9-9AAAAA99AA9A|2    |
|A9A99999-9999-9A99-9999-9999A9A9999A|2    |
|99A9AA9A-9999-9A99-AAA9-99A99AA99A99|1    |
|9AAA9A99-9A9A-99A9-A999-9AA9A999AA99|1    |
+------------------------------------+-----+


 SAMPLE VALUES — attrib_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-999AA999A999|99632125-7551-4588-8021-110ec349a416|
|99999999-9999-9999-9999-9A99AAA99AA9|35595636-3928-4804-9312-4a46acf31bd7|
|99999999-9999-9999-9999-A999999AA9AA|38582945-6029-4277-9728-e282348af1ea|
|99999999-9999-9999-99AA-99A999AA99A9|64551338-8726-4691-88be-09a877cf08a5|
|99999999-9999-9999-99AA-99AA99A99AA9|49117909-3261-4069-89df-56cf43f88dc6|
|99999999-9999-9999-9A9A-9999A9A999AA|85881192-8940-4111-9a9e-8891b2f390ea|
|99999999-9999-9999-9A9A-99A9999AA9A9|01176982-2296-4345-9e6a-13c7705cf9d8|
|99999999-9999-9999-9AAA-9A9A9A99A99A|51584008-3640-4494-9cbc-6f1e4a23b89b|
|99999999-9999-9999-A999-999AA9AA99A9|23888871-4054-4862-a273-782fc8aa68f7|
|99999999-9999-9999-A999-9A999A99A99A|42842984-6855-4555-a385-4c284a15d16b|
|99999999-9999-9999-A999-A99999A99999|31666906-0547-4695-a160-b59341a49665|
|99999999-9999-9999-A999-A9A9999999A9|71989784-3890-4277-a689-b8d6207015c1|
|99999999-9999-9999-A99A-A99A99A99A99|12621038-7317-4884-b14e-f06f38c76d72|
|99999999-9999-9999-A9A9-999AA9A9AA9A|57447324-2426-4408-a8f4-661fb6e1de9a|
|99999999-9999-9999-A9A9-A9A9A9999A9A|47332443-8651-4066-b9c1-b8d3c8490c0a|
|99999999-9999-9999-A9AA-99999AA9999A|50038787-3700-4716-b8fc-09885aa9564b|
|99999999-9999-9999-A9AA-99AA99AA99A9|42798767-9546-4246-b9ae-84eb14ff90f3|
|99999999-9999-9999-AA9A-A9AAAA99999A|54702930-9099-4049-ac8d-d3aedb64698e|
|99999999-9999-9999-AAA9-AA9A999999A9|15942675-4404-4609-bde0-fd7b680126e5|
|99999999-9999-9999-AAAA-A9AAA9AA9999|65285485-4295-4869-bfdc-b8eec8ee2007|
|99999999-9999-999A-9999-999999A9999A|91358159-9020-430d-8067-520343c2470c|
|99999999-9999-999A-9999-9A999999A999|91288908-6184-465b-8923-6f552743a706|
|99999999-9999-999A-9999-9AA9A9A99A9A|15130431-2682-477f-8174-6ed0f5d54c3a|
|99999999-9999-999A-999A-999AA9999999|86820017-6618-457a-986d-529fb9301966|
|99999999-9999-999A-99A9-999A9AA9A9A9|98791824-7867-465f-94c4-255e8eb1e1b5|
|99999999-9999-999A-9A9A-9A999A9A9A99|94936773-3920-429d-9b2b-9c114c7b8a25|
|99999999-9999-999A-9AA9-AAA9999999A9|20749538-5524-489f-8db9-cfb6328858c1|
|99999999-9999-999A-A999-AAA999AA9A99|74983835-5825-424c-a903-afd358dd1f34|
|99999999-9999-999A-A99A-A9999999A999|77395975-8830-412f-a84b-a0749804f878|
|99999999-9999-99A9-9999-99AA9AAA999A|97675818-6208-41b1-8507-53ed7bcb197c|
|99999999-9999-99A9-99A9-A99A9A9A9A99|91488129-6111-49f4-85d0-b23d4e7e3a55|
|99999999-9999-99A9-9A99-9AA9999AAAA9|91065338-8876-43c1-9a60-2cb9778afbd3|
|99999999-9999-99A9-9A99-9AAAAAAA9999|93386624-0527-44f2-9c16-4cbcbdbf4915|
|99999999-9999-99A9-9AA9-999999999AA9|49537632-1852-45b7-9fb1-407291722bc9|
|99999999-9999-99A9-A9A9-9AA9A9A999A9|04657688-1995-40e2-b7e8-5df1d4f009b1|
|99999999-9999-99A9-AA99-9AAA999AA9AA|77730038-0068-42d9-bf84-4bab515dc6bc|
|99999999-9999-99A9-AAA9-999A999A9A99|71240361-1910-47b5-bbd8-953e555c3d72|
|99999999-9999-99A9-AAA9-9A99A9A99A9A|38372818-6523-42c7-bfe5-0b12e7f14b9c|
|99999999-9999-99AA-99A9-99AA999A9999|75666452-6105-48bc-82e8-31cd847e0968|
|99999999-9999-99AA-9AA9-A9AA999AA999|03828438-3894-44ab-8cc6-a6ad009bc680|
|99999999-9999-99AA-A999-99999A9AA9AA|94600514-1298-48eb-a022-34551c1aa4bd|
|99999999-9999-99AA-A99A-A99A999AA999|27487158-8628-44ae-b91d-f23a993dd970|
|99999999-9999-99AA-AAA9-A99A9AAA9999|19904966-4859-45ca-afa7-d75d6bda7378|
|99999999-9999-9A99-99A9-999A999A9A99|99219281-3724-4c64-92c3-275c265f5e68|
|99999999-9999-9A99-99A9-A99AA9AA99A9|11086595-1565-4d31-81d8-d94bc3bb19d5|
|99999999-9999-9A99-99AA-9999AA99A9AA|29784216-2564-4f01-86fd-3037ec08d3ce|
|99999999-9999-9A99-99AA-A999A9AA9999|73151545-9596-4f57-91df-d205b5be7377|
|99999999-9999-9A99-9A9A-A999AA9999A9|45155407-0062-4c83-8c4c-a988af3443e9|
|99999999-9999-9A99-9AA9-9999999A9999|45967479-1262-4c10-9ce4-3383839e3431|
|99999999-9999-9A99-A999-9A9A9999AA99|59315098-1451-4a97-b389-2c0d7259dc47|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|1807 |
|9999A999|1174 |
|A9999999|1167 |
|99A99999|1165 |
|99999A99|1103 |
|999999A9|1094 |
|9A999999|1077 |
|999A9999|1042 |
|9999999A|1021 |
|999999AA|765  |
+--------+-----+


 SAMPLE VALUES — user_id
+--------+------------+
|shape   |sample_value|
+--------+------------+
|99999999|00047613    |
|99999999|00047613    |
|99999999|00047613    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|9999999A|0000452f    |
|999999A9|002277b1    |
|999999A9|003069d7    |
|999999A9|003069d7    |
|999999AA|007073eb    |
|999999AA|007073eb    |
|999999AA|013838da    |
|99999A99|00378d65    |
|99999A99|00697f39    |
|99999A99|00697f39    |
|99999A9A|01026c1c    |
|99999A9A|01026c1c    |
|99999A9A|01307a4f    |
|99999AA9|00178ef0    |
|99999AA9|00178ef0    |
|99999AA9|00430da3    |
|99999AAA|00056dbd    |
|99999AAA|00205aab    |
|99999AAA|00205aab    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A999|0015a687    |
|9999A99A|0030d89e    |
|9999A99A|0030d89e    |
|9999A99A|0030d89e    |
|9999A9A9|0005d1c3    |
|9999A9A9|0055b8b6    |
|9999A9A9|0055b8b6    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999A9AA|0029e1dd    |
|9999AA99|0002bc78    |
|9999AA99|0034cd97    |
|9999AA99|0034cd97    |
|9999AA9A|0070df5a    |
|9999AA9A|0102ac8b    |
|9999AA9A|0102ac8b    |
|9999AAA9|0009ebd5    |
|9999AAA9|0009ebd5    |
|9999AAA9|0040ebe3    |
|9999AAAA|0099dfce    |
|9999AAAA|0099dfce    |
|9999AAAA|0109bbcf    |
|999A9999|004a0944    |
|999A9999|004d3249    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — channel
+--------+-----+
|shape   |count|
+--------+-----+
|AAAAA   |26709|
|AAAAAA  |26668|
|AAAAAAAA|26623|
+--------+-----+


 SAMPLE VALUES — channel
+--------+------------+
|shape   |sample_value|
+--------+------------+
|AAAAA   |EMAIL       |
|AAAAA   |EMAIL       |
|AAAAA   |EMAIL       |
|AAAAAA  |google      |
|AAAAAA  |google      |
|AAAAAA  |google      |
|AAAAAAAA|facebook    |
|AAAAAAAA|facebook    |
|AAAAAAAA|facebook    |
+--------+------------+


 VALUE SHAPES — campaign
+-----------+-----+
|shape      |count|
+-----------+-----+
|AAAA       |19003|
|AAAAA      |15408|
|AAAAAA     |12301|
|AAAAAAA    |10068|
|AAA        |7960 |
|AAAAAAAA   |6344 |
|AAAAAAAAA  |3269 |
|AA         |2056 |
|AAAAAAAAAA |1939 |
|AAAAAAAAAAA|826  |
+-----------+-----+


 SAMPLE VALUES — campaign
+--------------+--------------+
|shape         |sample_value  |
+--------------+--------------+
|A             |I             |
|A             |I             |
|A             |I             |
|AA            |Mr            |
|AA            |Mr            |
|AA            |Mr            |
|AAA           |Mrs           |
|AAA           |Mrs           |
|AAA           |Mrs           |
|AAAA          |able          |
|AAAA          |able          |
|AAAA          |able          |
|AAAAA         |about         |
|AAAAA         |about         |
|AAAAA         |about         |
|AAAAAA        |accept        |
|AAAAAA        |accept        |
|AAAAAA        |accept        |
|AAAAAAA       |ability       |
|AAAAAAA       |ability       |
|AAAAAAA       |ability       |
|AAAAAAAA      |American      |
|AAAAAAAA      |American      |
|AAAAAAAA      |American      |
|AAAAAAAAA     |according     |
|AAAAAAAAA     |according     |
|AAAAAAAAA     |according     |
|AAAAAAAAAA    |Republican    |
|AAAAAAAAAA    |Republican    |
|AAAAAAAAAA    |Republican    |
|AAAAAAAAAAA   |development   |
|AAAAAAAAAAA   |development   |
|AAAAAAAAAAA   |development   |
|AAAAAAAAAAAA  |organization  |
|AAAAAAAAAAAA  |organization  |
|AAAAAAAAAAAA  |organization  |
|AAAAAAAAAAAAA |environmental |
|AAAAAAAAAAAAA |environmental |
|AAAAAAAAAAAAA |environmental |
|AAAAAAAAAAAAAA|administration|
|AAAAAAAAAAAAAA|administration|
|AAAAAAAAAAAAAA|administration|
+--------------+--------------+


 VALUE SHAPES — medium
+--------+-----+
|shape   |count|
+--------+-----+
|AAAAAAAA|39789|
|AAAA    |20264|
|AAAAAAA |19947|
+--------+-----+


 SAMPLE VALUES — medium
+--------+------------+
|shape   |sample_value|
+--------+------------+
|AAAA    |paid        |
|AAAA    |paid        |
|AAAA    |paid        |
|AAAAAAA |organic     |
|AAAAAAA |organic     |
|AAAAAAA |organic     |
|AAAAAAAA|REFERRAL    |
|AAAAAAAA|REFERRAL    |
|AAAAAAAA|REFERRAL    |
+--------+------------+


 VALUE SHAPES — source
+------+-----+
|shape |count|
+------+-----+
|AAAAA |32197|
|AAAAAA|31820|
|AA    |15983|
+------+-----+


 SAMPLE VALUES — source
+------+------------+
|shape |sample_value|
+------+------------+
|AA    |fb          |
|AA    |fb          |
|AA    |fb          |
|AAAAA |EMAIL       |
|AAAAA |EMAIL       |
|AAAAA |EMAIL       |
|AAAAAA|direct      |
|AAAAAA|direct      |
|AAAAAA|direct      |
+------+------------+


 VALUE SHAPES — touch_ts
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|80000|
+--------------------------+-----+


 SAMPLE VALUES — touch_ts
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-01-06 05:42:10.569939|
|9999-99-99 99:99:99.999999|2025-01-06 05:42:13.126048|
|9999-99-99 99:99:99.999999|2025-01-06 06:02:21.360113|
+--------------------------+--------------------------+


 Discovery complete for mkt_bronze_marketing_attribution — scanned 80000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_bronze_marketing_cost
====================================================================================================

 SCHEMA
root
 |-- spend_id: string (nullable = true)
 |-- channel: string (nullable = true)
 |-- spend: string (nullable = true)
 |-- spend_date: string (nullable = true)


 TOTAL ROWS: 365

 NULL COUNTS
+--------+-------+-----+----------+
|spend_id|channel|spend|spend_date|
+--------+-------+-----+----------+
|0       |0      |0    |0         |
+--------+-------+-----+----------+


 VALUE SHAPES — spend_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|AAA99A99-9AA9-9999-A9A9-9999AAAA999A|1    |
|99A99999-9A99-9A9A-99A9-A99AAAAA9A99|1    |
|AAA9A99A-9AA9-9A99-AA9A-A9999999AA99|1    |
|9AAA9AA9-9999-999A-AAA9-99A9A9AAA9A9|1    |
|A9AAAA99-AA9A-99A9-AAAA-9AAA9A9AA999|1    |
|A9A9A9A9-AA99-99AA-AAAA-9999999A9AA9|1    |
|99A9AAA9-9999-9999-9A99-99AA9A99A999|1    |
|9999A99A-9A9A-9A9A-AA99-9A999AA9A999|1    |
|99A999A9-AAAA-9AA9-9A9A-A9AAA999A999|1    |
|A9A999AA-9AAA-9AA9-9A9A-999AA9A9AA99|1    |
+------------------------------------+-----+


 SAMPLE VALUES — spend_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-AAA9-A99AA99AAA9A|85463143-1748-4399-bfc5-a60cf11fac0e|
|99999999-9999-9A99-AA9A-AAA9A9AAA999|16260363-6118-4d59-be0d-add3e5ecb394|
|99999999-99A9-9AAA-A999-99AA9999A999|33695888-62a9-4ffc-b689-52de2188b185|
|99999999-9A99-9AAA-A999-AAAAA9A9999A|29958096-7d36-4bdb-b235-ffeac7d0136e|
|99999999-9AA9-9A9A-A9A9-9A9A99AA9999|62343781-8ea7-4f8a-a3d4-1d1b49be8802|
|99999999-AA9A-99AA-9999-AA9A9999A999|69236082-ba5f-47eb-9092-ee5a1986b582|
|99999999-AAA9-9A99-9999-99999A9A9A99|76570130-cbc0-4f42-9490-09951a8a1d96|
|9999999A-9999-99AA-9A99-99AA9A99999A|4765380b-0485-48cb-8d68-99bc1e83689d|
|9999999A-9999-9A99-AAAA-A999A99AAA9A|6688212d-0763-4a58-baea-e766b89eec2d|
|9999999A-999A-9999-99AA-9999999AA9A9|3709056b-775a-4201-91bd-9507886cd5d2|
|9999999A-999A-9A9A-999A-9AAAAA999A99|3647120e-479e-4c1e-845c-7edcce626f04|
|9999999A-9AAA-9AAA-99A9-9999A9999A9A|2095316b-2acf-4eba-99d3-2937d7851e1f|
|9999999A-A99A-9A99-A999-9A9A99AAAA99|4512779b-f44b-4d38-b675-1d4e73efbc41|
|9999999A-AA99-9A99-A9A9-9A9999999A99|9930131c-ca94-4c21-b8d1-6f9496037b65|
|999999A9-99A9-9A99-A999-9AAAA9999A99|265642b5-18c8-4d97-b596-7bdeb2270f82|
|999999A9-99A9-9AA9-9AAA-99AAAA99999A|722347e8-58a7-4ca0-9bec-33ebde68607d|
|999999A9-9AA9-999A-9999-9A9A9AAAA999|717067e6-2af8-452a-9269-9c0d8ddfa283|
|999999A9-A999-9999-AAA9-9AA9A9A999A9|064026b8-d371-4042-acf8-4fd6d0a067f9|
|999999A9-A9AA-99A9-A99A-9999A9A9AA9A|190485b0-c5ad-41b4-a62c-2923f8d4ef2e|
|999999A9-AAA9-9A9A-A99A-A999AA9A9AAA|205009d1-cad2-4a7d-a81f-e263fb9b8fdb|
|999999AA-99AA-9999-A999-9A99AA9AA999|665896ae-35fb-4664-b997-7e62af6fe995|
|999999AA-9AA9-999A-A9AA-99A999A9AA99|741323cb-2ee0-485a-b6bd-46d667b1dd67|
|999999AA-A99A-9AAA-AAA9-9AA99AA9A999|018171de-c92b-4bbb-acb8-3fa26ad1a052|
|99999A99-9999-9999-99A9-A99AA999999A|77100c23-3857-4496-85d9-d03bb373811b|
|99999A99-9999-9999-A9AA-AA99A999AA9A|18327a02-2066-4473-a0ab-fd95d746cf8b|
|99999A99-999A-9A9A-9999-99A999AA9AA9|48913a91-633f-4a9f-9101-33a034aa1cc9|
|99999A99-A99A-99A9-AAA9-9A999A99A9A9|05281a58-b04b-41c2-baa3-8b646c78c6d4|
|99999A99-AAA9-9A99-9A9A-AA99A9999A9A|87612f56-fdf2-4a67-9d9d-cc41f2681e9a|
|99999A9A-99AA-9999-A999-999A9A9A9A99|77519a5b-66be-4598-b548-613b3a1f8b84|
|99999A9A-9A99-999A-999A-A9999A9A99A9|65068b4b-3f21-437b-834c-f7112f4d35a3|
|99999A9A-A999-9AAA-AAA9-9A999999A9AA|33660d5a-a359-4edd-bad6-7d608438a1da|
|99999AA9-9A9A-9A99-9999-A999A9A9A9A9|86909cf0-4e5b-4d42-9563-a920e9d8c0e8|
|99999AAA-9999-999A-99AA-9A9A9999AA99|24965bbd-7230-468f-91db-3e5e5222cb17|
|99999AAA-9A99-9999-A99A-AA9999999A99|35548fea-9a01-4236-b20e-da4808229f84|
|99999AAA-AAA9-99A9-9A9A-9A9999999A9A|86023fdc-abe3-43a5-8f7d-4a9090987a8d|
|9999A999-9999-99AA-9AAA-AA9A9999AA99|5657e254-3066-43af-8abb-db2e9966ea61|
|9999A999-99A9-9A99-AAAA-A9AA99A9AA99|3267d677-87d7-4e89-bbce-e8ca88b2bd17|
|9999A999-9AA9-9AA9-99A9-9A9A9999A999|5948a216-6fe2-4dc9-85d8-2e4f3464f302|
|9999A999-9AA9-9AA9-9A9A-99A999AAA9A9|0315d054-8ed0-4bd5-8d5f-07a140aed4c6|
|9999A999-9AA9-9AAA-9AAA-A9A9AA99A999|3732a795-7ea0-4bbe-8fde-e5e3be92d937|
|9999A999-A999-9A9A-99A9-AA999AAAAA99|0258d047-c364-4b4a-88d7-bb663ffdaa35|
|9999A999-A9A9-9999-99A9-9AAAA99AAAAA|4677c171-b8b4-4130-87d0-8edaf79ebece|
|9999A999-A9A9-999A-A999-A99999AA9A99|8069b037-a8f4-487f-b593-e65627ba2c22|
|9999A99A-9999-9AA9-9999-A9A9A9AA99A9|5496c57c-2792-4de3-9465-e5e8e8aa67d0|
|9999A99A-99AA-9A99-A99A-9A9999AAAA99|7736e14a-34ae-4d14-b16b-0b0888eafd83|
|9999A99A-9A9A-9A9A-AA99-9A999AA9A999|1599e96a-7a9b-4c7d-ad55-7e073ff9e054|
|9999A99A-9A9A-9AAA-AA9A-A9999AA9AA99|2836c80d-2b3a-4dae-ac4b-a8866ea9fa86|
|9999A99A-9AA9-999A-A999-99999A9999A9|9938b07f-0fe1-420f-b898-21067f5446f1|
|9999A99A-AA99-9999-9A9A-9999AA9999A9|4824c43c-bc65-4468-8f2e-3905fa4480e0|
|9999A9A9-9999-9999-9AAA-9999A9A9A999|3110b2e2-1540-4239-8adf-0976c2d1a020|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — channel
+--------+-----+
|shape   |count|
+--------+-----+
|AAAAAA  |132  |
|AAAAAAAA|119  |
|AAAAA   |114  |
+--------+-----+


 SAMPLE VALUES — channel
+--------+------------+
|shape   |sample_value|
+--------+------------+
|AAAAA   |EMAIL       |
|AAAAA   |EMAIL       |
|AAAAA   |EMAIL       |
|AAAAAA  |google      |
|AAAAAA  |google      |
|AAAAAA  |google      |
|AAAAAAAA|facebook    |
|AAAAAAAA|facebook    |
|AAAAAAAA|facebook    |
+--------+------------+


 VALUE SHAPES — spend
+-------+-----+
|shape  |count|
+-------+-----+
|9999.99|253  |
|999.99 |61   |
|9999.9 |43   |
|999.9  |8    |
+-------+-----+


 SAMPLE VALUES — spend
+-------+------------+
|shape  |sample_value|
+-------+------------+
|999.9  |101.5       |
|999.9  |162.7       |
|999.9  |419.7       |
|999.99 |113.35      |
|999.99 |114.47      |
|999.99 |114.51      |
|9999.9 |1060.0      |
|9999.9 |1184.3      |
|9999.9 |1210.2      |
|9999.99|1007.12     |
|9999.99|1039.84     |
|9999.99|1092.76     |
+-------+------------+


 VALUE SHAPES — spend_date
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|365  |
+--------------------------+-----+


 SAMPLE VALUES — spend_date
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-01-07 05:41:55.823932|
|9999-99-99 99:99:99.999999|2025-01-08 05:41:55.823932|
|9999-99-99 99:99:99.999999|2025-01-09 05:41:55.823932|
+--------------------------+--------------------------+


 Discovery complete for mkt_bronze_marketing_cost — scanned 365 rows

====================================================================================================
 DISCOVERING TABLE: mkt_bronze_promotions
====================================================================================================

 SCHEMA
root
 |-- promotion_code: string (nullable = true)
 |-- discount_pct: string (nullable = true)
 |-- valid_from: string (nullable = true)
 |-- valid_to: string (nullable = true)


 TOTAL ROWS: 500

 NULL COUNTS
+--------------+------------+----------+--------+
|promotion_code|discount_pct|valid_from|valid_to|
+--------------+------------+----------+--------+
|0             |0           |0         |0       |
+--------------+------------+----------+--------+


 VALUE SHAPES — promotion_code
+---------+-----+
|shape    |count|
+---------+-----+
|AAAAA9999|500  |
+---------+-----+


 SAMPLE VALUES — promotion_code
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAAAA9999|PROMO0000   |
|AAAAA9999|PROMO0001   |
|AAAAA9999|PROMO0002   |
+---------+------------+


 VALUE SHAPES — discount_pct
+-----+-----+
|shape|count|
+-----+-----+
|99   |412  |
|9    |88   |
+-----+-----+


 SAMPLE VALUES — discount_pct
+-----+------------+
|shape|sample_value|
+-----+------------+
|9    |5           |
|9    |5           |
|9    |5           |
|99   |10          |
|99   |10          |
|99   |10          |
+-----+------------+


 VALUE SHAPES — valid_from
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|500  |
+--------------------------+-----+


 SAMPLE VALUES — valid_from
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2024-07-15 14:55:18.581913|
|9999-99-99 99:99:99.999999|2024-07-16 21:24:03.581940|
|9999-99-99 99:99:99.999999|2024-07-18 02:58:37.574803|
+--------------------------+--------------------------+


 VALUE SHAPES — valid_to
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|9999-99-99 99:99:99.999999|500  |
+--------------------------+-----+


 SAMPLE VALUES — valid_to
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|9999-99-99 99:99:99.999999|2025-10-08 14:58:04.577648|
|9999-99-99 99:99:99.999999|2025-10-08 22:30:33.575411|
|9999-99-99 99:99:99.999999|2025-10-09 01:36:26.581199|
+--------------------------+--------------------------+


 Discovery complete for mkt_bronze_promotions — scanned 500 rows

 All table discovery completed
```

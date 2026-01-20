# Table Discovery Report

Database: washit_dw
Table pattern: %silver%
Generated: 2026-01-13 02:42:32 UTC

```text

 Discovered 14 tables:
  - crm_silver_devices
  - crm_silver_events
  - crm_silver_geo
  - crm_silver_order_items
  - crm_silver_order_status_history
  - crm_silver_orders
  - crm_silver_payment_attempts
  - crm_silver_referrals
  - crm_silver_user_preferences
  - crm_silver_users
  - mkt_silver_coupon_redemptions
  - mkt_silver_marketing_attribution
  - mkt_silver_marketing_cost
  - mkt_silver_promotions

====================================================================================================
 DISCOVERING TABLE: crm_silver_devices
====================================================================================================

 SCHEMA
root
 |-- device_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- device_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- platform: string (nullable = true)
 |-- device_model: string (nullable = true)
 |-- device_family: string (nullable = true)
 |-- mac_addr: string (nullable = true)
 |-- os_family: string (nullable = true)
 |-- os_major_version: integer (nullable = true)
 |-- browser_family: string (nullable = true)
 |-- browser_major_version: integer (nullable = true)
 |-- platform_os_mismatch: integer (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 20000

 NULL COUNTS
+---------+-------+---------+-------+--------+------------+-------------+--------+---------+----------------+--------------+---------------------+--------------------+-------------+
|device_sk|user_sk|device_id|user_id|platform|device_model|device_family|mac_addr|os_family|os_major_version|browser_family|browser_major_version|platform_os_mismatch|dw_created_at|
+---------+-------+---------+-------+--------+------------+-------------+--------+---------+----------------+--------------+---------------------+--------------------+-------------+
|0        |0      |0        |0      |0       |0           |0            |4024    |0        |6113            |0             |0                    |0                   |0            |
+---------+-------+---------+-------+--------+------------+-------------+--------+---------+----------------+--------------+---------------------+--------------------+-------------+


 VALUE SHAPES — device_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|685  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|479  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|450  |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|445  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|419  |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|409  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|377  |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|275  |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|271  |
|AAA9AAAAAAAAAAAAAAA9AAAAAA|269  |
+--------------------------+-----+


 SAMPLE VALUES — device_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2u5n2m5n2zlyjk5zjkzztjhot|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|y2i4m2i3m2uwywuwmtzjotdmod|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2i4y2y2ndc4mzq1zgu0zgqwmt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2u2n2m4nza3ztm5mjbkzgjkod|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2u3y2u2ogy3mgizngvjotg3zd|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e2m2q4ndi3ngmzodbjnzbknm|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|y2i5m2q3ztmzzjc2ywy5y2q2nt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u0y2q4zmrhntk2ntbizgu3mm|
|A9A9A9A9AAAAAAAAAAA9AAA9A9|y2e3n2q1mmyyyjixnzu1yta0m2|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2y1n2i1nzvkmmvintfhzgriyz|
|A9A9A9AAA9AAAAAAAAAAA9A9AA|m2q4y2uwm2yznznimtzly2y2yt|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|n2u0m2zjm2nlmtlknmewzjjimt|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|m2i5y2jjote3y2q5mtu0mgjjzm|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2i5y2nmodg3nju1nze5odgzog|
|A9A9A9AAAAA9AAA9AAAAA9A9AA|y2q2m2jknwy1mmu4nzhkm2m1mt|
|A9A9A9AAAAA9AAA9AAAAA9AAAA|m2y1y2jjyjm3mjk5mwjlm2jjnt|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|y2y5n2mwmtk4zte0zmiynmi0zt|
|A9A9A9AAAAA9AAA9AAAAAAAAAA|y2q0y2rizje2zdg2mtvmndrimw|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|n2y4n2izztm5yzizzjc2mtvinj|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|y2i0m2zmodu2yjqxmzu1nwnkzw|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|y2u5n2uxnwu0owywnze1ymrhyw|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|y2q5n2vlzjc1otrhyzzmnze3mw|
|A9A9A9AAAAA9AAAAAAAAAAAAA9|y2e4n2nimtk5ndllztawzdmzm2|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|m2e3m2rlmjc5ntazyjdjzjnjmw|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2q0n2fimdk4zdkznjqwmjvjmz|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|y2q4m2flmmy5ywuwotmwnzvinz|
|A9A9A9AAAAAAA9A9AAA9AAAAAA|y2y5n2uwodrhm2m4yjm4zdnhzt|
|A9A9A9AAAAAAAAA9AAAAAAAAAA|m2y0n2qzmdrhywq1ymmwyzhhzj|
|A9A9A9AAAAAAAAA9AAAAAAAAAA|y2m3n2rlymnjnwy3mgnmodmynd|
|A9A9A9AAAAAAAAA9AAAAAAAAAA|y2u4y2jmnmiyntk0ytrlmdzlnz|
|A9A9A9AAAAAAAAAAAAA9AAA9AA|y2i0n2njotblmzrknje1yzc5zj|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|m2m3m2qxodnlmtayntvmngu2nt|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|n2m1y2vimjqyzjvjywuwmjy3yt|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|y2m1y2iwnmixzdrinwmwzgm4mt|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|n2q0m2qxymnjndvjyjjmyzviog|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|n2q4y2zjyjdlntbmytbmmwrknm|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|y2i3m2jkzgjimtfjmmfmogvmod|
|A9A9AAA9A9A9AAA9AAA9AAA9AA|y2m1mjy3n2y2zwm3mzc4mte4nj|
|A9A9AAA9A9A9AAA9AAA9AAAAAA|m2q2zmq1y2y5nzq4mtg4mzmxmt|
|A9A9AAA9A9A9AAA9AAAAAAAAAA|m2e0zgq4n2u4nti3mgqzmgiyzd|
|A9A9AAA9A9A9AAA9AAAAAAAAAA|y2i3zji5n2e3ztg0ytjmzgmxod|
|A9A9AAA9A9A9AAA9AAAAAAAAAA|y2u0mtg1m2y5yty5yjqxmzljnj|
|A9A9AAA9A9A9AAAAAAA9AAAAAA|n2i4yzu5n2m5zjvizta0njjiyt|
|A9A9AAA9A9A9AAAAAAA9AAAAAA|y2q4mmm3m2u3zgnmyzg4mwewnd|
|A9A9AAA9A9A9AAAAAAAAAAA9AA|n2y0mdi1n2e2yznlmmjmzdi1zw|
|A9A9AAA9A9A9AAAAAAAAAAAAA9|m2i5mgy3m2y0ogmyndvjmdhln2|
|A9A9AAA9A9A9AAAAAAAAAAAAAA|n2u1mta3m2y1ndcyyzdlmzhmnm|
|A9A9AAA9A9AAA9A9A9AAAAA9AA|y2m3yzk0y2rim2y1n2exymm2mj|
|A9A9AAA9A9AAA9AAAAAAAAA9AA|n2m0oti0m2rjy2jlzmzhmmm5mz|
|A9A9AAA9A9AAAAA9AAA9AAAAA9|n2u5nte2n2zhndy0otg1ztuxm2|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|694  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|444  |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|443  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|442  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|413  |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|411  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|405  |
|AAAAAAAAAAA9AAAAAAAAAAA9AA|297  |
|AAA9AAA9AAAAAAAAAAAAAAAAAA|284  |
|AAAAAAA9AAAAAAA9AAAAAAAAAA|274  |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q5m2u5zwu0mweymtq0owy5yz|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q5m2u5zwu0mweymtq0owy5yz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9AAAAA9AAAAAAAAAA|m2m1m2mwn2viowe2zwyxytgwnm|
|A9A9A9AAA9AAAAA9AAAAAAAAAA|m2m1m2mwn2viowe2zwyxytgwnm|
|A9A9A9AAA9AAAAAAAAAAAAA9AA|y2u4y2yyy2uyytjhmduzyja4mz|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i4y2ziyjm0yzg0nmi4otblzj|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2u5m2vhmzk5ndk2zdk2ytljog|
|A9A9A9AAAAA9AAA9AAAAAAAAAA|m2q5n2vmmwi1ywq0nwvlntqwyz|
|A9A9A9AAAAA9AAA9AAAAAAAAAA|m2q5n2vmmwi1ywq0nwvlntqwyz|
|A9A9A9AAAAA9AAAAA9AAAAAAAA|m2y0y2fhzjg1mwewm2rhowvlyt|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|n2u2y2zjmjm4ztgwzmu5mzvkzg|
|A9A9A9AAAAA9AAAAAAAAAAA9A9|m2y2m2nimju0ndywywmxztu3n2|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|n2q5m2jjmti2otvjodhintg4nd|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|m2e3m2vjyjy2nzgymmrlmzhjnw|
|A9A9A9AAAAAAAAA9AAA9AAAAAA|y2m4y2uxzjyzndu5mgi5mdlmzt|
|A9A9A9AAAAAAAAA9AAA9AAAAAA|y2m4y2uxzjyzndu5mgi5mdlmzt|
|A9A9A9AAAAAAAAA9AAAAAAA9AA|y2y4n2zknwrlmtg4owzlzge5yw|
|A9A9A9AAAAAAAAAAAAA9AAA9A9|y2e5m2yxntjhndlkmgq1odg4m2|
|A9A9A9AAAAAAAAAAAAA9AAA9A9|y2e5m2yxntjhndlkmgq1odg4m2|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|m2i5n2njzjhjzgqyymflmjy3mt|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|m2u5n2jkztrkntuxotfhzmqxmj|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|m2u5n2jkztrkntuxotfhzmqxmj|
|A9A9AAA9A9A9A9A9AAAAAAAAAA|n2y5mgi3y2m0y2i4ndkxyznlmm|
|A9A9AAA9A9A9AAA9AAAAAAAAAA|n2i4nwu4y2i3yme2nwmynwuzmt|
|A9A9AAA9A9A9AAA9AAAAAAAAAA|n2i4nwu4y2i3yme2nwmynwuzmt|
|A9A9AAA9A9A9AAAAAAAAAAAAAA|n2m4oty2y2m0owrmzdnimtjhnw|
|A9A9AAA9A9AAAAA9AAA9AAA9AA|y2y3ntk2m2fmoti1ywm1ywy2mg|
|A9A9AAA9A9AAAAA9AAAAAAA9AA|m2m1ztq1n2yzngm3yzgwzgq2nd|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2u2zta1m2zhmdk0otvjntuyyt|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2u2zta1m2zhmdk0otvjntuyyt|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2y0yty1n2yxnta4ymyynjbknt|
|A9A9AAA9A9AAAAAAA9A9AAA9AA|y2i4mdi4y2zinjmxm2q0mtg2ow|
|A9A9AAA9A9AAAAAAAAA9A9AAAA|n2q5ymm0n2zkntbmoda0m2mznm|
|A9A9AAA9A9AAAAAAAAA9A9AAAA|n2q5ymm0n2zkntbmoda0m2mznm|
|A9A9AAA9A9AAAAAAAAA9AAA9AA|m2m0mtk1m2mwyjcwmjm0njc5ym|
|A9A9AAA9A9AAAAAAAAA9AAAAAA|y2u4zgy5y2rlmjbhzdm0nziymj|
|A9A9AAA9A9AAAAAAAAA9AAAAAA|y2u4zgy5y2rlmjbhzdm0nziymj|
|A9A9AAA9A9AAAAAAAAAAA9AAAA|m2y0ngu0n2nhytlhndfly2mwnt|
+--------------------------+--------------------------+
only showing top 50 rows

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
+-------+-----+
|shape  |count|
+-------+-----+
|AAA    |17824|
|AAAAAAA|2176 |
+-------+-----+


 SAMPLE VALUES — platform
+-------+------------+
|shape  |sample_value|
+-------+------------+
|AAA    |ios         |
|AAA    |ios         |
|AAA    |ios         |
|AAAAAAA|android     |
|AAAAAAA|android     |
|AAAAAAA|android     |
+-------+------------+


 VALUE SHAPES — device_model
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+
|shape                                                                                                                                             |count|
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA AA 9.9; AAAAAAA/9.9)                                                                                   |1995 |
|AAAAAAA/9.9 (AAAA; A; AAA AAAAAA AA 9_9 AAAA AAA AA A; AA-AA) AAAAAAAAAAA/999.99.9 (AAAAA, AAAA AAAAA) AAAAAAA/9.9.9 AAAAAA/9A999 AAAAAA/9999.99.9|828  |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                  |757  |
|AAAAA/9.99.(AAAAAAA AA 9.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                   |737  |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                                                                |710  |
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA AA 99.9; AAAAAAA/9.9)                                                                                  |597  |
|AAAAAAA/9.9 (AAAAAAAAAA; AAAA 9.9; AAAAAAA 99; AAAAAAA/9.9)                                                                                       |567  |
|AAAAAAA/9.9 (AAAAA; AAAAAAA 9.9.9) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9                                           |472  |
|AAAAAAA/9.9 (AAAAAAA 9.9.9; AAAAAA; AA:99.9) AAAAA/99.9 AAAAAAA/99.9                                                                              |417  |
|AAAAAAA/9.9 (AAAAAAA AA 9.9) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9                                                 |402  |
+--------------------------------------------------------------------------------------------------------------------------------------------------+-----+


 SAMPLE VALUES — device_model
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|shape                                                                                             |sample_value                                                                                      |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.10.(x11; linux i686; ce-ru) presto/2.9.163 version/10.00                                  |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.10.(x11; linux i686; ky-kg) presto/2.9.165 version/11.00                                  |
|AAAAA/9.99.(A99; AAAAA A999; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.10.(x11; linux i686; lg-ug) presto/2.9.160 version/11.00                                  |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.10.(x11; linux i686; doi-in) presto/2.9.182 version/11.00                                 |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.11.(x11; linux i686; brx-in) presto/2.9.182 version/12.00                                 |
|AAAAA/9.99.(A99; AAAAA A999; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.11.(x11; linux i686; gez-et) presto/2.9.167 version/11.00                                 |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                |opera/8.10.(x11; linux x86_64; hr-hr) presto/2.9.189 version/10.00                                |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                |opera/8.10.(x11; linux x86_64; om-et) presto/2.9.182 version/11.00                                |
|AAAAA/9.99.(A99; AAAAA A99_99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                |opera/8.11.(x11; linux x86_64; da-dk) presto/2.9.188 version/10.00                                |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                               |opera/8.10.(x11; linux x86_64; csb-pl) presto/2.9.162 version/10.00                               |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                               |opera/8.10.(x11; linux x86_64; quz-pe) presto/2.9.186 version/11.00                               |
|AAAAA/9.99.(A99; AAAAA A99_99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                               |opera/8.11.(x11; linux x86_64; fur-it) presto/2.9.164 version/12.00                               |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.10.(windows 95; iw-il) presto/2.9.164 version/12.00                                       |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.10.(windows 98; kw-gb) presto/2.9.169 version/11.00                                       |
|AAAAA/9.99.(AAAAAAA 99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.11.(windows 95; oc-fr) presto/2.9.188 version/11.00                                       |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                          |opera/8.14.(windows 98; win 9x 4.90; ca-ad) presto/2.9.175 version/10.00                          |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                          |opera/8.16.(windows 98; win 9x 4.90; dz-bt) presto/2.9.176 version/12.00                          |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                          |opera/8.16.(windows 98; win 9x 4.90; li-be) presto/2.9.181 version/10.00                          |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                         |opera/8.10.(windows 98; win 9x 4.90; shs-ca) presto/2.9.188 version/10.00                         |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                         |opera/8.10.(windows 98; win 9x 4.90; wal-et) presto/2.9.176 version/10.00                         |
|AAAAA/9.99.(AAAAAAA 99; AAA 9A 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                         |opera/8.11.(windows 98; win 9x 4.90; crh-ua) presto/2.9.185 version/10.00                         |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.11.(windows 95; niu-nu) presto/2.9.167 version/10.00                                      |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.17.(windows 95; the-np) presto/2.9.184 version/10.00                                      |
|AAAAA/9.99.(AAAAAAA 99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.18.(windows 95; fur-it) presto/2.9.188 version/11.00                                      |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.12.(windows nt 5.01; fy-de) presto/2.9.178 version/12.00                                  |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.19.(windows nt 5.01; ik-ca) presto/2.9.168 version/12.00                                  |
|AAAAA/9.99.(AAAAAAA AA 9.99; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.22.(windows nt 5.01; cv-ru) presto/2.9.163 version/11.00                                  |
|AAAAA/9.99.(AAAAAAA AA 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.13.(windows nt 5.01; fil-ph) presto/2.9.177 version/10.00                                 |
|AAAAA/9.99.(AAAAAAA AA 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.14.(windows nt 5.01; ayc-pe) presto/2.9.178 version/10.00                                 |
|AAAAA/9.99.(AAAAAAA AA 9.99; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.27.(windows nt 5.01; tcy-in) presto/2.9.167 version/10.00                                 |
|AAAAA/9.99.(AAAAAAA AA 9.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                   |opera/8.10.(windows nt 4.0; ak-gh) presto/2.9.173 version/12.00                                   |
|AAAAA/9.99.(AAAAAAA AA 9.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                   |opera/8.10.(windows nt 5.2; fy-de) presto/2.9.168 version/11.00                                   |
|AAAAA/9.99.(AAAAAAA AA 9.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                   |opera/8.10.(windows nt 6.1; th-th) presto/2.9.169 version/12.00                                   |
|AAAAA/9.99.(AAAAAAA AA 9.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.10.(windows nt 6.0; mni-in) presto/2.9.175 version/11.00                                  |
|AAAAA/9.99.(AAAAAAA AA 9.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.11.(windows nt 4.0; apn-in) presto/2.9.164 version/11.00                                  |
|AAAAA/9.99.(AAAAAAA AA 9.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.12.(windows nt 6.0; fur-it) presto/2.9.160 version/10.00                                  |
|AAAAA/9.99.(AAAAAAA AA 99.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.10.(windows nt 10.0; yo-ng) presto/2.9.167 version/10.00                                  |
|AAAAA/9.99.(AAAAAAA AA 99.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.11.(windows nt 10.0; ne-np) presto/2.9.162 version/10.00                                  |
|AAAAA/9.99.(AAAAAAA AA 99.9; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                  |opera/8.11.(windows nt 10.0; pt-pt) presto/2.9.177 version/10.00                                  |
|AAAAA/9.99.(AAAAAAA AA 99.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.12.(windows nt 10.0; wal-et) presto/2.9.176 version/10.00                                 |
|AAAAA/9.99.(AAAAAAA AA 99.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.13.(windows nt 10.0; gez-et) presto/2.9.172 version/10.00                                 |
|AAAAA/9.99.(AAAAAAA AA 99.9; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                 |opera/8.13.(windows nt 11.0; the-np) presto/2.9.160 version/12.00                                 |
|AAAAA/9.99.(AAAAAAA AA; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.10.(windows ce; ak-gh) presto/2.9.163 version/11.00                                       |
|AAAAA/9.99.(AAAAAAA AA; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.11.(windows ce; fo-fo) presto/2.9.163 version/12.00                                       |
|AAAAA/9.99.(AAAAAAA AA; AA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                       |opera/8.14.(windows ce; ia-fr) presto/2.9.189 version/11.00                                       |
|AAAAA/9.99.(AAAAAAA AA; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.20.(windows ce; nso-za) presto/2.9.160 version/12.00                                      |
|AAAAA/9.99.(AAAAAAA AA; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.23.(windows ce; lij-it) presto/2.9.176 version/10.00                                      |
|AAAAA/9.99.(AAAAAAA AA; AAA-AA) AAAAAA/9.9.999 AAAAAAA/99.99                                      |opera/8.38.(windows ce; niu-nz) presto/2.9.164 version/12.00                                      |
|AAAAAAA/9.9 (A99; AAAAA A999) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9|mozilla/5.0 (x11; linux i686) applewebkit/531.0 (khtml, like gecko) chrome/13.0.806.0 safari/531.0|
|AAAAAAA/9.9 (A99; AAAAA A999) AAAAAAAAAAA/999.9 (AAAAA, AAAA AAAAA) AAAAAA/99.9.999.9 AAAAAA/999.9|mozilla/5.0 (x11; linux i686) applewebkit/531.0 (khtml, like gecko) chrome/14.0.860.0 safari/531.0|
+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
only showing top 50 rows

 VALUE SHAPES — device_family
+----------+-----+
|shape     |count|
+----------+-----+
|AAAAAAA   |7676 |
|AAAAAAA_AA|6428 |
|AAA       |2950 |
|AAAAAA    |2127 |
|AAAA      |819  |
+----------+-----+


 SAMPLE VALUES — device_family
+----------+------------+
|shape     |sample_value|
+----------+------------+
|AAA       |mac         |
|AAA       |mac         |
|AAA       |mac         |
|AAAA      |ipad        |
|AAAA      |ipad        |
|AAAA      |ipad        |
|AAAAAA    |iphone      |
|AAAAAA    |iphone      |
|AAAAAA    |iphone      |
|AAAAAAA   |android     |
|AAAAAAA   |android     |
|AAAAAAA   |android     |
|AAAAAAA_AA|windows_pc  |
|AAAAAAA_AA|windows_pc  |
|AAAAAAA_AA|windows_pc  |
+----------+------------+


 VALUE SHAPES — mac_addr
+-----------------+-----+
|shape            |count|
+-----------------+-----+
|99:99:99:99:99:99|57   |
|99:99:99:99:99:A9|42   |
|99:A9:99:99:99:99|42   |
|99:99:99:A9:99:99|41   |
|99:99:99:99:A9:99|41   |
|99:99:99:9A:99:99|38   |
|99:99:9A:99:99:99|38   |
|99:9A:99:99:99:99|36   |
|9A:99:99:99:99:99|33   |
|99:99:A9:99:99:99|33   |
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

 VALUE SHAPES — os_family
+-------+-----+
|shape  |count|
+-------+-----+
|AAAAAAA|10518|
|AAAAA  |6536 |
|AAA    |2946 |
+-------+-----+


 SAMPLE VALUES — os_family
+-------+------------+
|shape  |sample_value|
+-------+------------+
|AAA    |ios         |
|AAA    |ios         |
|AAA    |ios         |
|AAAAA  |linux       |
|AAAAA  |linux       |
|AAAAA  |linux       |
|AAAAAAA|android     |
|AAAAAAA|android     |
|AAAAAAA|android     |
+-------+------------+


 VALUE SHAPES — browser_family
+-----------------+-----+
|shape            |count|
+-----------------+-----+
|AAAAAA           |7970 |
|AAAAAAA          |4064 |
|AAAAAAAA_AAAAAAAA|4016 |
|AAAAA            |3950 |
+-----------------+-----+


 SAMPLE VALUES — browser_family
+-----------------+-----------------+
|shape            |sample_value     |
+-----------------+-----------------+
|AAAAA            |opera            |
|AAAAA            |opera            |
|AAAAA            |opera            |
|AAAAAA           |chrome           |
|AAAAAA           |chrome           |
|AAAAAA           |chrome           |
|AAAAAAA          |firefox          |
|AAAAAAA          |firefox          |
|AAAAAAA          |firefox          |
|AAAAAAAA_AAAAAAAA|internet_explorer|
|AAAAAAAA_AAAAAAAA|internet_explorer|
|AAAAAAAA_AAAAAAAA|internet_explorer|
+-----------------+-----------------+


 Discovery complete for crm_silver_devices — scanned 20000 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_events
====================================================================================================

 SCHEMA
root
 |-- event_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- device_sk: string (nullable = true)
 |-- event_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- event_type: string (nullable = true)
 |-- event_category: string (nullable = true)
 |-- event_ts: timestamp (nullable = true)
 |-- device_id: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 827167

 NULL COUNTS
+--------+-------+---------+--------+-------+----------+--------------+--------+---------+-------------+
|event_sk|user_sk|device_sk|event_id|user_id|event_type|event_category|event_ts|device_id|dw_created_at|
+--------+-------+---------+--------+-------+----------+--------------+--------+---------+-------------+
|0       |0      |0        |0       |0      |0         |0             |0       |0        |0            |
+--------+-------+---------+--------+-------+----------+--------------+--------+---------+-------------+


 VALUE SHAPES — event_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|29383|
|AAAAAAA9AAAAAAAAAAAAAAAAAA|18150|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|17854|
|AAAAAAAAAAA9AAAAAAAAAAAAAA|17834|
|AAA9AAAAAAAAAAAAAAAAAAAAAA|17721|
|AAAAAAAAAAAAAAA9AAAAAAAAAA|17708|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|17686|
|AAA9AAAAAAAAAAAAAAA9AAAAAA|10814|
|AAAAAAA9AAAAAAAAAAA9AAAAAA|10786|
|AAAAAAAAAAAAAAA9AAA9AAAAAA|10752|
+--------------------------+-----+


 SAMPLE VALUES — event_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9A9AAAAAAA9A9AA|y2u0y2e2n2e2n2nmmdizy2e5ym|
|A9A9A9A9A9A9AAA9AAA9AAA9A9|m2y0m2m3y2y1zgm1mwu5mju4m2|
|A9A9A9A9A9A9AAA9AAA9AAA9A9|y2e2m2e4y2q1mje4nja3ztc1m2|
|A9A9A9A9A9A9AAA9AAA9AAA9AA|m2i1n2i5n2m0otq0zmu2yjc2zd|
|A9A9A9A9A9A9AAA9AAA9AAAAAA|m2i1m2m1m2i0zwi2owu1zjyxyt|
|A9A9A9A9A9A9AAA9AAA9AAAAAA|m2m4n2i4y2u0ztc3ntq1ywmzog|
|A9A9A9A9A9A9AAA9AAAAAAAAAA|y2e5m2m3y2q5mzk2mdfjmjhmmj|
|A9A9A9A9A9A9AAAAA9AAAAAAAA|n2m2y2i1m2q2mjzly2zjotyxzt|
|A9A9A9A9A9A9AAAAA9AAAAAAAA|n2q4y2i2m2q1mjfhn2flmdkynt|
|A9A9A9A9A9A9AAAAAAA9AAA9AA|m2e2n2u3y2q4owrhzgi0ymi0yz|
|A9A9A9A9A9A9AAAAAAA9AAA9AA|m2u1n2i3m2u3ywnjzmy0zte0og|
|A9A9A9A9A9A9AAAAAAA9AAA9AA|m2u5m2m5n2q4nmvjyjm3zdu0mz|
|A9A9A9A9A9A9AAAAAAA9AAAAA9|n2e1n2i3n2u0ntblmgi0ownhm2|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2q0m2y0y2y1zjrhytq4nzgzog|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|y2e5n2y5y2u1njnlzje0zmjmmw|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|y2y5y2e1y2u1mtdjzgm5mmviot|
|A9A9A9A9A9A9AAAAAAAAAAA9AA|m2u4y2y5m2y5nwuymzkzmzg2od|
|A9A9A9A9A9A9AAAAAAAAAAAAAA|m2m0y2u4y2q3nmvlmtkyymjimg|
|A9A9A9A9A9A9AAAAAAAAAAAAAA|m2q2m2y1y2y0mmfkztnmnjgzzw|
|A9A9A9A9A9A9AAAAAAAAAAAAAA|m2q3m2i3m2y5ymfjmtfjnjnlzt|
|A9A9A9A9A9AAA9AAAAAAAAAAAA|n2i4n2q1m2qxy2jhzgywmzuyzj|
|A9A9A9A9A9AAAAA9AAAAA9AAAA|n2i1m2y0m2niowy2otgzy2njmw|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|n2q2y2e4n2fkmmu5yjblmgy1md|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|y2e3y2e2y2rjmtc5ymmznjc4yj|
|A9A9A9A9A9AAAAA9AAAAAAAAAA|m2q2m2u0y2fhzwu4nwuxmwrinz|
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2e1n2m3y2uwogm2mgfmmdexnz|
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2m1y2y3m2ezzwi0mdkxodyynz|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|y2q1n2y3m2mwnjjizwq3mta1nj|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|n2m0n2m2m2zmmjezzdc3ymixot|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|n2y1n2y3n2izyjvjnme4njljnj|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2u4n2y3y2nkymrlymi4ndlhzm|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|n2u5y2u3m2exyzmxmwjhyji4nm|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|n2y0y2i2y2iwmdfmmmqymtg1od|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|y2q5n2m2n2uzntrhndnkoti5zg|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2m1m2e3y2uxnthlmzvintkymt|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|n2m5y2m1m2rmngzimjjlmdgxym|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|y2u2m2i2m2fhnjbkzdqxogfhod|
|A9A9A9A9AAA9A9A9AAAAAAA9AA|m2u5y2q4ytm2m2u1otmwnjk5nz|
|A9A9A9A9AAA9A9A9AAAAAAA9AA|y2e1y2e4yjm3y2i5ywzmodc5nz|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|m2e4y2i5zju4n2u3njrhnjbimz|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|m2u3m2y4ngi0y2njowy2ytu2mm|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|n2y2m2y0yji5m2rlngq2zgq5mz|
|A9A9A9A9AAA9A9AAAAA9AAAAAA|y2e3n2q5mjy2y2rkndy3otzjmw|
|A9A9A9A9AAA9A9AAAAA9AAAAAA|y2y3m2u3mwi0y2mymmu2mjbmmt|
|A9A9A9A9AAA9A9AAAAAAAAAAAA|n2y0n2m2zdu3n2ewmtazmjlmmz|
|A9A9A9A9AAA9AAA9A9A9AAA9AA|m2m5m2y4ndk1nzg3m2i0mzc3mg|
|A9A9A9A9AAA9AAA9A9A9AAA9AA|n2q1m2e3zda0ndm5y2e5oty4nt|
|A9A9A9A9AAA9AAA9A9A9AAAAAA|m2e2n2e2njg1ztg0n2m5mtmzyw|
|A9A9A9A9AAA9AAA9A9A9AAAAAA|m2i1n2e0ogq5yti0n2e0zjizzt|
|A9A9A9A9AAA9AAA9A9AAAAA9AA|y2y0y2y1mme5mje3n2eyymy2mj|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|29334|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|17913|
|AAAAAAAAAAAAAAA9AAAAAAAAAA|17872|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|17824|
|AAA9AAAAAAAAAAAAAAAAAAAAAA|17547|
|AAAAAAAAAAA9AAAAAAAAAAAAAA|17543|
|AAAAAAA9AAAAAAAAAAAAAAAAAA|17476|
|AAAAAAAAAAA9AAAAAAA9AAAAAA|11339|
|AAA9AAAAAAA9AAAAAAAAAAAAAA|11084|
|AAAAAAA9AAAAAAAAAAA9AAAAAA|10998|
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2q2mgu1zwuwntaxzwjkzm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2q2mgu1zwuwntaxzwjkzm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2q2mgu1zwuwntaxzwjkzm|
|A9A9A9A9AAAAA9AAA9AAAAA9AA|y2i1m2i1otyyn2jhm2ixywm5mj|
|A9A9A9A9AAAAA9AAA9AAAAA9AA|y2i1m2i1otyyn2jhm2ixywm5mj|
|A9A9A9A9AAAAA9AAA9AAAAA9AA|y2i1m2i1otyyn2jhm2ixywm5mj|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — device_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|28420|
|AAA9AAAAAAAAAAAAAAAAAAAAAA|19543|
|AAAAAAA9AAAAAAAAAAAAAAAAAA|18462|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|18370|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|17706|
|AAAAAAAAAAAAAAA9AAAAAAAAAA|16853|
|AAAAAAAAAAA9AAAAAAAAAAAAAA|15732|
|AAAAAAAAAAAAAAAAAAA9AAA9AA|11204|
|AAAAAAAAAAAAAAA9AAA9AAAAAA|11162|
|AAA9AAAAAAAAAAAAAAA9AAAAAA|11148|
+--------------------------+-----+


 SAMPLE VALUES — device_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2u5n2m5n2zlyjk5zjkzztjhot|
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2u5n2m5n2zlyjk5zjkzztjhot|
|A9A9A9A9A9AAAAA9AAAAAAAAAA|n2u5n2m5n2zlyjk5zjkzztjhot|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|y2i4m2i3m2uwywuwmtzjotdmod|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|y2i4m2i3m2uwywuwmtzjotdmod|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|y2i4m2i3m2uwywuwmtzjotdmod|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2i4y2y2ndc4mzq1zgu0zgqwmt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2i4y2y2ndc4mzq1zgu0zgqwmt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2i4y2y2ndc4mzq1zgu0zgqwmt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2u2n2m4nza3ztm5mjbkzgjkod|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2u2n2m4nza3ztm5mjbkzgjkod|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2u2n2m4nza3ztm5mjbkzgjkod|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2u3y2u2ogy3mgizngvjotg3zd|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2u3y2u2ogy3mgizngvjotg3zd|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2u3y2u2ogy3mgizngvjotg3zd|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e2m2q4ndi3ngmzodbjnzbknm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e2m2q4ndi3ngmzodbjnzbknm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e2m2q4ndi3ngmzodbjnzbknm|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|y2i5m2q3ztmzzjc2ywy5y2q2nt|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|y2i5m2q3ztmzzjc2ywy5y2q2nt|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|y2i5m2q3ztmzzjc2ywy5y2q2nt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u0y2q4zmrhntk2ntbizgu3mm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u0y2q4zmrhntk2ntbizgu3mm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u0y2q4zmrhntk2ntbizgu3mm|
|A9A9A9A9AAAAAAAAAAA9AAA9A9|y2e3n2q1mmyyyjixnzu1yta0m2|
|A9A9A9A9AAAAAAAAAAA9AAA9A9|y2e3n2q1mmyyyjixnzu1yta0m2|
|A9A9A9A9AAAAAAAAAAA9AAA9A9|y2e3n2q1mmyyyjixnzu1yta0m2|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2y1n2i1nzvkmmvintfhzgriyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2y1n2i1nzvkmmvintfhzgriyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2y1n2i1nzvkmmvintfhzgriyz|
|A9A9A9AAA9AAAAAAAAAAA9A9AA|m2q4y2uwm2yznznimtzly2y2yt|
|A9A9A9AAA9AAAAAAAAAAA9A9AA|m2q4y2uwm2yznznimtzly2y2yt|
|A9A9A9AAA9AAAAAAAAAAA9A9AA|m2q4y2uwm2yznznimtzly2y2yt|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|n2u0m2zjm2nlmtlknmewzjjimt|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|n2u0m2zjm2nlmtlknmewzjjimt|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|n2u0m2zjm2nlmtlknmewzjjimt|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|m2i5y2jjote3y2q5mtu0mgjjzm|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|m2i5y2jjote3y2q5mtu0mgjjzm|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|m2i5y2jjote3y2q5mtu0mgjjzm|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2i5y2nmodg3nju1nze5odgzog|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2i5y2nmodg3nju1nze5odgzog|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2i5y2nmodg3nju1nze5odgzog|
|A9A9A9AAAAA9AAA9AAAAA9A9AA|y2q2m2jknwy1mmu4nzhkm2m1mt|
|A9A9A9AAAAA9AAA9AAAAA9A9AA|y2q2m2jknwy1mmu4nzhkm2m1mt|
|A9A9A9AAAAA9AAA9AAAAA9A9AA|y2q2m2jknwy1mmu4nzhkm2m1mt|
|A9A9A9AAAAA9AAA9AAAAA9AAAA|m2y1y2jjyjm3mjk5mwjlm2jjnt|
|A9A9A9AAAAA9AAA9AAAAA9AAAA|m2y1y2jjyjm3mjk5mwjlm2jjnt|
|A9A9A9AAAAA9AAA9AAAAA9AAAA|m2y1y2jjyjm3mjk5mwjlm2jjnt|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|y2y5n2mwmtk4zte0zmiynmi0zt|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|y2y5n2mwmtk4zte0zmiynmi0zt|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — event_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|9A999A99-9999-9999-AA99-9A999A999999|3    |
|9A99999A-9AAA-9999-A999-999A999999A9|3    |
|9A99A999-9999-999A-A999-A9999A999999|3    |
|99999999-9999-999A-9A99-999999999999|3    |
|9A999999-9999-99A9-9A99-999A99999A9A|3    |
|99A99999-9A99-9AA9-99A9-99A999A9A9A9|2    |
|999AA999-9A9A-9A99-A99A-99A9A9999A99|2    |
|9AA99999-A999-9999-99A9-9A999999A99A|2    |
|99999999-999A-9A9A-A9A9-99999AA9AAAA|2    |
|99A9A9A9-9999-9A9A-9999-AAA99A99999A|2    |
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
|99999999-9999-9999-999A-99A999999A99|05498721-2144-4212-836b-38d366641f10|
|99999999-9999-9999-999A-99AA9AA9AA99|07709447-9742-4995-834d-92df5fa3ea98|
|99999999-9999-9999-999A-99AAAA9999AA|86326447-0457-4478-887d-29fefe7338de|
|99999999-9999-9999-999A-A9A99A999999|97209974-8421-4712-912c-f6f53e580638|
|99999999-9999-9999-999A-A9AA9A99A999|24176229-2805-4065-815c-b3cf3b77a172|
|99999999-9999-9999-999A-A9AA9A9AA99A|19236986-2646-4728-873a-b4eb8c4fc14d|
|99999999-9999-9999-999A-A9AAAAA9999A|31780875-9203-4948-895f-b3bdfff8314d|
|99999999-9999-9999-999A-AA999999999A|24795220-2148-4328-999a-bb867561022c|
|99999999-9999-9999-999A-AA99A9999AA9|23514948-5489-4881-924d-fe83a6910bf9|
|99999999-9999-9999-999A-AA9AAA9A99A9|74317227-5898-4666-943b-da8fcc0a29b5|
|99999999-9999-9999-999A-AAAA999999A9|87131121-2592-4561-992b-cddc790356f9|
|99999999-9999-9999-999A-AAAA9A9A999A|06508699-6362-4556-973d-bfcf1b9e748c|
|99999999-9999-9999-99A9-99999A99AAA9|01089993-6308-4183-80a5-54792e68aed6|
|99999999-9999-9999-99A9-9999AA9A9AA9|07298364-5234-4488-90a3-8262ed5e6ea0|
|99999999-9999-9999-99A9-999A9A999A9A|85736757-9671-4487-83b1-496e8d325a1c|
|99999999-9999-9999-99A9-9A9999999999|97323576-0412-4932-82b0-4b1029525080|
|99999999-9999-9999-99A9-9A9999A9999A|14985178-5140-4122-91b3-5e1713a2976d|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|19235|
|9999A999|12227|
|999999A9|11869|
|9A999999|11603|
|99A99999|11589|
|A9999999|11556|
|99999A99|11470|
|9999999A|10842|
|999A9999|10838|
|A999A999|7933 |
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
+--------------+------+
|shape         |count |
+--------------+------+
|AAA-AAAA      |333135|
|AAAA          |222054|
|AAA-AA-AAAA   |111426|
|AAAAA-AAAAAAAA|111214|
|AAAAAA-AAAAAAA|49338 |
+--------------+------+


 SAMPLE VALUES — event_type
+--------------+--------------+
|shape         |sample_value  |
+--------------+--------------+
|AAA-AA-AAAA   |Add-To-Cart   |
|AAA-AA-AAAA   |Add-To-Cart   |
|AAA-AA-AAAA   |Add-To-Cart   |
|AAA-AAAA      |App-Open      |
|AAA-AAAA      |App-Open      |
|AAA-AAAA      |App-Open      |
|AAAA          |View          |
|AAAA          |View          |
|AAAA          |View          |
|AAAAA-AAAAAAAA|Order-Complete|
|AAAAA-AAAAAAAA|Order-Complete|
|AAAAA-AAAAAAAA|Order-Complete|
|AAAAAA-AAAAAAA|Signup-Started|
|AAAAAA-AAAAAAA|Signup-Started|
|AAAAAA-AAAAAAA|Signup-Started|
+--------------+--------------+


 VALUE SHAPES — event_category
+----------+------+
|shape     |count |
+----------+------+
|AAAAAAAAAA|555189|
|AAAAAAAA  |222640|
|AAAAAA    |49338 |
+----------+------+


 SAMPLE VALUES — event_category
+----------+------------+
|shape     |sample_value|
+----------+------------+
|AAAAAA    |Signup      |
|AAAAAA    |Signup      |
|AAAAAA    |Signup      |
|AAAAAAAA  |Commerce    |
|AAAAAAAA  |Commerce    |
|AAAAAAAA  |Commerce    |
|AAAAAAAAAA|Engagement  |
|AAAAAAAAAA|Engagement  |
|AAAAAAAAAA|Engagement  |
+----------+------------+


 VALUE SHAPES — device_id
+----------+-----+
|shape     |count|
+----------+-----+
|99999999-9|11984|
|9999999A-9|8224 |
|99999A99-9|7968 |
|99999999-A|7726 |
|999A9999-9|7654 |
|9A999999-9|7652 |
|99A99999-9|7130 |
|A9999999-9|6919 |
|9999A999-9|6882 |
|999999A9-9|6717 |
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

 Discovery complete for crm_silver_events — scanned 827167 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_geo
====================================================================================================

 SCHEMA
root
 |-- geo_sk: string (nullable = true)
 |-- area_sk: string (nullable = true)
 |-- city_raw: string (nullable = true)
 |-- city: string (nullable = true)
 |-- country_raw: string (nullable = true)
 |-- country: string (nullable = true)
 |-- latitude: double (nullable = true)
 |-- longitude: double (nullable = true)
 |-- geo_percision: string (nullable = true)
 |-- is_city_resolved: boolean (nullable = true)
 |-- is_country_resolved: boolean (nullable = true)
 |-- is_geo_valid: boolean (nullable = true)
 |-- geo_quality_score: byte (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 9986

 NULL COUNTS
+------+-------+--------+----+-----------+-------+--------+---------+-------------+----------------+-------------------+------------+-----------------+-------------+
|geo_sk|area_sk|city_raw|city|country_raw|country|latitude|longitude|geo_percision|is_city_resolved|is_country_resolved|is_geo_valid|geo_quality_score|dw_created_at|
+------+-------+--------+----+-----------+-------+--------+---------+-------------+----------------+-------------------+------------+-----------------+-------------+
|0     |0      |0       |0   |0          |0      |459     |491      |0            |0               |0                  |0           |0                |0            |
+------+-------+--------+----+-----------+-------+--------+---------+-------------+----------------+-------------------+------------+-----------------+-------------+


 VALUE SHAPES — geo_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAA9AAA9AAAAAAAAAAAAAAAAAA|2846 |
|A9AAAAAAAAA9AAAAAAA9AAAAAA|1489 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1434 |
|AAAAAAAAA9A9AAA9AAAAAAAAAA|1424 |
|AAAAAAA9A9AAAAAAA9A9AAAAAA|1408 |
|AAAAAAAAAAA9AAAAA9A9A9AAAA|1385 |
+--------------------------+-----+


 SAMPLE VALUES — geo_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
+--------------------------+--------------------------+


 VALUE SHAPES — area_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|366  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|247  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|246  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|212  |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|212  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|211  |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|205  |
|AAA9AAA9AAAAAAAAAAAAAAAAAA|149  |
|AAAAAAA9AAAAAAAAAAAAAAA9AA|145  |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|143  |
+--------------------------+-----+


 SAMPLE VALUES — area_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAAAAAAAAAA9AA|n2m3y2y4n2y4mtrizjyzywm5mg|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2y1m2i4ntg0mtjmyzyyzdcyng|
|A9A9A9A9AAAAA9A9AAAAAAA9AA|y2u2n2q3mdyxy2e0yzdinzu3mj|
|A9A9A9A9AAAAAAA9AAAAAAA9A9|m2q3m2u4mwzkotc4zgrinmm1y2|
|A9A9A9A9AAAAAAAAAAA9AAA9A9|n2m3y2y2yjfknwewmtm4mjq0m2|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|n2m3m2u5ngvlnwmyndfizgm4md|
|A9A9A9AAA9AAA9AAAAAAAAAAAA|y2m4m2rkn2mxn2rmnzvkmmixnm|
|A9A9A9AAAAA9AAAAAAA9AAA9AA|y2i1n2fmngq4nddknmi5otm4zt|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|m2y4y2uzztk0mtazzdljmzuymj|
|A9A9A9AAAAAAA9A9AAA9AAAAAA|n2y1y2jmztuwy2m3mge2mwnhyt|
|A9A9A9AAAAAAAAA9AAA9AAA9AA|n2q5y2fkntkxmde3nmm5zdg4zj|
|A9A9A9AAAAAAAAAAA9A9AAAAAA|m2m4m2vlotdkmjdhy2m2nwnmow|
|A9A9A9AAAAAAAAAAA9AAAAA9AA|n2i0n2njztezmwqxm2zlogu0nj|
|A9A9A9AAAAAAAAAAA9AAAAAAAA|n2u0y2nknmmzmjvmy2nlmmfind|
|A9A9A9AAAAAAAAAAAAA9AAA9AA|y2q5m2jmzwzkmzmymge5mjk3mz|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2m3mwm2y2jhyjk2zgnhmjnlmg|
|A9A9AAA9A9AAAAAAAAAAAAAAAA|n2i4zja4n2vjngqyntcxymzkot|
|A9A9AAA9AAA9A9A9A9AAAAAAAA|m2m5nwe2mde3m2q5y2mxmgrknd|
|A9A9AAA9AAA9A9A9AAAAAAAAAA|y2i1yzc2mzq0y2e1ymyzowvizt|
|A9A9AAA9AAA9A9A9AAAAAAAAAA|y2i1zdk0njy5n2e2ntzmogzkyt|
|A9A9AAA9AAA9A9AAAAAAAAAAAA|y2q2ztk5nwm1n2zkzwmymtexmd|
|A9A9AAA9AAA9AAA9AAA9AAA9A9|m2e4ymi3mdc1odg3odi3zjy1m2|
|A9A9AAA9AAA9AAA9AAA9AAA9AA|y2q4nmu5mgm4mde2mmm4zmq1mj|
|A9A9AAA9AAA9AAA9AAA9AAAAAA|y2q0odi2mdi4nja3yti3nzliod|
|A9A9AAA9AAA9AAA9AAAAA9A9AA|n2i4mmy3ymu5yzk2zgiwy2m2md|
|A9A9AAA9AAA9AAA9AAAAAAA9AA|n2u0zme0zji5njq5yzfmngq0mw|
|A9A9AAA9AAA9AAA9AAAAAAA9AA|n2u5ota2mjk1nwq5mdyzogm4mj|
|A9A9AAA9AAA9AAA9AAAAAAA9AA|y2e5yze0ndm3zgq2mtzjndm3zd|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|m2i1zjg1nji5zta4mmnlnzhkow|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|m2u1yte5ndk3yzy0ythmzdnkzw|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|y2e1mde1ytg4ota0nmezyjcyyt|
|A9A9AAA9AAA9AAAAA9A9AAAAA9|n2i1zwu1zjm3mmrin2e2otbkm2|
|A9A9AAA9AAA9AAAAA9A9AAAAAA|m2u0zjy0ntk5mwfjy2u0zmeynm|
|A9A9AAA9AAA9AAAAA9AAAAA9AA|n2u3nme3zmi4zjaym2fjodq1nd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2m5ntm1mjq4nwzimtm4nmq3yj|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|n2q2ndy0zgy3zgrinje2ndc0yj|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|y2e0mwi0mgq1ytrhndg2zmq2zw|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|m2e1mzy5zjg5mmjiytk0njvmyz|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2y3mwy4ytq5ztrhmtg0mdbknz|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|y2i0nti2mjm2ngnlmdm2ztdmnm|
|A9A9AAA9AAA9AAAAAAAAA9AAAA|y2m0ztc3nmq1ndixotmzm2nmmt|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2q4zwy5yze2mzcwmzliyja2zd|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|n2e5mzk5ywe1mdjhmdezymi3nd|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|y2e0nzk2ntg5zwqyntbhzwm2nd|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|m2i4ztg2ota3owizndcwnmexzg|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|m2m1yjq2ztc3zjyymmqwzgmwmg|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|m2u3zde1yzc2yzkzmgyyymqwmj|
|A9A9AAA9AAAAA9A9AAA9A9AAAA|m2u4nti2mzvjy2q5mzm4y2qyzm|
|A9A9AAA9AAAAA9A9AAAAAAAAAA|y2y1yji4oguzm2e5mwzhndexnm|
|A9A9AAA9AAAAA9AAAAAAAAAAAA|n2y5odg1zgyzm2ewyzzkzmjjnz|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — city_raw
+----------------+-----+
|shape           |count|
+----------------+-----+
|AAAAA           |2762 |
|AA AAA          |1444 |
|AAA AAAAA       |1389 |
|AAA AA AAAAAAA  |1374 |
|AAAAAAA         |1372 |
|AAAAAAAA        |1348 |
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


 VALUE SHAPES — city
+--------------+-----+
|shape         |count|
+--------------+-----+
|AAAAA         |2832 |
|AA AAA        |1489 |
|AAA AAAAA     |1434 |
|AAAAAAA       |1425 |
|AAA AA AAAAAAA|1421 |
|AAAAAAAA      |1385 |
+--------------+-----+


 SAMPLE VALUES — city
+--------------+--------------+
|shape         |sample_value  |
+--------------+--------------+
|AA AAA        |Al Ain        |
|AA AAA        |Al Ain        |
|AA AAA        |Al Ain        |
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AAAAA     |Abu Dhabi     |
|AAA AAAAA     |Abu Dhabi     |
|AAA AAAAA     |Abu Dhabi     |
|AAAAA         |Ajman         |
|AAAAA         |Ajman         |
|AAAAA         |Ajman         |
|AAAAAAA       |Sharjah       |
|AAAAAAA       |Sharjah       |
|AAAAAAA       |Sharjah       |
|AAAAAAAA      |Fujairah      |
|AAAAAAAA      |Fujairah      |
|AAAAAAAA      |Fujairah      |
+--------------+--------------+


 VALUE SHAPES — country_raw
+----------------------+-----+
|shape                 |count|
+----------------------+-----+
|AAA                   |4836 |
|AAAAAA AAAA AAAAAAAA  |2490 |
|A.A.A                 |2405 |
|AAA??                 |128  |
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


 VALUE SHAPES — country
+-----+-----+
|shape|count|
+-----+-----+
|AAA  |9986 |
+-----+-----+


 SAMPLE VALUES — country
+-----+------------+
|shape|sample_value|
+-----+------------+
|AAA  |uae         |
|AAA  |uae         |
|AAA  |uae         |
+-----+------------+


 VALUE SHAPES — geo_percision
+----------+-----+
|shape     |count|
+----------+-----+
|AAAAA     |9043 |
|AAAA-AAAAA|943  |
+----------+-----+


 SAMPLE VALUES — geo_percision
+----------+------------+
|shape     |sample_value|
+----------+------------+
|AAAA-AAAAA|city-level  |
|AAAA-AAAAA|city-level  |
|AAAA-AAAAA|city-level  |
|AAAAA     |exact       |
|AAAAA     |exact       |
|AAAAA     |exact       |
+----------+------------+


 Discovery complete for crm_silver_geo — scanned 9986 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_order_items
====================================================================================================

 SCHEMA
root
 |-- order_item_sk: string (nullable = true)
 |-- order_sk: string (nullable = true)
 |-- order_item_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- product_name: string (nullable = true)
 |-- qty: integer (nullable = true)
 |-- unit_price: decimal(10,2) (nullable = true)
 |-- line_total: decimal(10,2) (nullable = true)
 |-- is_total_valid: boolean (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 359798

 NULL COUNTS
+-------------+--------+-------------+--------+------------+---+----------+----------+--------------+-------------+
|order_item_sk|order_sk|order_item_id|order_id|product_name|qty|unit_price|line_total|is_total_valid|dw_created_at|
+-------------+--------+-------------+--------+------------+---+----------+----------+--------------+-------------+
|0            |0       |0            |0       |0           |0  |0         |0         |0             |0            |
+-------------+--------+-------------+--------+------------+---+----------+----------+--------------+-------------+


 VALUE SHAPES — order_item_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|12994|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|7809 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|7784 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|7713 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|7684 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|7667 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|7615 |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|4693 |
|AAAAAAAAAAA9AAAAAAAAAAA9AA|4681 |
|AAAAAAAAAAA9AAA9AAAAAAAAAA|4677 |
+--------------------------+-----+


 SAMPLE VALUES — order_item_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAA9A9A9AAA9AA|n2q3m2m3n2u1mti1m2m4nwu3mt|
|A9A9A9A9A9A9AAA9AAAAAAAAAA|m2q3y2e5m2i2zde4mwfhndfimt|
|A9A9A9A9A9A9AAA9AAAAAAAAAA|n2m4m2q4n2u4zgm0mgfmowfhnm|
|A9A9A9A9A9A9AAAAAAA9AAA9AA|m2u2n2e1m2u4nthjmdi0mdk2mt|
|A9A9A9A9A9A9AAAAAAAAAAA9AA|n2q0n2m0n2u2ndzjyjaymjm1mz|
|A9A9A9A9A9AAA9AAAAAAAAAAAA|m2e0m2m3n2rjn2fmnmzimtdimj|
|A9A9A9A9A9AAAAA9A9AAAAA9AA|m2i3n2y0n2rhnge5y2qwyjm1ot|
|A9A9A9A9A9AAAAA9AAA9AAAAAA|m2i5m2y2n2rhmwi4ymi2nwnjzg|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2i4n2q0y2fimtg3odnjyta0zw|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q2m2i5y2fmywq1otvlotk0yz|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|n2u5m2u2n2jmoty3ntfhoty2nj|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2m4y2e0n2nkztczyta1zmu2ng|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|m2q3y2e0m2jmztlmywi3nwrhmd|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|n2e5y2q0m2vjndhjmmy5zdaxyw|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|n2m3y2q1y2nmmtmznzu5yzexod|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|n2m5m2q3y2uwndbkntqwoda3mm|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|y2y0y2u2y2zmndhkytjkzta4nz|
|A9A9A9A9AAA9A9A9AAA9AAA9AA|y2i4y2u5yzu2n2y2ytk0ytk3ng|
|A9A9A9A9AAA9A9A9AAAAA9AAAA|m2m2m2e3ndq2m2u2zwmzy2mwyz|
|A9A9A9A9AAA9A9A9AAAAAAA9AA|m2u5n2i0odk3n2y1mtkxowy5nw|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|m2m2m2m3ztm1y2zhzdy2nzg1nz|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|n2y4n2u1nza1n2ewzdq0mdq4mg|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|y2u5y2y1ngu5y2jkngy5zme1mm|
|A9A9A9A9AAA9A9AAAAAAAAAAAA|n2i2y2m2nte0y2zkodhjymnmmg|
|A9A9A9A9AAA9A9AAAAAAAAAAAA|y2m1n2u3mgy3n2jkyjrmotcznd|
|A9A9A9A9AAA9AAA9A9A9AAAAAA|m2u0y2m2nmy2owe0m2y2zgvlzw|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y0n2m5nmm2yzq5otc3yzk5yw|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|n2y0m2i3ngy5mje5yti0nje3ot|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|n2y5n2q0mte4mdk4oti5nzk4nt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2i4n2m4yjm1mgu4mze2nzuwog|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|y2u5n2e3nje3zwe4odm2yjhiyw|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|y2y1y2y0mji3zjm2otk2nguwod|
|A9A9A9A9AAA9AAA9AAAAA9AAAA|m2e1y2q1ytg4mzu2mgzmy2iwzg|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|m2q1m2i4mwe3owq3ndnjmza1zd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|m2q3y2q0mmy4mty1ytkxnjy1ot|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|m2q3y2y4mzg5yjk5nzvmota1nm|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2q2n2y1ngu1mgi0zmuxytcwym|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2q3y2u5yji0mdm1zdnlmwriow|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2u2y2m1yje1mzc1zgzjzmvmnm|
|A9A9A9A9AAA9AAAAA9A9A9A9AA|n2q5y2i0zja3ztflm2u3y2q5zd|
|A9A9A9A9AAA9AAAAA9AAAAA9AA|y2u5m2u2mda3mzqyn2uymjc5mw|
|A9A9A9A9AAA9AAAAA9AAAAAAAA|m2e0y2u2zgi0zwqzm2yymjcymj|
|A9A9A9A9AAA9AAAAA9AAAAAAAA|m2y0m2e3nwm5zmiwm2iwogzkmw|
|A9A9A9A9AAA9AAAAAAA9AAA9A9|m2q2n2q4ymq3otzhntg2zwy0y2|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2e1m2e5ndk0zmfkogi0odm0zg|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2i5n2m5mme0odfkzdi1zjc4yt|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2q5y2u1mjk3njiyody0zgm4mm|
|A9A9A9A9AAA9AAAAAAA9AAAAA9|n2y2y2y3ymm0njkxnzq5mjbky2|
|A9A9A9A9AAA9AAAAAAA9AAAAA9|y2i1m2m5mdk4mdlinwy0zdvhm2|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2i1n2i3mdk1mmfjmja3njqwot|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — order_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|13177|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|7799 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|7773 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|7770 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|7760 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|7662 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|7374 |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|4836 |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|4752 |
|AAAAAAA9AAAAAAAAAAAAAAA9AA|4737 |
+--------------------------+-----+


 SAMPLE VALUES — order_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAAAAAA9A9A9AA|n2e3y2q2m2i5mdbhywm1m2e4md|
|A9A9A9A9A9A9AAAAAAA9A9A9AA|n2e3y2q2m2i5mdbhywm1m2e4md|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2i1m2q3n2myzgrlmmi0zdq2nj|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2q0y2u5n2nmyzqwmjm1yzcwyz|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2q0y2u5n2nmyzqwmjm1yzcwyz|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2y4m2m5m2rimzbinmy0ywvlng|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2y2y2u3n2rhmmvjodhhzgvmnm|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|y2i5y2m5mzc5y2i1mjgxzmmyyt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m1y2q3owe2owm3ogq4odnmmj|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m1y2q3owe2owm3ogq4odnmmj|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m2m2y1ndc3mtq0nwu1zdflzd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2m5m2q1oti0ngu1mdlhmjc5yt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2m5m2i2mjc1mdg4mzkxotvhmw|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2m5m2i2mjc1mdg4mzkxotvhmw|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2m5m2i2mjc1mdg4mzkxotvhmw|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2e3y2m3mgm1ntuynwm5nmqymt|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2e3y2m3mgm1ntuynwm5nmqymt|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2e3y2m3mgm1ntuynwm5nmqymt|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2m5n2m1mwy0mjhlngnky2nlmj|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2m5n2m1mwy0mjhlngnky2nlmj|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2m5n2m1mwy0mjhlngnky2nlmj|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|n2q4n2m2nzc0owqxndzkotg3n2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|y2y1m2q3zge2yzzhzjqyodi3m2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|y2y1m2q3zge2yzzhzjqyodi3m2|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i1y2m2mzi4ntbkztdhodi5og|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i1y2m2mzi4ntbkztdhodi5og|
|A9A9A9A9AAA9AAAAAAAAAAAAA9|m2e2m2e4ogi3yjqzytjkmdlmy2|
|A9A9A9A9AAA9AAAAAAAAAAAAA9|m2e2m2e4ogi3yjqzytjkmdlmy2|
|A9A9A9A9AAA9AAAAAAAAAAAAA9|m2e2m2e4ogi3yjqzytjkmdlmy2|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2i3m2e0ztk0zwnmoddhmwzkot|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e0y2i5zti5mjaynmqymzlhnz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e0y2i5zti5mjaynmqymzlhnz|
|A9A9A9A9AAAAA9A9AAA9AAAAAA|y2y0n2u1mmnkn2e5ngi5mmrlnd|
|A9A9A9A9AAAAA9AAAAA9AAAAAA|y2q2n2m1ntgwy2qwndk0ntbjzw|
|A9A9A9A9AAAAA9AAAAA9AAAAAA|y2q2n2m1ntgwy2qwndk0ntbjzw|
|A9A9A9A9AAAAA9AAAAA9AAAAAA|y2q2n2m1ntgwy2qwndk0ntbjzw|
|A9A9A9A9AAAAA9AAAAAAAAA9A9|y2u3m2u1zjlmm2jintkzody0n2|
|A9A9A9A9AAAAA9AAAAAAAAA9A9|y2u3m2u1zjlmm2jintkzody0n2|
+--------------------------+--------------------------+
only showing top 50 rows

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
+-------+------+
|shape  |count |
+-------+------+
|AAAAA  |239841|
|AAAAAA |79798 |
|AAAAAAA|40159 |
+-------+------+


 SAMPLE VALUES — product_name
+-------+------------+
|shape  |sample_value|
+-------+------------+
|AAAAA  |abaya       |
|AAAAA  |abaya       |
|AAAAA  |abaya       |
|AAAAAA |hoodie      |
|AAAAAA |hoodie      |
|AAAAAA |hoodie      |
|AAAAAAA|blanket     |
|AAAAAAA|blanket     |
|AAAAAAA|blanket     |
+-------+------------+


 Discovery complete for crm_silver_order_items — scanned 359798 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_order_status_history
====================================================================================================

 SCHEMA
root
 |-- order_status_history_sk: string (nullable = true)
 |-- order_sk: string (nullable = true)
 |-- change_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- order_status: string (nullable = true)
 |-- changed_ts: timestamp (nullable = true)
 |-- has_terminal_before: integer (nullable = true)
 |-- is_invalid_stage: integer (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 178915

 NULL COUNTS
+-----------------------+--------+---------+--------+------------+----------+-------------------+----------------+-------------+
|order_status_history_sk|order_sk|change_id|order_id|order_status|changed_ts|has_terminal_before|is_invalid_stage|dw_created_at|
+-----------------------+--------+---------+--------+------------+----------+-------------------+----------------+-------------+
|0                      |0       |0        |0       |0           |0         |105074             |0               |0            |
+-----------------------+--------+---------+--------+------------+----------+-------------------+----------------+-------------+


 VALUE SHAPES — order_status_history_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|6444 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|3899 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|3891 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|3878 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|3811 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|3711 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|3706 |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|2343 |
|AAAAAAAAAAA9AAA9AAAAAAAAAA|2334 |
|AAA9AAAAAAAAAAAAAAAAAAA9AA|2329 |
+--------------------------+-----+


 SAMPLE VALUES — order_status_history_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9A9AAAAA9AAAAAA|n2y4n2m3m2u3m2rhzmy0nthjym|
|A9A9A9A9A9A9AAA9AAA9A9AAAA|m2u2y2e0n2e1njg5ogm4n2mymt|
|A9A9A9A9A9A9AAAAA9A9AAAAAA|n2m1n2e1m2m3mjzmn2m2mtjizt|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|m2m0n2e4y2q5mwqyzwi0odgwyw|
|A9A9A9A9A9AAAAA9AAAAAAA9A9|n2q2n2e0m2zhodc1mgflnty2n2|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|y2y1n2m2m2nmnzy1zmmzzdq0ng|
|A9A9A9A9A9AAAAAAAAAAAAA9AA|m2y0y2i3n2vjymqwndninjy0nz|
|A9A9A9A9AAA9A9AAAAA9AAA9AA|m2m5n2e3zti1n2jkmzm0mtq0mt|
|A9A9A9A9AAA9A9AAAAAAAAAAAA|n2y5y2m3nmm5y2rlotlhytuymm|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|n2i2m2y4owy3nmq3njc1ota5og|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|n2m4m2y5zwy5zdi5odg2nmy5zd|
|A9A9A9A9AAA9AAA9AAA9AAAAA9|y2u0m2y0mzi0njq5ndi5mjlkm2|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m0n2i2mwi0mmm0mti0mzjkzg|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m1m2q2yjk3njy0mja4zmqwmd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|m2e3m2u0mje1yzc5otexzjq5od|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|y2q1n2y0nju5mda1ymqwyjy1yt|
|A9A9A9A9AAA9AAA9AAAAAAAAA9|y2i3m2m3mwq5mzi2zmiwzddiy2|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e1n2m1mzq1mde0mzgwowqxyj|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2i0y2u5owe5zmy3odlmzjzlmt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2q3y2e2yza5mzg3mjbindaymw|
|A9A9A9A9AAA9AAAAA9AAAAAAAA|m2i3m2q3yjc2ytyzn2mzzmjmzt|
|A9A9A9A9AAA9AAAAA9AAAAAAAA|m2q2n2e5nmq2mmrin2qwotmwng|
|A9A9A9A9AAA9AAAAA9AAAAAAAA|n2i1n2m3ymu2othjm2njzdbimz|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2y0y2q5owi3mdqzyzy1yje4nt|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2y5n2e1zgi4ndfkmty0mdq5mt|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2i4n2m2zjk0zjkzzdg0zjy5yt|
|A9A9A9A9AAA9AAAAAAA9AAAAA9|n2e0m2e1mjc1otaynji0yzjhn2|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2e3m2u3ytu3mwuwzgu1yzexyj|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2u1n2q2ztu0ytuxmtk5mmuwnw|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2u2y2m3mdk5zdbkymi0ywzmyj|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|n2e4m2q3yjg3otmzzgnky2njmt|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|y2m2y2q3yjg0zgixndlln2exyw|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|m2m5m2q2zgu4ymizywuwmdq1m2|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2u4n2q5ndg0nzexytrjodk5mg|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2e2y2e3zwq2zwfiytnhzja3mt|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2e3y2e0mzc2ndkwymuynzk0mg|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2q1y2u4njy0ndcxywvizjizyz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2y2m2y5mdq3yzuzzdfkmznind|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2e1m2m4ndm4mdrhmdbhmdqzym|
|A9A9A9A9AAAAA9A9A9A9AAA9AA|n2e0n2y4mzriy2y1y2q0yjm0zg|
|A9A9A9A9AAAAA9A9AAAAAAA9AA|n2u4y2q0yzzhn2e3ntdlzje3nd|
|A9A9A9A9AAAAA9A9AAAAAAAAAA|n2m1m2y3mgexy2i2nzzkntjmyz|
|A9A9A9A9AAAAA9AAAAAAAAA9AA|n2i0y2y1njdhy2zlmtjkytq0zg|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|n2i2n2i2nddmn2zmzjmzzdlimw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|n2q3n2e5ytmwm2zjntblywvjzm|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|n2y5m2y5ymrimzk0y2q5ztnmzg|
|A9A9A9A9AAAAAAA9A9AAAAAAAA|n2u0y2m5ntjiyza0m2nmnddizg|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|n2i4m2m1ywrjnzg5nmy3mge4zd|
|A9A9A9A9AAAAAAA9AAA9AAAAA9|n2i1y2u3ywjkowe2mme1odzmn2|
|A9A9A9A9AAAAAAA9AAA9AAAAA9|n2m3m2e2ognjowe0nzy1ntuzm2|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — order_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|6522 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|3954 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|3946 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|3918 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|3875 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|3770 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|3637 |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|2424 |
|AAAAAAA9AAAAAAAAAAAAAAA9AA|2408 |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|2390 |
+--------------------------+-----+


 SAMPLE VALUES — order_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAAAAAA9A9A9AA|n2e3y2q2m2i5mdbhywm1m2e4md|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2i1m2q3n2myzgrlmmi0zdq2nj|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2i1m2q3n2myzgrlmmi0zdq2nj|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2y4m2m5m2rimzbinmy0ywvlng|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2y4m2m5m2rimzbinmy0ywvlng|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|y2i5y2m5mzc5y2i1mjgxzmmyyt|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|y2i5y2m5mzc5y2i1mjgxzmmyyt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m1y2q3owe2owm3ogq4odnmmj|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m2m2y1ndc3mtq0nwu1zdflzd|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m2m2y1ndc3mtq0nwu1zdflzd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2m5m2q1oti0ngu1mdlhmjc5yt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2m5m2i2mjc1mdg4mzkxotvhmw|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2y4m2e0mtm2mdu1nzuzmmqzzd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2y4m2e0mtm2mdu1nzuzmmqzzd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2y5y2i3ntg4yzblnzc3mjc0mz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2e3y2m3mgm1ntuynwm5nmqymt|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2m5m2u5mda2ytriytm5zjzlog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2m5m2u5mda2ytriytm5zjzlog|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2m5n2m1mwy0mjhlngnky2nlmj|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|n2q4n2m2nzc0owqxndzkotg3n2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|n2q4n2m2nzc0owqxndzkotg3n2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|y2y1m2q3zge2yzzhzjqyodi3m2|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAAAA9|m2e2m2e4ogi3yjqzytjkmdlmy2|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2i3m2e0ztk0zwnmoddhmwzkot|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2i3m2e0ztk0zwnmoddhmwzkot|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e0y2i5zti5mjaynmqymzlhnz|
|A9A9A9A9AAAAA9A9AAA9AAAAAA|y2y0n2u1mmnkn2e5ngi5mmrlnd|
|A9A9A9A9AAAAA9AAAAAAAAA9A9|y2u3m2u1zjlmm2jintkzody0n2|
|A9A9A9A9AAAAAAA9A9A9AAA9AA|m2i1y2m0ngyxndm3n2i1mda0nt|
|A9A9A9A9AAAAAAA9A9A9AAA9AA|m2i1y2m0ngyxndm3n2i1mda0nt|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|n2i3n2m5mjuxzgy3ndu5y2y2nm|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|n2i3n2m5mjuxzgy3ndu5y2y2nm|
|A9A9A9A9AAAAAAA9AAA9A9AAAA|n2q0y2e2zjqyyzc5ndm0n2rmog|
|A9A9A9A9AAAAAAA9AAA9A9AAAA|n2q0y2e2zjqyyzc5ndm0n2rmog|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|m2m5n2e1nzbkngq4zta0zdg1md|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|y2m5m2y5zjkymta5mtc2zty5mz|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — change_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|999999A9-9999-99A9-A9A9-999A99A99999|3    |
|9999A999-999A-9999-999A-999999999999|2    |
|9A9A999A-AA99-99AA-A999-AA999A99A999|2    |
|9AA99A99-9999-9999-AA99-9A9A999A99A9|2    |
|9AAA9A99-A9A9-9A9A-9999-999999999AAA|2    |
|A9A9999A-9A99-9999-99A9-9A999A99A9A9|2    |
|99A9A99A-9A99-9999-9999-999A9A999999|2    |
|99999999-99A9-9999-99A9-99A99999A999|2    |
|A9999999-A999-9999-999A-A9999A9AA999|2    |
|99999999-9999-9999-A999-AA9999AAAA99|2    |
+------------------------------------+-----+


 SAMPLE VALUES — change_id
+------------------------------------+------------------------------------+
|shape                               |sample_value                        |
+------------------------------------+------------------------------------+
|99999999-9999-9999-9999-999999999999|18865823-1765-4519-8131-323861508825|
|99999999-9999-9999-9999-99AA999A9999|05528930-1505-4059-8529-86ee246d9505|
|99999999-9999-9999-9999-9AA9AAAAAAA9|83504434-2566-4380-9737-4ee4dceccaf6|
|99999999-9999-9999-9999-A999AA99A9AA|94698507-2539-4114-9568-f745ac02e6fb|
|99999999-9999-9999-9999-A99A99A999A9|98757421-8360-4680-8017-e08a27a298a0|
|99999999-9999-9999-9999-A9A999A9AA9A|83616947-3697-4878-8573-b3c736c1ff8b|
|99999999-9999-9999-9999-A9AAA9A9AA99|87819253-1892-4895-8617-c5bca8b0cb99|
|99999999-9999-9999-99A9-A999A9AAA999|03910494-6813-4920-95c9-b073e5cbf346|
|99999999-9999-9999-99AA-99A99A9999A9|14101339-1969-4506-93ed-70e60f5589c9|
|99999999-9999-9999-9A99-9999A99A99A9|30244660-2700-4624-9a94-0420c52d89c1|
|99999999-9999-9999-9A99-99AAA99999A9|35290595-5735-4967-8c58-61dfe53869e4|
|99999999-9999-9999-9A99-9A99A99A9A9A|85451739-6140-4163-8d86-7d22f62e9d9e|
|99999999-9999-9999-9A99-9AAA9A99A99A|39511149-2356-4809-9c35-2fae6b43c97f|
|99999999-9999-9999-9A99-A99A99999A99|52230175-4690-4604-8d34-b76b21428b40|
|99999999-9999-9999-9A9A-A9A9A999A999|68540463-2308-4807-9c1c-e7a5f157b790|
|99999999-9999-9999-9A9A-AAA99A99AAAA|30579670-2216-4925-9e4f-dca03d07fcab|
|99999999-9999-9999-9AA9-9999999A9999|73863362-3786-4690-9ea8-8189726b9894|
|99999999-9999-9999-9AA9-AA9A999A9A99|44540071-7901-4591-8ac3-aa5c596a3c94|
|99999999-9999-9999-A999-999A99A9A99A|41764070-2610-4886-a800-798f65d8f41e|
|99999999-9999-9999-A999-99AA99999999|36721360-1982-4349-b076-32be60351646|
|99999999-9999-9999-A999-9A9AA9A9A99A|57431778-6792-4086-a977-9d4cb0e1e54c|
|99999999-9999-9999-A999-9AA99A9A999A|43955705-3074-4267-b147-3fd87d0f937c|
|99999999-9999-9999-A999-A99A99A999AA|12999970-6487-4857-b771-c96a09a121dd|
|99999999-9999-9999-A999-AA9999AAAA99|06181046-5028-4101-a440-ee5538cadc93|
|99999999-9999-9999-A999-AA9999AAAA99|62647729-4814-4530-b977-ab2433dbeb40|
|99999999-9999-9999-A99A-999A99A9999A|34727720-3373-4555-b31c-202b05a8278d|
|99999999-9999-9999-A99A-99A999999999|11140162-6675-4310-b53c-28d849413458|
|99999999-9999-9999-A99A-A9999999A99A|31611887-2554-4138-b20f-d6996261b19e|
|99999999-9999-9999-A9A9-99AA9A99AAAA|46129972-1060-4460-a1e9-24dc3e84ddbb|
|99999999-9999-9999-A9A9-9A999A999A99|53757536-6255-4251-b7e6-2f053c823a57|
|99999999-9999-9999-A9A9-9A999AA99AA9|47944633-9863-4702-a5a8-3d607de40ea7|
|99999999-9999-9999-A9A9-A99A9AAA9999|83557181-8366-4248-b6e5-b55b1aac6493|
|99999999-9999-9999-A9A9-A9A99999A999|24945755-0701-4960-a2d5-d3b35680c916|
|99999999-9999-9999-A9AA-9A99AAA9A99A|33206534-6974-4701-a9cf-9d73ecb2f30a|
|99999999-9999-9999-A9AA-9A9A9A999A9A|25796284-3658-4643-b7ef-6f0d4b616d5c|
|99999999-9999-9999-A9AA-A99AAA9A9999|61739256-3115-4920-b5da-c38aad3d2492|
|99999999-9999-9999-A9AA-AA99A9AA9AAA|77545641-8481-4165-b2fd-ae15d8cc6bde|
|99999999-9999-9999-AA99-99AA9AA9AA99|89341227-3018-4194-ae64-61cf1fb0ff13|
|99999999-9999-9999-AA99-9AA9999AA999|81353038-8184-4602-af56-9ce5917cd952|
|99999999-9999-9999-AA99-AA999A99999A|16438779-4622-4022-be66-cf369c37988b|
|99999999-9999-9999-AA9A-99999999999A|43280543-2862-4718-ba4f-65950525988f|
|99999999-9999-9999-AA9A-9999AA9AA9A9|31195150-5610-4802-bb6e-2480ab1da8c6|
|99999999-9999-9999-AA9A-999A99AA9AAA|10850154-7069-4826-bf8f-912b16fb8dbe|
|99999999-9999-9999-AA9A-99A99AAA9AA9|48542170-8807-4005-bc1a-55f72acd4ee0|
|99999999-9999-9999-AA9A-9A99A99A99A9|49167100-7462-4109-bf2d-7d63e73e75a5|
|99999999-9999-9999-AA9A-9A9AAA99A999|21823383-8443-4908-aa6a-3f0aab84a308|
|99999999-9999-9999-AA9A-AA99A99A9999|05862938-9674-4031-ab0f-ad34f50e6314|
|99999999-9999-9999-AA9A-AA9A9999999A|51634166-2918-4078-ac4b-ed2a7032389b|
|99999999-9999-9999-AAA9-A999AAA9AA99|80235973-9728-4302-bac3-c104bfe6eb92|
|99999999-9999-9999-AAA9-A9AA9A9999A9|99580649-1340-4709-aaf5-e1fc4e4699a3|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — order_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|4106 |
|99A99999|2619 |
|9999999A|2552 |
|999999A9|2529 |
|A9999999|2488 |
|999A9999|2458 |
|9A999999|2457 |
|99999A99|2435 |
|9999A999|2418 |
|9AA99999|1646 |
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
|9999999A|0004751d    |
|999999A9|001127d4    |
|999999A9|001127d4    |
|999999A9|001223a8    |
|999999AA|001847de    |
|999999AA|002763ad    |
|999999AA|002936cb    |
|99999A99|00028b78    |
|99999A99|00093f42    |
|99999A99|00093f42    |
|99999A9A|00075a5c    |
|99999A9A|00075a5c    |
|99999A9A|00139f1b    |
|99999AA9|00144dc0    |
|99999AA9|00144dc0    |
|99999AA9|00197cf1    |
|99999AAA|00018bfe    |
|99999AAA|00018bfe    |
|99999AAA|00035aaa    |
|9999A999|0008a621    |
|9999A999|0012c603    |
|9999A999|0012d106    |
|9999A99A|0013f04a    |
|9999A99A|0013f04a    |
|9999A99A|0026a33e    |
|9999A9A9|0025a0d9    |
|9999A9A9|0025a0d9    |
|9999A9A9|0035a4c7    |
|9999A9AA|0016b5ea    |
|9999A9AA|0067d9ce    |
|9999A9AA|0069e0cd    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA99|0008fd91    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034ac4e    |
|9999AA9A|0034ac4e    |
|9999AAA9|0002afd2    |
|9999AAA9|0002afd2    |
|9999AAA9|0052fac2    |
|9999AAAA|0009dbff    |
|9999AAAA|0009dbff    |
|9999AAAA|0090bbfc    |
|999A9999|000f8535    |
|999A9999|001b8590    |
+--------+------------+
only showing top 50 rows

 VALUE SHAPES — order_status
+-----------+------+
|shape      |count |
+-----------+------+
|AAAAAAAA   |113849|
|AA-AAAAAAAA|65066 |
+-----------+------+


 SAMPLE VALUES — order_status
+-----------+------------+
|shape      |sample_value|
+-----------+------------+
|AA-AAAAAAAA|in-progress |
|AA-AAAAAAAA|in-progress |
|AA-AAAAAAAA|in-progress |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
+-----------+------------+


 Discovery complete for crm_silver_order_status_history — scanned 178915 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_orders
====================================================================================================

 SCHEMA
root
 |-- order_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- provider_sk: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- created_at: timestamp (nullable = true)
 |-- order_status: string (nullable = true)
 |-- payment_provider: string (nullable = true)
 |-- payment_method: string (nullable = true)
 |-- line_total: decimal(10,2) (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 119997

 NULL COUNTS
+--------+-------+-----------+--------+-------+----------+------------+----------------+--------------+----------+-------------+
|order_sk|user_sk|provider_sk|order_id|user_id|created_at|order_status|payment_provider|payment_method|line_total|dw_created_at|
+--------+-------+-----------+--------+-------+----------+------------+----------------+--------------+----------+-------------+
|0       |0      |0          |0       |0      |0         |0           |0               |0             |0         |0            |
+--------+-------+-----------+--------+-------+----------+------------+----------------+--------------+----------+-------------+


 VALUE SHAPES — order_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|4388 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|2633 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|2618 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|2607 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|2594 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|2548 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|2452 |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|1602 |
|AAAAAAA9AAAAAAAAAAAAAAA9AA|1597 |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|1569 |
+--------------------------+-----+


 SAMPLE VALUES — order_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAAAAAA9A9A9AA|n2e3y2q2m2i5mdbhywm1m2e4md|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2i1m2q3n2myzgrlmmi0zdq2nj|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2q0y2u5n2nmyzqwmjm1yzcwyz|
|A9A9A9A9A9AAAAAAAAA9AAAAAA|y2y4m2m5m2rimzbinmy0ywvlng|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2e3y2y1n2yyowrlmwmzodmwow|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2y2y2u3n2rhmmvjodhhzgvmnm|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|y2i5y2m5mzc5y2i1mjgxzmmyyt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m1y2q3owe2owm3ogq4odnmmj|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m2m2y1ndc3mtq0nwu1zdflzd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2m5m2q1oti0ngu1mdlhmjc5yt|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2y4n2i1ogq0mja2njlhmzu1yz|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2m5m2i2mjc1mdg4mzkxotvhmw|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2y4m2e0mtm2mdu1nzuzmmqzzd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2m3n2q1mdy2ndlkmja0yzc2ot|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2y5y2i3ntg4yzblnzc3mjc0mz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2e3y2m3mgm1ntuynwm5nmqymt|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2m5m2u5mda2ytriytm5zjzlog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2u3m2y5nmy2yzgyywm1oduymm|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2m5n2m1mwy0mjhlngnky2nlmj|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|n2q4n2m2nzc0owqxndzkotg3n2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|y2y1m2q3zge2yzzhzjqyodi3m2|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i1y2m2mzi4ntbkztdhodi5og|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2q4m2q5mjy5njcxmduymwe4yj|
|A9A9A9A9AAA9AAAAAAAAAAAAA9|m2e2m2e4ogi3yjqzytjkmdlmy2|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2i3m2e0ztk0zwnmoddhmwzkot|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e0y2i5zti5mjaynmqymzlhnz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2i1n2y3yjg0zdvkywvknjczmd|
|A9A9A9A9AAAAA9A9AAA9AAAAAA|y2y0n2u1mmnkn2e5ngi5mmrlnd|
|A9A9A9A9AAAAA9AAAAA9AAAAAA|y2q2n2m1ntgwy2qwndk0ntbjzw|
|A9A9A9A9AAAAA9AAAAAAAAA9A9|y2u3m2u1zjlmm2jintkzody0n2|
|A9A9A9A9AAAAAAA9A9A9AAA9AA|m2i1y2m0ngyxndm3n2i1mda0nt|
|A9A9A9A9AAAAAAA9AAA9A9A9AA|n2i3n2m5mjuxzgy3ndu5y2y2nm|
|A9A9A9A9AAAAAAA9AAA9A9AAAA|n2q0y2e2zjqyyzc5ndm0n2rmog|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|m2m5n2e1nzbkngq4zta0zdg1md|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|y2m5m2y5zjkymta5mtc2zty5mz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2i5y2y1nzizmzg1mda0yzvjmg|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2q5y2e5otuwzgy4nji4ognjmz|
|A9A9A9A9AAAAAAA9AAAAA9AAAA|n2e2m2y4mtbiyja4ytljm2fmyj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|m2m4y2i1ntcyotc1zjzimzc0zt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|m2q0n2i2nmnmzta0ytnjngy2mj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2y0y2m2mgrizdq2mwrlzdm3nm|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|m2m0y2u1mzhimdy5nzcxmtjjmg|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2i1n2u5mwyzzdi3ywezmdqzzt|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2i2y2q2mdrkntm4ymjmzdqwmj|
|A9A9A9A9AAAAAAAAAAA9A9A9AA|n2q4m2e5zjixzmvinzq5n2q3nw|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|n2u2n2q2yznjyjdiywy5ytc1nd|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|4415 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|2607 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|2555 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|2521 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|2509 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|2505 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|2479 |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|1657 |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|1652 |
|AAA9AAA9AAAAAAAAAAAAAAAAAA|1640 |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2q2mgu1zwuwntaxzwjkzm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAAAA9AAA9AAAAA9AA|y2i1m2i1otyyn2jhm2ixywm5mj|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u1n2q5ntvmmti1mjiwmtq5ot|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2m4n2u4yzhlmjbmmwe4nzu0nz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2e2n2q0zdlkzjdiodvjntqyyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2e2n2q0zdlkzjdiodvjntqyyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2e2n2q0zdlkzjdiodvjntqyyz|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — provider_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAA9AA|51469|
|AAA9A9A9A9A9AAA9AAA9AAAAAA|34145|
|AAA9AAA9AAA9AAA9A9A9AAAAAA|17284|
|AAAAAAAAAAA9AAA9AAAAA9AAAA|17099|
+--------------------------+-----+


 SAMPLE VALUES — provider_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|AAA9A9A9A9A9AAA9AAA9AAAAAA|nzi5y2q4n2m2mzi5nda4ztjiym|
|AAA9A9A9A9A9AAA9AAA9AAAAAA|nzi5y2q4n2m2mzi5nda4ztjiym|
|AAA9A9A9A9A9AAA9AAA9AAAAAA|nzi5y2q4n2m2mzi5nda4ztjiym|
|AAA9AAA9AAA9AAA9A9A9AAAAAA|mta1mwi2zme0zjc1m2y1zdyxyw|
|AAA9AAA9AAA9AAA9A9A9AAAAAA|mta1mwi2zme0zjc1m2y1zdyxyw|
|AAA9AAA9AAA9AAA9A9A9AAAAAA|mta1mwi2zme0zjc1m2y1zdyxyw|
|AAAAAAAAAAA9AAA9AAAAA9AAAA|ywiwzmnlyza4zte4ytdiy2nkyt|
|AAAAAAAAAAA9AAA9AAAAA9AAAA|ywiwzmnlyza4zte4ytdiy2nkyt|
|AAAAAAAAAAA9AAA9AAAAA9AAAA|ywiwzmnlyza4zte4ytdiy2nkyt|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|mmjlzdiwmzjlzdnkodmwmgi3nz|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|mmjlzdiwmzjlzdnkodmwmgi3nz|
|AAAAAAAAAAAAAAAAAAAAAAA9AA|mmjlzdiwmzjlzdnkodmwmgi3nz|
+--------------------------+--------------------------+


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
|99999A99|1615 |
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

 VALUE SHAPES — order_status
+-----------+-----+
|shape      |count|
+-----------+-----+
|AAAAAAAA   |68592|
|AA-AAAAAAAA|34188|
|AAAAAAAAA  |17217|
+-----------+-----+


 SAMPLE VALUES — order_status
+-----------+------------+
|shape      |sample_value|
+-----------+------------+
|AA-AAAAAAAA|in-progress |
|AA-AAAAAAAA|in-progress |
|AA-AAAAAAAA|in-progress |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
|AAAAAAAA   |canceled    |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
|AAAAAAAAA  |cancelled   |
+-----------+------------+


 VALUE SHAPES — payment_provider
+---------+-----+
|shape    |count|
+---------+-----+
|AAAAAA   |51469|
|AAA      |34145|
|AAAAA-AAA|17284|
|AAAA     |17099|
+---------+-----+


 SAMPLE VALUES — payment_provider
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAA      |tap         |
|AAA      |tap         |
|AAA      |tap         |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAAA-AAA|apple-pay   |
|AAAAA-AAA|apple-pay   |
|AAAAA-AAA|apple-pay   |
|AAAAAA   |stripe      |
|AAAAAA   |stripe      |
|AAAAAA   |stripe      |
+---------+------------+


 VALUE SHAPES — payment_method
+----------------+-----+
|shape           |count|
+----------------+-----+
|AAAAAA          |68753|
|AAAA AA AAAAAAAA|51244|
+----------------+-----+


 SAMPLE VALUES — payment_method
+----------------+----------------+
|shape           |sample_value    |
+----------------+----------------+
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAAAA          |Online          |
|AAAAAA          |Online          |
|AAAAAA          |Online          |
+----------------+----------------+


 Discovery complete for crm_silver_orders — scanned 119997 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_payment_attempts
====================================================================================================

 SCHEMA
root
 |-- payment_attempt_sk: string (nullable = true)
 |-- order_sk: string (nullable = true)
 |-- attempt_id: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- payment_provider: string (nullable = true)
 |-- payment_method: string (nullable = true)
 |-- amount_attempted: string (nullable = true)
 |-- is_success: string (nullable = true)
 |-- attempt_ts: timestamp (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 80000

 NULL COUNTS
+------------------+--------+----------+--------+----------------+--------------+----------------+----------+----------+-------------+
|payment_attempt_sk|order_sk|attempt_id|order_id|payment_provider|payment_method|amount_attempted|is_success|attempt_ts|dw_created_at|
+------------------+--------+----------+--------+----------------+--------------+----------------+----------+----------+-------------+
|0                 |0       |0         |0       |0               |0             |0               |0         |0         |0            |
+------------------+--------+----------+--------+----------------+--------------+----------------+----------+----------+-------------+


 VALUE SHAPES — payment_attempt_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|2913 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|1798 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|1761 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1759 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|1748 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|1702 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|1690 |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|1093 |
|AAAAAAAAAAAAAAA9AAAAAAA9AA|1093 |
|AAAAAAA9AAAAAAA9AAAAAAAAAA|1064 |
+--------------------------+-----+


 SAMPLE VALUES — payment_attempt_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9A9AAAAA9AAAAAA|n2u2m2i2nji1y2jkodq0odlhot|
|A9A9A9A9AAA9AAA9AAA9AAA9AA|n2e3n2q1zgi5mji1zjc0ndk2yz|
|A9A9A9A9AAA9AAA9AAAAA9A9AA|m2y3m2m0yjk0mwy4nmzjy2y5zd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|y2q3n2m4mdm3zwe1odmzmdq2ng|
|A9A9A9A9AAA9AAA9AAAAAAAAA9|y2y1y2u0ogy0ywy3zgiwnznmn2|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|n2i2m2q5yme5ymu1odeynznizj|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|y2y1n2y5ody0mmvkm2i4zwzjzj|
|A9A9A9A9AAA9AAAAA9AAA9AAAA|y2y5y2e5mdm4zjfkn2iwn2iwzj|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2u3m2y2zjk1ntbjymi1ndy1od|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2i0y2q2mda0mguwzdi5mguxyz|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|m2u1m2y2ywy5ntjmytexm2uwyt|
|A9A9A9A9AAA9AAAAAAAAA9AAAA|n2e2m2e1ytm5nwewzjeyy2ewmm|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2e0n2u4yzk0yzgxztcynjk2ow|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2i4n2q2ndq4ywnhowmxymq1mg|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2q1m2m5mmi0yjuzyzdkmgu5zt|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2i3m2e2ytc1zdjjmwmzmgvkyz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2y1y2q0ywi0nwvkzmzlnmrjmg|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2e4y2u3mjm1ymvjzjuzmmiymm|
|A9A9A9A9AAAAA9A9AAAAAAAAAA|m2e1y2i4zdjky2e5mjjjyjyxmd|
|A9A9A9A9AAAAAAA9A9AAA9A9AA|n2m5m2y3nmnjyzq5m2rjm2u2mm|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|y2m2n2q0mweyymu2zdy2ywq5yz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2m0y2i4ogvlzdu5mjc5otaxmd|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|y2q5y2q1mzninwu5ody1ywzlnw|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|m2e5n2q2yjkxzdc1mgfhnzi0ot|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2m2n2m3yjnjyze3yjbkotlkyw|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2u2m2q2ywuyzda4zwflmmniog|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y0y2y0zthiytq2mzcyyznkzg|
|A9A9A9A9AAAAAAAAAAA9A9AAAA|n2y2m2y4nddjnjnlmzy1m2niot|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|m2y4y2q2zgzhywrkodc3yjy2nd|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|n2y4y2q1zmzlmzvizgq5ntyymj|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|n2y5y2u4zwnkyzbimzm5ztjlod|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2m1m2u0mgnjytuyowe1mgmynm|
|A9A9A9A9AAAAAAAAAAAAAAA9A9|m2e1y2m3othkodkxngfiyje3y2|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|m2i4y2q2mzgzowzlodczmme1zj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|m2q2m2m4mwnhodaxotfkoge0mg|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|m2u1n2q4nwvintvknmjmyzy1nt|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2q1y2m2nduxmmnmnjuwyzfhnd|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2u3y2u0ntmymtdlzwuyoguwzd|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|n2e0y2m1zgyzmznkmgzkzdljnt|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2e1m2nkn2q3odeyzjrhnda0mz|
|A9A9A9AAA9A9AAAAAAAAAAAAAA|m2m4n2vln2u5owjkmtdlntdkzt|
|A9A9A9AAA9AAAAA9A9A9A9A9AA|y2q4n2fiy2ixnmq1y2u1m2y0od|
|A9A9A9AAA9AAAAA9A9AAAAA9AA|y2e5n2jkm2vmnzm0m2qwnzk3yt|
|A9A9A9AAA9AAAAA9AAAAAAA9AA|y2y5n2rmy2rknja2zjrlzdg0mw|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|m2m5m2nlm2ziodezzmmxognlnd|
|A9A9A9AAAAA9A9A9AAA9AAA9AA|y2e4m2zjmmq0n2m4mmu2yzm3ot|
|A9A9A9AAAAA9A9AAAAAAAAAAAA|n2u5m2vjmzc4y2zizjhkntlhmd|
|A9A9A9AAAAA9AAA9A9A9AAA9AA|m2e4m2yxztg1zdc0n2e0zty5nm|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|m2u2y2nlmzc3zwi1mge3mze0yj|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|n2u1y2vjzdy3zje5yzq1njg0yt|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — order_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|2978 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|1815 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|1742 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|1732 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1669 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|1655 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|1534 |
|AAAAAAA9AAAAAAAAAAAAAAA9AA|1112 |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|1096 |
|AAAAAAA9AAA9AAAAAAAAAAAAAA|1070 |
+--------------------------+-----+


 SAMPLE VALUES — order_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAAAAAA9A9A9AA|n2e3y2q2m2i5mdbhywm1m2e4md|
|A9A9A9A9A9A9AAAAAAA9AAAAAA|n2m4m2m0y2y5odhhyje3ndgyot|
|A9A9A9A9A9AAAAA9AAAAAAA9AA|m2q4y2y0m2fknwq4zjawoti2mt|
|A9A9A9A9A9AAAAAAAAA9AAA9AA|m2i1m2q3n2myzgrlmmi0zdq2nj|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2y2y2u3n2rhmmvjodhhzgvmnm|
|A9A9A9A9AAA9A9A9AAAAAAAAAA|y2i5y2m5mzc5y2i1mjgxzmmyyt|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2m1y2q3owe2owm3ogq4odnmmj|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|n2m2m2y1ndc3mtq0nwu1zdflzd|
|A9A9A9A9AAA9AAA9AAAAAAA9AA|n2e0n2e5mgu3ode4mmixntm4nw|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|y2y4m2e0mtm2mdu1nzuzmmqzzd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2y5y2i3ntg4yzblnzc3mjc0mz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2u3m2y5nmy2yzgyywm1oduymm|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2u3m2y5nmy2yzgyywm1oduymm|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2u3m2y5nmy2yzgyywm1oduymm|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|n2q4n2m2nzc0owqxndzkotg3n2|
|A9A9A9A9AAA9AAAAAAAAAAA9A9|y2y1m2q3zge2yzzhzjqyodi3m2|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|n2i0m2q2nmm5mdrmmjhjnjk5nw|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|y2u4y2i0mzi1otyxmzvjoti3mz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2i3m2e0ztk0zwnmoddhmwzkot|
|A9A9A9A9AAAAA9AAAAA9AAAAAA|y2q2n2m1ntgwy2qwndk0ntbjzw|
|A9A9A9A9AAAAA9AAAAAAAAA9A9|y2u3m2u1zjlmm2jintkzody0n2|
|A9A9A9A9AAAAAAA9A9A9AAA9AA|m2i1y2m0ngyxndm3n2i1mda0nt|
|A9A9A9A9AAAAAAA9AAA9AAA9AA|y2m5m2y5zjkymta5mtc2zty5mz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2i5y2y1nzizmzg1mda0yzvjmg|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2i5y2y1nzizmzg1mda0yzvjmg|
|A9A9A9A9AAAAAAA9AAAAA9AAAA|n2e2m2y4mtbiyja4ytljm2fmyj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2e1m2e2ztvimjy5mdhkzjy4og|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2q5y2y3mwvhodq4zwqxmdg4ot|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|n2u2n2q2yznjyjdiywy5ytc1nd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2i2y2q3nwfhmjqxytm2ywm5ot|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2i2y2q3nwfhmjqxytm2ywm5ot|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2u3m2q1mzhiodrlmda1ngrkyt|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2y0n2i2ntiwnzriody2nmrjnw|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2i4m2q4mjnkyzexzme3mdqymj|
|A9A9A9A9AAAAAAAAAAAAA9AAA9|y2i0m2i3odhkzmjlyzdhn2fky2|
|A9A9A9A9AAAAAAAAAAAAA9AAA9|y2i0m2i3odhkzmjlyzdhn2fky2|
|A9A9A9A9AAAAAAAAAAAAA9AAA9|y2i0m2i3odhkzmjlyzdhn2fky2|
|A9A9A9A9AAAAAAAAAAAAAAA9A9|y2m2y2u1mthlnmnmzjqwmge1n2|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|n2m3y2e0ymrlntqzymnjmjc3mj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|n2m3y2e0ymrlntqzymnjmjc3mj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2q4n2u2zdzmmwfkmdvimzg3nm|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|n2i3y2i5njbhyjmymwrkmmmwng|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|n2m4m2i0mwjkogzkyzfkyznhzw|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|n2y2n2i3nziyzgjlntgwmtfinz|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|y2q3n2fkm2i4nzdlnguzzwm5nm|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|y2q3n2fkm2i4nzdlnguzzwm5nm|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|y2q3n2fkm2i4nzdlnguzzwm5nm|
|A9A9A9AAA9A9AAAAAAAAAAAAAA|n2y1n2ywy2q1zdjimzljndaxyz|
|A9A9A9AAA9AAA9AAAAA9AAAAAA|n2y0m2jim2zim2vlyzu2ywjkmz|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — attempt_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|A9999999-9999-99AA-999A-9AA9A99999A9|2    |
|999A9A99-9999-9999-A999-999A9A99A9AA|2    |
|999A999A-9999-9999-9999-A9A9999999A9|2    |
|99999999-999A-9A99-9999-A999999999A9|2    |
|A999A999-9AA9-9999-99AA-9999999A9A99|2    |
|9AA99AA9-999A-9999-A9A9-999A99AAAAA9|2    |
|AA9A9A99-99A9-9999-A999-99A9A9AAAA99|2    |
|9AA99AAA-A9A9-9999-9999-A9A999999A99|2    |
|999999AA-A999-9999-9AA9-9AAA999A99A9|1    |
|999A9A99-9A9A-9A99-9A9A-99AA99999999|1    |
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

 VALUE SHAPES — payment_provider
+---------+-----+
|shape    |count|
+---------+-----+
|AAAAAA   |34276|
|AAA      |23046|
|AAAA     |11419|
|AAAAA-AAA|11259|
+---------+-----+


 SAMPLE VALUES — payment_provider
+---------+------------+
|shape    |sample_value|
+---------+------------+
|AAA      |tap         |
|AAA      |tap         |
|AAA      |tap         |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAA     |cash        |
|AAAAA-AAA|apple-pay   |
|AAAAA-AAA|apple-pay   |
|AAAAA-AAA|apple-pay   |
|AAAAAA   |stripe      |
|AAAAAA   |stripe      |
|AAAAAA   |stripe      |
+---------+------------+


 VALUE SHAPES — payment_method
+----------------+-----+
|shape           |count|
+----------------+-----+
|AAAAAA          |45535|
|AAAA AA AAAAAAAA|34465|
+----------------+-----+


 SAMPLE VALUES — payment_method
+----------------+----------------+
|shape           |sample_value    |
+----------------+----------------+
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAA AA AAAAAAAA|Cash On Delivery|
|AAAAAA          |Online          |
|AAAAAA          |Online          |
|AAAAAA          |Online          |
+----------------+----------------+


 VALUE SHAPES — amount_attempted
+------+-----+
|shape |count|
+------+-----+
|999.99|66536|
|99.99 |13464|
+------+-----+


 SAMPLE VALUES — amount_attempted
+------+------------+
|shape |sample_value|
+------+------------+
|99.99 |20.00       |
|99.99 |20.01       |
|99.99 |20.02       |
|999.99|100.01      |
|999.99|100.01      |
|999.99|100.01      |
+------+------------+


 VALUE SHAPES — is_success
+-----+-----+
|shape|count|
+-----+-----+
|9    |80000|
+-----+-----+


 SAMPLE VALUES — is_success
+-----+------------+
|shape|sample_value|
+-----+------------+
|9    |0           |
|9    |0           |
|9    |0           |
+-----+------------+


 Discovery complete for crm_silver_payment_attempts — scanned 80000 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_referrals
====================================================================================================

 SCHEMA
root
 |-- referral_sk: string (nullable = true)
 |-- referral_id: string (nullable = true)
 |-- referrer_user_id: string (nullable = true)
 |-- referrer_user_sk: string (nullable = true)
 |-- referred_user_id: string (nullable = true)
 |-- referred_user_sk: string (nullable = true)
 |-- referral_ts: timestamp (nullable = true)
 |-- is_self_referral: boolean (nullable = true)
 |-- referral_ts_parse_status: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 3000

 NULL COUNTS
+-----------+-----------+----------------+----------------+----------------+----------------+-----------+----------------+------------------------+-------------+
|referral_sk|referral_id|referrer_user_id|referrer_user_sk|referred_user_id|referred_user_sk|referral_ts|is_self_referral|referral_ts_parse_status|dw_created_at|
+-----------+-----------+----------------+----------------+----------------+----------------+-----------+----------------+------------------------+-------------+
|0          |0          |0               |0               |0               |0               |0          |0               |0                       |0            |
+-----------+-----------+----------------+----------------+----------------+----------------+-----------+----------------+------------------------+-------------+


 VALUE SHAPES — referral_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|109  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|75   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|71   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|69   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|61   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|53   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|51   |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|49   |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|48   |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|43   |
+--------------------------+-----+


 SAMPLE VALUES — referral_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAA9A9AAAAAAAA|n2u3n2u0otzhmgu0y2rinjnjmj|
|A9A9A9A9AAAAAAAAA9AAA9AAAA|m2q3m2m2ztflnwvlm2rmy2rmmz|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|n2m3y2jjnjg4mjywodbkzgq2mt|
|A9A9A9AAAAAAAAAAAAA9AAA9A9|n2i5n2mzngjlowizmzg5nwm5n2|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|m2m1n2vkndlimtmxywe2zjvlnt|
|A9A9AAA9A9A9AAA9AAAAAAA9AA|n2e5zmm0y2i3zgy1ztzizdk5nt|
|A9A9AAA9A9AAAAA9AAA9AAAAAA|n2y5ymy3y2ixmgy0ngu4mtrkzj|
|A9A9AAA9AAA9A9A9AAAAA9A9AA|y2u0njy4yju5m2q0ytbkm2y3yt|
|A9A9AAA9AAA9A9AAAAAAAAAAAA|y2i3ngi2zja0m2uwmjmzodhmmj|
|A9A9AAA9AAA9AAA9AAAAAAA9AA|n2y5mdu3mdm5yzy1yzzhnme0nd|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|n2e3owm0nwm4mtm5zjriodbjmg|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2e4nty5mzy0zjhhmtu0zji2nm|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|y2e2ndy1oda5ndzmyjk4ztq2zj|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|m2q1nzi1nwu2zwzmyjqzytgzzj|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|m2q4nwu5ota1ntcyogezowfhmj|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|n2m0nti4mjg5ntvlzjzjntrjmw|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|m2y1ndy0zdgwzgu1zgvkzwq2yw|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|y2e3ngu2nzcwoda0zwvkody5md|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|n2e4otc1ztaxywy5ndhiotdizd|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|n2u4yzm3ztmwnzk2ntfjzmywmz|
|A9A9AAA9AAAAAAAAA9A9AAAAAA|n2q4nmi4ogqzowewy2e0nddkng|
|A9A9AAA9AAAAAAAAAAA9A9A9AA|n2u1nzu2mtzmmthjnjm4n2q0zj|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|m2y3ywm0zjnkzmrmzwi2zgy1zw|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|n2m3yte1mdhmywflnzk2ntc3mt|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|n2u4nge3ztzlmjuxmzu5ytywyj|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|n2y5mtk4mjrlmjlmmdq2ndawzd|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|n2i3yzu3zgyxnmyzngjkodg3zt|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2m5zjq2ntyzzdaznjywzwe4zj|
|A9A9AAA9AAAAAAAAAAAAAAAAA9|n2i2zme0zgziyzzkzjhlodzmn2|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2m4ntk2yjzhzmvlzjziymfhzd|
|A9A9AAAAA9A9AAA9AAAAAAAAAA|m2y5otjjy2y3ztc1mjkxnmzimt|
|A9A9AAAAA9AAAAA9AAA9AAA9AA|y2i2mzkxn2jimdk2zmm5yty3md|
|A9A9AAAAA9AAAAA9AAAAAAAAAA|y2i4yjhhn2qwnwq1nmmwmjazzd|
|A9A9AAAAAAA9A9A9AAAAAAAAAA|y2u5mzbkmwy1y2u2mwzmmmriot|
|A9A9AAAAAAA9A9AAAAAAAAAAAA|n2e4nzexowy1n2qxyziwmjkzmt|
|A9A9AAAAAAA9AAA9A9A9AAAAAA|m2q0ntuyoge5zwu4n2u3mjiyyz|
|A9A9AAAAAAA9AAA9AAA9A9A9AA|y2i5zjblztu0mwu5zgm0y2u3md|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|n2u0zjfiymq4yzi2ndi2yjq4yz|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|m2y1ogviywi0ymq2mda0mdllym|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2y2ymzmndq4nwm5ntk4nmuwyz|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|y2u5odhjogm1njq2nji4mwrlyw|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|m2m2njayzjy3nwq3njyynzq4mg|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|n2m5zmzlogy5mza1odfjytc3od|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|n2y0ntnjnme5mdm3yjziztq5mm|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|n2y1mmrlztg2ymy0odiwnwezmd|
|A9A9AAAAAAA9AAAAAAA9AAA9AA|n2i5ngnhzwy0njizmmi3zmi4ym|
|A9A9AAAAAAA9AAAAAAA9AAAAAA|n2i5mjaxnzm5nmiznjq4njqynz|
|A9A9AAAAAAA9AAAAAAA9AAAAAA|n2q1nmfmnmq3ngmynme1mdmxzg|
|A9A9AAAAAAA9AAAAAAA9AAAAAA|n2u3ogrjnte1ntiyotk0nmzmyz|
|A9A9AAAAAAA9AAAAAAAAAAA9A9|y2m5owjjmjy0mjrlnzqxytc1y2|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — referral_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|99999A99-9A9A-9A9A-999A-AA9AA999A9A9|1    |
|999AA99A-AAAA-9A9A-AA9A-AA999A9AA99A|1    |
|99AAAAA9-A9A9-9AA9-AA99-9A99A9A99999|1    |
|99A9A9A9-99A9-9999-A9A9-AA9A9A99A999|1    |
|999AAA9A-9A99-9A9A-A99A-9999A9999A99|1    |
|99A9999A-99A9-9999-A999-99A9A9999999|1    |
|99999A9A-9A9A-999A-9A99-99AA9AA9A99A|1    |
|99A9A9A9-9A99-9999-9A99-9A99AA99A999|1    |
|999999A9-999A-9999-9A99-9AAA9999A999|1    |
|99999AAA-9999-9A99-A9A9-99999999AA9A|1    |
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

 VALUE SHAPES — referrer_user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|104  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|75   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|70   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|63   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|60   |
|AAAAAAA9AAAAAAAAAAA9AAAAAA|53   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|51   |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|50   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|49   |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|48   |
+--------------------------+-----+


 SAMPLE VALUES — referrer_user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|m2y0y2vhngy4odjhothmmgi4zd|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|n2u0m2yzztjlyznmodbhodq0mm|
|A9A9AAA9A9AAAAAAAAA9AAA9AA|m2m0mtk1m2mwyjcwmjm0njc5ym|
|A9A9AAA9A9AAAAAAAAA9AAA9AA|y2m2mzg0y2jmmzjkmjm5nmi1mm|
|A9A9AAA9AAA9AAA9AAA9AAA9AA|m2q3mza5ngm2yjm2nje2ogy5nz|
|A9A9AAA9AAA9AAA9AAAAA9A9AA|n2u4odm4ywi0zdi0zjmyn2y1mt|
|A9A9AAA9AAA9AAA9AAAAAAAAA9|n2y2njc3yjk3zge3mjlmndkwn2|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|m2u5nwe1ymi3mzy3ywrhnjeynm|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|n2u1nda4odg2mzgzota0otg2nd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|y2e2zdu3oda4zdbiyzm1mtg2nz|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|y2y0ngi1zmq0mtfjogu4mge3yj|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|m2m5yzg3zgy1mmixmmm3mmrlow|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2e5ntc4ndy3ymzkngu2yjflmm|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2i5mjm3zmi2njjlnme5zgyxmd|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|n2m0njk0zdu1zdviyjfkywqxzd|
|A9A9AAA9AAAAA9A9AAA9AAAAAA|n2i1ywu1zmeyy2u4mdi4ndnjod|
|A9A9AAA9AAAAAAA9A9AAAAA9AA|n2e5mte5mmzmngy4n2zhntu4ow|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|y2e5odu3ztkxzwe4ndawmtk3zg|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|m2e0mjg1mdvhoge2owixngewmt|
|A9A9AAA9AAAAAAAAA9A9AAAAAA|y2u0ntk1nwmzognlm2q4mdvlmd|
|A9A9AAA9AAAAAAAAA9AAAAA9AA|n2e2mji4ytbmzdlky2ywndi4mg|
|A9A9AAA9AAAAAAAAA9AAAAAAAA|y2u4mdq3ntlmztjhm2zmmzljzj|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|m2q2nwi4mzuzzdzhyjq2ogm2zt|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m5yze2ntaxodzmyzg4zjczmz|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|n2m4ota0zdmznwziztbinja0mm|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2y2ota0ogewzwvlntjmymq0ot|
|A9A9AAAAA9A9A9AAA9A9AAAAAA|m2m5zjkwn2y0m2vmn2m1zwjhmz|
|A9A9AAAAA9AAAAA9AAA9AAAAAA|y2y0ogywm2rimwu3zgq2zjiwym|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|m2q4ywixnty4zjm1zgy5nzy3ot|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|y2m4yjlhmzk4mwu1njc1mtk2nw|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|n2y3zjcxzgy3zgm5ndjiyzi3zd|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|y2i1zthlote3yme5zmqxmjm3yj|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|n2i3ywyxytm0zji5yzfjmtnlym|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|y2i1otflnde2yti2nzkxndhinw|
|A9A9AAAAAAA9AAAAA9AAAAAAAA|m2e1mgyyzjm4mjcwm2jjyjhmzg|
|A9A9AAAAAAA9AAAAAAA9A9AAAA|n2i0mdnknwq2ztjkmjc3n2fhnj|
|A9A9AAAAAAA9AAAAAAA9AAA9AA|n2m5mmjmyjq2mdmwzta5odi1yz|
|A9A9AAAAAAA9AAAAAAA9AAAAA9|y2m1otnjywi0njnkngq2nddiy2|
|A9A9AAAAAAA9AAAAAAA9AAAAAA|y2i4nmixodu0yjgyztu1otzhow|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|n2e1mznkoge4owzjmwyynju3og|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|y2q2mzrkmgm0mmvjnjizmde3nd|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|m2e0mjvinjk5zwrmymnmymezod|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|n2m5odbjmzg3yjewmtcxmdixnt|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|y2y1mwzhymu5zmjhmjixnwzlmt|
|A9A9AAAAAAAAA9AAAAAAAAAAA9|n2q1ytcxnjdhy2jlmtgzzgyxy2|
|A9A9AAAAAAAAA9AAAAAAAAAAAA|y2e0ywiwzmqzn2zinzrmmdllzd|
|A9A9AAAAAAAAAAA9AAA9AAA9AA|n2m1ythmmgnkyja4nde4ztk2ym|
|A9A9AAAAAAAAAAA9AAA9AAAAAA|m2e3yzcxndqwmzg4mje1zwrizw|
|A9A9AAAAAAAAAAA9AAA9AAAAAA|n2q3zjhmmzixotm3mgy2ndixmt|
+--------------------------+--------------------------+
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

 VALUE SHAPES — referred_user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|116  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|66   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|65   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|60   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|59   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|58   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|54   |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|43   |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|42   |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|42   |
+--------------------------+-----+


 SAMPLE VALUES — referred_user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u1n2q5ntvmmti1mjiwmtq5ot|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2u5m2vhmzk5ndk2zdk2ytljog|
|A9A9A9AAAAA9AAAAA9AAAAA9AA|y2e5m2uzyju0mwzln2rjnme0nz|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|m2y0m2iwyzi2mmfjodiyytu0mz|
|A9A9A9AAAAAAAAA9AAAAAAAAAA|y2e3y2uzyjnkzji5mduyyzvjot|
|A9A9A9AAAAAAAAAAAAAAA9AAAA|y2m1m2fkngyxodcwnjzmy2nhyt|
|A9A9AAA9A9A9AAAAAAA9A9AAAA|y2q2zmq3m2q0mdjmzwq1n2fmnm|
|A9A9AAA9A9A9AAAAAAA9AAA9AA|y2e2zmi5y2m2mwjhmme0zja4yt|
|A9A9AAA9A9A9AAAAAAA9AAA9AA|y2y3zde2m2i3ntrjnjg2ytk0mt|
|A9A9AAA9A9AAAAA9AAA9AAAAAA|m2y2ntg5m2niztm1zmm0otuxnm|
|A9A9AAA9AAA9AAA9AAA9AAAAA9|y2i1mze2mwe1ndc0ody4zdgxm2|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|m2e2ngi5zty0ztk2mtcznjdkmw|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|n2y5nje5nzm3zjnknwy1zmy3nz|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|y2q0odm3ywy5zmuzmdy5yzmzzd|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|n2y5mdq1zju0ymfmztgwmtbknm|
|A9A9AAA9AAAAA9A9AAAAAAAAAA|n2e5ytq2zwqyy2u3yznjowewmw|
|A9A9AAA9AAAAAAA9AAA9AAA9AA|y2u0nzq5zwuxyze0nty4ote5yz|
|A9A9AAA9AAAAAAA9AAA9AAAAAA|n2i0mtu3ztaxyme0mtq1ymnhot|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|m2q3nmq0zjjjzdk4yzexndk3yj|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|y2e5odu3ztkxzwe4ndawmtk3zg|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|m2u4zjm3mjkzywy3ytdlmguzod|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2e3nge0ytiyndq0owexmgmxzm|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2m2mda1zjdlntc4nmjkztexyz|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|m2q3mjq1zmrinwjmnjg4ody4nw|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2m5nme0nddhotrlnzfingm1yt|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2m5nme0nddhotrlnzfingm1yt|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2y2ota0ogewzwvlntjmymq0ot|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2m4nte4nzqzndiymjyxntjkzj|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2y4nmy2yjqyzgrjmdeyodliot|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2i4mdc0yjbhyzvjnjzhmtjkmw|
|A9A9AAAAA9A9AAAAAAAAAAAAAA|n2u1zgywy2m3ztczntlmmjljmg|
|A9A9AAAAAAA9AAA9A9A9AAAAAA|n2q2otiyowe0odk4y2y3nwmyzm|
|A9A9AAAAAAA9AAA9AAA9A9A9AA|y2u2nddimta1odu5ody3n2e3ot|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|m2u3ztnjztk4mjq4zgq5ymq5yj|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|n2m1ndrjzdy4zti1odm5mwm1og|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|y2y1odewztq0nwq4ztq2mjlhmt|
|A9A9AAAAAAA9AAA9AAAAAAA9A9|m2m2nwizyji4nwi0yzgxyjy5n2|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|y2i3njeymtg3nwy4mdfjyjq5zd|
|A9A9AAAAAAA9AAA9AAAAAAAAA9|n2u3mzkyywi3zda3ogjlndriy2|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|m2e2yjblnju0ogm0yjzmowjlzg|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|n2i3ywyxytm0zji5yzfjmtnlym|
|A9A9AAAAAAA9AAAAAAA9A9AAA9|n2i2odfhzde1ogiwmty5y2zjy2|
|A9A9AAAAAAA9AAAAAAA9AAA9AA|m2m2mjiyogm1mjawyzq2mme3zd|
|A9A9AAAAAAA9AAAAAAA9AAAAAA|m2m4nzdkzjg5odgwmdk5zgeznd|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|n2e1mjgxmwy1mwriodjjmmy2nt|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|n2m0otnjmwy5mwfknmrlngq4md|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|y2e1zthjnge4nthjogywytqymz|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|y2m5zdnhoti1mtmxowiwzmjmnt|
|A9A9AAAAAAA9AAAAAAAAAAAAAA|y2q1mtczmti4nzjkowfjztuzym|
|A9A9AAAAAAAAA9AAAAA9AAAAAA|y2i3ntkxnjnim2vlmwe4nmqxog|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — referral_ts_parse_status
+------+-----+
|shape |count|
+------+-----+
|AAAAAA|3000 |
+------+-----+


 SAMPLE VALUES — referral_ts_parse_status
+------+------------+
|shape |sample_value|
+------+------------+
|AAAAAA|parsed      |
|AAAAAA|parsed      |
|AAAAAA|parsed      |
+------+------------+


 Discovery complete for crm_silver_referrals — scanned 3000 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_user_preferences
====================================================================================================

 SCHEMA
root
 |-- user_sk: string (nullable = true)
 |-- pref_key: string (nullable = true)
 |-- user_preference_sk: string (nullable = true)
 |-- pref_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- pref_value: string (nullable = true)
 |-- updated_ts: timestamp (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 18688

 NULL COUNTS
+-------+--------+------------------+-------+-------+----------+----------+-------------+
|user_sk|pref_key|user_preference_sk|pref_id|user_id|pref_value|updated_ts|dw_created_at|
+-------+--------+------------------+-------+-------+----------+----------+-------------+
|0      |0       |0                 |0      |0      |0         |0         |0            |
+-------+--------+------------------+-------+-------+----------+----------+-------------+


 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|662  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|424  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|410  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|402  |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|395  |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|393  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|366  |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|254  |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|250  |
|AAAAAAAAAAA9AAA9AAAAAAAAAA|247  |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|y2m3m2e1ntfmm2uzndhlyjhkmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2e2n2q0zdlkzjdiodvjntqyyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2y2y2i4ogrjzmixyzawnwmxmz|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|n2y5y2uyyme0n2q3mzg1odgwmj|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|y2e0m2yxzde4zme1mjk0ymi4zm|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i4y2ziyjm0yzg0nmi4otblzj|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2m1n2vimjg0zwu4ytu1mtnlzd|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|m2y0y2vhngy4odjhothmmgi4zd|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|y2e0y2fmntg3zdiwmdrjyzvkyj|
|A9A9A9AAAAAAA9AAAAA9AAA9AA|m2e3m2myymuxy2mzotm2mda3yj|
|A9A9A9AAAAAAAAA9AAA9AAAAAA|y2m4y2uxzjyzndu5mgi5mdlmzt|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|n2y0n2uyotnhmdzimzq1mgvjyz|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|n2u0m2yzztjlyznmodbhodq0mm|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|m2i4m2mxzgmxndjlmjnmnzvmnd|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|m2u2m2iwmwnlmzjlymfjmwnkzg|
|A9A9AAA9A9A9A9A9AAAAAAAAAA|n2y5mgi3y2m0y2i4ndkxyznlmm|
|A9A9AAA9A9A9A9AAAAAAAAA9AA|m2e0nja5y2e1n2rhzmrjyjy4md|
|A9A9AAA9A9A9AAA9AAAAAAA9AA|n2i5nwi2m2y2zje2odizodg2yj|
|A9A9AAA9A9AAAAA9AAA9AAA9AA|y2y3ntk2m2fmoti1ywm1ywy2mg|
|A9A9AAA9A9AAAAA9AAA9AAAAAA|y2e4ndi3y2jlzty5ode0mdvhmt|
|A9A9AAA9A9AAAAA9AAA9AAAAAA|y2e4ndi3y2jlzty5ode0mdvhmt|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|m2e2mgy4n2zkmtc2mtvhztcyyt|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2u2zta1m2zhmdk0otvjntuyyt|
|A9A9AAA9A9AAAAAAAAA9AAA9AA|m2m0mtk1m2mwyjcwmjm0njc5ym|
|A9A9AAA9A9AAAAAAAAAAAAAAAA|y2m5zmi1n2fimzkynmjhmjuymz|
|A9A9AAA9A9AAAAAAAAAAAAAAAA|y2y5yzy0y2fiyjmyntmyowvhmt|
|A9A9AAA9AAA9A9A9AAAAAAAAAA|y2e2ody3zjm2y2m0njzlmgfimm|
|A9A9AAA9AAA9A9AAAAA9AAAAAA|m2m4mjy5ywm4m2uxotg5otnjot|
|A9A9AAA9AAA9A9AAAAA9AAAAAA|y2i2yjk3ytu4n2vjyjg4zwrhyz|
|A9A9AAA9AAA9A9AAAAAAAAAAAA|n2i0mmm5oty5n2eymgmyodkwnj|
|A9A9AAA9AAA9A9AAAAAAAAAAAA|n2i0mmm5oty5n2eymgmyodkwnj|
|A9A9AAA9AAA9AAA9A9A9AAAAAA|n2q2zja2ywy5oty0m2m2njfizt|
|A9A9AAA9AAA9AAA9AAA9AAA9AA|m2q3mza5ngm2yjm2nje2ogy5nz|
|A9A9AAA9AAA9AAA9AAA9AAA9AA|n2q3ntq0zju5ndk3nzu3mmy1nd|
|A9A9AAA9AAA9AAA9AAA9AAA9AA|n2u5mje1nje4mtu1ytg0mta5mj|
|A9A9AAA9AAA9AAA9AAA9AAAAAA|m2i2zde0mtg5ytg5zwi1mmmyzw|
|A9A9AAA9AAA9AAA9AAA9AAAAAA|m2y5mdm4zgu0ogm1zwq1ywfhyj|
|A9A9AAA9AAA9AAA9AAA9AAAAAA|n2e4mty0zgq4ytc3odm0mdzjnd|
|A9A9AAA9AAA9AAA9AAAAA9A9AA|n2u4odm4ywi0zdi0zjmyn2y1mt|
|A9A9AAA9AAA9AAA9AAAAA9A9AA|n2u4odm4ywi0zdi0zjmyn2y1mt|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — pref_key
+-------------+-----+
|shape        |count|
+-------------+-----+
|AAAAAAAA     |6252 |
|AAAAAA       |6223 |
|AAAAAAAAAAAAA|6213 |
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


 VALUE SHAPES — user_preference_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|681  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|409  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|395  |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|394  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|391  |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|379  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|372  |
|AAA9AAAAAAAAAAAAAAAAAAA9AA|266  |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|262  |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|261  |
+--------------------------+-----+


 SAMPLE VALUES — user_preference_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2y5m2y5zdg3odq3ody5zjqwmd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2q1y2q1ntg5mjixzdu0mwy4md|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i0n2u0ytm4ztljmwi3nzjhod|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|y2y3y2y3zjc2mtvmnza1ndiynj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2m4yme1odbizdiymduxmm|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2u5m2m4mdmwm2qymgizytzlyw|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2u4n2y4owzlmze4mmfhnmu0od|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|m2i3n2i5nwzmodi1ndbiognimw|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|n2e3n2y3yzzkmgzmmjc1nmq5nm|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2e2y2e1mjeyodfhmgfjmgi5ot|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2m1n2m1mzqymdljmwvkoguznm|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2m5y2e4yzbiytvkmjyxnmvhmd|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2u3m2u4yzvhogrmnjzizmmzmw|
|A9A9A9AAA9AAAAAAAAAAAAA9A9|m2q4n2vmy2rlmdlhzjewnze0n2|
|A9A9A9AAA9AAAAAAAAAAAAAAAA|y2m2m2ezm2fiytbhywyxzddhzg|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|m2m5m2nhyzy4otq0mzrmmwe1nd|
|A9A9A9AAAAA9AAAAAAA9AAA9AA|m2u2m2eynwy3ndfhmde4ywe2nw|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|n2e4y2mwmmu0ytyyywy4mzljzt|
|A9A9A9AAAAA9AAAAAAAAAAA9AA|n2q3n2mymzi5ngziymrkywu4nw|
|A9A9A9AAAAA9AAAAAAAAAAAAA9|m2u0m2nhmmu1mzaznwfioduxn2|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|m2y1n2fizji4nzzhnzuyztizmd|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2i0y2nmzdm4nwiyymrlzwrhyw|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2y3n2qyyze4odvimmjlyznhyt|
|A9A9A9AAAAAAA9AAAAAAAAA9AA|y2e3m2nlmjdin2vlztiwmzy4mt|
|A9A9A9AAAAAAAAA9A9A9AAA9AA|n2e1m2ywmzmwymy0n2e3ywu4md|
|A9A9A9AAAAAAAAA9AAA9AAA9AA|y2i5y2jintfknjy3ytq4zte2mm|
|A9A9A9AAAAAAAAA9AAA9AAAAAA|m2q3y2flnjgxyzm2zwq4yzrmzw|
|A9A9A9AAAAAAAAA9AAAAAAA9A9|y2q0n2ywngrkyzg0njmyzdi4m2|
|A9A9A9AAAAAAAAA9AAAAAAA9AA|m2i1n2vjzwqzymi4mtaxndq1ng|
|A9A9A9AAAAAAAAA9AAAAAAA9AA|m2y4n2qxnzawmjy5yjcwngu0zt|
|A9A9A9AAAAAAAAA9AAAAAAAAAA|n2m2y2finzdiowi5njywmmzind|
|A9A9A9AAAAAAAAAAA9AAAAA9AA|m2e4y2iwzwmyogqxm2jlyja0nm|
|A9A9A9AAAAAAAAAAAAA9AAA9AA|m2u4y2flzjziogqxytm5zja1nt|
|A9A9A9AAAAAAAAAAAAA9AAA9AA|y2q4m2yxowvmodrjnza2ndk3yw|
|A9A9A9AAAAAAAAAAAAA9AAAAA9|n2i5n2jmzmqyzdjkndq3zwrhn2|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|n2u0y2rjotrmnzcxnty5mzjlzt|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|y2u4y2nlzwvmmtvjymu0zdkzmt|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|n2y4m2yxmtrizwvjodvlywe3zt|
|A9A9A9AAAAAAAAAAAAAAAAA9AA|y2m4m2zlntninjlhzjhkzmu0nz|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|m2y4y2zkytyyzgywyjyxodqyyz|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|n2q3m2uxmdgymdqwndrlntqxmm|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|y2i2y2vkodvkmzdlzduwntuwmd|
|A9A9AAA9A9A9AAA9AAA9AAA9AA|m2e5zda1y2u0ntq4mdc3mta2ow|
|A9A9AAA9A9A9AAA9AAA9AAAAAA|y2q0ogm4n2e5mti2otm1ntmznz|
|A9A9AAA9A9A9AAAAAAA9AAAAAA|n2u3ytg3y2q1nwviytk2nwnkow|
|A9A9AAA9A9A9AAAAAAAAAAAAAA|m2i1ody1m2e2otqzothmytqyyt|
|A9A9AAA9A9A9AAAAAAAAAAAAAA|y2e5mzq1y2q2mmmznjjkzgjlzm|
|A9A9AAA9A9A9AAAAAAAAAAAAAA|y2q5zdi4y2m1ytvhyjkxnmvjnz|
|A9A9AAA9A9AAA9AAAAA9AAAAAA|y2q1mgq2m2uxn2viowy1ymvmmz|
|A9A9AAA9A9AAAAA9AAA9AAA9AA|m2i4mzc1y2nkytu5yjg2mdu4md|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — pref_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|AA99A999-AA99-9A99-99AA-9AA9999A99A9|1    |
|9AAAAAA9-A9AA-9999-AA9A-9A9A9A9A9A99|1    |
|AA99AA99-AAAA-9999-A999-A9AA9AA99A99|1    |
|A999AA9A-9AA9-9A9A-9A99-A99999999AAA|1    |
|A9999999-9999-9999-AA9A-9999AAA9AA9A|1    |
|9A9AA9AA-AAAA-9999-999A-99A999A9AAAA|1    |
|9A9999AA-A9A9-9999-9A99-99A9AA9A9A99|1    |
|A99AA999-999A-9AA9-999A-99A9AAA9AAA9|1    |
|A99999AA-9A99-9AAA-AA9A-A99A9999999A|1    |
|9AA99999-AA99-9999-999A-AA99AA999AA9|1    |
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
|99999999-9999-9999-9A99-99AAAAAA9AAA|51546261-5138-4525-8c81-20dfcfbd5bff|
|99999999-9999-9999-9A99-A9A9AA9AAA99|62407409-9271-4896-8b54-f4c4ba2aeb41|
|99999999-9999-9999-9A99-AAA9A9AA99AA|35545563-0573-4741-9b05-fee9d6db16bd|
|99999999-9999-9999-9A9A-99A9A9999999|59767485-1978-4289-8f7d-69c3b2529020|
|99999999-9999-9999-A999-999A99A99AA9|97812188-9130-4817-a554-256c44a18ce8|
|99999999-9999-9999-A9A9-99A99999A9AA|47096124-1228-4489-a3d3-24b57582c8dd|
|99999999-9999-9999-A9A9-99A99A99A9AA|19336464-2720-4414-b8c1-29a28b70b6da|
|99999999-9999-999A-9999-AA9A9A999A9A|26542582-2436-460c-9099-ae6d8b389e0d|
|99999999-9999-999A-9999-AA9A9A9A9A99|60585898-7265-425a-8722-af6d3d2b4b66|
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
|99999999-9999-99AA-A99A-9999A9999A9A|86936702-5714-43bb-a36f-5487f9540a5b|
|99999999-9999-99AA-A99A-99A9A9999999|24475880-3277-40cf-a93b-23b0c4461793|
|99999999-9999-99AA-AA99-99A99A9A9999|13511320-8713-48bf-ab83-71d90f8f0524|
|99999999-9999-99AA-AA99-A99AA9A999AA|87995330-7857-40fc-bd05-d80ff6d576db|
|99999999-9999-9A99-99A9-999A9999A999|25563998-7392-4d77-85b0-648d6904f672|
|99999999-9999-9A99-99A9-9A9AA9A9A999|95026621-8687-4d42-93b6-8e1ac9a1f796|
|99999999-9999-9A99-9A99-9999A9A9A999|62676843-5942-4d82-9a15-7047d4c4d747|
|99999999-9999-9A99-9A9A-AA99A999999A|75892445-8983-4f47-8c6f-be57c940220c|
|99999999-9999-9A99-9AAA-9A99AAA99999|22212712-3676-4d46-9abb-1f15faf38068|
|99999999-9999-9A99-A999-99A9999AA99A|79080836-6383-4e36-b765-25f4606ef20f|
|99999999-9999-9A99-A999-9A99A9A9A9A9|70094910-2678-4c95-a624-0d88f9a3e6f3|
|99999999-9999-9A99-A999-A9A9A9999999|94600892-3580-4c64-b794-a4a4a2646691|
+------------------------------------+------------------------------------+
only showing top 50 rows

 VALUE SHAPES — user_id
+--------+-----+
|shape   |count|
+--------+-----+
|99999999|467  |
|9999A999|299  |
|99A99999|275  |
|999A9999|268  |
|99999A99|266  |
|999999A9|264  |
|9A999999|250  |
|9999999A|242  |
|A9999999|238  |
|999A99A9|178  |
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
|99999AA9|01709aa0    |
|99999AAA|01143cbc    |
|99999AAA|01597ede    |
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
|9999A9AA|0104c3ff    |
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

 VALUE SHAPES — pref_value
+-----+-----+
|shape|count|
+-----+-----+
|AA   |10056|
|AAA  |8632 |
+-----+-----+


 SAMPLE VALUES — pref_value
+-----+------------+
|shape|sample_value|
+-----+------------+
|AA   |ar          |
|AA   |ar          |
|AA   |ar          |
|AAA  |yes         |
|AAA  |yes         |
|AAA  |yes         |
+-----+------------+


 Discovery complete for crm_silver_user_preferences — scanned 18688 rows

====================================================================================================
 DISCOVERING TABLE: crm_silver_users
====================================================================================================

 SCHEMA
root
 |-- user_sk: string (nullable = true)
 |-- geo_sk: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- full_name: string (nullable = true)
 |-- initials: string (nullable = true)
 |-- first_name: string (nullable = true)
 |-- last_name: string (nullable = true)
 |-- email: string (nullable = true)
 |-- phone: string (nullable = true)
 |-- signup_date: timestamp (nullable = true)
 |-- status: string (nullable = true)
 |-- city_raw: string (nullable = true)
 |-- city: string (nullable = true)
 |-- address_raw: string (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 50000

 NULL COUNTS
+-------+------+-------+---------+--------+----------+---------+-----+-----+-----------+------+--------+----+-----------+-------------+
|user_sk|geo_sk|user_id|full_name|initials|first_name|last_name|email|phone|signup_date|status|city_raw|city|address_raw|dw_created_at|
+-------+------+-------+---------+--------+----------+---------+-----+-----+-----------+------+--------+----+-----------+-------------+
|0      |0     |0      |0        |49048   |0         |0        |3498 |0    |0          |0     |0       |0   |7547       |0            |
+-------+------+-------+---------+--------+----------+---------+-----+-----+-----------+------+--------+----+-----------+-------------+


 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|1785 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1081 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|1077 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|1070 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|1064 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|1059 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|1058 |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|682  |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|671  |
|AAA9AAA9AAAAAAAAAAAAAAAAAA|660  |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAAAAA|m2u5y2i2ytu2zdezm2u3mmuyzg|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q5m2u5zwu0mweymtq0owy5yz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|m2y3n2u0nzc3ymzizgm0mjhkog|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2q2mgu1zwuwntaxzwjkzm|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAAAA9AAA9AAAAA9AA|y2i1m2i1otyyn2jhm2ixywm5mj|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|y2m3m2e1ntfmm2uzndhlyjhkmz|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2u1n2q5ntvmmti1mjiwmtq5ot|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2m4n2u4yzhlmjbmmwe4nzu0nz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2i0n2i2mdbmztzlowy2nzgzyz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2e2n2q0zdlkzjdiodvjntqyyz|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2y2y2i4ogrjzmixyzawnwmxmz|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
|A9A9A9AAA9AAAAA9AAAAAAAAAA|m2m1m2mwn2viowe2zwyxytgwnm|
|A9A9A9AAA9AAAAAAAAA9AAAAAA|m2y0y2zln2ezodjjngm1ntzlot|
|A9A9A9AAA9AAAAAAAAAAAAA9AA|y2u4y2yyy2uyytjhmduzyja4mz|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|n2y5y2uyyme0n2q3mzg1odgwmj|
|A9A9A9AAAAA9AAA9A9AAAAAAAA|y2i5n2yyodi1mmq0y2ziodmymt|
|A9A9A9AAAAA9AAA9AAA9A9AAAA|m2m0m2nhmzc5mge4yze1m2nmyj|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|y2e0m2yxzde4zme1mjk0ymi4zm|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i4y2ziyjm0yzg0nmi4otblzj|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2m1n2vimjg0zwu4ytu1mtnlzd|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2u5m2vhmzk5ndk2zdk2ytljog|
|A9A9A9AAAAA9AAA9AAAAAAA9A9|n2q4n2uzywe4zje0yzezodg3m2|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|m2y2y2zmymu5nzy0zjhkyjq4ot|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|n2y3m2ezzgq3mgy2yzizyza5mm|
|A9A9A9AAAAA9AAA9AAAAAAA9AA|y2u4n2zmmtg5njy3mtixnzg2ym|
|A9A9A9AAAAA9AAA9AAAAAAAAAA|m2q5n2vmmwi1ywq0nwvlntqwyz|
|A9A9A9AAAAA9AAAAA9AAAAA9AA|y2e5m2uzyju0mwzln2rjnme0nz|
|A9A9A9AAAAA9AAAAA9AAAAAAAA|m2y0y2fhzjg1mwewm2rhowvlyt|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|n2q4n2uyngy3yzjjotg0ntqyot|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|n2u2y2zjmjm4ztgwzmu5mzvkzg|
|A9A9A9AAAAA9AAAAAAAAAAA9A9|m2y2m2nimju0ndywywmxztu3n2|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — geo_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAA9AAA9AAAAAAAAAAAAAAAAAA|14345|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|7192 |
|AAAAAAA9A9AAAAAAA9A9AAAAAA|7150 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|7137 |
|A9AAAAAAAAA9AAAAAAA9AAAAAA|7132 |
|AAAAAAAAA9A9AAA9AAAAAAAAAA|7044 |
+--------------------------+-----+


 SAMPLE VALUES — geo_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|A9AAAAAAAAA9AAAAAAA9AAAAAA|m2nmyjblzdm4otnmyjq2ndbjmj|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAA9AAA9AAAAAAAAAAAAAAAAAA|njm0nme4ngvlnmnjngjhyjnhnt|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAA9A9AAAAAAA9A9AAAAAA|mjjmzji3n2ixmgrhm2e2zmjhym|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAA9A9AAA9AAAAAAAAAA|mjezmzdim2y3otm1ngfmytuwzj|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAA9AAAAA9A9A9AAAA|odvimmjlmja4ymzhn2m1n2rmmg|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
|AAAAAAAAAAAAAAAAAAA9AAAAAA|yzcwngjimwjlyjewnwq2nmninj|
+--------------------------+--------------------------+


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
|AAAAA AAAAAA   |3217 |
|AAAAA AAAAA    |3068 |
|AAAAAA AAAAAA  |3015 |
|AAAAAA AAAAA   |2890 |
|AAAAAAA AAAAAA |2795 |
|AAAAAAA AAAAA  |2656 |
|AAAAA AAAAAAA  |2084 |
|AAAAAA AAAAAAA |1986 |
|AAAAAAA AAAAAAA|1964 |
|AAAA AAAAAA    |1687 |
+---------------+-----+


 SAMPLE VALUES — full_name
+--------------------+--------------------+
|shape               |sample_value        |
+--------------------+--------------------+
|AA AAAA             |jo ruiz             |
|AA AAAAA            |jo berry            |
|AA AAAAAA           |jo keller           |
|AA AAAAAA           |jo miller           |
|AA AAAAAAA          |jo leblanc          |
|AA AAAAAAAA         |jo anderson         |
|AA. AAA AAAA        |dr. amy paul        |
|AA. AAA AAAA        |dr. amy tate        |
|AA. AAA AAAA AA     |mr. dan ruiz md     |
|AA. AAA AAAAA       |ms. joy ellis       |
|AA. AAA AAAAAA      |dr. amy nguyen      |
|AA. AAA AAAAAA      |dr. ana foster      |
|AA. AAA AAAAAA      |mr. don larson      |
|AA. AAA AAAAAA AA.  |mr. joe nelson jr.  |
|AA. AAA AAAAAAA     |mr. ray hampton     |
|AA. AAAA AAA        |mr. troy fry        |
|AA. AAAA AAAA       |dr. alan wade       |
|AA. AAAA AAAA       |dr. jill bush       |
|AA. AAAA AAAA       |dr. sean cruz       |
|AA. AAAA AAAA AA    |dr. lisa todd md    |
|AA. AAAA AAAA AA.   |dr. john ward jr.   |
|AA. AAAA AAAA AA.   |dr. todd gray jr.   |
|AA. AAAA AAAA AAA   |mr. ryan boyd dds   |
|AA. AAAA AAAAA      |dr. erin moses      |
|AA. AAAA AAAAA      |dr. jodi smith      |
|AA. AAAA AAAAA      |dr. john berry      |
|AA. AAAA AAAAA AA   |mr. ryan allen md   |
|AA. AAAA AAAAA AAA  |dr. john smith dvm  |
|AA. AAAA AAAAAA     |dr. adam miller     |
|AA. AAAA AAAAAA     |dr. eric torres     |
|AA. AAAA AAAAAA     |dr. joel haynes     |
|AA. AAAA AAAAAA AA  |dr. erin castro md  |
|AA. AAAA AAAAAA AA  |mr. jack porter ii  |
|AA. AAAA AAAAAA AA  |mr. ryan rivera md  |
|AA. AAAA AAAAAA AA. |dr. cody hunter jr. |
|AA. AAAA AAAAAA AA. |mr. sean arnold jr. |
|AA. AAAA AAAAAA AAA |dr. dana torres dvm |
|AA. AAAA AAAAAA AAA |dr. jodi martin phd |
|AA. AAAA AAAAAA AAA |mr. dale bailey dvm |
|AA. AAAA AAAAAAA    |dr. gina oconnor    |
|AA. AAAA AAAAAAA    |dr. joel johnson    |
|AA. AAAA AAAAAAA    |dr. mary fleming    |
|AA. AAAA AAAAAAA AA |mr. mark jackson md |
|AA. AAAA AAAAAAA AAA|mr. mark leonard iii|
|AA. AAAA AAAAAAA AAA|mr. sean benitez dds|
|AA. AAAA AAAAAAAA   |dr. chad martinez   |
|AA. AAAA AAAAAAAA   |dr. john johnston   |
|AA. AAAA AAAAAAAA   |dr. kyle calderon   |
|AA. AAAA AAAAAAAA AA|mr. karl chandler md|
|AA. AAAA AAAAAAAA AA|mr. kurt martinez ii|
+--------------------+--------------------+
only showing top 50 rows

 VALUE SHAPES — initials
+-----+-----+
|shape|count|
+-----+-----+
|AA   |715  |
|AAA  |237  |
+-----+-----+


 SAMPLE VALUES — initials
+-----+------------+
|shape|sample_value|
+-----+------------+
|AA   |Dr          |
|AA   |Dr          |
|AA   |Dr          |
|AAA  |Mrs         |
|AAA  |Mrs         |
|AAA  |Mrs         |
+-----+------------+


 VALUE SHAPES — first_name
+-----------+-----+
|shape      |count|
+-----------+-----+
|AAAAA      |12512|
|AAAAAA     |11872|
|AAAAAAA    |11259|
|AAAA       |6678 |
|AAAAAAAA   |4122 |
|AAAAAAAAA  |1868 |
|AAA        |841  |
|AAAAAAAAAAA|680  |
|AAAAAAAAAA |162  |
|AA         |6    |
+-----------+-----+


 SAMPLE VALUES — first_name
+-----------+------------+
|shape      |sample_value|
+-----------+------------+
|AA         |jo          |
|AA         |jo          |
|AA         |jo          |
|AAA        |amy         |
|AAA        |amy         |
|AAA        |amy         |
|AAAA       |adam        |
|AAAA       |adam        |
|AAAA       |adam        |
|AAAAA      |aaron       |
|AAAAA      |aaron       |
|AAAAA      |aaron       |
|AAAAAA     |adrian      |
|AAAAAA     |adrian      |
|AAAAAA     |adrian      |
|AAAAAAA    |abigail     |
|AAAAAAA    |abigail     |
|AAAAAAA    |abigail     |
|AAAAAAAA   |adrienne    |
|AAAAAAAA   |adrienne    |
|AAAAAAAA   |adrienne    |
|AAAAAAAAA  |alejandra   |
|AAAAAAAAA  |alejandra   |
|AAAAAAAAA  |alejandra   |
|AAAAAAAAAA |alexandria  |
|AAAAAAAAAA |alexandria  |
|AAAAAAAAAA |alexandria  |
|AAAAAAAAAAA|christopher |
|AAAAAAAAAAA|christopher |
|AAAAAAAAAAA|christopher |
+-----------+------------+


 VALUE SHAPES — last_name
+----------+-----+
|shape     |count|
+----------+-----+
|AAAAAA    |12875|
|AAAAA     |12204|
|AAAAAAA   |8607 |
|AAAAAAAA  |5752 |
|AAAA      |5450 |
|AAAAAAAAA |2179 |
|AAA       |836  |
|AAAAAAAAAA|628  |
|AAAAAA AAA|158  |
|AAAAA AAA |143  |
+----------+-----+


 SAMPLE VALUES — last_name
+---------------+---------------+
|shape          |sample_value   |
+---------------+---------------+
|AA             |ho             |
|AA             |ho             |
|AA             |ho             |
|AA AA          |le md          |
|AA AAA         |ho dds         |
|AA AAA         |yu dds         |
|AAA            |ali            |
|AAA            |ali            |
|AAA            |ali            |
|AAA AA         |key md         |
|AAA AA         |kim md         |
|AAA AA         |lee md         |
|AAA AA.        |liu jr.        |
|AAA AA.        |ray jr.        |
|AAA AAA        |cox dds        |
|AAA AAA        |cox dds        |
|AAA AAA        |day dvm        |
|AAA AAAAAA     |amy cooper     |
|AAA AAAAAA     |zoe nguyen     |
|AAA AAAAAAA AAA|amy higgins dds|
|AAAA           |ball           |
|AAAA           |ball           |
|AAAA           |ball           |
|AAAA AA        |ball ii        |
|AAAA AA        |bass ii        |
|AAAA AA        |byrd md        |
|AAAA AA.       |cobb jr.       |
|AAAA AA.       |cole jr.       |
|AAAA AA.       |cruz jr.       |
|AAAA AAA       |bean phd       |
|AAAA AAA       |bell dds       |
|AAAA AAA       |bell dds       |
|AAAA AAAAAA    |mary branch    |
|AAAA AAAAAA AA |lynn adkins md |
|AAAA AAAAAAA   |dawn ferrell   |
|AAAA AAAAAAAA  |lisa williams  |
|AAAAA          |adams          |
|AAAAA          |adams          |
|AAAAA          |adams          |
|AAAAA A        |hurst v        |
|AAAAA AA       |adams md       |
|AAAAA AA       |adams md       |
|AAAAA AA       |adams md       |
|AAAAA AA.      |cowan jr.      |
|AAAAA AA.      |davis jr.      |
|AAAAA AA.      |davis jr.      |
|AAAAA AAA      |adams dds      |
|AAAAA AAA      |adams phd      |
|AAAAA AAA      |ayala dds      |
|AAAAA AAAAA    |janet stone    |
+---------------+---------------+
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
+-------------+-----+
|shape        |count|
+-------------+-----+
|+999999999999|50000|
+-------------+-----+


 SAMPLE VALUES — phone
+-------------+-------------+
|shape        |sample_value |
+-------------+-------------+
|+999999999999|+971510000475|
|+999999999999|+971510001272|
|+999999999999|+971510004458|
+-------------+-------------+


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
|AAAAAAA |blocked     |
|AAAAAAA |blocked     |
|AAAAAAA |blocked     |
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


 VALUE SHAPES — city
+--------------+-----+
|shape         |count|
+--------------+-----+
|AAAAA         |14194|
|AAAAAAA       |7248 |
|AAAAAAAA      |7192 |
|AAA AAAAA     |7137 |
|AA AAA        |7132 |
|AAA AA AAAAAAA|7097 |
+--------------+-----+


 SAMPLE VALUES — city
+--------------+--------------+
|shape         |sample_value  |
+--------------+--------------+
|AA AAA        |Al Ain        |
|AA AAA        |Al Ain        |
|AA AAA        |Al Ain        |
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AA AAAAAAA|Ras Al Khaimah|
|AAA AAAAA     |Abu Dhabi     |
|AAA AAAAA     |Abu Dhabi     |
|AAA AAAAA     |Abu Dhabi     |
|AAAAA         |Ajman         |
|AAAAA         |Ajman         |
|AAAAA         |Ajman         |
|AAAAAAA       |Sharjah       |
|AAAAAAA       |Sharjah       |
|AAAAAAA       |Sharjah       |
|AAAAAAAA      |Fujairah      |
|AAAAAAAA      |Fujairah      |
|AAAAAAAA      |Fujairah      |
+--------------+--------------+


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
|999 AA AAAA               |483 wu road               |
|999 AA AAAA               |512 wu road               |
|999 AA AAAA               |831 li burg               |
|999 AA AAAAA              |285 wu field              |
|999 AA AAAAA              |629 yu cliff              |
|999 AA AAAAA              |652 li curve              |
|999 AA AAAAA AAA. 999     |516 ho lodge apt. 341     |
|999 AA AAAAA AAA. 999     |923 yu creek apt. 281     |
|999 AA AAAAA AAAAA 999    |472 le curve suite 919    |
|999 AA AAAAA AAAAA 999    |941 wu green suite 539    |
|999 AA AAAAAA             |377 le hollow             |
|999 AA AAAAAA AAA. 999    |073 le shores apt. 890    |
|999 AA AAAAAA AAA. 999    |728 yu divide apt. 449    |
|999 AA AAAAAA AAAAA 999   |406 li lights suite 063   |
|999 AA AAAAAAA            |236 le viaduct            |
|999 AA AAAAAAA AAAAA 999  |173 le heights suite 996  |
|999 AA AAAAAAAAA AAA. 999 |205 yu mountains apt. 219 |
|999 AA AAAAAAAAA AAA. 999 |549 jo junctions apt. 920 |
|999 AA AAAAAAAAA AAAAA 999|750 wu stravenue suite 444|
|999 AA AAAAAAAAAA         |787 wu extensions         |
|999 AAA AAA               |742 ann row               |
|999 AAA AAA AAA. 999      |353 day via apt. 280      |
|999 AAA AAA AAA. 999      |729 orr dam apt. 022      |
|999 AAA AAAA              |014 joy pine              |
|999 AAA AAAA              |095 may burg              |
|999 AAA AAAA              |185 lee club              |
|999 AAA AAAA AAA. 999     |008 dan loop apt. 453     |
|999 AAA AAAA AAA. 999     |018 amy mill apt. 902     |
|999 AAA AAAA AAA. 999     |082 lee mill apt. 014     |
|999 AAA AAAA AAAAA 999    |186 cox glen suite 716    |
|999 AAA AAAA AAAAA 999    |280 lin ways suite 451    |
|999 AAA AAAA AAAAA 999    |473 mia road suite 777    |
|999 AAA AAAAA             |056 amy inlet             |
|999 AAA AAAAA             |080 amy brook             |
|999 AAA AAAAA             |094 amy flats             |
|999 AAA AAAAA AAA. 999    |039 key light apt. 196    |
|999 AAA AAAAA AAA. 999    |129 ray burgs apt. 350    |
|999 AAA AAAAA AAA. 999    |264 gay lodge apt. 015    |
|999 AAA AAAAA AAAAA 999   |160 joy curve suite 460   |
|999 AAA AAAAA AAAAA 999   |410 lee field suite 492   |
|999 AAA AAAAA AAAAA 999   |504 don crest suite 048   |
|999 AAA AAAAAA            |012 lin tunnel            |
|999 AAA AAAAAA            |062 ana garden            |
|999 AAA AAAAAA            |082 amy forges            |
|999 AAA AAAAAA AAA. 999   |114 cox groves apt. 821   |
|999 AAA AAAAAA AAA. 999   |326 day common apt. 987   |
|999 AAA AAAAAA AAA. 999   |530 ann brooks apt. 609   |
|999 AAA AAAAAA AAAAA 999  |074 gay cliffs suite 163  |
|999 AAA AAAAAA AAAAA 999  |212 day groves suite 284  |
|999 AAA AAAAAA AAAAA 999  |212 orr points suite 414  |
+--------------------------+--------------------------+
only showing top 50 rows

 Discovery complete for crm_silver_users — scanned 50000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_silver_coupon_redemptions
====================================================================================================

 SCHEMA
root
 |-- coupon_redemption_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- order_sk: string (nullable = true)
 |-- promotion_sk: string (nullable = true)
 |-- redemption_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- promotion_code: string (nullable = true)
 |-- order_id: string (nullable = true)
 |-- redeemed_ts: timestamp (nullable = true)
 |-- is_valid_redeem: integer (nullable = true)
 |-- has_multiple_promos: integer (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 4000

 NULL COUNTS
+--------------------+-------+--------+------------+-------------+-------+--------------+--------+-----------+---------------+-------------------+-------------+
|coupon_redemption_sk|user_sk|order_sk|promotion_sk|redemption_id|user_id|promotion_code|order_id|redeemed_ts|is_valid_redeem|has_multiple_promos|dw_created_at|
+--------------------+-------+--------+------------+-------------+-------+--------------+--------+-----------+---------------+-------------------+-------------+
|0                   |0      |0       |0           |0            |0      |0             |0       |0          |0              |0                  |0            |
+--------------------+-------+--------+------------+-------------+-------+--------------+--------+-----------+---------------+-------------------+-------------+


 VALUE SHAPES — coupon_redemption_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|134  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|91   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|89   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|89   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|88   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|85   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|82   |
|AAAAAAA9AAA9AAAAAAAAAAAAAA|71   |
|AAA9AAA9AAAAAAAAAAAAAAAAAA|62   |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|60   |
+--------------------------+-----+


 SAMPLE VALUES — coupon_redemption_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAA9AAA9AAA9AA|m2i4y2y5ytyxmzc3ywy1ngq2yj|
|A9A9A9AAAAA9AAAAA9A9AAA9AA|m2y0y2uwzdg1zmzky2i5otq4nz|
|A9A9A9AAAAAAAAAAA9AAAAAAAA|n2e0y2yznwvjzjjin2ixzdjhnt|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|y2e1n2eymthiyzyzmtk2mtbhnt|
|A9A9A9AAAAAAAAAAAAAAA9A9AA|y2m0y2zkztqynmyxngyym2m0nm|
|A9A9AAA9A9A9A9AAAAAAAAAAAA|n2m1mmi0y2e0m2uynjbhmmezzd|
|A9A9AAA9A9AAAAA9AAAAAAAAAA|y2i4mza0n2fjmzu3mgmzztzjnt|
|A9A9AAA9AAA9A9A9AAAAA9AAAA|y2i2nje0zge3n2u5owyxy2uzyt|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|y2m1ytm2yzg2zjq2otlknjczzd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2e2yjq0mmq0ytiwotk4nja5zd|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|m2e0ntc0ngq5ymyyzdc4ywyzyw|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|m2q5zty1ndu2zmqzzdi4mjfmmt|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2e2yzi1nmi1nzrhyjk5zgeyzw|
|A9A9AAA9AAA9AAAAAAAAA9A9AA|n2m2zgm0mwy4zgrkodljn2y3mj|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|y2m0mtg0mda2ogvkmmzmyjy5mg|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|y2q1zdy2nte5mjmwmtayywu4nj|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|n2i1zja5zgi5mdgwmtjmnzzjow|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|y2u0mje3mwi1zdmzzmnlyzbknz|
|A9A9AAA9AAAAA9A9AAAAA9AAAA|n2q0yzm0zjawm2m4ztbin2mwyz|
|A9A9AAA9AAAAA9A9AAAAAAA9AA|y2i1yzu4ytdky2u2nmjkngy2nt|
|A9A9AAA9AAAAA9A9AAAAAAAAAA|m2q0ytq3njnin2i5mzblogfjzg|
|A9A9AAA9AAAAA9AAAAAAAAA9AA|m2u3mtc5mgjin2finjjinmq4md|
|A9A9AAA9AAAAAAA9AAA9AAA9AA|m2i3nzu4ztnjyte3yzu5mtm4zt|
|A9A9AAA9AAAAAAA9AAAAA9A9AA|m2m2mgi5njbmmta0mgqxn2m0mm|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|m2y1mdq5mgyznzq2mdfhnjm2mt|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|n2i1ngm3yzmxmdu2mmjlowm3zj|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|n2y3ngq2otgwogi1ntmzyjm4nm|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|m2i5ntk3ytnlmwe1ywvizjdiym|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|n2e1zgq5zjnlytu2ntmxnjrjnj|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2e0mgq4ztgzzta0odjjzdqwnd|
|A9A9AAA9AAAAAAAAAAA9A9A9AA|n2i1zwy4odeyzwfjmta1y2e4mz|
|A9A9AAA9AAAAAAAAAAA9A9AAAA|m2u4ytm3yzbjmgvjmmu2y2jlyt|
|A9A9AAA9AAAAAAAAAAA9A9AAAA|n2i1zje4nwqxzwzizmi1m2qxot|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|n2e5nmi3mdcyyzcxzjk1oty0nw|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|y2i5zwu5ntqzndcxote3nzy4zj|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|y2u3ndk0nwqyowzkodc4ywy1zd|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2y1yjq3ztzkzwyzzge0otlizg|
|A9A9AAA9AAAAAAAAAAAAA9A9AA|y2i5zdu5ndvingqymzyyy2e1ot|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|y2e0nza0nwmzzjlkzmnim2rlmm|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2q4mgi4zmzkmgizztbmzmy1nt|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2e3otq2ymqwntrmndvmyji3mt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2e1zmi3ymnjmznjnjnimteymw|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2i4odc5yjcymzbhzgrimtriyt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2y4zdu3yjliztlkogmxmwfimt|
|A9A9AAAAA9AAAAA9AAAAAAA9AA|y2y5zjiyn2yyyze4ntyxyju2ng|
|A9A9AAAAA9AAAAAAAAA9AAA9AA|y2m1mjfln2zmmzhmnjm1mza3ow|
|A9A9AAAAA9AAAAAAAAA9AAAAAA|y2q3ztewy2nlyzazmwm0ognkog|
|A9A9AAAAA9AAAAAAAAAAAAAAAA|y2y0zwvkm2exmzbmmdiwodgwnm|
|A9A9AAAAAAA9A9A9A9A9A9AAAA|y2y5zjczyzu1y2i5y2m4m2jizm|
|A9A9AAAAAAA9AAA9A9A9AAAAAA|m2m2nzbiztu3mzg4m2y1ntjizt|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|146  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|94   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|91   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|89   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|85   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|73   |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|62   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|59   |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|58   |
|AAAAAAA9AAA9AAAAAAAAAAAAAA|55   |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9AAA9AAAAA9AAAAAAAAAA|m2m1m2mwn2viowe2zwyxytgwnm|
|A9A9A9AAAAA9AAA9AAAAAAAAAA|m2q5n2vmmwi1ywq0nwvlntqwyz|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|m2e3m2vjyjy2nzgymmrlmzhjnw|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2e1m2iwnjq0owjmmwizmjuxng|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2i4y2flyjk1mmeynzkyytczmm|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|n2y0n2uyotnhmdzimzq1mgvjyz|
|A9A9A9AAAAAAAAAAAAAAAAAAAA|n2e3m2ixowzjnmzknmmynzkxmz|
|A9A9AAA9A9A9AAAAAAA9A9AAAA|y2q2zmq3m2q0mdjmzwq1n2fmnm|
|A9A9AAA9A9AAAAA9AAA9AAAAAA|m2y4mzg1n2jiyzq2ogi3zdbiym|
|A9A9AAA9A9AAAAAAAAA9AAA9AA|y2m2mzg0y2jmmzjkmjm5nmi1mm|
|A9A9AAA9A9AAAAAAAAAAA9AAAA|m2y0ngu0n2nhytlhndfly2mwnt|
|A9A9AAA9A9AAAAAAAAAAAAA9AA|y2e3otg4n2iyntaxmjziodm1zt|
|A9A9AAA9A9AAAAAAAAAAAAAAAA|y2m1mwy5m2rjnzzlodhlywiwmd|
|A9A9AAA9A9AAAAAAAAAAAAAAAA|y2y5yzy0y2fiyjmyntmyowvhmt|
|A9A9AAA9AAA9A9A9AAAAA9AAAA|y2q1yjk1zdk5y2y5ogeym2qwmm|
|A9A9AAA9AAA9A9AAAAA9AAA9AA|n2y3mzg1zjm1y2eymwq0owq5zw|
|A9A9AAA9AAA9AAA9A9AAAAA9A9|n2e0ymi0zda1yzy3m2eymwm4m2|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|y2y5zgm2mdk1mji4nwmyzjjmzm|
|A9A9AAA9AAA9AAAAA9A9AAAAAA|m2i3zde4nzy1nzrmm2q2mzfiyt|
|A9A9AAA9AAA9AAAAAAA9A9AAAA|m2m4ngu1njg4owjkzdm0y2yxmt|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2u1zdk1odg0mzawoge5ymy3ow|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|n2i4zge4owy1otfhmdi2ndi5nd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|y2e1zwu5ytm5ndjlzwq1mje0mm|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2u0ywy4zji5ywmynzi0ztqznt|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2i5mza2zwu0odmxzdyymwu2ym|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2i5mza2zwu0odmxzdyymwu2ym|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|y2m0ndu0zgm2mtgwyjlhodixnd|
|A9A9AAA9AAAAAAA9A9A9AAAAA9|m2y3nte2zjkzzte2y2e4mjriy2|
|A9A9AAA9AAAAAAA9AAA9AAA9AA|m2i3zje0ngvkztm3mza3yza5zw|
|A9A9AAA9AAAAAAA9AAA9AAAAAA|m2q0otc5odiyytu2yjc3ogflzw|
|A9A9AAA9AAAAAAA9AAA9AAAAAA|y2m4mtu0nmywotu0mdk3mtuwnd|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|n2e1ndi3nteyngm0ymezytg2nz|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|n2u5ode1ownhowe1zjzhzgy4mz|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|y2y5nji5mtzlndy2mdvhzgy3ow|
|A9A9AAA9AAAAAAA9AAAAAAAAA9|y2q5nza1mjqwmgy0mjaymzyxn2|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|m2e0mjg1mdvhoge2owixngewmt|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2q0nza0odkxzmy4yzkxnzezod|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|m2e5zti3mjcznmuwyzg4nwm3nt|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|n2m5yte0zdcymtmymjq2owy0zj|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|m2q4ogu3mjhhmzazngu2ywvkyj|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|m2y5mgy5zjvhmmexyti4ztezzg|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2e0ngy2yziyodzlnme0nwzhmw|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|m2u0ymq4ntniyjhjndezy2mwng|
|A9A9AAA9AAAAAAAAAAAAAAA9A9|m2u2mjq5odvhnznhyjljnzu0m2|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2e1otg0zdhmnjlhnzywotg1yj|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2u3nmi0ztjjmdkyntuznmi3nt|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2e0nwm3ntbiyjvlnznmzta4mt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2e3mge3nmexzjbjmdnlymzhzd|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|m2q1ymm2ownhngvhnjvkmziwzw|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — order_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|150  |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|100  |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|97   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|96   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|94   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|76   |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|76   |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|63   |
|AAAAAAAAAAA9AAA9AAAAAAAAAA|60   |
|AAAAAAAAAAA9AAAAAAAAAAA9AA|60   |
+--------------------------+-----+


 SAMPLE VALUES — order_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAA9AAA9A9A9AA|n2i3n2m5mjuxzgy3ndu5y2y2nm|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2m4m2y3zdexowywmzdlmdjjyj|
|A9A9A9AAAAA9AAAAAAA9AAA9AA|n2e5y2myzwi5zdzjowm3zgq5zg|
|A9A9A9AAAAA9AAAAAAAAAAAAAA|n2e1n2zhmtq3mzvmnjgwngqxnw|
|A9A9AAA9AAA9AAA9AAA9AAAAAA|m2q0ymi3zda3yjm5owe4zgflnm|
|A9A9AAA9AAA9AAA9AAAAAAA9AA|y2m3yte0ngy1mjq2zjzlnjc5nd|
|A9A9AAA9AAA9AAAAA9AAAAAAAA|y2i3ngy2odc0othhn2mxnjfiyw|
|A9A9AAA9AAA9AAAAA9AAAAAAAA|y2m4yjy0yju5yteyy2yxmjaxzm|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|n2m0zty2mgi0nmriyzi0ogy3ng|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|m2e4ngi5mme4mjixmzk4nzhknw|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2u5yjg5nty4yjuynwy0mdvlym|
|A9A9AAA9AAA9AAAAAAA9AAAAAA|n2y3yzk4yje5zjnhnjq1ngjlnz|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2m5mdg5odq4ytdkzgvmnwm1nj|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2q2mtu2oge1ymvjmwfhnjc4yw|
|A9A9AAA9AAA9AAAAAAAAAAA9AA|m2u0mty1nwy2mgzmmgvkmdc2nw|
|A9A9AAA9AAA9AAAAAAAAAAAAAA|y2y3ytg3mzy1mwzjntuzzthlyw|
|A9A9AAA9AAAAA9AAAAAAAAA9AA|n2m1ztm2ntixn2fimmnhzdg1zm|
|A9A9AAA9AAAAA9AAAAAAAAAAAA|m2q1nge4mtyxy2rkztdlytzlmz|
|A9A9AAA9AAAAAAA9AAA9A9AAAA|y2q5mdk4yzkzmja3zwu2y2vhot|
|A9A9AAA9AAAAAAA9AAA9AAA9AA|n2e0mza4nmyzotg0yja5mwu3mj|
|A9A9AAA9AAAAAAA9AAA9AAA9AA|y2e1mge3nzlmzdc2mti1odg1yj|
|A9A9AAA9AAAAAAA9AAA9AAAAAA|n2m3mtc3ngmxzwm0yjy1yjhiyj|
|A9A9AAA9AAAAAAA9AAA9AAAAAA|n2u2otc0njjjowq4zmu0mjaynw|
|A9A9AAA9AAAAAAA9AAAAAAA9AA|m2y5ytg3ytixmgm4zgjhyju4nd|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2u3mji4mtjmoda2zwjiytezzd|
|A9A9AAA9AAAAAAA9AAAAAAAAAA|y2y4nge1mzzmmdy2zdzjngqwnj|
|A9A9AAA9AAAAAAAAA9AAAAAAA9|n2i0ode4nwewmjfln2riodkyy2|
|A9A9AAA9AAAAAAAAA9AAAAAAAA|m2q1nda5zjuzmmfmm2vjotgxnz|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|y2q0zta4yzewytnkogm5mwm1nz|
|A9A9AAA9AAAAAAAAAAA9AAA9AA|y2u3mzy2mdfkntzmzjm2mmi4nj|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2e1zdc0ymzingqxode4mzlind|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m2mzm4ntbjnwfjzdq3ntuyzg|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|n2e0mme5zdqxnmvintfjngi5nd|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|n2u2ndc1mdjhodlmotljnju2mz|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|n2y2zji2mmqzmdqxmzhjmmq0mg|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2q3yjk0owuymmqwnwqxotkwmz|
|A9A9AAAAA9A9A9AAAAA9AAAAAA|m2q4ytnjn2y2m2uwzde5mzvlog|
|A9A9AAAAA9A9AAA9AAA9A9AAAA|n2u3nwizm2u4zmi5nwy2m2vhzw|
|A9A9AAAAA9AAAAAAAAA9AAAAA9|y2e3nwzin2iwymvjnzy0njljn2|
|A9A9AAAAA9AAAAAAAAAAAAA9AA|m2q2zdvhy2vlzjvhytvjzjm0yz|
|A9A9AAAAA9AAAAAAAAAAAAAAAA|y2u4zwzhy2niyjyxotmymdhmyt|
|A9A9AAAAAAA9A9A9AAAAAAAAAA|y2u5mwzizjc0n2i5njrjmmyxzd|
|A9A9AAAAAAA9A9AAAAAAAAA9AA|n2y2nduyyta3y2jimwyxmze3nd|
|A9A9AAAAAAA9AAA9AAA9AAA9AA|m2q1zjbhndc2yjy5ytm2nmy3nz|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2i1mgjhmmm4yze5mdy1ytzhmw|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|n2e1nmvjmmq1ytm5ztbkoti2mt|
|A9A9AAAAAAA9AAA9AAAAAAA9AA|n2i0mzqwnje1njc4yjhmmgu5mg|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|m2m4nzdkmti2zmq1njzinduxzg|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|m2y5mjazzwi2mjy5ymmymmiyot|
|A9A9AAAAAAA9AAA9AAAAAAAAAA|n2e0mznhyja5ztm1ndaxmdiznz|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — promotion_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|154  |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|128  |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|99   |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|96   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|96   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|87   |
|AAA9AAAAAAAAAAA9AAA9AAAAAA|76   |
|AAAAAAA9AAA9AAAAAAAAAAAAAA|74   |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|70   |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|68   |
+--------------------------+-----+


 SAMPLE VALUES — promotion_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9AAA9AAA9AAA9AAAAAAAAAA|n2y2zmy2mdu1ndc3owizmtczzd|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|n2y2zmy2mdu1ndc3owizmtczzd|
|A9A9AAA9AAA9AAA9AAAAAAAAAA|n2y2zmy2mdu1ndc3owizmtczzd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2u1yza5yta4mdnkmzu0zwi3nm|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2u1yza5yta4mdnkmzu0zwi3nm|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2u1yza5yta4mdnkmzu0zwi3nm|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m2mjq0otdhowzmzgi0ytbmyz|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m2mjq0otdhowzmzgi0ytbmyz|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m2mjq0otdhowzmzgi0ytbmyz|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|y2u1mjg4zjrinjhmothmn2uxym|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|y2u1mjg4zjrinjhmothmn2uxym|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|y2u1mjg4zjrinjhmothmn2uxym|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2u5ntq2zdewzdqzowrmoda3zd|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2u5ntq2zdewzdqzowrmoda3zd|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2u5ntq2zdewzdqzowrmoda3zd|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2e3zmm4mwyynjnkngyxzdcxnt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2e3zmm4mwyynjnkngyxzdcxnt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2e3zmm4mwyynjnkngyxzdcxnt|
|A9A9AAAAAAA9A9AAAAAAAAA9AA|y2e3ywzjmwq5m2rknddjmtg4nm|
|A9A9AAAAAAA9A9AAAAAAAAA9AA|y2e3ywzjmwq5m2rknddjmtg4nm|
|A9A9AAAAAAA9A9AAAAAAAAA9AA|y2e3ywzjmwq5m2rknddjmtg4nm|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2e0mdzjzju0nwu2mmm1mwyznd|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2e0mdzjzju0nwu2mmm1mwyznd|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2e0mdzjzju0nwu2mmm1mwyznd|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|m2e1ztrlotk4ymewnmuzzmy5yt|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|m2e1ztrlotk4ymewnmuzzmy5yt|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|m2e1ztrlotk4ymewnmuzzmy5yt|
|A9A9AAAAAAAAA9A9AAA9A9A9AA|m2y0zjcxnwfim2m1ndm2m2m0od|
|A9A9AAAAAAAAA9A9AAA9A9A9AA|m2y0zjcxnwfim2m1ndm2m2m0od|
|A9A9AAAAAAAAA9A9AAA9A9A9AA|m2y0zjcxnwfim2m1ndm2m2m0od|
|A9A9AAAAAAAAA9AAA9AAAAAAAA|y2i4zwixnmyxy2qwn2vjythknz|
|A9A9AAAAAAAAA9AAA9AAAAAAAA|y2i4zwixnmyxy2qwn2vjythknz|
|A9A9AAAAAAAAA9AAA9AAAAAAAA|y2i4zwixnmyxy2qwn2vjythknz|
|A9A9AAAAAAAAAAAAAAAAAAA9A9|y2q5mwuwndviyzgwmduwzgu4n2|
|A9A9AAAAAAAAAAAAAAAAAAA9A9|y2q5mwuwndviyzgwmduwzgu4n2|
|A9A9AAAAAAAAAAAAAAAAAAA9A9|y2q5mwuwndviyzgwmduwzgu4n2|
|A9AAA9A9AAA9AAAAAAAAAAAAAA|y2jjn2y5ymm5mgrkotazywjlmg|
|A9AAA9A9AAA9AAAAAAAAAAAAAA|y2jjn2y5ymm5mgrkotazywjlmg|
|A9AAA9A9AAA9AAAAAAAAAAAAAA|y2jjn2y5ymm5mgrkotazywjlmg|
|A9AAA9AAAAA9AAA9AAAAAAA9AA|m2nmy2nhyze0otk3njqynda0zj|
|A9AAA9AAAAA9AAA9AAAAAAA9AA|m2nmy2nhyze0otk3njqynda0zj|
|A9AAA9AAAAA9AAA9AAAAAAA9AA|m2nmy2nhyze0otk3njqynda0zj|
|A9AAA9AAAAAAAAA9AAAAAAA9AA|m2fhm2rkowzjmza4zmixyja2nd|
|A9AAA9AAAAAAAAA9AAAAAAA9AA|m2fhm2rkowzjmza4zmixyja2nd|
|A9AAA9AAAAAAAAA9AAAAAAA9AA|m2fhm2rkowzjmza4zmixyja2nd|
|A9AAAAA9AAA9A9A9AAA9AAA9AA|n2uyyzk0nzi3m2u2mti0yjg1nd|
|A9AAAAA9AAA9A9A9AAA9AAA9AA|n2uyyzk0nzi3m2u2mti0yjg1nd|
|A9AAAAA9AAA9A9A9AAA9AAA9AA|n2uyyzk0nzi3m2u2mti0yjg1nd|
|A9AAAAA9AAA9AAA9AAAAAAA9AA|y2jkzdq0zjg2mtc2ytnhmme1ow|
|A9AAAAA9AAA9AAA9AAAAAAA9AA|y2jkzdq0zjg2mtc2ytnhmme1ow|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — redemption_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|99AA9999-999A-9AA9-9999-9A9AA9A9A999|1    |
|99A999AA-9999-9AA9-AA9A-A99999AA9AAA|1    |
|AAAA9AAA-999A-999A-A999-9A9A9AA9AA99|1    |
|9AA9A9A9-999A-999A-A999-9A99999A9A9A|1    |
|AAAA9999-99A9-999A-A99A-A9A99999999A|1    |
|9A999999-9A9A-9999-9A99-A999999A999A|1    |
|A999AA99-A99A-9999-9A99-A999A999AA99|1    |
|A9A99999-99A9-9A99-AA99-999A9A9A9999|1    |
|99AA9AAA-A999-9A99-9999-A9A99999AAAA|1    |
|99AAAA99-9999-9999-AA99-A9A999999999|1    |
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
|99999A99|54   |
|A9999999|54   |
|99A99999|54   |
|9A999999|50   |
|9999999A|46   |
|999A9999|46   |
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

 Discovery complete for mkt_silver_coupon_redemptions — scanned 4000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_silver_marketing_attribution
====================================================================================================

 SCHEMA
root
 |-- marketing_attribution_sk: string (nullable = true)
 |-- user_sk: string (nullable = true)
 |-- attrib_id: string (nullable = true)
 |-- user_id: string (nullable = true)
 |-- channel: string (nullable = true)
 |-- campaign: string (nullable = true)
 |-- medium: string (nullable = true)
 |-- source: string (nullable = true)
 |-- is_first_touch: integer (nullable = true)
 |-- touch_ts: timestamp (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 80000

 NULL COUNTS
+------------------------+-------+---------+-------+-------+--------+------+------+--------------+--------+-------------+
|marketing_attribution_sk|user_sk|attrib_id|user_id|channel|campaign|medium|source|is_first_touch|touch_ts|dw_created_at|
+------------------------+-------+---------+-------+-------+--------+------+------+--------------+--------+-------------+
|0                       |0      |0        |0      |0      |0       |0     |0     |0             |0       |0            |
+------------------------+-------+---------+-------+-------+--------+------+------+--------------+--------+-------------+


 VALUE SHAPES — marketing_attribution_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|2896 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|1744 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|1738 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|1735 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1701 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|1699 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|1650 |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|1074 |
|AAAAAAAAAAAAAAA9AAA9AAAAAA|1072 |
|AAAAAAAAAAAAAAA9AAAAAAA9AA|1044 |
+--------------------------+-----+


 SAMPLE VALUES — marketing_attribution_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9A9A9AAA9AAA9AAAAAA|y2y5n2i4n2u2ztg3yzi2zwvlod|
|A9A9A9A9A9AAAAA9AAA9AAAAAA|m2i1y2m1y2jlmdk2mmy5nzcxzw|
|A9A9A9A9A9AAAAAAAAA9A9AAAA|y2y1m2i0n2uyntmzodk0y2izot|
|A9A9A9A9A9AAAAAAAAAAAAAAAA|m2q2y2q5m2mwndeynwzhnzvinj|
|A9A9A9A9AAA9A9AAAAAAAAAAAA|y2u5y2e3ztu3m2fhoguxywzjnj|
|A9A9A9A9AAA9AAA9A9A9A9A9AA|m2q0n2i1yja1zdm4n2m5n2u5nm|
|A9A9A9A9AAA9AAA9A9A9AAAAAA|n2u2n2i0ytg1ngq2m2y2ztuwyw|
|A9A9A9A9AAA9AAA9AAA9AAAAAA|m2e3m2q3zju3zdu5ywe1nddizg|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|n2m5n2u1yzc1mjc0odmwzmfjmz|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|n2q5n2y2ntc0zjq3zdrkyjawmz|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|m2q5m2i0mdu2yjjkmjq1yjk0zj|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|n2e2m2m2nme0zwjiyta0odg0zt|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|y2m0y2e3mmy1zdawnte5otzlym|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|y2m3n2i3ntu2mwrlodi3ndfmnd|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|m2u1m2e1ogm5zgjlodziztgxod|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|n2m3m2m1ywy1zthjndcymgmyzt|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2u4y2u3mtu5odzknjnkowqxmz|
|A9A9A9A9AAAAA9A9AAA9AAAAAA|y2u0y2m3owvhy2q4ndg3owrlot|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|y2q4n2i4ytiyn2qwnzmxzdcxot|
|A9A9A9A9AAAAAAA9AAA9AAA9A9|y2u2m2m3njiymzm4ntm3ogm1n2|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2q5m2u3mmyxngq0nzy1mwmxmg|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|y2e4y2u4zdeyowi3yzm2ztcyyt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2y4y2q3mmuzmzm4ztizzwq0yt|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|y2y5y2e2ndlhywy4zmfjndq0ot|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|m2m4y2e0yzyzzwy3mtniztizmw|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|m2u4m2m0ntnkytm2ytvkzjiwmm|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2m4n2m0zdnjyju5mwmzngezyt|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|n2u2n2y3nzkyyzbiywi0ngy0mz|
|A9A9A9A9AAAAAAAAAAA9AAAAA9|m2i5n2i4mtllmtixmtm2ytrkm2|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|m2y2y2i4mznlnthkzje1ymuynt|
|A9A9A9A9AAAAAAAAAAAAA9AAAA|y2i3m2m4mwewndblnthly2uyng|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|n2e0n2m1yjmymwrjmzblmjq4mj|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2q0m2q3ngiwndnmzdrkzjazod|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|m2q4m2i3ymuxnjqyytezzgrjnm|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|n2i4n2i2zwviytuwmdmwztizzt|
|A9A9A9AAA9A9AAA9A9AAAAAAAA|y2q3m2vhy2u3nzm3y2viodnlmg|
|A9A9A9AAA9A9AAAAAAA9A9A9AA|y2u5n2zjm2m4ndrjntg4m2y1zj|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|y2m4m2uyn2e3otdmotyxzja1nt|
|A9A9A9AAA9A9AAAAAAAAAAAAAA|m2y1n2zjm2e0njgxzduwotzlod|
|A9A9A9AAA9A9AAAAAAAAAAAAAA|n2e3n2qxn2m3nzlhodzhotzmzm|
|A9A9A9AAA9A9AAAAAAAAAAAAAA|y2e2m2jhm2i0ngexnjlkywzjmw|
|A9A9A9AAA9AAAAAAAAA9AAAAAA|y2i1n2vkn2iyyjvkyji4yzdlzw|
|A9A9A9AAAAA9A9A9AAA9A9AAAA|y2i3n2fiowu2y2i3mtm0n2niyz|
|A9A9A9AAAAA9A9A9AAA9AAA9AA|y2m0n2uwzdg5n2q1ngi0yty4nt|
|A9A9A9AAAAA9A9AAAAAAAAAAAA|m2q1n2rjnzu4n2rhyjuzotlmzm|
|A9A9A9AAAAA9A9AAAAAAAAAAAA|y2e2n2eymte2m2rmnzyyntdlog|
|A9A9A9AAAAA9AAA9A9AAA9AAAA|m2q5n2ezodi5nda2n2zmy2exnj|
|A9A9A9AAAAA9AAA9AAA9A9AAAA|m2u1y2nlodc2ztg1mwm5n2yynj|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|n2i4y2iwymy1nwi0ywy1odu2mz|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i5n2fkmmu2ndq1ote3nwuxod|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — user_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|2873 |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|1737 |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|1725 |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|1673 |
|AAAAAAAAAAAAAAA9AAAAAAAAAA|1670 |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|1644 |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|1637 |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|1092 |
|AAA9AAAAAAA9AAAAAAAAAAAAAA|1092 |
|AAAAAAA9AAAAAAA9AAAAAAAAAA|1082 |
+--------------------------+-----+


 SAMPLE VALUES — user_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAA9AAA9AAA9AAA9AA|m2y4n2m5yzy3yjg1mgy2mtu1zt|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAA9AAAAAAAAAA|m2e0n2y3nzu1owm0nzbinzhjnd|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAA9A9AAA9AA|n2e3m2i1nwi1mdgwn2i2yzg3yz|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q4m2y2odg3mmfmmji1owq0zd|
|A9A9A9A9AAA9AAAAAAA9AAA9AA|y2q5m2u5zwu0mweymtq0owy5yz|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAA9AAAAAA|n2i2m2e1mje5yjhkzmi4mtmyzj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAA9AA|m2m3m2y5owy0yzgxmzrloti3nj|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAA9AAAAAAAAAAAAAA|y2q3n2y1ogm3ymflzjlkmdjlyz|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAA9AAAAAAAAAAAA|m2y1n2q4otuwn2nhnjiymwyzyw|
|A9A9A9A9AAAAAAA9A9A9AAAAAA|y2m0n2e5ogeymzi3m2q3nzlmmz|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|m2y3y2i4nzjjmdk3nti3zdqwyt|
|A9A9A9A9AAAAAAA9AAA9AAAAAA|n2i5y2m1zdblmge0mjy3owrizj|
|A9A9A9A9AAAAAAA9AAAAAAA9AA|n2m0m2u0ymqwmzm3nzvhzwe0nm|
|A9A9A9A9AAAAAAA9AAAAAAAAAA|n2y5y2e2otiymdm3nzeznzgwzd|
|A9A9A9A9AAAAAAAAA9A9AAAAAA|m2i2y2i0odgwmgnim2u5odjlmt|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2e4m2m2yzlmmtuxmtk5owi5zd|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2m4n2u4yzhlmjbmmwe4nzu0nz|
|A9A9A9A9AAAAAAAAAAA9AAA9AA|y2m4n2u4yzhlmjbmmwe4nzu0nz|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAA9AAAAAA|y2e4m2e2mjjiowexzgi1ytjjnj|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9A9AAAAAAAAAAAAAAA9AA|y2m4n2e2owjhmgfhodllmjy1og|
|A9A9A9A9AAAAAAAAAAAAAAAAAA|y2y2y2i4ogrjzmixyzawnwmxmz|
|A9A9A9AAA9A9AAA9AAAAAAAAAA|m2m4n2iyn2e1yjc1mzfjyzrmyj|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
|A9A9A9AAA9A9AAAAAAAAAAA9AA|n2y4n2zhy2q4zjcyztnlyzy1od|
|A9A9A9AAA9AAAAA9AAAAAAAAAA|m2m1m2mwn2viowe2zwyxytgwnm|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|n2y5y2uyyme0n2q3mzg1odgwmj|
|A9A9A9AAAAA9A9A9AAA9AAAAAA|n2y5y2uyyme0n2q3mzg1odgwmj|
|A9A9A9AAAAA9AAA9A9AAAAAAAA|y2i5n2yyodi1mmq0y2ziodmymt|
|A9A9A9AAAAA9AAA9AAA9A9AAAA|m2m0m2nhmzc5mge4yze1m2nmyj|
|A9A9A9AAAAA9AAA9AAA9A9AAAA|m2m0m2nhmzc5mge4yze1m2nmyj|
|A9A9A9AAAAA9AAA9AAA9A9AAAA|m2m0m2nhmzc5mge4yze1m2nmyj|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|y2e0m2yxzde4zme1mjk0ymi4zm|
|A9A9A9AAAAA9AAA9AAA9AAA9AA|y2e0m2yxzde4zme1mjk0ymi4zm|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i4y2ziyjm0yzg0nmi4otblzj|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|m2i4y2ziyjm0yzg0nmi4otblzj|
|A9A9A9AAAAA9AAA9AAA9AAAAAA|n2u5m2vhmzk5ndk2zdk2ytljog|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — attrib_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|99999999-9999-9AA9-9999-A9A99AAA9999|2    |
|9AA99A99-9999-9AAA-AA9A-9A9A999999A9|2    |
|99999999-9A99-99A9-99A9-999A9A9AAA99|2    |
|99A999AA-9999-99A9-9A99-9A9AA9AA9999|2    |
|9A999999-999A-9A99-99A9-9AAAAA99AA9A|2    |
|999A99A9-A99A-9999-9999-9999999A9999|2    |
|9999A999-99A9-9999-9999-999A9A9999A9|2    |
|A9A99999-9999-9A99-9999-9999A9A9999A|2    |
|99999999-AA99-99AA-9999-A9AAA99A9999|1    |
|9AA99A99-9A9A-9AA9-9AAA-9999A99999A9|1    |
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
|AAAAA   |email       |
|AAAAA   |email       |
|AAAAA   |email       |
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
|A             |a             |
|A             |a             |
|A             |a             |
|AA            |as            |
|AA            |as            |
|AA            |as            |
|AAA           |act           |
|AAA           |act           |
|AAA           |act           |
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
|AAAAAAAA      |activity      |
|AAAAAAAA      |activity      |
|AAAAAAAA      |activity      |
|AAAAAAAAA     |according     |
|AAAAAAAAA     |according     |
|AAAAAAAAA     |according     |
|AAAAAAAAAA    |collection    |
|AAAAAAAAAA    |collection    |
|AAAAAAAAAA    |collection    |
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
|AAAAAAAA|referral    |
|AAAAAAAA|referral    |
|AAAAAAAA|referral    |
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
|AAAAA |email       |
|AAAAA |email       |
|AAAAA |email       |
|AAAAAA|direct      |
|AAAAAA|direct      |
|AAAAAA|direct      |
+------+------------+


 Discovery complete for mkt_silver_marketing_attribution — scanned 80000 rows

====================================================================================================
 DISCOVERING TABLE: mkt_silver_marketing_cost
====================================================================================================

 SCHEMA
root
 |-- marketing_cost_sk: string (nullable = true)
 |-- spend_id: string (nullable = true)
 |-- channel: string (nullable = true)
 |-- spend: string (nullable = true)
 |-- spend_date: timestamp (nullable = true)
 |-- dw_created_at: timestamp (nullable = true)


 TOTAL ROWS: 365

 NULL COUNTS
+-----------------+--------+-------+-----+----------+-------------+
|marketing_cost_sk|spend_id|channel|spend|spend_date|dw_created_at|
+-----------------+--------+-------+-----+----------+-------------+
|0                |0       |0      |0    |0         |0            |
+-----------------+--------+-------+-----+----------+-------------+


 VALUE SHAPES — marketing_cost_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAA9AAAAAAAAAA|12   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|11   |
|AAAAAAAAAAAAAAAAAAAAAAAAAA|11   |
|AAA9AAAAAAAAAAAAAAAAAAA9AA|8    |
|AAAAAAA9AAAAAAA9AAAAAAAAAA|8    |
|AAA9AAAAAAAAAAA9AAAAAAAAAA|8    |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|8    |
|AAAAAAAAAAAAAAAAAAA9AAA9AA|7    |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|6    |
|AAAAAAAAAAAAAAA9AAAAAAA9AA|6    |
+--------------------------+-----+


 SAMPLE VALUES — marketing_cost_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9A9A9AAAAAAAAAAAAAAA9AA|n2i2y2e1mtnmywjkntlkmjg4mz|
|A9A9A9AAAAA9AAAAAAA9AAAAAA|y2m3y2rkzdm1odnjyjy5mmqzmg|
|A9A9A9AAAAAAAAAAAAA9AAAAAA|n2u2n2nkmtjmyjlimmy4ymzhnt|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|m2m4yze0zwmyotqwyta1mtvjmj|
|A9A9AAAAAAAAAAAAAAAAAAA9A9|m2i2njhlmdnjmgnkywjmnmm3y2|
|A9A9AAAAAAAAAAAAAAAAAAA9AA|m2e4ztkymtzmmmuzmjmxmjg3yj|
|A9A9AAAAAAAAAAAAAAAAAAA9AA|y2m2ogfmyjvintlimznhmmm4og|
|A9A9AAAAAAAAAAAAAAAAAAAAAA|m2i4nzzlmgqyzdqymwzkmwyymm|
|A9A9AAAAAAAAAAAAAAAAAAAAAA|m2u5zwjlnjkzmdfkmjkyytyynw|
|A9AAA9AAAAAAAAA9AAAAAAA9AA|n2rlm2nknjnmzju0mwexmty5mm|
|A9AAAAA9AAA9AAAAAAAAAAAAAA|m2ewmmi1mzu0njdhmdyxmtcwnj|
|A9AAAAA9AAA9AAAAAAAAAAAAAA|y2vmzwe3mgy4otbjzdrlmdflnw|
|A9AAAAA9AAAAAAA9AAA9AAA9A9|m2zimjg4mgywnzu0mme2mwu3n2|
|A9AAAAA9AAAAAAA9AAA9AAA9AA|m2iwmdm1mdbhmdg0ywm5njm4zg|
|A9AAAAA9AAAAAAA9AAAAAAAAA9|y2qyyjc2ywvhowi1ymzkotdmm2|
|A9AAAAA9AAAAAAA9AAAAAAAAAA|n2eymzq5mzcyytk5owrhzdzkmw|
|A9AAAAA9AAAAAAA9AAAAAAAAAA|n2niodu1ywfimgi1yzzjndzlnd|
|A9AAAAA9AAAAAAA9AAAAAAAAAA|n2rindc5mtvimmy2mgrhmgzjzt|
|A9AAAAA9AAAAAAAAAAAAAAAAAA|m2vjymu5ytbmmdjhotcxnthhyt|
|A9AAAAAAA9A9AAAAAAA9AAAAAA|m2vhmzfim2e5mjzlngy3mjhknm|
|A9AAAAAAA9AAAAA9AAAAAAA9AA|m2zkzddhy2jinzg2yjvizmu2nt|
|A9AAAAAAAAA9AAA9AAAAAAA9AA|m2rlmtfjody4mdi3mdrjmzc1nz|
|A9AAAAAAAAA9AAA9AAAAAAAAAA|m2exnjlmymu2zjk3yjqyzmnjnz|
|A9AAAAAAAAAAAAA9AAA9A9AAAA|m2vinjrhnjdjogq1ywq0n2mwot|
|A9AAAAAAAAAAAAA9AAA9AAA9AA|m2izowezmdmyztm3zda0mzu5mt|
|A9AAAAAAAAAAAAA9AAA9AAAAAA|y2uzzjzjodezota4zti1nwizyj|
|A9AAAAAAAAAAAAA9AAAAAAA9AA|n2zhndyyymzkmgy3nzbkzti4md|
|A9AAAAAAAAAAAAA9AAAAAAAAAA|n2ezzmfmmwvjzda3nmjkmtjkzj|
|A9AAAAAAAAAAAAAAAAAAAAA9AA|n2vjntbkodexzjhhmzbjmge5zm|
|A9AAAAAAAAAAAAAAAAAAAAA9AA|n2zlywuwytblzwzjotqymwq4mw|
|A9AAAAAAAAAAAAAAAAAAAAAAAA|n2uwogyxytliymuzngfimzmyod|
|AAA9A9A9AAAAAAAAAAA9AAA9AA|oda0y2y1nwjhmgzmmmu5mde5nd|
|AAA9A9AAAAAAAAAAAAAAAAAAAA|ytm3m2rjnmviodvlztgxzdvizw|
|AAA9AAA9A9A9AAAAA9AAAAAAAA|mdi2yjk4m2u4zwewm2nmyzhmnd|
|AAA9AAA9A9AAAAA9AAA9A9A9AA|mtm2mtq4n2yxmzi4mtk5m2q2ng|
|AAA9AAA9A9AAAAA9AAAAAAAAAA|mtq0mmm1y2iwodq1otqyymvkmw|
|AAA9AAA9A9AAAAAAAAA9AAA9AA|mwi2mwu5n2rjztrmnja1yzk1zj|
|AAA9AAA9AAA9A9A9AAAAAAA9AA|mtu2yju5zwu0m2i1ztfhmju0mm|
|AAA9AAA9AAA9A9AAAAAAAAA9AA|nje4owy5ntg1m2mznmfiztm0zg|
|AAA9AAA9AAA9AAA9A9A9AAAAAA|mzy3ota5ote1zmy2y2i5nwfizw|
|AAA9AAA9AAA9AAA9AAA9AAA9AA|ntc2ytu2zdi0yzu1mgm4nwi1zm|
|AAA9AAA9AAA9AAA9AAA9AAAAAA|zjq3nwm5mmm0yjk2zdg3zdbhzm|
|AAA9AAA9AAA9AAA9AAAAAAA9AA|mdu4ote3zdq4ndq3odjknzg0mt|
|AAA9AAA9AAA9AAA9AAAAAAA9AA|mjc0zte4odm2njm2zwnlzdk4zj|
|AAA9AAA9AAA9AAA9AAAAAAAAAA|nzq1ngq5nzu3ngq1mzczzjgzmj|
|AAA9AAA9AAA9AAAAAAA9AAAAAA|odu5mdu0ywi5njqxogi3mzewnt|
|AAA9AAA9AAA9AAAAAAAAAAA9AA|yme1mjy0nmi2njzhzwnhnju4mj|
|AAA9AAA9AAA9AAAAAAAAAAAAAA|mwm2yza5mda0ntdiyjgymjbjow|
|AAA9AAA9AAA9AAAAAAAAAAAAAA|nge5ywe2ota0zwuzmzcyyjflnd|
|AAA9AAA9AAA9AAAAAAAAAAAAAA|njk3ntk5mge5odkwyjhindhhnw|
+--------------------------+--------------------------+
only showing top 50 rows

 VALUE SHAPES — spend_id
+------------------------------------+-----+
|shape                               |count|
+------------------------------------+-----+
|99A99AA9-9999-9A9A-AAA9-99A999AA9A99|1    |
|999AA999-999A-9AAA-9A9A-9999999A9A9A|1    |
|999A999A-9999-9999-A999-99999999AA9A|1    |
|9999A999-A9A9-9999-99A9-9AAAA99AAAAA|1    |
|AAA99A99-9AA9-9999-A9A9-9999AAAA999A|1    |
|A99AA999-9AAA-9999-A99A-9AA99A99999A|1    |
|9AAA9AA9-A9AA-9A99-A999-9999A9A999A9|1    |
|99AAAAA9-A9AA-9A99-AAAA-99999A9A99AA|1    |
|9A99AA99-AA9A-99A9-99A9-A99999A9A999|1    |
|A99AAA99-99AA-9A9A-9999-AA9A9A99AAA9|1    |
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
|AAAAA   |email       |
|AAAAA   |email       |
|AAAAA   |email       |
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
|9999.99|296  |
|999.99 |69   |
+-------+-----+


 SAMPLE VALUES — spend
+-------+------------+
|shape  |sample_value|
+-------+------------+
|999.99 |101.50      |
|999.99 |113.35      |
|999.99 |114.47      |
|9999.99|1007.12     |
|9999.99|1039.84     |
|9999.99|1060.00     |
+-------+------------+


 Discovery complete for mkt_silver_marketing_cost — scanned 365 rows

====================================================================================================
 DISCOVERING TABLE: mkt_silver_promotions
====================================================================================================

 SCHEMA
root
 |-- promotion_sk: string (nullable = true)
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


 TOTAL ROWS: 500

 NULL COUNTS
+------------+--------------+------------+----------+--------+----------+----------------+-----------------+---------+------------+----------+-------------+
|promotion_sk|promotion_code|discount_pct|valid_from|valid_to|valid_days|promotion_status|is_invalid_window|is_active|is_scheduled|is_expired|dw_created_at|
+------------+--------------+------------+----------+--------+----------+----------------+-----------------+---------+------------+----------+-------------+
|0           |0             |0           |0         |0       |0         |0               |0                |0        |0           |0         |0            |
+------------+--------------+------------+----------+--------+----------+----------------+-----------------+---------+------------+----------+-------------+


 VALUE SHAPES — promotion_sk
+--------------------------+-----+
|shape                     |count|
+--------------------------+-----+
|AAAAAAAAAAAAAAAAAAAAAAAAAA|20   |
|AAAAAAAAAAA9AAAAAAAAAAAAAA|15   |
|AAAAAAA9AAAAAAAAAAAAAAAAAA|12   |
|AAA9AAAAAAAAAAAAAAAAAAAAAA|12   |
|AAAAAAAAAAA9AAAAAAA9AAAAAA|11   |
|AAAAAAAAAAAAAAAAAAA9AAAAAA|11   |
|AAAAAAA9AAAAAAA9AAAAAAAAAA|9    |
|AAAAAAA9AAA9AAAAAAAAAAAAAA|9    |
|AAAAAAAAAAA9AAA9AAAAAAAAAA|9    |
|AAAAAAAAAAAAAAAAAAAAAAA9AA|9    |
+--------------------------+-----+


 SAMPLE VALUES — promotion_sk
+--------------------------+--------------------------+
|shape                     |sample_value              |
+--------------------------+--------------------------+
|A9A9AAA9AAA9AAA9AAAAAAAAAA|n2y2zmy2mdu1ndc3owizmtczzd|
|A9A9AAA9AAA9AAAAAAA9AAA9AA|m2u1yza5yta4mdnkmzu0zwi3nm|
|A9A9AAA9AAAAAAAAAAA9AAAAAA|y2m2mjq0otdhowzmzgi0ytbmyz|
|A9A9AAA9AAAAAAAAAAAAA9AAAA|y2u1mjg4zjrinjhmothmn2uxym|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|m2u5ntq2zdewzdqzowrmoda3zd|
|A9A9AAA9AAAAAAAAAAAAAAA9AA|y2u5mju1mwiwogexzgzjogq4yw|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|n2e3zmm4mwyynjnkngyxzdcxnt|
|A9A9AAA9AAAAAAAAAAAAAAAAAA|y2e0owe4ztfjyjgxzjayngrlnt|
|A9A9AAAAAAA9A9AAAAAAAAA9AA|y2e3ywzjmwq5m2rknddjmtg4nm|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2e0mdzjzju0nwu2mmm1mwyznd|
|A9A9AAAAAAA9AAA9AAA9AAAAAA|n2u5ywywzjc0ndy5nju0yzlkng|
|A9A9AAAAAAA9AAAAAAAAAAA9AA|m2e1ztrlotk4ymewnmuzzmy5yt|
|A9A9AAAAAAAAA9A9AAA9A9A9AA|m2y0zjcxnwfim2m1ndm2m2m0od|
|A9A9AAAAAAAAA9AAA9AAAAAAAA|y2i4zwixnmyxy2qwn2vjythknz|
|A9A9AAAAAAAAAAAAAAAAAAA9A9|y2q5mwuwndviyzgwmduwzgu4n2|
|A9AAA9A9AAA9AAAAAAAAAAAAAA|y2jjn2y5ymm5mgrkotazywjlmg|
|A9AAA9AAAAA9AAA9AAAAAAA9AA|m2nmy2nhyze0otk3njqynda0zj|
|A9AAA9AAAAAAAAA9AAAAAAA9AA|m2fhm2rkowzjmza4zmixyja2nd|
|A9AAAAA9AAA9A9A9AAA9AAA9AA|n2uyyzk0nzi3m2u2mti0yjg1nd|
|A9AAAAA9AAA9AAA9AAAAAAA9AA|y2jkzdq0zjg2mtc2ytnhmme1ow|
|A9AAAAA9AAA9AAAAAAAAAAA9AA|m2rintg1otq2mmrlnwezztq4zd|
|A9AAAAA9AAA9AAAAAAAAAAA9AA|y2nmmjc5zdi2zjdhzwrlodk4mw|
|A9AAAAA9AAAAAAA9A9AAAAAAAA|y2zhotq3nzmwmwq1y2zjmjqwnz|
|A9AAAAA9AAAAAAA9AAA9AAAAAA|y2fmodk4ztizody2owq1mguwot|
|A9AAAAA9AAAAAAAAAAAAAAAAAA|n2eyyte3zdjkndlhntexmtdinm|
|A9AAAAAAA9AAAAA9AAAAAAAAAA|y2uxztbkm2ixotm0mdfizjfing|
|A9AAAAAAAAA9AAAAAAAAAAAAAA|n2vkngqyoda4nwmzodlmztewod|
|A9AAAAAAAAAAA9AAAAAAAAA9AA|n2fimjyyytgwy2mwnmuxogm4zj|
|A9AAAAAAAAAAA9AAAAAAAAAAAA|y2njzdhkodkxm2zhyjrmmtawzj|
|A9AAAAAAAAAAAAA9A9AAAAAAAA|m2nhmzyxytjjotk4m2jjmjvhmm|
|A9AAAAAAAAAAAAA9AAAAAAAAAA|m2viodzjmtawyjc1ytaxmjdjzg|
|A9AAAAAAAAAAAAA9AAAAAAAAAA|n2njmdqymjrhmdm0mtqzytywyj|
|A9AAAAAAAAAAAAA9AAAAAAAAAA|y2izndcxyjaynmq2zwiwzgrhmj|
|A9AAAAAAAAAAAAAAAAA9AAAAAA|n2fmmtnlmmqymjjlzwi5mtnmmz|
|A9AAAAAAAAAAAAAAAAA9AAAAAA|n2nhngfmyzvlntkxyjk0nmfhzd|
|A9AAAAAAAAAAAAAAAAA9AAAAAA|y2fkndcymjhiogmzntu5ntjhzd|
|A9AAAAAAAAAAAAAAAAAAAAA9AA|n2jjotvkzwrizwqwnwfmmte0zm|
|A9AAAAAAAAAAAAAAAAAAAAA9AA|n2yxyzexmtdizdlkyjazmzk1mz|
|AAA9A9A9A9AAAAA9AAAAAAAAAA|zmy2y2m2y2exmtc0mmexyzyyyw|
|AAA9A9A9AAA9AAAAAAA9AAAAAA|mmi3y2e2zme4zmfimdk5mmnjzj|
|AAA9A9A9AAA9AAAAAAAAAAA9AA|mwm5n2m2mzi3ndhizjjindk2yw|
|AAA9A9A9AAAAAAAAAAAAA9AAAA|yzq1m2m3njuwmzawzthmm2flnd|
|AAA9A9A9AAAAAAAAAAAAAAAAAA|mgu0y2u5mjnlmteyythintrknt|
|AAA9A9A9AAAAAAAAAAAAAAAAAA|mjq4n2e0nmvjztzimgywotixmd|
|AAA9A9AAA9AAAAAAAAAAA9AAAA|ytc2m2exy2njnzmxnmzim2nmyt|
|AAA9A9AAAAA9A9AAAAA9AAAAAA|mzm1m2zizmm0y2fkyzg4mjjmnw|
|AAA9A9AAAAA9AAA9AAA9AAAAAA|zjg2y2uzymu2nge1zji4mgzknd|
|AAA9A9AAAAA9AAA9AAAAAAAAAA|zdg1n2viyjk3yju3ztizzdmznj|
|AAA9A9AAAAA9AAA9AAAAAAAAAA|zmy2n2vlzjg2zmi0mwyyotzhng|
|AAA9A9AAAAA9AAAAAAA9AAAAAA|mjk2m2rmytq3ymiznwq0mjzmzm|
+--------------------------+--------------------------+
only showing top 50 rows

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


 VALUE SHAPES — valid_from
+-------------------+-----+
|shape              |count|
+-------------------+-----+
|9999-99-99 99:99:99|500  |
+-------------------+-----+


 SAMPLE VALUES — valid_from
+-------------------+-------------------+
|shape              |sample_value       |
+-------------------+-------------------+
|9999-99-99 99:99:99|2024-07-15 14:55:18|
|9999-99-99 99:99:99|2024-07-16 21:24:03|
|9999-99-99 99:99:99|2024-07-18 02:58:37|
+-------------------+-------------------+


 VALUE SHAPES — valid_to
+-------------------+-----+
|shape              |count|
+-------------------+-----+
|9999-99-99 99:99:99|500  |
+-------------------+-----+


 SAMPLE VALUES — valid_to
+-------------------+-------------------+
|shape              |sample_value       |
+-------------------+-------------------+
|9999-99-99 99:99:99|2025-10-08 14:58:04|
|9999-99-99 99:99:99|2025-10-08 22:30:33|
|9999-99-99 99:99:99|2025-10-09 01:36:26|
+-------------------+-------------------+


 VALUE SHAPES — promotion_status
+-------+-----+
|shape  |count|
+-------+-----+
|AAAAAAA|500  |
+-------+-----+


 SAMPLE VALUES — promotion_status
+-------+------------+
|shape  |sample_value|
+-------+------------+
|AAAAAAA|expired     |
|AAAAAAA|expired     |
|AAAAAAA|expired     |
+-------+------------+


 Discovery complete for mkt_silver_promotions — scanned 500 rows

 All table discovery completed
```

# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-12 13:27:42 UTC

```text

 Discovered 1 tables:
  - mkt_bronze_marketing_attribution

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
|99999999-9A99-99A9-99A9-999A9A9AAA99|2    |
|9AA99A99-9999-9AAA-AA9A-9A9A999999A9|2    |
|99999999-9999-9AA9-9999-A9A99AAA9999|2    |
|99A999AA-9999-99A9-9A99-9A9AA9AA9999|2    |
|9999A999-99A9-9999-9999-999A9A9999A9|2    |
|999A99A9-A99A-9999-9999-9999999A9999|2    |
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

 All table discovery completed
```

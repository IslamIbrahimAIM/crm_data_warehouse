# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-07 14:10:16 UTC

```text

 Discovered 1 tables:
  - crm_silver_geo

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

 All table discovery completed
```

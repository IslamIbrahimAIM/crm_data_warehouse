# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-07 14:30:33 UTC

```text

 Discovered 1 tables:
  - crm_bronze_users

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

 All table discovery completed
```

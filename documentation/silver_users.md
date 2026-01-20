# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-07 18:38:02 UTC

```text

 Discovered 1 tables:
  - crm_silver_users

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

 All table discovery completed
```

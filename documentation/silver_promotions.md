# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-08 10:48:38 UTC

```text

 Discovered 1 tables:
  - mkt_silver_promotions

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

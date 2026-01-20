# Table Discovery Report

Database: washit_dw
Table pattern: %_bronze_%
Generated: 2026-01-09 07:25:20 UTC

```text

 Discovered 1 tables:
  - crm_silver_order_items

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

 All table discovery completed
```

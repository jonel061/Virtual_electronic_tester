

from flask import request
import sqlite3


def Test_teorie():
    if request.method == 'GET':
        connection = sqlite3.connect('identifier.sqlite')
        # print("Opened database successfully")
        cursor = connection.cursor()
        # intrebare 1
        intrebare1 = ("select intrebare from test_teorie where id='1' ")
        result1 = cursor.execute(intrebare1)
        result1 = result1.fetchall()[0][0]
        # intrebare 1 raspuns1
        intrebare1_raspuns1 = ("select raspuns1 from test_teorie where id='1'")
        result1_raspuns1 = cursor.execute(intrebare1_raspuns1)
        result1_raspuns1 = result1_raspuns1.fetchall()[0][0]
        # intrebare 1 raspuns 2
        intrebare1_raspuns2 = ("select raspuns2 from test_teorie where id='1'")
        result1_raspuns2 = cursor.execute(intrebare1_raspuns2)
        result1_raspuns2 = result1_raspuns2.fetchall()[0][0]
        # intrebare 1 raspuns 3
        intrebare1_raspuns3 = ("select raspuns3 from test_teorie where id='1'")
        result1_raspuns3 = cursor.execute(intrebare1_raspuns3)
        result1_raspuns3 = result1_raspuns3.fetchall()[0][0]
        # intrebare 1 raspuns 4
        intrebare1_raspuns4 = ("select raspuns4 from test_teorie where id='1'")
        result1_raspuns4 = cursor.execute(intrebare1_raspuns4)
        result1_raspuns4 = result1_raspuns4.fetchall()[0][0]
        # intrebarea 2
        intrebare2 = ("select intrebare from test_teorie where id='2' ")
        result2 = cursor.execute(intrebare2)
        result2 = result2.fetchall()[0][0]
        # intrebarea 2 raspuns 1
        intrebare2_raspuns1 = ("select raspuns1 from test_teorie where id='2' ")
        result2_raspuns1 = cursor.execute(intrebare2_raspuns1)
        result2_raspuns1 = result2_raspuns1.fetchall()[0][0]
        # intrebarea 2 raspuns 2
        intrebare2_raspuns2 = ("select raspuns2 from test_teorie where id='2' ")
        result2_raspuns2 = cursor.execute(intrebare2_raspuns2)
        result2_raspuns2 = result2_raspuns2.fetchall()[0][0]
        # intrebarea 2 raspuns 3
        intrebare2_raspuns3 = ("select raspuns3 from test_teorie where id='2' ")
        result2_raspuns3 = cursor.execute(intrebare2_raspuns3)
        result2_raspuns3 = result2_raspuns3.fetchall()[0][0]
        # intrebarea 2 raspuns 4
        intrebare2_raspuns4 = ("select raspuns4 from test_teorie where id='2' ")
        result2_raspuns4 = cursor.execute(intrebare2_raspuns4)
        result2_raspuns4 = result2_raspuns4.fetchall()[0][0]
        # intrebare 3
        intrebare3 = ("select intrebare from test_teorie where id='3' ")
        result3 = cursor.execute(intrebare3)
        result3 = result3.fetchall()[0][0]
        # intrebarea 3 raspuns 1
        intrebare3_raspuns1 = ("select raspuns1 from test_teorie where id='3' ")
        result3_raspuns1 = cursor.execute(intrebare3_raspuns1)
        result3_raspuns1 = result3_raspuns1.fetchall()[0][0]
        # intrebarea 3 raspuns 2
        intrebare3_raspuns2 = ("select raspuns2 from test_teorie where id='3' ")
        result3_raspuns2 = cursor.execute(intrebare3_raspuns2)
        result3_raspuns2 = result3_raspuns2.fetchall()[0][0]
        # intrebarea 3 raspuns 3
        intrebare3_raspuns3 = ("select raspuns3 from test_teorie where id='3' ")
        result3_raspuns3 = cursor.execute(intrebare3_raspuns3)
        result3_raspuns3 = result3_raspuns3.fetchall()[0][0]
        # intrebarea 3 raspuns 4
        intrebare3_raspuns4 = ("select raspuns4 from test_teorie where id='3' ")
        result3_raspuns4 = cursor.execute(intrebare3_raspuns4)
        result3_raspuns4 = result3_raspuns4.fetchall()[0][0]
        # intrebare 4
        intrebare4 = ("select intrebare from test_teorie where id='4' ")
        result4 = cursor.execute(intrebare4)
        result4 = result4.fetchall()[0][0]
        # intrebare 4 raspuns1
        intrebare4_raspuns1 = ("select raspuns1 from test_teorie where id='4' ")
        result4_raspuns1= cursor.execute(intrebare4_raspuns1)
        result4_raspuns1 = result4_raspuns1.fetchall()[0][0]
        # intrebare 4 raspuns2
        intrebare4_raspuns2 = ("select raspuns2 from test_teorie where id='4' ")
        result4_raspuns2 = cursor.execute(intrebare4_raspuns2)
        result4_raspuns2 = result4_raspuns2.fetchall()[0][0]
        # intrebare 4 raspuns3
        intrebare4_raspuns3 = ("select raspuns3 from test_teorie where id='4' ")
        result4_raspuns3 = cursor.execute(intrebare4_raspuns3)
        result4_raspuns3 = result4_raspuns3.fetchall()[0][0]
        # intrebare 4 raspuns 4
        intrebare4_raspuns4 = ("select raspuns4 from test_teorie where id='4' ")
        result4_raspuns4 = cursor.execute(intrebare4_raspuns4)
        result4_raspuns4 = result4_raspuns4.fetchall()[0][0]
        # intrebare 5
        intrebare5 = ("select intrebare from test_teorie where id='5' ")
        result5 = cursor.execute(intrebare5)
        result5 = result5.fetchall()[0][0]
        # intrebare 5 raspuns 1
        intrebare5_raspuns1 = ("select raspuns1 from test_teorie where id='5' ")
        result5_raspuns1 = cursor.execute(intrebare5_raspuns1)
        result5_raspuns1= result5_raspuns1.fetchall()[0][0]
        # intrebare 5 raspuns 2
        intrebare5_raspuns2 = ("select raspuns2 from test_teorie where id='5' ")
        result5_raspuns2 = cursor.execute(intrebare5_raspuns2)
        result5_raspuns2 = result5_raspuns2.fetchall()[0][0]
        # intrebare 5 raspuns 3
        intrebare5_raspuns3 = ("select raspuns3 from test_teorie where id='5' ")
        result5_raspuns3 = cursor.execute(intrebare5_raspuns3)
        result5_raspuns3 = result5_raspuns3.fetchall()[0][0]
        # intrebare 5 raspuns 4
        intrebare5_raspuns4 = ("select raspuns4 from test_teorie where id='5' ")
        result5_raspuns4 = cursor.execute(intrebare5_raspuns4)
        result5_raspuns4 = result5_raspuns4.fetchall()[0][0]
        # intrebare 6
        intrebare6 = ("select intrebare from test_teorie where id='6' ")
        result6 = cursor.execute(intrebare6)
        result6 = result6.fetchall()[0][0]
        # intrebare 6 raspuns 1
        intrebare6_raspuns1 = ("select raspuns1 from test_teorie where id='6' ")
        result6_raspuns1 = cursor.execute(intrebare6_raspuns1)
        result6_raspuns1 = result6_raspuns1.fetchall()[0][0]
        # intrebare 6 raspuns 2
        intrebare6_raspuns2 = ("select raspuns2 from test_teorie where id='6' ")
        result6_raspuns2 = cursor.execute(intrebare6_raspuns2)
        result6_raspuns2 = result6_raspuns2.fetchall()[0][0]
        # intrebare 6 raspuns 3
        intrebare6_raspuns3 = ("select raspuns3 from test_teorie where id='6' ")
        result6_raspuns3 = cursor.execute(intrebare6_raspuns3)
        result6_raspuns3 = result6_raspuns3.fetchall()[0][0]
        # intrebare 6 raspuns 4
        intrebare6_raspuns4 = ("select raspuns4 from test_teorie where id='6' ")
        result6_raspuns4 = cursor.execute(intrebare6_raspuns4)
        result6_raspuns4 = result6_raspuns4.fetchall()[0][0]
        # intrebare 7
        intrebare7 = ("select intrebare from test_teorie where id='7' ")
        result7 = cursor.execute(intrebare7)
        result7 = result7.fetchall()[0][0]
        # intrebare 7 raspuns 1
        intrebare7_raspuns1 = ("select raspuns1 from test_teorie where id='7' ")
        result7_raspuns1 = cursor.execute(intrebare7_raspuns1)
        result7_raspuns1 = result7_raspuns1.fetchall()[0][0]
        # intrebare 7 raspuns 2
        intrebare7_raspuns2 = ("select raspuns2 from test_teorie where id='7' ")
        result7_raspuns2 = cursor.execute(intrebare7_raspuns2)
        result7_raspuns2 = result7_raspuns2.fetchall()[0][0]
        # intrebare 7 raspuns 3
        intrebare7_raspuns3 = ("select raspuns3 from test_teorie where id='7' ")
        result7_raspuns3 = cursor.execute(intrebare7_raspuns3)
        result7_raspuns3 = result7_raspuns3.fetchall()[0][0]
        # intrebare 7 raspuns 4
        intrebare7_raspuns4 = ("select raspuns4 from test_teorie where id='7' ")
        result7_raspuns4 = cursor.execute(intrebare7_raspuns4)
        result7_raspuns4 = result7_raspuns4.fetchall()[0][0]
        # intrebare 8
        intrebare8 = ("select intrebare from test_teorie where id='8' ")
        result8 = cursor.execute(intrebare8)
        result8 = result8.fetchall()[0][0]
        # intrebare 8 raspuns 1
        intrebare8_raspuns1 = ("select raspuns1 from test_teorie where id='8' ")
        result8_raspuns1 = cursor.execute(intrebare8_raspuns1)
        result8_raspuns1 = result8_raspuns1.fetchall()[0][0]
        # intrebare 8 raspuns 2
        intrebare8_raspuns2 = ("select raspuns2 from test_teorie where id='8' ")
        result8_raspuns2 = cursor.execute(intrebare8_raspuns2)
        result8_raspuns2 = result8_raspuns2.fetchall()[0][0]
        # intrebare 8 raspuns 3
        intrebare8_raspuns3 = ("select raspuns3 from test_teorie where id='8' ")
        result8_raspuns3 = cursor.execute(intrebare8_raspuns3)
        result8_raspuns3 = result8_raspuns3.fetchall()[0][0]
        # intrebare 8 raspuns 4
        intrebare8_raspuns4 = ("select raspuns4 from test_teorie where id='8' ")
        result8_raspuns4 = cursor.execute(intrebare8_raspuns4)
        result8_raspuns4 = result8_raspuns4.fetchall()[0][0]
        # intrebare 9
        intrebare9 = ("select intrebare from test_teorie where id='9' ")
        result9 = cursor.execute(intrebare9)
        result9 = result9.fetchall()[0][0]
        # intrebare 9 raspuns 1
        intrebare9_raspuns1 = ("select raspuns1 from test_teorie where id='9' ")
        result9_raspuns1 = cursor.execute(intrebare9_raspuns1)
        result9_raspuns1 = result9_raspuns1.fetchall()[0][0]
        # intrebare 9 raspuns 2
        intrebare9_raspuns2 = ("select raspuns2 from test_teorie where id='9' ")
        result9_raspuns2 = cursor.execute(intrebare9_raspuns2)
        result9_raspuns2 = result9_raspuns2.fetchall()[0][0]
        # intrebare 9 raspuns 3
        intrebare9_raspuns3 = ("select raspuns3 from test_teorie where id='9' ")
        result9_raspuns3 = cursor.execute(intrebare9_raspuns3)
        result9_raspuns3 = result9_raspuns3.fetchall()[0][0]
        # intrebare 9 raspuns 4
        intrebare9_raspuns4 = ("select raspuns4 from test_teorie where id='9' ")
        result9_raspuns4 = cursor.execute(intrebare9_raspuns4)
        result9_raspuns4 = result9_raspuns4.fetchall()[0][0]
        # intrebare 10
        intrebare10 = ("select intrebare from test_teorie where id='10' ")
        result10 = cursor.execute(intrebare10)
        result10 = result10.fetchall()[0][0]
        # intrebare 10 raspuns 1
        intrebare10_raspuns1 = ("select raspuns1 from test_teorie where id='10' ")
        result10_raspuns1 = cursor.execute(intrebare10_raspuns1)
        result10_raspuns1 = result10_raspuns1.fetchall()[0][0]
        # intrebare 10 raspuns 2
        intrebare10_raspuns2 = ("select raspuns2 from test_teorie where id='10' ")
        result10_raspuns2 = cursor.execute(intrebare10_raspuns2)
        result10_raspuns2 = result10_raspuns2.fetchall()[0][0]
        # intrebare 10 raspuns 3
        intrebare10_raspuns3 = ("select raspuns3 from test_teorie where id='10' ")
        result10_raspuns3 = cursor.execute(intrebare10_raspuns3)
        result10_raspuns3 = result10_raspuns3.fetchall()[0][0]
        # intrebare 10 raspuns 4
        intrebare10_raspuns4 = ("select raspuns4 from test_teorie where id='10' ")
        result10_raspuns4 = cursor.execute(intrebare10_raspuns4)
        result10_raspuns4 = result10_raspuns4.fetchall()[0][0]
        # intrebare 11
        intrebare11 = ("select intrebare from test_teorie where id='11' ")
        result11 = cursor.execute(intrebare11)
        result11 = result11.fetchall()[0][0]
        # intrebare 11 raspuns 1
        intrebare11_raspuns1 = ("select raspuns1 from test_teorie where id='11' ")
        result11_raspuns1 = cursor.execute(intrebare11_raspuns1)
        result11_raspuns1 = result11_raspuns1.fetchall()[0][0]
        # intrebare 11 raspuns 2
        intrebare11_raspuns2 = ("select raspuns2 from test_teorie where id='11' ")
        result11_raspuns2 = cursor.execute(intrebare11_raspuns2)
        result11_raspuns2 = result11_raspuns2.fetchall()[0][0]
        # intrebare 11 raspuns 3
        intrebare11_raspuns3 = ("select raspuns3 from test_teorie where id='11' ")
        result11_raspuns3 = cursor.execute(intrebare11_raspuns3)
        result11_raspuns3 = result11_raspuns3.fetchall()[0][0]
        # intrebare 11 raspuns 4
        intrebare11_raspuns4 = ("select raspuns4 from test_teorie where id='11' ")
        result11_raspuns4 = cursor.execute(intrebare11_raspuns4)
        result11_raspuns4 = result11_raspuns4.fetchall()[0][0]
        # intrebare 12
        intrebare12= ("select intrebare from test_teorie where id='12' ")
        result12 = cursor.execute(intrebare12)
        result12 = result12.fetchall()[0][0]
        # intrebare 12 raspuns 1
        intrebare12_raspuns1 = ("select raspuns1 from test_teorie where id='12' ")
        result12_raspuns1 = cursor.execute(intrebare12_raspuns1)
        result12_raspuns1 = result12_raspuns1.fetchall()[0][0]
        # intrebare 12 raspuns 2
        intrebare12_raspuns2 = ("select raspuns2 from test_teorie where id='12' ")
        result12_raspuns2 = cursor.execute(intrebare12_raspuns2)
        result12_raspuns2 = result12_raspuns2.fetchall()[0][0]
        # intrebare 12 raspuns 3
        intrebare12_raspuns3 = ("select raspuns3 from test_teorie where id='12' ")
        result12_raspuns3 = cursor.execute(intrebare12_raspuns3)
        result12_raspuns3 = result12_raspuns3.fetchall()[0][0]
        # intrebare 12 raspuns 4
        intrebare12_raspuns4 = ("select raspuns4 from test_teorie where id='12' ")
        result12_raspuns4 = cursor.execute(intrebare12_raspuns4)
        result12_raspuns4 = result12_raspuns4.fetchall()[0][0]
        # intrebare 12 raspuns 5
        intrebare12_raspuns5 = ("select raspuns5 from test_teorie where id='12' ")
        result12_raspuns5 = cursor.execute(intrebare12_raspuns5)
        result12_raspuns5 = result12_raspuns5.fetchall()[0][0]
        # intrebare 12 raspuns 6
        intrebare12_raspuns6 = ("select raspuns6 from test_teorie where id='12' ")
        result12_raspuns6 = cursor.execute(intrebare12_raspuns6)
        result12_raspuns6 = result12_raspuns6.fetchall()[0][0]
        # intrebare 13
        intrebare13 = ("select intrebare from test_teorie where id='13' ")
        result13 = cursor.execute(intrebare13)
        result13 = result13.fetchall()[0][0]
        # intrebare 13 raspuns 1
        intrebare13_raspuns1 = ("select raspuns1 from test_teorie where id='13' ")
        result13_raspuns1 = cursor.execute(intrebare13_raspuns1)
        result13_raspuns1 = result13_raspuns1.fetchall()[0][0]
        # intrebare 13 raspuns 2
        intrebare13_raspuns2 = ("select raspuns2 from test_teorie where id='13' ")
        result13_raspuns2 = cursor.execute(intrebare13_raspuns2)
        result13_raspuns2 = result13_raspuns2.fetchall()[0][0]
        # intrebare 13 raspuns 3
        intrebare13_raspuns3 = ("select raspuns3 from test_teorie where id='13' ")
        result13_raspuns3 = cursor.execute(intrebare13_raspuns3)
        result13_raspuns3 = result13_raspuns3.fetchall()[0][0]
        # intrebare 13 raspuns 4
        intrebare13_raspuns4 = ("select raspuns4 from test_teorie where id='13' ")
        result13_raspuns4 = cursor.execute(intrebare13_raspuns4)
        result13_raspuns4 = result13_raspuns4.fetchall()[0][0]
        # intrebare 14
        intrebare14 = ("select intrebare from test_teorie where id='14' ")
        result14 = cursor.execute(intrebare14)
        result14= result14.fetchall()[0][0]
        # intrebare 14 raspuns 1
        intrebare14_raspuns1 = ("select raspuns1 from test_teorie where id='14' ")
        result14_raspuns1 = cursor.execute(intrebare14_raspuns1)
        result14_raspuns1 = result14_raspuns1.fetchall()[0][0]
        # intrebare 14 raspuns 2
        intrebare14_raspuns2 = ("select raspuns2 from test_teorie where id='14' ")
        result14_raspuns2 = cursor.execute(intrebare14_raspuns2)
        result14_raspuns2 = result14_raspuns2.fetchall()[0][0]
        # intrebare 14 raspuns 3
        intrebare14_raspuns3 = ("select raspuns3 from test_teorie where id='14' ")
        result14_raspuns3 = cursor.execute(intrebare14_raspuns3)
        result14_raspuns3 = result14_raspuns3.fetchall()[0][0]
        # intrebare 13 raspuns 4
        intrebare14_raspuns4 = ("select raspuns4 from test_teorie where id='14' ")
        result14_raspuns4 = cursor.execute(intrebare14_raspuns4)
        result14_raspuns4 = result14_raspuns4.fetchall()[0][0]

        return result1,result1_raspuns1,result1_raspuns2,result1_raspuns3,result1_raspuns4 \
             , result2,result2_raspuns1,result2_raspuns2,result2_raspuns3,result2_raspuns4 \
             , result3,result3_raspuns1,result3_raspuns2,result3_raspuns3,result3_raspuns4 \
             , result4,result4_raspuns1,result4_raspuns2,result4_raspuns3,result4_raspuns4 \
             , result5,result5_raspuns1,result5_raspuns2,result5_raspuns3,result5_raspuns4 \
             , result6,result6_raspuns1,result6_raspuns2,result6_raspuns3,result6_raspuns4 \
             , result7,result7_raspuns1,result7_raspuns2,result7_raspuns3,result7_raspuns4 \
             , result8,result8_raspuns1,result8_raspuns2,result8_raspuns3,result8_raspuns4 \
             , result9,result9_raspuns1,result9_raspuns2,result9_raspuns3,result9_raspuns4 \
             , result10,result10_raspuns1,result10_raspuns2,result10_raspuns3,result10_raspuns4 \
             , result11, result11_raspuns1, result11_raspuns2, result11_raspuns3, result11_raspuns4 \
            , result12, result12_raspuns1, result12_raspuns2, result12_raspuns3, result12_raspuns4,result12_raspuns5,result12_raspuns6 \
            , result13, result13_raspuns1, result13_raspuns2, result13_raspuns3, result13_raspuns4 \
            , result14, result14_raspuns1, result14_raspuns2, result14_raspuns3, result14_raspuns4 \

from flask import Flask, render_template

import baze_de_date
from baze_de_date import *

# from Legea_Ohm import operation_result_din_OHM

app: Flask = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/Teoria')
def teoria():
    return render_template('Teoria/Teoria.html')


@app.route('/Resistor')
def Resistor():
    return render_template('Teoria/Resistor.html')


@app.route('/Condesator')
def Condesator():
    return render_template('Teoria/Condesator.html')


@app.route('/Inductor')
def Inductor():
    return render_template('Teoria/Inductor.html')


@app.route('/Curentul electric')
def Curentul():
    return render_template('Teoria/Curentul electric.html')


@app.route('/Tensiunea electrică')
def Tensiunea():
    return render_template('Teoria/Tensiune electrică.html')


@app.route('/Rezistența electrică')
def Rezistența():
    return render_template('Teoria/Rezistența electrică.html')


@app.route('/Puterea electrică')
def Puterea():
    return render_template('Teoria/Puterea electrică.html')


@app.route('/Legea lui Ohm')
def Legea_lui_Ohm():
    return render_template('Teoria/Legea lui Ohm.html')


@app.route('/Semiconductor')
def Semiconductor():
    return render_template('Teoria/Semiconductor.html')


@app.route('/Joncțiune PN')
def Joncțiune_PN():
    return render_template('Teoria/Joncțiune PN.html')


@app.route('/Dioda')
def Dioda():
    return render_template('Teoria/Dioda.html')


@app.route('/Porți logicii')
def Porți_logicii():
    return render_template('Teoria/Porți logicii.html')


@app.route('/Tranzistor')
def Tranzistor():
    return render_template('Teoria/Tranzistor.html')


@app.route('/Amplificator')
def Amplificator():
    return render_template('Teoria/Amplificator.html')


@app.route('/Calculatoare')
def Calculatoare():
    return render_template('Calculatoare/Menu calculatoare.html')


@app.route('/Home_Test_teorie')
def Home_Test_teorie():
    return render_template('Test teorie/Home_test_teorie.html')


# transmit informatile din database  sqlite3 paginii test teorie
@app.route('/Test_teorie', methods=['GET', 'POST'])
def apelare_bd():
    i1, i1r1, i1r2, i1r3, i1r4, \
    i2, i2r1, i2r2, i2r3, i2r4, \
    i3, i3r1, i3r2, i3r3, i3r4, \
    i4, i4r1, i4r2, i4r3, i4r4, \
    i5, i5r1, i5r2, i5r3, i5r4, \
    i6, i6r1, i6r2, i6r3, i6r4, \
    i7, i7r1, i7r2, i7r3, i7r4, \
    i8, i8r1, i8r2, i8r3, i8r4, \
    i9, i9r1, i9r2, i9r3, i9r4, \
    i10, i10r1, i10r2, i10r3, i10r4, \
    i11, i11r1, i11r2, i11r3, i11r4, \
    i12, i12r1, i12r2, i12r3, i12r4, i12r5, i12r6, \
    i13, i13r1, i13r2, i13r3, i13r4, \
    i14, i14r1, i14r2, i14r3, i14r4 \
        = baze_de_date.Test_teorie()

    return render_template('Test teorie/Test teorie.html'
                           , intrebare1=i1, intrebare1_raspuns1=i1r1, intrebare1_raspuns2=i1r2,
                           intrebare1_raspuns3=i1r3, intrebare1_raspuns4=i1r4
                           , intrebare2=i2, intrebare2_raspuns1=i2r1, intrebare2_raspuns2=i2r2,
                           intrebare2_raspuns3=i2r3, intrebare2_raspuns4=i2r4
                           , intrebare3=i3, intrebare3_raspuns1=i3r1, intrebare3_raspuns2=i3r2,
                           intrebare3_raspuns3=i3r3, intrebare3_raspuns4=i3r4
                           , intrebare4=i4, intrebare4_raspuns1=i4r1, intrebare4_raspuns2=i4r2,
                           intrebare4_raspuns3=i4r3, intrebare4_raspuns4=i4r4
                           , intrebare5=i5, intrebare5_raspuns1=i5r1, intrebare5_raspuns2=i5r2,
                           intrebare5_raspuns3=i5r3, intrebare5_raspuns4=i5r4
                           , intrebare6=i6, intrebare6_raspuns1=i6r1, intrebare6_raspuns2=i6r2,
                           intrebare6_raspuns3=i6r3, intrebare6_raspuns4=i6r4
                           , intrebare7=i7, intrebare7_raspuns1=i7r1, intrebare7_raspuns2=i7r2,
                           intrebare7_raspuns3=i7r3, intrebare7_raspuns4=i7r4
                           , intrebare8=i8, intrebare8_raspuns1=i8r1, intrebare8_raspuns2=i8r2,
                           intrebare8_raspuns3=i8r3, intrebare8_raspuns4=i8r4
                           , intrebare9=i9, intrebare9_raspuns1=i9r1, intrebare9_raspuns2=i9r2,
                           intrebare9_raspuns3=i9r3, intrebare9_raspuns4=i9r4
                           , intrebare10=i10, intrebare10_raspuns1=i10r1, intrebare10_raspuns2=i10r2,
                           intrebare10_raspuns3=i10r3, intrebare10_raspuns4=i10r4
                           , intrebare11=i11, intrebare11_raspuns1=i11r1, intrebare11_raspuns2=i11r2,
                           intrebare11_raspuns3=i11r3, intrebare11_raspuns4=i11r4
                           , intrebare12=i12, intrebare12_raspuns1=i12r1, intrebare12_raspuns2=i12r2,
                           intrebare12_raspuns3=i12r3, intrebare12_raspuns4=i12r4, intrebare12_raspuns5=i12r5,
                           intrebare12_raspuns6=i12r6
                           , intrebare13=i13, intrebare13_raspuns1=i13r1, intrebare13_raspuns2=i13r2,
                           intrebare13_raspuns3=i13r3, intrebare13_raspuns4=i13r4
                           , intrebare14=i14, intrebare14_raspuns1=i14r1, intrebare14_raspuns2=i14r2,
                           intrebare14_raspuns3=i14r3, intrebare14_raspuns4=i14r4

                           )


@app.route('/Test_teorie_rezultat/', methods=['POST', 'GET'])
def Test_teorie_rezultat():
    # radio button valoarea # option = request.form['options']
    # check button # option = request.form.getlist('options')
    correct = 0
    incorect = 0
    nota = 0

    if request.method == 'POST':
        # conectare la baze de date
        connection = sqlite3.connect('identifier.sqlite')
        # print("Opened database successfully")
        cursor = connection.cursor()
        # extragem raspunsul corect pentru prima intrebare
        intrebare1_raspuns1 = ("select raspuns1 from test_teorie where id='1'")
        intrebare1_raspuns_corect = cursor.execute(intrebare1_raspuns1)
        intrebare1_raspuns_corect = intrebare1_raspuns_corect.fetchall()[0][0]

        # verificare raspuns1
        if request.form.getlist('Intrebarea1') and request.form['Intrebarea1'] == intrebare1_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # extragem raspunsurile  corecte pentru a doua intrebare
        intrebare2_raspuns1 = ("select raspuns1 from test_teorie where id='2' ")
        intrebare2_raspuns_corect_1 = cursor.execute(intrebare2_raspuns1)
        intrebare2_raspuns_corect_1 = intrebare2_raspuns_corect_1.fetchall()[0][0]
        # intrebarea 2 raspuns 2
        intrebare2_raspuns2 = ("select raspuns2 from test_teorie where id='2' ")
        intrebare2_raspuns_corect_2 = cursor.execute(intrebare2_raspuns2)
        intrebare2_raspuns_corect_2 = intrebare2_raspuns_corect_2.fetchall()[0][0]

        # intrebarea 2 raspuns 4
        intrebare2_raspuns4 = ("select raspuns4 from test_teorie where id='2' ")
        intrebare2_raspuns_corect_3 = cursor.execute(intrebare2_raspuns4)
        intrebare2_raspuns_corect_3 = intrebare2_raspuns_corect_3.fetchall()[0][0]
        # inserarea raspunsurilor intr-o lista
        raspuns_corect_intrebarea2 = [intrebare2_raspuns_corect_1, intrebare2_raspuns_corect_2,
                                      intrebare2_raspuns_corect_3]

        raspuns_corect_r2 = raspuns_corect_intrebarea2
        # verificare raspuns2
        intrebare2 = request.form.getlist('Intrebarea2')
        if (raspuns_corect_r2 == intrebare2):
            correct = correct + 1
        else:
            incorect = incorect + 1

        intrebare3_raspuns1 = ("select raspuns1 from test_teorie where id='3' ")
        intrebare3_raspuns_corect1 = cursor.execute(intrebare3_raspuns1)
        intrebare3_raspuns_corect1 = intrebare3_raspuns_corect1.fetchall()[0][0]
        intrebare3_raspuns3 = ("select raspuns3 from test_teorie where id='3' ")
        intrebare3_raspuns_corect2 = cursor.execute(intrebare3_raspuns3)
        intrebare3_raspuns_corect2 = intrebare3_raspuns_corect2.fetchall()[0][0]

        # inserarea raspunsurilor intr-o lista
        raspuns_corect_intrebarea3 = [intrebare3_raspuns_corect1, intrebare3_raspuns_corect2]

        # verificare raspuns3
        raspuns_corect_r3 = raspuns_corect_intrebarea3
        intrebare3 = request.form.getlist('Intrebarea3')
        if (raspuns_corect_r3 == intrebare3):
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 4 raspuns1
        intrebare4_raspuns1 = ("select raspuns1 from test_teorie where id='4' ")
        intrebare4_raspuns_corect1 = cursor.execute(intrebare4_raspuns1)
        intrebare4_raspuns_corect1 = intrebare4_raspuns_corect1.fetchall()[0][0]
        # intrebare 4 raspuns2
        intrebare4_raspuns2 = ("select raspuns2 from test_teorie where id='4' ")
        intrebare4_raspuns_corect2 = cursor.execute(intrebare4_raspuns2)
        intrebare4_raspuns_corect2 = intrebare4_raspuns_corect2.fetchall()[0][0]
        # intrebare 4 raspuns3
        intrebare4_raspuns3 = ("select raspuns3 from test_teorie where id='4' ")
        intrebare4_raspuns_corect3 = cursor.execute(intrebare4_raspuns3)
        intrebare4_raspuns_corect3 = intrebare4_raspuns_corect3.fetchall()[0][0]
        # intrebare 4 raspuns 4
        intrebare4_raspuns4 = ("select raspuns4 from test_teorie where id='4' ")
        intrebare4_raspuns_corect4 = cursor.execute(intrebare4_raspuns4)
        intrebare4_raspuns_corect4 = intrebare4_raspuns_corect4.fetchall()[0][0]

        # inserare in lista
        raspuns_corect_intrebarea4 = [intrebare4_raspuns_corect1, intrebare4_raspuns_corect2,
                                      intrebare4_raspuns_corect3, intrebare4_raspuns_corect4]

        # verificare raspuns4
        raspuns_corect_r4 = raspuns_corect_intrebarea4
        intrebare4 = request.form.getlist('Intrebarea4')
        if (raspuns_corect_r4 == intrebare4):
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 5 raspuns 2
        intrebare5_raspuns2 = ("select raspuns2 from test_teorie where id='5' ")
        intrebare5_raspuns_corect = cursor.execute(intrebare5_raspuns2)
        intrebare5_raspuns_corect = intrebare5_raspuns_corect.fetchall()[0][0]

        # verificare raspuns5
        if request.form.getlist('Intrebarea5') and request.form['Intrebarea5'] == intrebare5_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 6 raspuns 3
        intrebare6_raspuns3 = ("select raspuns3 from test_teorie where id='6' ")
        intrebare6_raspuns_corect = cursor.execute(intrebare6_raspuns3)
        intrebare6_raspuns_corect = intrebare6_raspuns_corect.fetchall()[0][0]

        # verificare raspuns6
        if request.form.getlist('Intrebarea6') and request.form['Intrebarea6'] == intrebare6_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # verificare raspuns7

        # intrebare 7 raspuns 1
        intrebare7_raspuns1 = ("select raspuns1 from test_teorie where id='7' ")
        intrebare7_raspuns_corect1 = cursor.execute(intrebare7_raspuns1)
        intrebare7_raspuns_corect1 = intrebare7_raspuns_corect1.fetchall()[0][0]
        # intrebare 7 raspuns 2
        intrebare7_raspuns2 = ("select raspuns2 from test_teorie where id='7' ")
        intrebare7_raspuns_corect2 = cursor.execute(intrebare7_raspuns2)
        intrebare7_raspuns_corect2 = intrebare7_raspuns_corect2.fetchall()[0][0]

        # inserez intr-o lista
        raspuns_corect_intrebarea7 = [intrebare7_raspuns_corect1, intrebare7_raspuns_corect2]

        raspuns_corect_r7 = raspuns_corect_intrebarea7
        intrebare7 = request.form.getlist('Intrebarea7')
        if (raspuns_corect_r7 == intrebare7):
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 8 raspuns 3
        intrebare8_raspuns3 = ("select raspuns3 from test_teorie where id='8' ")
        intrebare8_raspuns_corect = cursor.execute(intrebare8_raspuns3)
        intrebare8_raspuns_corect = intrebare8_raspuns_corect.fetchall()[0][0]

        # verificare raspuns8
        if request.form.getlist('Intrebarea8') and request.form['Intrebarea8'] == intrebare8_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 9 raspuns 1
        intrebare9_raspuns1 = ("select raspuns1 from test_teorie where id='9' ")
        intrebare9_raspuns_corect = cursor.execute(intrebare9_raspuns1)
        intrebare9_raspuns_corect = intrebare9_raspuns_corect.fetchall()[0][0]

        # verificare raspuns9
        if request.form.getlist('Intrebarea9') and request.form['Intrebarea9'] == intrebare9_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 10 raspuns 1
        intrebare10_raspuns1 = ("select raspuns1 from test_teorie where id='10' ")
        intrebare10_raspuns_corect1 = cursor.execute(intrebare10_raspuns1)
        intrebare10_raspuns_corect1 = intrebare10_raspuns_corect1.fetchall()[0][0]
        # intrebare 10 raspuns 3
        intrebare10_raspuns3 = ("select raspuns3 from test_teorie where id='10' ")
        intrebare10_raspuns_corect2 = cursor.execute(intrebare10_raspuns3)
        intrebare10_raspuns_corect2 = intrebare10_raspuns_corect2.fetchall()[0][0]
        # intrebare 10 raspuns 4
        intrebare10_raspuns4 = ("select raspuns4 from test_teorie where id='10' ")
        intrebare10_raspuns_corect3 = cursor.execute(intrebare10_raspuns4)
        intrebare10_raspuns_corect3 = intrebare10_raspuns_corect3.fetchall()[0][0]

        # inserez  intr-o lista

        raspuns_corect_intrebarea10 = [intrebare10_raspuns_corect1, intrebare10_raspuns_corect2,
                                       intrebare10_raspuns_corect3]

        # verificare raspuns10
        raspuns_corect_r10 = raspuns_corect_intrebarea10
        intrebare10 = request.form.getlist('Intrebarea10')
        if (raspuns_corect_r10 == intrebare10):
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 11 raspuns 1
        intrebare11_raspuns1 = ("select raspuns1 from test_teorie where id='11' ")
        intrebare11_raspuns_corect = cursor.execute(intrebare11_raspuns1)
        intrebare11_raspuns_corect = intrebare11_raspuns_corect.fetchall()[0][0]

        # verificare raspuns11
        if request.form.getlist('Intrebarea11') and request.form['Intrebarea11'] == intrebare11_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 12 raspuns 1
        intrebare12_raspuns1 = ("select raspuns1 from test_teorie where id='12' ")
        intrebare12_raspuns_corect1 = cursor.execute(intrebare12_raspuns1)
        intrebare12_raspuns_corect1 = intrebare12_raspuns_corect1.fetchall()[0][0]
        # intrebare 12 raspuns 2
        intrebare12_raspuns2 = ("select raspuns2 from test_teorie where id='12' ")
        intrebare12_raspuns_corect2 = cursor.execute(intrebare12_raspuns2)
        intrebare12_raspuns_corect2 = intrebare12_raspuns_corect2.fetchall()[0][0]
        # intrebare 12 raspuns 3
        intrebare12_raspuns3 = ("select raspuns3 from test_teorie where id='12' ")
        intrebare12_raspuns_corect3 = cursor.execute(intrebare12_raspuns3)
        intrebare12_raspuns_corect3 = intrebare12_raspuns_corect3.fetchall()[0][0]
        # intrebare 12 raspuns 4
        intrebare12_raspuns4 = ("select raspuns4 from test_teorie where id='12' ")
        intrebare12_raspuns_corect4 = cursor.execute(intrebare12_raspuns4)
        intrebare12_raspuns_corect4 = intrebare12_raspuns_corect4.fetchall()[0][0]
        # intrebare 12 raspuns 5
        intrebare12_raspuns5 = ("select raspuns5 from test_teorie where id='12' ")
        intrebare12_raspuns_corect5 = cursor.execute(intrebare12_raspuns5)
        intrebare12_raspuns_corect5 = intrebare12_raspuns_corect5.fetchall()[0][0]
        # intrebare 12 raspuns 6
        intrebare12_raspuns6 = ("select raspuns6 from test_teorie where id='12' ")
        intrebare12_raspuns_corect6 = cursor.execute(intrebare12_raspuns6)
        intrebare12_raspuns_corect6 = intrebare12_raspuns_corect6.fetchall()[0][0]

        # inserare in lista
        raspuns_corect_intrebarea12 = [intrebare12_raspuns_corect1, intrebare12_raspuns_corect2,
                                       intrebare12_raspuns_corect3, intrebare12_raspuns_corect4,
                                       intrebare12_raspuns_corect5]
        raspuns_corect_intrebarea12_varianta2 = [intrebare12_raspuns_corect6]
        raspuns_corect_r12 = raspuns_corect_intrebarea12
        raspuns_corect_r12a = raspuns_corect_intrebarea12_varianta2
        intrebare12 = request.form.getlist('Intrebarea12')
        if (raspuns_corect_r12 == intrebare12) or (raspuns_corect_r12a == intrebare12):
            correct = correct + 1
        else:
            incorect = incorect + 1

            # intrebare 13 raspuns 4
        intrebare13_raspuns4 = ("select raspuns4 from test_teorie where id='13' ")
        intrebare13_raspuns_corect = cursor.execute(intrebare13_raspuns4)
        intrebare13_raspuns_corect = intrebare13_raspuns_corect.fetchall()[0][0]

        # verificare raspuns13
        if request.form.getlist('Intrebarea13') and request.form['Intrebarea13'] == intrebare13_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

        # intrebare 14 raspuns 2
        intrebare14_raspuns2 = ("select raspuns2 from test_teorie where id='14' ")
        intrebare14_raspuns_corect = cursor.execute(intrebare14_raspuns2)
        intrebare14_raspuns_corect = intrebare14_raspuns_corect.fetchall()[0][0]

        # verificare raspuns14
        if request.form.getlist('Intrebarea14') and request.form['Intrebarea14'] == intrebare14_raspuns_corect:
            correct = correct + 1
        else:
            incorect = incorect + 1

    if (correct == 5):
        nota = 5
    if (correct == 6 or correct == 7):
        nota = 6
    if (correct == 8 or correct == 9):
        nota = 7
    if (correct == 10 or correct == 11):
        nota = 8
    if (correct == 12 or correct == 13):
        nota = 9
    if (correct == 14):
        nota = 10
    if (correct < 5):
        nota = 4

    return render_template('Test teorie/rezultat.html', correct=correct, incorect=incorect, nota_obtinuta=nota,
                           )


@app.route('/Home_Test_practic')
def Home_Test_pracit():
    return render_template('Test practic/Home_test_practic.html')


@app.route('/Test_practic')
def Test_pracit():
    return render_template('Test practic/Test practic.html')


@app.route('/Test_pracit_rezultat', methods=['POST'])
def Test_pracit_rezultat():
    global mesaj3_b, mesaj3_c, mesaj3_d
    error = None
    mesaj1_a = None
    mesaj1_b = None
    mesaj1_c = None
    mesaj2_a = None
    mesaj2_b = None
    mesaj2_c = None
    mesaj2_d = None
    mesaj3_a = None
    nota = 0
    corect = 0
    incorect = 0
    if request.method == 'POST':
        connection = sqlite3.connect('identifier.sqlite')
        cursor = connection.cursor()
        # exercitiu 1 subpunctul a raspuns corect extragere din baze de date
        exercitiu1 = ("select raspuns_corect_subpunctul_a from test_practic_raspunsuri where id='1' ")
        raspuns_corect_subpunctula_ex1 = cursor.execute(exercitiu1)
        raspuns_corect_subpunctula_ex1 = raspuns_corect_subpunctula_ex1.fetchall()[0][0]

        # exercitiu 1 subpunctul b raspuns corect extragere din baze de date
        exercitiu1 = ("select raspuns_corect_subpunctul_b from test_practic_raspunsuri where id='1' ")
        raspuns_corect_subpunctulb_ex1 = cursor.execute(exercitiu1)
        raspuns_corect_subpunctulb_ex1 = raspuns_corect_subpunctulb_ex1.fetchall()[0][0]
        # exercitiu 1 subpunctul c raspuns corect extragere din baze de date
        exercitiu1 = ("select raspuns_corect_subpunctul_c from test_practic_raspunsuri where id='1' ")
        raspuns_corect_subpunctulc_ex1 = cursor.execute(exercitiu1)
        raspuns_corect_subpunctulc_ex1 = raspuns_corect_subpunctulc_ex1.fetchall()[0][0]

        # exercitiu 1 a
        if request.form['Exercitiu1_a'] == raspuns_corect_subpunctula_ex1 or request.form[
            'Exercitiu1_a'] == raspuns_corect_subpunctula_ex1 + "Ohm" or request.form[
            'Exercitiu1_a'] == raspuns_corect_subpunctula_ex1 + "ohm":
            corect = corect + 1
            mesaj1_a = "ati raspuns corect la exercitiu 1  subpunctul a"
        else:
            incorect = incorect + 1
            mesaj1_a = "nu ati raspuns corect la exercitiu 1  subpunctul a"
        # exercitiu 1 b
        if request.form['Exercitiu1_b'] == raspuns_corect_subpunctulb_ex1 or request.form[
            'Exercitiu1_b'] == raspuns_corect_subpunctulb_ex1 + "V" or request.form[
            'Exercitiu1_b'] == raspuns_corect_subpunctulb_ex1 + "v":
            corect = corect + 1
            mesaj1_b = "ati raspuns corect la exercitiu 1 subpunctul b"
        else:
            incorect = incorect + 1
            mesaj1_b = "nu ati raspuns corect la exercitiu 1 subpunctul b "
            # exercitiu 1 c
        if request.form['Exercitiu1_c'] == raspuns_corect_subpunctulc_ex1 or request.form[
            'Exercitiu1_c'] == raspuns_corect_subpunctulc_ex1 + "W" or request.form[
            'Exercitiu1_c'] == raspuns_corect_subpunctulc_ex1 + "w":
            corect = corect + 1
            mesaj1_c = "ati raspuns corect la exercitiu 1 subpunctul c"
        else:
            incorect = incorect + 1
            mesaj1_c = "nu ati raspuns corect la exercitiu 1 subpunctul c "

        # exercitiu 2 subpunctul a raspuns corect extragere din baze de date
        exercitiu2 = ("select raspuns_corect_subpunctul_a from test_practic_raspunsuri where id='2' ")
        raspuns_corect_subpunctula_ex2 = cursor.execute(exercitiu2)
        raspuns_corect_subpunctula_ex2 = raspuns_corect_subpunctula_ex2.fetchall()[0][0]

        # exercitiu 2 subpunctul b raspuns corect extragere din baze de date
        exercitiu2 = ("select raspuns_corect_subpunctul_b from test_practic_raspunsuri where id='2' ")
        raspuns_corect_subpunctulb_ex2 = cursor.execute(exercitiu2)
        raspuns_corect_subpunctulb_ex2 = raspuns_corect_subpunctulb_ex2.fetchall()[0][0]
        # exercitiu 2 subpunctul c raspuns corect extragere din baze de date
        exercitiu2 = ("select raspuns_corect_subpunctul_c from test_practic_raspunsuri where id='2' ")
        raspuns_corect_subpunctulc_ex2 = cursor.execute(exercitiu2)
        raspuns_corect_subpunctulc_ex2 = raspuns_corect_subpunctulc_ex2.fetchall()[0][0]
        # exercitiu 2 subpunctul d raspuns corect extragere din baze de date
        exercitiu2 = ("select raspuns_corect_subpunctul_d from test_practic_raspunsuri where id='2' ")
        raspuns_corect_subpunctuld_ex2 = cursor.execute(exercitiu2)
        raspuns_corect_subpunctuld_ex2 = raspuns_corect_subpunctuld_ex2.fetchall()[0][0]

        # exercitiu 2 problema a
        if request.form['Exercitiu2_XL'] == raspuns_corect_subpunctula_ex2 or request.form[
            'Exercitiu2_XL'] == raspuns_corect_subpunctula_ex2 + "Ohm" or request.form[
            'Exercitiu2_XL'] == raspuns_corect_subpunctula_ex2 + "ohm":
            corect = corect + 1
            mesaj2_a = "ati raspuns corect la exercitiu 2 subpunctul a"
        else:
            incorect = incorect + 1
            mesaj2_a = "nu ati raspuns corect la exercitiu  2 subpunctul a "
        # exercitiu 2 problema b
        if request.form['Exercitiu2_XC'] == raspuns_corect_subpunctulb_ex2 or request.form[
            'Exercitiu2_XC'] == raspuns_corect_subpunctulb_ex2 + "Ohm" or request.form[
            'Exercitiu2_XC'] == raspuns_corect_subpunctulb_ex2 + "ohm":
            corect = corect + 1
            mesaj2_b = "ati raspuns corect la exercitiu 2 subpunctul b"
        else:
            incorect = incorect + 1
            mesaj2_b = "nu ati raspuns corect la exercitiu  2 subpunctul b "
        # exercitiu 2 problema c

        if request.form["Exercitiu2_UC"] == raspuns_corect_subpunctulc_ex2 or request.form[
            "Exercitiu2_UC"] == raspuns_corect_subpunctulc_ex2 + "V" or request.form[
            "Exercitiu2_UC"] == raspuns_corect_subpunctulc_ex2 + "v":
            corect = corect + 1
            mesaj2_c = "ati raspuns corect la exercitiu 2 subpunctul c"
        else:
            incorect = incorect + 1
            mesaj2_c = "nu ati raspuns corect la exercitiu  2 subpunctul c "
        # exercitiu 2 problema d
        if request.form["Exercitiu2_UL"] == raspuns_corect_subpunctuld_ex2 or request.form[
            "Exercitiu2_UL"] == raspuns_corect_subpunctuld_ex2 + "V" or request.form[
            "Exercitiu2_UL"] == raspuns_corect_subpunctuld_ex2 + "v":
            corect = corect + 1
            mesaj2_d = "ati raspuns corect la exercitiu 2 subpunctul d"
        else:
            incorect = incorect + 1
            mesaj2_d = "nu ati raspuns corect la exercitiu  2 subpunctul d "

        # exercitiu 3 subpunctul a raspuns corect extragere din baze de date
        exercitiu3 = ("select raspuns_corect_subpunctul_a from test_practic_raspunsuri where id='3' ")
        raspuns_corect_subpunctula_ex3 = cursor.execute(exercitiu3)
        raspuns_corect_subpunctula_ex3 = raspuns_corect_subpunctula_ex3.fetchall()[0][0]

        # exercitiu 3 subpunctul b raspuns corect extragere din baze de date
        exercitiu3 = ("select raspuns_corect_subpunctul_b from test_practic_raspunsuri where id='3' ")
        raspuns_corect_subpunctulb_ex3 = cursor.execute(exercitiu3)
        raspuns_corect_subpunctulb_ex3 = raspuns_corect_subpunctulb_ex3.fetchall()[0][0]
        # exercitiu 3 subpunctul c raspuns corect extragere din baze de date
        exercitiu3 = ("select raspuns_corect_subpunctul_c from test_practic_raspunsuri where id='3' ")
        raspuns_corect_subpunctulc_ex3 = cursor.execute(exercitiu3)
        raspuns_corect_subpunctulc_ex3 = raspuns_corect_subpunctulc_ex3.fetchall()[0][0]
        # exercitiu 3 subpunctul d raspuns corect extragere din baze de date
        exercitiu3 = ("select raspuns_corect_subpunctul_d from test_practic_raspunsuri where id='3' ")
        raspuns_corect_subpunctuld_ex3 = cursor.execute(exercitiu3)
        raspuns_corect_subpunctuld_ex3 = raspuns_corect_subpunctuld_ex3.fetchall()[0][0]

        # exercitiu 3 problema a
        if request.form["Exercitiu3_U1"] == raspuns_corect_subpunctula_ex3 or request.form[
            "Exercitiu3_U1"] == raspuns_corect_subpunctula_ex3 + "V" or request.form[
            "Exercitiu3_U1"] == raspuns_corect_subpunctula_ex3 + "v":
            corect = corect + 1
            mesaj3_a = "ati raspuns corect la exercitiu 3 subpunctul a"
        else:
            incorect = incorect + 1
            mesaj3_a = "nu ati raspuns corect la exercitiu  3 subpunctul a "
        # exercitiu 3 problema b
        if request.form["Exercitiu3_U2"] == raspuns_corect_subpunctulb_ex3 or request.form[
            "Exercitiu3_U2"] == raspuns_corect_subpunctulb_ex3 + "V" or request.form[
            "Exercitiu3_U2"] == raspuns_corect_subpunctulb_ex3 + "v":
            corect = corect + 1
            mesaj3_b = "ati raspuns corect la exercitiu 3 subpunctul b"
        else:
            incorect = incorect + 1
            mesaj3_b = "nu ati raspuns corect la exercitiu  3 punctul b "
        if request.form["Exercitiu3_Q2"] == raspuns_corect_subpunctulc_ex3 or request.form[
            "Exercitiu3_Q2"] == raspuns_corect_subpunctulc_ex3 + "nC" or request.form[
            "Exercitiu3_Q2"] == raspuns_corect_subpunctulc_ex3 + "nc":
            corect = corect + 1
            mesaj3_c = "ati raspuns corect la exercitiu 3 subpunctul b"
        else:
            incorect = incorect + 1
            mesaj3_c = "nu ati raspuns corect la exercitiu  3 punctul b "
        if request.form["Exercitiu3_Q12"] == raspuns_corect_subpunctuld_ex3 or request.form[
            "Exercitiu3_Q12"] == raspuns_corect_subpunctuld_ex3 + "nC" or request.form[
            "Exercitiu3_Q12"] == raspuns_corect_subpunctuld_ex3 + "nc":
            corect = corect + 1
            mesaj3_d = "ati raspuns corect la exercitiu 3 subpunctul d"
        else:
            incorect = incorect + 1
            mesaj3_d = "nu ati raspuns corect la exercitiu  3 subpunctul d "

    if (corect < 5):
        nota=4
    if (corect == 5):
        nota = 5
    if (corect == 6):
        nota = 6
    if (corect == 7):
        nota = 7
    if (corect == 8):
        nota = 8
    if (corect == 9):
        nota = 9
    if (corect == 10 or corect == 11):
        nota = 10

    return render_template('Test practic/rezultat_test_pracitic.html', corect=corect,
                           incorect=incorect, mesaj1a=mesaj1_a, mesaj1b=mesaj1_b, mesaj1c=mesaj1_c,
                           mesaj2=mesaj2_a, mesaj2b=mesaj2_b, mesaj2c=mesaj2_c, mesaj2d=mesaj2_d,
                           mesaj3a=mesaj3_a, mesaj3b=mesaj3_b, mesaj3c=mesaj3_c, mesaj3d=mesaj3_d, nota=nota)


@app.route('/Problema1_pasii_de_rezolvare', methods=['GET'])
def Problema1_pasii_de_rezolvare():
    return render_template("Prezentari reveal/Problema1_pasii_de_rezolvare.html")


@app.route('/Problema2_pasii_de_rezolvare', methods=['GET'])
def Problema2_pasii_de_rezolvare():
    return render_template("Prezentari reveal/Problema2_pasii_de_rezolvare.html")


@app.route('/Problema3_pasii_de_rezolvare', methods=['GET'])
def Problema3_pasii_de_rezolvare():
    return render_template("Prezentari reveal/Problema3_pasii_de_rezolvare.html")


@app.route('/Rezistor_calculator_color', methods=['GET'])
def Calculator_Rezistor():
    return render_template("Calculatoare/Resistor_color/Resistor_color.html")


@app.route('/Rezistor_calculator', methods=['GET'])
def Rezistor_calculator():
    return render_template("Calculatoare/Rezistor_calculator.html")


@app.route('/operation_result2/', methods=['POST'])
def operation_rezistor2():
    error = None
    result = None

    first_input = request.form['Input1']
    second_input = request.form["Input2"]
    operation = request.form['operation']
    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "serial":
            result = input1 + input2


        else:
            if operation == "paralel":
                result = (1 / ((1 / input1) + (1 / input2)))

        return render_template(
            'Calculatoare/Rezistor_calculator.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True

        )
    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Rezistor_calculator.html',
            input1=first_input,
            input2=first_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )

    except ValueError:
        return render_template(
            'Calculatoare/Rezistor_calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se pot efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Capacitor', methods=['GET'])
def calc_capacitor():
    return render_template("Calculatoare/Capacitor_calculator.html")


@app.route('/capacitor_calculator/', methods=['POST'])
def capacitor_calculator():
    error = None
    result = None

    first_input = request.form['Input1']
    second_input = request.form["Input2"]
    operation = request.form['operation']
    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operation on webpage is addition
        if operation == "serial":
            result = (1 / ((1 / input1) + (1 / input2)))


        else:
            if operation == "paralel":
                result = input1 + input2

        return render_template(
            'Calculatoare/Capacitor_calculator.html',
            input1=input1,
            input2=input2,
            operation=operation,
            result=result,
            calculation_success=True

        )
    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Capacitor_calculator.html',
            input1=first_input,
            input2=first_input,
            operation=operation,
            result="Ai introdus valoare greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )

    except ValueError:
        return render_template(
            'Calculatoare/Capacitor_calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se pot efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Legea_Lui_Ohm_t')
def Legea_Lui_Ohm_t():
    return render_template('Calculatoare/Legea_Ohm/Legea_Ohm_tensiunea.html')


@app.route('/Legea_Ohm_tensiunea/', methods=['GET', 'POST'])
def Legea_Ohm_tensiunea():
    error = None
    result = None

    i = request.form["curentul"]
    r = request.form["rezistenta"]
    p = request.form["puterea"]
    try:
        rezistenta = float(r)
        curentul = float(i)
        puterea = float(p)

        # On default, the operation on webpage is addition
        if (curentul > 0 and rezistenta > 0 and puterea == 0 or puterea == None):
            result = float(curentul * rezistenta)
        if (curentul > 0 and puterea > 0 and rezistenta == 0 or rezistenta == None):
            result = float(puterea / curentul)


        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_tensiunea.html',
            curentul=i,
            rezistenta=r,
            puterea=p,
            result=result,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_tensiunea.html',
            curentul=i,
            rezistenta=r,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )
    except ValueError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_tensiunea.html',
            curentul=i,
            rezistenta=r,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Legea_Lui_Ohm_r')
def Legea_Lui_Ohm_r():
    return render_template('Calculatoare/Legea_Ohm/Legea_Ohm_Rezistenta.html')


@app.route('/Legea_Ohm_rezistenta/', methods=['GET', 'POST'])
def Legea_Ohm_rezistenta():
    error = None
    result = None

    i = request.form["curentul"]
    p = request.form["puterea"]
    u = request.form["tensiunea"]
    try:

        curentul = float(i)
        tensiunea = float(u)
        puterea = float(p)

        if (tensiunea > 0 and curentul > 0 and puterea == 0):
            result = tensiunea / curentul
        if (puterea > 0 and curentul > 0 and tensiunea == 0):
            result = puterea / pow(curentul, 2)
        if (tensiunea > 0 and curentul > 0 and puterea > 0):
            result = ("nu se poate calcula cu trei valori")

        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_Rezistenta.html',
            curentul=i,
            tensiunea=u,
            puterea=p,
            result=result,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_Rezistenta.html',
            curentul=i,
            tensiunea=u,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )
    except ValueError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_Rezistenta.html',
            curentul=i,
            tensiunea=u,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Legea_Lui_Ohm_i')
def Legea_Lui_Ohm_i():
    return render_template('Calculatoare/Legea_Ohm/Legea_Ohm_curentul.html')


@app.route('/Legea_Ohm_curentul/', methods=['GET', 'POST'])
def Legea_Ohm_curentul():
    error = None
    result = None

    r = request.form["rezistenta"]
    p = request.form["puterea"]
    u = request.form["tensiunea"]
    try:

        rezistenta = float(r)
        tensiunea = float(u)
        puterea = float(p)

        if (tensiunea > 0 and rezistenta > 0 and puterea == 0):
            result = float(tensiunea / rezistenta)
        if (puterea > 0 and tensiunea > 0 and rezistenta == 0):
            result = float(puterea / tensiunea)

        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_curentul.html',
            tensiunea=u,
            rezistenta=r,
            puterea=p,
            result=result,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_curentul.html',
            tensiunea=u,
            rezistenta=r,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )
    except ValueError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_curentul.html',
            tensiunea=u,
            rezistenta=r,
            puterea=p,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Legea_Lui_Ohm_p')
def Legea_Lui_Ohm_p():
    return render_template('Calculatoare/Legea_Ohm/Legea_Ohm_puterea.html')


@app.route('/Legea_Ohm_puterea/', methods=['GET', 'POST'])
def Legea_Ohm_puterea():
    error = None
    result = None

    r = request.form["rezistenta"]
    i = request.form["curentul"]
    u = request.form["tensiunea"]
    try:
        rezistenta = float(r)
        tensiunea = float(u)
        curentul = float(i)

        if (curentul > 0 and rezistenta > 0 and tensiunea == 0):
            result = (pow(curentul, 2) * rezistenta)
        if (tensiunea > 0 and rezistenta > 0 and curentul == 0):
            result = (pow(tensiunea, 2) / rezistenta)

        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_puterea.html',
            curentul=i,
            rezistenta=r,
            tensiunea=u,
            result=result,
            calculation_success=True
        )

    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_puterea.html',
            curentul=i,
            rezistenta=r,
            tensiunea=u,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți împărți cu zero"
        )
    except ValueError:
        return render_template(
            'Calculatoare/Legea_Ohm/Legea_Ohm_puterea.html',
            curentul=i,
            rezistenta=r,
            tensiunea=u,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Calculator_Portii')
def Calculator2():
    return render_template('Calculatoare/Portii_logicii_calculator.html')


@app.route('/operation_result/', methods=['POST'])
def operation_result():
    error = None
    result = None

    # request.form cauta:
    # etichete html cu potrivire "nume ="

    first_input = request.form['A']
    second_input = request.form['B']
    operation = request.form['operation']

    try:
        A = int(first_input)
        B = int(second_input)

        # On default, the operation on webpage is addition
        if operation == "AND":
            if (A == 0 and B == 0):
                result = "Q=0"
            if (A == 1 and B == 0):
                result = "Q=0"
            if (A == 0 and B == 1):
                result = "Q=0"
            if (A == 1 and B == 1):
                result = "Q=1"

        elif operation == "NAND":
            if (A == 0 and B == 0):
                result = "Q=1"
            if (A == 1 and B == 0):
                result = "Q=1"
            if (A == 0 and B == 1):
                result = "Q=1"
            if (A == 1 and B == 1):
                result = "Q=0"

        elif operation == "OR":
            if (A == 0 and B == 0):
                result = "Q=0"
            if (A == 1 and B == 0):
                result = "Q=1"
            if (A == 0 and B == 1):
                result = "Q=1"
            if (A == 1 and B == 1):
                result = "Q=1"

        elif operation == "Inverter":
            if (A == 0 and (str(B == "Nu introduc"))):
                result = "¬A=1"
            if (A == 1 and (str(B == "Nu introduc"))):
                result = "¬A=0"
            if (B == 0 and (str(A == "Nu introduc"))):
                result = "¬B=1"
            if (B == 1 and (str(A == "Nu introduc"))):
                result = "¬B=0"


        elif operation == "NOR":
            if (A == 0 and B == 0):
                result = "Q=1"
            if (A == 1 and B == 0):
                result = "Q=0"
            if (A == 0 and B == 1):
                result = "Q=0"
            if (A == 1 and B == 1):
                result = "Q=0"

        elif operation == "XNOR":
            if (A == 0 and B == 0):
                result = "Q=1"
            if (A == 1 and B == 0):
                result = "Q=0"
            if (A == 0 and B == 1):
                result = "Q=0"
            if (A == 1 and B == 1):
                result = "Q=1"

        return render_template(
            'Calculatoare/Portii_logicii_calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result=result,
            calculation_success=True
        )


    except ValueError:
        return render_template(
            'Calculatoare/Portii_logicii_calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Valoarea trebuie sa fie 0 sau 1"
        )


@app.route('/AC_DC_Convertor', methods=['GET'])
def AC_DC_Convertor():
    return render_template('Calculatoare/AC_DC_Convertor.html')


@app.route('/AcToDc/', methods=['POST'])
def AcToDc():
    error = None
    result = None
    mesaj1 = "AC="
    mesaj2 = "DC="

    # request.form looks for:
    # html tags with matching "name= "

    first_input = request.form['AC']
    second_input = request.form['DC']
    operation = request.form['operation']

    try:
        AC = float(first_input)
        DC = float(second_input)

        if operation == ("AC to DC"):
            if (AC > 0 and DC == 0):
                result = mesaj2 + str(float(AC * 0.636))
        if operation == ("DC to AC"):
            if (DC > 0 and AC == 0):
                result = mesaj1 + str(float((DC / 0.636)))

        return render_template(
            'Calculatoare/AC_DC_Convertor.html',
            AC=first_input,
            DC=second_input,
            operation=operation,
            result=result,
            calculation_success=True

        )
    except ZeroDivisionError:
        return render_template(
            'Calculatoare/AC_DC_Convertor.html',
            AC=first_input,
            DC=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )
    except ValueError:
        return render_template(
            'Calculatoare/AC_DC_Convertor.html',
            AC=first_input,
            DC=second_input,
            operation=operation,
            result="Bad Input",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


@app.route('/Inductor_calc', methods=['GET'])
def Inductor_calc():
    return render_template("Calculatoare/Inductor_Calculator.html")


@app.route('/inductor_calculator/', methods=['POST'])
def inductor_calculator():
    error = None
    result = None

    first_input = request.form['Inductor1']
    second_input = request.form["Inductor2"]
    operation = request.form['operation']
    try:
        Inductor1 = float(first_input)
        Inductor2 = float(second_input)

        if operation == "serial":
            result = Inductor1 + Inductor2


        else:
            if operation == "paralel":
                result = 1 / ((1 / Inductor1) + (1 / Inductor2))

        return render_template(
            'Calculatoare/Inductor_Calculator.html',
            input1=Inductor1,
            input2=Inductor2,
            operation=operation,
            result=result,
            calculation_success=True

        )
    except ZeroDivisionError:
        return render_template(
            'Calculatoare/Inductor_Calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu poți impărți cu zero"
        )

    except ValueError:
        return render_template(
            'Calculatoare/Inductor_Calculator.html',
            input1=first_input,
            input2=second_input,
            operation=operation,
            result="Ai introdus parametrii greșit",
            calculation_success=False,
            error="Nu se poate efectua operația numerică cu intrarea furnizată"
        )


FLASK_DEBUG = True;

if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)


//colectez raspunsurile
//le grupeg intr-un obiect exemplu json
//trimit obiectul catre o functie python pentru validare
//validez in python folosind acest cod de la js
//trimit raspuns catre js
//afiseaza datele
//https://stackoverflow.com/questions/16338582/python-code-from-javascript-using-ajax

function check() {

     //const sqlite3 = require('sqlite3').verbose();
      //const db = new sqlite3.Database('identifier.sqlite');

    var intrebarea1 = document.test.Intrebarea1.value;
    var intrebarea5 = document.test.Intrebarea5.value;
    var intrebarea6 = document.test.Intrebarea6.value;
    var intrebarea8 = document.test.Intrebarea8.value;
    var intrebarea9 = document.test.Intrebarea9.value;
    var intrebarea11 = document.test.Intrebarea11.value;
    var intrebarea13 = document.test.Intrebarea13.value;
    var intrebarea14 = document.test.Intrebarea14.value;
    var corect = 0;
    var incorecte = 0;
    var nota = 0;


     //let raspuns1;
    /// raspuns1 = db.get("select raspuns1 from test_teorie where id='1'");


    if (intrebarea1 === "U=I/R") {
        corect++;
    } else {
        incorecte++;
    }
    if (document.getElementById("Emiter").checked === true && document.getElementById("Baza").checked === true && document.getElementById("Colector").checked === true) {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("Emiter").checked === true && document.getElementById("Baza").checked === true && document.getElementById("Colector").checked === true && document.getElementById("Comutator").checked === true) {
        corect--;
        incorecte++;
    }

    if (document.getElementById("Anoda").checked === true && document.getElementById("Catoda").checked === true) {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("Anoda").checked === true && document.getElementById("Catoda").checked === true && document.getElementById("Tub").checked === true && document.getElementById("Filament").checked === true) {
        corect--;
        incorecte++;
    }

    if (document.getElementById("Electrolic").checked === true && document.getElementById("Tantal").checked === true && document.getElementById("Ceramic").checked === true && document.getElementById("Poliester").checked === true) {
        corect++;
    } else {
        incorecte++;
    }
    if (intrebarea5 === "1/Rt=(1/R1)+(1/R2)+(1/R3)") {
        corect++;
    } else {
        incorecte++;
    }

    if (intrebarea6 === "0,6V") {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("Permanente").checked === true && document.getElementById("Variabile").checked === true) {
        corect++;
    } else {
        incorecte++;
    }


    if (document.getElementById("Permanente").checked === true && document.getElementById("Variabile").checked === true && document.getElementById("Pasive").checked === true && document.getElementById("Active").checked === true) {
        corect--;
        incorecte++;
    } else if (document.getElementById("Permanente").checked === true && document.getElementById("Variabile").checked === true && document.getElementById("Active").checked === true) {
        corect--;
        incorecte++;
    } else if (document.getElementById("Permanente").checked === true && document.getElementById("Variabile").checked === true && document.getElementById("Pasive").checked === true) {
        corect--;
        incorecte++;
    }

    if (intrebarea8 === "Ct=C1+C2+C3+C4") {
        corect++;
    } else {
        incorecte++;
    }


    if (intrebarea9 === "Voltmetru") {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("P=U*I").checked === true && document.getElementById("P=(U^2)/R").checked === true && document.getElementById("P=(I^2)+R").checked === true) {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("P=U*I").checked === true && document.getElementById("P=(U^2)/R").checked === true && document.getElementById("P=(I^2)+R").checked === true && document.getElementById("P=(R^2)+U").checked === true) {
        corect--;
        incorecte++;
    }


    if (intrebarea11 === "Amplifactoruli sunt circuite elctronice care la intrare aduc semnal și la ieșire primim semnal cu aceași forma dar cu o valoare mai mare") {
        corect++;
    } else {
        incorecte++;
    }

    if (document.getElementById("Toate răspunsurile sunt corecte").checked === true || document.getElementById("And").checked === true && document.getElementById("OR").checked === true &&
        document.getElementById("NAND").checked === true && document.getElementById("NOR").checked === true && document.getElementById("XOR").checked === true) {
        corect++;
    } else {
        incorecte++;
    }

    if (intrebarea13 === "Farad(F)") {
        corect++;
    } else {
        incorecte++;
    }


    if (intrebarea14 === "Ohm") {
        corect++;
    } else {
        incorecte++;
    }


    if (corect === 5) {
        nota = 5;
    }
    if (corect === 6 || corect === 7) {
        nota = 6;
    }
    if (corect === 8 || corect === 9) {
        nota = 7;
    }
    if (corect === 10 || corect === 11) {
        nota = 8;
    }
    if (corect === 12 || corect === 13) {
        nota = 9;
    }
    if (corect === 14) {
        nota = 10;
    }


    if (corect < 5) {
        nota = 4;
    }


    document.getElementById("rezultat").style.visibility = "visible";
    document.getElementById("raspunsuri_corecte").innerHTML = "Ati raspuns la " + corect + " raspunsuri corecte";
    document.getElementById("raspunsuri_incorecte").innerHTML = "Număr răspunsuri " + incorecte + " incorecte";
    document.getElementById("nota").innerHTML = "Nota obținuta este " + nota;


}

function check(){
    if(document.getElementById("four").checked)
        document.getElementById("A_treia_banda").disabled=true;

    if(document.getElementById("four").checked)
        document.getElementById("TCR").disabled=true;

    if(document.getElementById("five").checked)
        document.getElementById("A_treia_banda").disabled=false;

    if (document.getElementById("five").checked)
        document.getElementById("TCR").disabled=true;

    if(document.getElementById("six").checked)
        document.getElementById("TCR").disabled=false;


    }


    function change_color1(select){
        document.getElementById("Prima_banda").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }
    function  change_color2(select){
        document.getElementById("A_doua_banda").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }
    function  change_color3(select){
        document.getElementById("Multiplicator").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }
    function  change_color4(select){
        document.getElementById("toleranta").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }
    function  change_color5(select){
        document.getElementById("A_treia_banda").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }
    function  change_color6(select){
        document.getElementById("TCR").style.backgroundColor=select.options[select.selectedIndex].textContent;
    }

function calculate(){


    if(document.getElementById("five").checked)
        num=parseInt(document.getElementById("Prima_banda").value.toString()+document.getElementById("A_doua_banda").value.toString()+document.getElementById("A_treia_banda").value.toString());
        var mul=Math.pow(10,parseInt(document.getElementById("Multiplicator").value));
    if(document.getElementById("toleranta").value === "10")
        var tol = 10;
    if (document.getElementById("toleranta").value === "11")
          tol=5;

    if (document.getElementById("TCR").value==="0")
        tcr=250;
    if (document.getElementById("TCR").value==="1")
        tcr=100;
    if (document.getElementById("TCR").value==="2")
         tcr=50;
    if (document.getElementById("TCR").value==="3")
         tcr=15;
    if (document.getElementById("TCR").value==="4")
         tcr=25;
    if (document.getElementById("TCR").value==="5")
         tcr=20;
    if (document.getElementById("TCR").value==="6")
         tcr=10;
    if (document.getElementById("TCR").value==="7")
         tcr=5;
    if (document.getElementById("TCR").value==="8")
         tcr=1;
    if(document.getElementById("four").checked)
        tcr=0
      num=parseInt(document.getElementById("Prima_banda").value.toString()+document.getElementById("A_doua_banda").value.toString());
      document.getElementById("ans").innerHTML="Rezistența totală este "+num*mul.toString()+" ohms = "+abbrNum(num*mul,2).toString()+" ohms .Iar toleranța variază "+Math.round(num*mul*(1-tol/100))+" - "+Math.round(num*mul*(1+tol/100))+" ohms.";

    if(document.getElementById("five").checked)
        tcr=0
        num=parseInt(document.getElementById("Prima_banda").value.toString()+document.getElementById("A_doua_banda").value.toString()+document.getElementById("A_treia_banda").value.toString());
        document.getElementById("ans").innerHTML="Rezistența totală este "+num*mul.toString()+" ohms = "+abbrNum(num*mul,2).toString()+" ohms .Iar toleranța variază "+Math.round(num*mul*(1-tol/100))+" - "+Math.round(num*mul*(1+tol/100))+" ohms.";

    if (document.getElementById("six").checked)
        num=parseInt(document.getElementById("Prima_banda").value.toString()+document.getElementById("A_doua_banda").value.toString()+document.getElementById("A_treia_banda").value.toString())+document.getElementById("toleranta").value.toString()+document.getElementById("TCR").value.toString();
        document.getElementById("ans").innerHTML="Rezistența totală este "+num*mul.toString()+" ohms = "+abbrNum(num*mul,2).toString()+" ohms .Iar toleranța variază "+Math.round(num*mul*(1-tol/100))+" - "+Math.round(num*mul*(1+tol/100))+" ohms."+"tcr="+tcr;
    }

     function abbrNum(number, decPlaces) {
            // 2 decimal places => 100, 3 => 1000, etc
            decPlaces = Math.pow(10,decPlaces);

            // Enumerează abrevieri de număr
            var abbrev = [ "K", "M", "B", "T" ];

           // Parcurge matricea înapoi, așa că face mai întâi cea mai mare
            for (var i=abbrev.length-1; i>=0; i--) {


                // Conversia indexului matricei în „1000”, „1000000” etc.
                var size = Math.pow(10,(i+1)*3);

               // Dacă numărul este mai mare sau egal, face abrevierea
                if(size <= number) {
                   // Aici, ne înmulțim cu decPlaces, rotunjim și apoi împărțim cu decPlaces.
                    // Acest lucru ne oferă o rotunjire frumoasă la o anumită zecimală.
                    number = Math.round(number*decPlaces/size)/decPlaces;

                 // Adăugați litera pentru abreviere
                    number += abbrev[i];

                  // Am terminat ... se oprește
                    break;
                }
            }
              return number;
        }
     function reset(){
            document.getElementById("four") .checked=true;
            document.getElementById("five") .checked=true;
            document.getElementById("Prima_banda") .value="--";
            document.getElementById("Prima_banda").style.backgroundColor='white';
            document.getElementById("A_doua_banda") .value="--";
            document.getElementById("A_doua_banda").style.backgroundColor='white';
            document.getElementById("A_treia_banda") .value="--";
            document.getElementById("A_treia_banda").style.backgroundColor='white';
            document.getElementById("Multiplicator") .value="--";
            document.getElementById("Multiplicator").style.backgroundColor='white';
            document.getElementById("toleranta") .value="--";
            document.getElementById("toleranta").style.backgroundColor='white';
            document.getElementById("TCR") .value="--";
            document.getElementById("TCR").style.backgroundColor='white';
            document.getElementById("ans").innerHTML="";

        }
import webbrowser
from os import linesep
import analizador_menu 


def reportar(lista_tokens):
    report=webbrowser.open("menu.html","w")
    report.write(
        "<!DOCTYPE html>"
    +"<html lang=\"en\">"
    +"<head>"
    +"<meta charset=\"UTF-8\">"
    +"<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
    +"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">"
    +"<title>Document</title>"
    +"<h1>TABLA DE TOKENS</h1>"
    +"<style>"
       + "h1 { color: #f1f1ee;"
           + "opacity: 0.5; "
            +"font-style: oblique;"
            +"text-align: center;}"
    +"</style>"

    
    +"</head>"

    +"<body background=\"imagen1.jpg\"></body>"
    +"<body>"
    

    +"<table  align =\"center\">"
        +"<thead style =\"background: #ddb75d; opacity:0.6\">"

       
        +"<tr>"
           + "<th>NÚMERO </th>"
           + "<th>LEXEMA  </th>"
           + "<th>FILA</th>"
           + "<th>COLUMNA</th>"
           + "<th>TOKEN</th>"

       + " </tr>"
        
        +"</thead>"

        +"<tbody style =\"background: #1e779b;opacity: 0.6\">")
    for x in lista_tokens:
        #print (x.numero,x.lexema,x.fila,x.columna,x.token) 
        report.write(
        "<tr>"
        + " <td> "+str(x.numero)+" </td>"
        + "<td> "+x.lexema+"</td>"
        + "<td> "+str(x.fila)+" </td>"
        + "<td> "+str(x.columna)+"</td>"
        + "<td> "+x.token+"</td>"
        + "</tr>")
    report.write(
    "</tbody>"
    + "</table>"

    +"</body>"
    +"</html>"

    )
    
    report.close()
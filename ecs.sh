#!/bin/bash
testfunction(){
    echo "Consultando al SAT"
    rm -r lista.csv
    wget http://omawww.sat.gob.mx/cifras_sat/Documents/Listado_Completo_69-B.csv
    mv Listado_Completo_69-B.csv ./lista.csv 
    sed "1d" lista.csv > lista1.csv
    sed "1d" lista1.csv > lista2.csv
    rm -r lista1.csv
    mv lista2.csv  ./lista.csv
    python3 index.py 
}
testfunction
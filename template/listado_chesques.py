import csv
import argparse
from datetime import datetime

"""

    5) Si el estado del cheque no se pasa, se deberán imprimir los cheques sin filtrar por estado 

    Aclaracion: En la descripción de los campos, falta el campo TIPO, que es un string 
        que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO"
"""
# ejemplo1: py template\listado_chesques.py test.csv 40998788 Pantalla 123 -ec aprobado
# ejemplo2: py template\listado_chesques.py test.csv 40998788 Pantalla 123 -ec rechazado
# ejemplo3: py template\listado_chesques.py test.csv 40998788 Pantalla 123
# ejemplo4: py template\listado_chesques.py test.csv 23665789 Csv 123
parser = argparse.ArgumentParser("""Ingresa Nombre del archivo csv, DNI, Salida,
        Tipo de cheque, Estado de cheque(opcional), Rango de fecha(opcional)""")
parser.add_argument('csv',type=str,help='Ingresa nombre del archivo csv')
parser.add_argument('dni',type=int,help='Ingresa el dni que quieres filtrar')
parser.add_argument('salida',type=str,help='Ingresa tipo de salida (pantalla o csv)')
parser.add_argument('tipocheque',type=str,help='Ingresa el tipo de cheque (emitido o depositado)')
parser.add_argument('-ec','--estadocheque',type=str,help='Ingresa el estado del cheque (pendiente, aprobado, rechazado)',default=None)
parser.add_argument('-rf','--rangofecha',type=str,help='Ingresa un rango de fechas con el formato: xx-xx-xxxx:yy-yy-yyyy')

args = parser.parse_args()

def escribir(resultado):
    dt=datetime.now()
    ts=datetime.timestamp(dt)
    with open(f'{resultado[0][8]}{ts}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for cheque in resultado:
            valor = [cheque [3], cheque[5], cheque[6], cheque[7]]
            writer.writerow(valor)    

def filtrarCheque(resultado, estadoCheque):
    return filter(lambda cheque: cheque[10]== estadoCheque.upper(), resultado)

def leer(archivo, dni, salida, tipoCheque, estadoCheque, rangoFecha="01-01-0000:31-12-9999"):
    diccionario = {}
    with open(f"template\{archivo}",'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        generarDiccionarioCSV(f,reader, diccionario)
        f.close()
        #print(diccionario)
        resultado = diccionario.get(str(dni))
        if(estadoCheque != None):
            resultado = filtrarCheque(resultado, estadoCheque)
        imprimirResultados(salida,resultado)
        

def generarDiccionarioCSV(f,reader, diccionario):
    for NroCheque,CodBanco,CodiScurusal,NroCuentaOrigen,NroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
        datos = [NroCheque,CodBanco,CodiScurusal,NroCuentaOrigen,NroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado]
        if(DNI in diccionario):
            try:
                verificarChequeRepetido(diccionario.get(DNI), NroCheque, NroCuentaOrigen)
            except ValueError:
                print(f"Error-->El cheque con nro:{NroCheque} se encuentra repetido en la cuenta: {NroCuentaOrigen}")
                f.close()
                exit()
            diccionario[DNI].append(datos)
        else:
            diccionario[DNI] = [datos]

def verificarChequeRepetido(datos, NroCheque, NroCuentaOrigen):
    for dato in datos:
        if (NroCheque in dato and NroCuentaOrigen in dato):
            raise ValueError

def imprimirResultados(salida,resultado):
    if(salida.upper() == "PANTALLA"):
   
        for cheque in resultado:
            print(f"""\nNroCheque:{cheque[0]}\nCodBanco:{cheque[1]}\nCodiScurusal:{cheque[2]}
NroCuentaOrigen:{cheque[3]}\nNroCuentaDestino:{cheque[4]}\nValor:{cheque[5]}
FechaOrigen:{cheque[6]}\nFechaPago:{cheque[7]}\nDNI:{cheque[8]}
Tipo:{cheque[9]}\nEstado:{cheque[10]}\n=======================""")

    elif(salida.upper() == "CSV"):
        escribir(resultado)
    else :
        print(f"Error-->La salida: {salida} no es valida")
        exit()

if(args.rangofecha):
    leer(args.csv, args.dni, args.salida,args.tipocheque,args.estadocheque,args.rangofecha)
else:
    leer(args.csv, args.dni, args.salida,args.tipocheque,args.estadocheque)
# leer("test.csv","40998788","PantaLla",123)

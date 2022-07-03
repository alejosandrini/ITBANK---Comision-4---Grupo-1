import csv
import argparse
"""
    2)Recibir argumentos por consola: Nombre del archivo csv, DNI, Salida,
        Tipo de cheque, Estado de cheque(opcional), Rango de fecha(opcional)
    4)El csv de respuesta debe tener: nombre del archivo <DNI><TIMESTAMPS ACTUAL>.csv
        Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.

    Aclaracion: En la descripción de los campos, falta el campo TIPO, que es un string 
        que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO"
"""
parser = argparse.ArgumentParser("""Ingresa Nombre del archivo csv, DNI, Salida,
        Tipo de cheque, Estado de cheque(opcional), Rango de fecha(opcional)""")
parser.add_argument('csv',type=str,help='Ingresa nombre del archivo csv')
parser.add_argument('dni',type=int,help='Ingresa el dni que quieres filtrar')
parser.add_argument('salida',type=str,help='Ingresa tipo de salida (pantalla o csv)')
parser.add_argument('tipocheque',type=str,help='Ingresa el tipo de cheque (emitido o depositado)')
parser.add_argument('-ec','--estadocheque',type=str,help='Ingresa el estado del cheque (pendiente, aprobado, rechazado)',default=None)
parser.add_argument('-rf','--rangofecha',type=str,help='Ingresa un rango de fechas con el formato: xx-xx-xxxx:yy-yy-yyyy')

args = parser.parse_args()

def escribir():
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

def leer(archivo, dni, salida, tipoCheque, estadoCheque, rangoFecha="01-01-0000:31-12-9999"):
    diccionario = {}
    with open(f"template\{archivo}", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        generarDiccionarioCSV(f,reader, diccionario)
        f.close()
        print(diccionario)
        resultado = diccionario.get(str(dni))
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
        print("\nLa salida es pantalla\n")
        print(resultado)

if(args.rangofecha):
    leer(args.csv, args.dni, args.salida,args.tipocheque,args.estadocheque,args.rangofecha)
else:
    leer(args.csv, args.dni, args.salida,args.tipocheque,args.estadocheque)
# leer("test.csv","40998788","PantaLla",123)
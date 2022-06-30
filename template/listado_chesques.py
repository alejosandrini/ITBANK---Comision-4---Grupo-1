import csv
"""
    2)El csv de datos tiene: NroCheque,CodigoBanco,CodigoScurusal,
        NumeroCuentaOrigen,NumeroCuentaDestino,Valor,FechaOrigen,
        FechaPago,DNI,Tipo,Estado
    3)Si se repite numero de cheque --> error por pantalla
    4)El csv de respuesta debe tener: nombre del archivo <DNI><TIMESTAMPS ACTUAL>.csv
        Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.

    Aclaracion: En la descripción de los campos, falta el campo TIPO, que es un string 
        que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO"
"""

def escribir():
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

def leer(archivo, dni, salida, tipoCheque, estadoCheque="todos", rangoFecha="01-01-0000:31-12-9999"):
    with open(f"template\{archivo}", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# leer("test.csv",123,132,123)
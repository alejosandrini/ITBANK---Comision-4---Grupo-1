import csv
"""
    2)Recibir argumentos por consola: Nombre del archivo csv, DNI, Salida,
        Tipo de cheque, Estado de cheque(opcional), Rango de fecha(opcional)
    4)El csv de respuesta debe tener: nombre del archivo <DNI><TIMESTAMPS ACTUAL>.csv
        Se tiene que exportar las dos fechas, el valor del cheque y la cuenta.

    Aclaracion: En la descripción de los campos, falta el campo TIPO, que es un string 
        que puede tener los siguientes valores  "EMITIDO" o "DEPOSITADO"
"""
def escribir():
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

def leer(archivo, dni, salida, tipoCheque, estadoCheque="todos", rangoFecha="01-01-0000:31-12-9999"):
    diccionario = {}
    with open(f"template\{archivo}", newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        generarDiccionarioCSV(reader, diccionario)
        f.close()
        print(diccionario)

def generarDiccionarioCSV(reader, diccionario):
    for NroCheque,CodBanco,CodiScurusal,NroCuentaOrigen,NroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado in reader:
        datos = [NroCheque,CodBanco,CodiScurusal,NroCuentaOrigen,NroCuentaDestino,Valor,FechaOrigen,FechaPago,DNI,Tipo,Estado]
        if(DNI in diccionario):
            try:
                verificarChequeRepetido(diccionario.get(DNI), NroCheque, NroCuentaOrigen)
            except ValueError:
                print(f"Error-->El cheque con nro:{NroCheque} se encuentra repetido en la cuenta: {NroCuentaOrigen}")
                exit()
            diccionario[DNI].append(datos)
        else:
            diccionario[DNI] = [datos]

def verificarChequeRepetido(datos, NroCheque, NroCuentaOrigen):
    for dato in datos:
        if (NroCheque in dato and NroCuentaOrigen in dato):
            raise ValueError

leer("test.csv",123,132,123)
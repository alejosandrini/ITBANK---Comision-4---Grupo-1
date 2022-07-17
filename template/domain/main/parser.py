import json
from clientes.cliente import *
class Parser():
    def generarCliente(path):
        with open(f".\entradas-salidas\{path}",'r', newline='', encoding='utf-8') as f:
            obj = json.load(f)
        f.close()
        if(obj['tipo'].upper() == "BLACK"):
            cliente = Black(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'])
        elif(obj['tipo'].upper() == "GOLD"):
            cliente = Gold(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'])
        elif(obj['tipo'].upper() == "CLASSIC"):
            cliente = Classic(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'])
        else:
            raise ValueError("Tipo de cuenta invalido")
        return cliente


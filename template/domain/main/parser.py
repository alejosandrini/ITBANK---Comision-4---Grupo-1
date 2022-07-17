import json
from clientes.cliente import *
from clientes.direccion import Direccion
class Parser():
    def generarCliente(path):
        with open(f".\entradas-salidas\{path}",'r', newline='', encoding='utf-8') as f:
            obj = json.load(f)
        f.close()
        obj_dir = obj['direccion']
        direccion = Direccion(obj_dir['calle'],obj_dir['numero'],obj_dir['ciudad'],obj_dir['provincia'],obj_dir['pais'])
        if(obj['tipo'].upper() == "BLACK"):
            cliente = Black(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'], direccion)
        elif(obj['tipo'].upper() == "GOLD"):
            cliente = Gold(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'], direccion)
        elif(obj['tipo'].upper() == "CLASSIC"):
            cliente = Classic(obj['nombre'], obj['apellido'], obj['numero'], obj['dni'], direccion)
        else:
            raise ValueError("Tipo de cuenta invalido")
        return cliente


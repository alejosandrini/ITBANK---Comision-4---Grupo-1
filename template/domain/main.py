import sys
from main.parser import Parser
from main.exporter import Exporter

def obtenerJson():
    cliente = Parser.generarCliente(sys.argv[1])
    return cliente
def imprimirHtml(cliente):
    Exporter.generarReporte(cliente)

if __name__ == '__main__':
    cliente = obtenerJson()
    print(cliente)
    imprimirHtml(cliente)

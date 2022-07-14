from template.domain.clientes.cuenta import Cuenta


class Cliente:
    def __init__(self, nombre, apellido, numero, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.max_chequeras = 0
        self.cantidad_chequeras = 0
        self.max_tarjetas_credito = 0
        self.cantidad_tarjetas_credito = 0

    def puede_crear_chequera(self):
        return self.cantidad_chequeras < self.max_chequeras
    def puede_crear_tarjeta_credito(self):
        return self.cantidad_tarjetas_credito < self.max_tarjetas_credito
    def puede_comprar_dolar():
        return False

class Classic(Cliente):
    pass

class Gold(Cliente):
    pass

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.cuenta = Cuenta(100000,None,0,0,10000)
        self.max_chequeras = 2
        self.max_tarjetas_credito = 5

    def puede_comprar_dolar():
        return True
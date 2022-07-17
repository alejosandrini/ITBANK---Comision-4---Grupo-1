from .cuenta import Cuenta


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
        self.max_tarjetas_debito = 0
        self.cantidad_tarjetas_debito = 0


    def puede_crear_chequera(self):
        return self.cantidad_chequeras < self.max_chequeras
    def puede_crear_tarjeta_credito(self):
        return self.cantidad_tarjetas_credito < self.max_tarjetas_credito
    def puede_crear_tarjeta_debito(self):
        return self.cantidad_tarjetas_debito < self.max_tarjetas_debito
    def puede_comprar_dolar():
        return False

class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.cuenta = Cuenta(10000,150000,0,1,0)
        self.max_tarjetas_debito = 1
        self.max_chequeras = 0
        self.max_tarjetas_credito = 0
        
    def puede_comprar_dolar():
        return False

class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.cuenta = Cuenta(20000,500000,0,0,5,10000)
        self.max_tarjetas_debito = 1
        self.max_chequeras = 1
        self.max_tarjetas_credito = 1
        
    def puede_comprar_dolar():
        return False

class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni):
        super().__init__(nombre, apellido, numero, dni)
        self.cuenta = Cuenta(100000,None,0,0,10000)
        self.max_chequeras = 2
        self.max_tarjetas_credito = 5

    def __str__(self):
        return f"Nombre: {self.nombre}"

    def puede_comprar_dolar():
        return True
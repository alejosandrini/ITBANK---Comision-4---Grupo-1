class Razon():
    def __init__(self, type):
        self.type = type
    def resolver(self, cliente, evento):
        pass

class RazonAltaChequera(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)
class RazonAltaTarjetaCredito(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)
class RazonComprarDolar(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)
class RazonRetiroEfectivo(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)
class RazonTransferenciaEnviada(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)
class RazonTransferenciaRecibida(Razon):
    def __init__(self, type):
        super().__init__(type)
    def resolver(self, cliente, evento):
        return super().resolver(cliente, evento)


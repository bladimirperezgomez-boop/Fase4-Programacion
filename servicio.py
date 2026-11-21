
from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass


class ServicioSala(Servicio):

    def __init__(self, horas):
        super().__init__("Sala", 50000)
        self.horas = horas

    def calcular_costo(self, impuesto=0):

        costo = self.costo_base * self.horas

        if impuesto > 0:
            costo = costo + (costo * impuesto)

        return costo

    def describir(self):
        return f"Sala por {self.horas} horas"


class ServicioEquipo(Servicio):

    def __init__(self, dias):
        super().__init__("Equipo", 80000)
        self.dias = dias

    def calcular_costo(self):
        return self.costo_base * self.dias

    def describir(self):
        return f"Equipo por {self.dias} dias"


class ServicioAsesoria(Servicio):

    def __init__(self, horas):
        super().__init__("Asesoria", 120000)
        self.horas = horas

    def calcular_costo(self):
        return self.costo_base * self.horas

    def describir(self):
        return f"Asesoria por {self.horas} horas"

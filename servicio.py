from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, nombre, precio, horas):

        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")

        super().__init__(nombre, precio)
        self.horas = horas

    def calcular_costo(self):
        return self.precio * self.horas

    def descripcion(self):
        return f"Reserva de sala durante {self.horas} horas"


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio, dias):

        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")

        super().__init__(nombre, precio)
        self.dias = dias

    def calcular_costo(self):
        return self.precio * self.dias

    def descripcion(self):
        return f"Alquiler de equipo durante {self.dias} días"


class Asesoria(Servicio):

    def __init__(self, nombre, precio, sesiones):

        if sesiones <= 0:
            raise ValueError("Las sesiones deben ser mayores a 0")

        super().__init__(nombre, precio)
        self.sesiones = sesiones

    def calcular_costo(self):
        return self.precio * self.sesiones

    def descripcion(self):
        return f"Asesoría especializada de {self.sesiones} sesiones"
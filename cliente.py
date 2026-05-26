from excepciones import ClienteError


class Cliente:

    def __init__(self, nombre, correo):

        if nombre.strip() == "":
            raise ClienteError("El nombre está vacío")

        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo
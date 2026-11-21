from excepciones import ClienteInvalidoError


class Cliente:

    def __init__(self, nombre, documento, correo):

        if nombre == "":
            raise ClienteInvalidoError("El nombre está vacío")

        if documento <= 0:
            raise ClienteInvalidoError("Documento inválido")

        if "@" not in correo:
            raise ClienteInvalidoError("Correo inválido")

        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    def mostrar_info(self):

        print("Nombre:", self.nombre)
        print("Documento:", self.documento)
        print("Correo:", self.correo)

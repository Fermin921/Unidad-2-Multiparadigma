from logger_base import log


class Cliente:
    def __init__(self, id=None, nombre=None) -> None:
        self.id = id
        self.nombre = nombre

    def __str__(self) -> str:
        return f"""
        ID Cliente: {self.id}, Nombre: {self.nombre}
        """

    @property
    def idCliente(self):
        return self.id

    @idCliente.setter
    def idCliente(self, id):
        self.id = id

    @property
    def Nombre(self):
        return self.nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self.nombre = nombre


if __name__ == "__main__":
    persona1 = Cliente(1, "Juan")
    log.debug(persona1)

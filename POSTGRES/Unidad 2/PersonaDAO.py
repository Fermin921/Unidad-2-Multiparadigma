# DAO = DATA ACCESS OUT
from Persona import Cliente
from Conexion2 import Conexion
from CursorPoll import CursorDelPool
from logger_base import log


class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM cliente ORDER BY id"
    _INSERTAR = "INSERT INTO cliente (id,nombre) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE cliente set nombre = %s where id = %s"
    _BORRAR = "DELETE FROM cliente where id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                personas.append(Cliente(r[0], r[1]))
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id, persona.nombre)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls, nombre, persona):
        with CursorDelPool() as cursor:
            valores = (nombre, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return persona

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = persona.id
            cursor.execute(cls._BORRAR, valores)
            return cursor.rowcount

    # end def


if __name__ == "__main__":
    persona2 = PersonaDAO.seleccionar()
    for p in persona2:
        log.debug(p)

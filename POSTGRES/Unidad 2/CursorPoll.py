from logger_base import log
from Conexion2 import Conexion


class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Inicio de bloque with")
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_exception, valor_exception, detalle_excepcion):
        log.debug("Se ejecuta exit")
        if valor_exception:
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()

        Conexion.LiberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as Cursor:
        log.debug("Bloque with")
        Cursor.execute("SELECT * FROM cliente")
        log.debug(Cursor.fetchall())

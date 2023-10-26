import psycopg2
from psycopg2 import pool
from logger_base import log


class Conexion:
    _DATABASE = "postgres"
    _USERNAME = "postgres"
    _PASSWORD = "19100209"
    _PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CONEXIONES = 1
    _MAX_CONEXIONES = 5
    _POOL = None

    @classmethod
    def ObtenerPool(cls):
        try:
            if cls._POOL == None:
                cls._POOL = pool.SimpleConnectionPool(
                    cls._MIN_CONEXIONES,
                    cls._MAX_CONEXIONES,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._PORT,
                    database=cls._DATABASE,
                )
                log.debug("Creacion del pool", pool)
                return cls._POOL
            else:
                return cls._POOL

        except Exception as e:
            log.error(e)

    @classmethod
    def ObtenerConexion(cls):
        Conexion = cls.ObtenerPool().getconn()
        log.debug(f"Conexion Realizada {Conexion}")
        return Conexion

    @classmethod
    def LiberarConexion(cls, conexion):
        cls.ObtenerPool().putconn(conexion)
        log.debug(f"Conexion regresada {conexion}")

    @classmethod
    def CerrarConexiones(cls):
        cls.ObtenerPool().closeall()
        log.debug("Conexiones Cerradas")


if __name__ == "__main__":
    conexion1 = Conexion.ObtenerConexion()

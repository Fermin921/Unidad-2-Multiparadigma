import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postgres",
    password="19100209",
    host="127.0.0.1",
    port="5432",
    database="postgres",
)

try:
    with conexion:
        with conexion.cursor() as cursos:
            sentencia = "Update CLIENTE SET Nombre=%s WHERE ID = %s"
            valores = (
                ("Fermin", "1"),
                ("Juan", "2"),
                ("Gerardo", "3"),
                ("Victor", "4"),
                ("Jorge", "5"),
            )
            cursos.executemany(sentencia, valores)
            registrosInsertados = cursos.rowcount
            log.debug("Registros Insertados: {registrosInsertados}")
except Exception as e:
    log.error(e)
    pass
finally:
    conexion.close()

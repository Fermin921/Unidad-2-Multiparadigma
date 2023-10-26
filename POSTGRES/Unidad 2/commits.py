import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="19100209",
    host="127.0.0.1",
    port="5432",
    database="postgres",
)
from logger_base import log

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO cliente(nombre,id) VALUES (%s,%s)"
    valores = ("Jorge", 5)
    cursor.execute(sentencia, valores)
    conexion.commit()
except Exception as e:
    conexion.rollback()
    log.error(e)

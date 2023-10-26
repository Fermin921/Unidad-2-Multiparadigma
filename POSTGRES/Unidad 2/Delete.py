import psycopg2
from logger_base import log

conexion = psycopg2.connect(
    user="postgres",
    password="19100209",
    host="127.0.0.1",
    port="5432",
    database="postgres",
)

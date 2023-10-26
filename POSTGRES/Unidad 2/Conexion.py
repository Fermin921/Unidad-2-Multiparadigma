# Semana 1

import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="19100209",
    host="127.0.0.1",
    port="5432",
    database="postgres",
)

cursor = conexion.cursor()
resultado = cursor.execute("SELECT * FROM public.cliente")
resultado = cursor.fetchall()
print(resultado)

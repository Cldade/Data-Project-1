'''
import psycopg2
import random
from random import randrange
from datetime import timedelta,datetime

def genera_factura ():

    # Abrimos conexión con el servidor de postgresql
    conn = psycopg2.connect(host="localhost", database="root",user = "root",password="root")
    cursor = conn.cursor()

    # Realizamos una consulta para sacar el numero de clientes
    query = "SELECT COUNT(id) FROM cliente"
    cursor.execute(query)
    numero = cursor.fetchall()
    id_cliente = random.randint(1,numero[0][0])
    print(f'Cliente: {id_cliente}')

    # Realizamos una consulta para sacar la fecha
    query = "SELECT COUNT(fecha) FROM venta"
    cursor.execute(query)
    numero = cursor.fetchall()
    fecha = self.random_date(d1, d2)
    print(f'La fecha: {fecha}')

    # Realizamos una consulta para sacar el numero de productos
    query = "SELECT COUNT(unidades_producto) FROM producto"
    cursor.execute(query)
    numero = cursor.fetchall()
    unidades_producto = 

    # Calculamos el importe total


genera_factura()
'''
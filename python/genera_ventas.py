import time
import psycopg2
import random
from random import randrange
from datetime import timedelta,datetime


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def insert_venta(id):
    # Abrimos conexión con el servidor de postgresql
    conn = psycopg2.connect(host="localhost", database="root",user = "root",password="root")
    cursor = conn.cursor()
    # Realizamos una consulta para sacar el numero de clientes
    query = "SELECT COUNT(id) FROM cliente"
    cursor.execute(query)
    numero = cursor.fetchall()
    id_cliente = random.randint(1,numero[0][0])
    print(id_cliente)
    # Realizamos una consulta para sacar el numero de producto
    query = "SELECT COUNT(id_producto) FROM producto"
    cursor.execute(query)
    numero = cursor.fetchall()
    id_producto = random.randint(1,numero[0][0])
    print(id_producto)
    # Realizamos una consulta para sacar el numero de unidades que se consumen
    unidades = random.randint(1,10)
    print(unidades)
    # Realizamos una consulta para sacar la fecha
    d1 = datetime.strptime('1/1/2021', '%d/%m/%Y')
    d2 = datetime.strptime('31/12/2021', '%d/%m/%Y')
    print(random_date(d1, d2))

insert_venta(1)
    
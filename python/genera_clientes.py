from faker import Faker
import random
import psycopg2


def insert_clientes(id):
    #Generamos un nombre y apellido aleatorio para cada cliente
    faker = Faker()
    First_name = str(faker.first_name())
    Last_name = str(faker.last_name())
    print(f'Cliente con nombre: {First_name} y apellido: {Last_name}')
    try:
        conn = psycopg2.connect(host="postgres", database="root",user = "root",password="root", port=5432)
        cursor = conn.cursor()
    except:
        print("Error al conectarnos a la bbdd para insertar clientes")
    try:
        query = "INSERT INTO cliente (id , nombre, apellido) VALUES (%s,%s,%s)"
        record_to_insert = (id, First_name, Last_name)
        cursor.execute(query, record_to_insert)
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error insertando un cliente", error)
    








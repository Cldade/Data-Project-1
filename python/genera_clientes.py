from faker import Faker
import time
import psycopg2

def insert_clientes(id):
    faker = Faker()
    First_name = str(faker.first_name())

    Last_name = str(faker.last_name())
    print(f'Cliente con nombre: {First_name} y apellido: {Last_name}')
    conn = psycopg2.connect(host="localhost", database="root",user = "root",password="root")
    cursor = conn.cursor()
    query = "INSERT INTO cliente (id , nombre, apellido) VALUES (%s,%s,%s)"
    record_to_insert = (id, First_name, Last_name)
    cursor.execute(query, record_to_insert)
    conn.commit()
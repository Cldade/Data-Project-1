from faker import Faker
import random
import psycopg2


def insert_clientes(id):
    #Lista con las provincias españolas
    provincias=["Álava", "Albacete", "Alicante", "Almería", "Asturias", "Ávila", "Badajoz", "Barcelona", "Burgos", "Cáceres", "Cádiz", "Cantabria", "Castellón", "Ciudad Real", "Córdoba", "Cuenca", "Gerona", "Granada", "Guadalajara", "Guipúzcoa", "Huelva", "Huesca", "Islas Baleares", "Jaén", "La Coruña", "La Rioja", "Las Palmas", "León", "Lérida", "Lugo", "Madrid", "Málaga", "Murcia", "Navarra", "Orense", "Palencia", "Pontevedra", "Salamanca", "Santa Cruz de Tenerife", "Segovia", "Sevilla", "Soria", "Tarragona", "Teruel", "Toledo", "Valencia", "Valladolid", "Vizcaya", "Zamora", "Zaragoza"];
    provincia = random.choice(provincias)
    #Generamos un nombre y apellido aleatorio para cada cliente
    faker = Faker()
    First_name = str(faker.first_name())
    Last_name = str(faker.last_name())
    print(f'Cliente con nombre: {First_name} y apellido: {Last_name}, de la provincia: {provincia}')
    try:
        conn = psycopg2.connect(host="postgres", database="root",user = "root",password="root", port=5432)
        cursor = conn.cursor()
    except:
        print("Error al conectarnos a la bbdd para insertar clientes")
    try:
        query = "INSERT INTO cliente (id , nombre, apellido, provincia) VALUES (%s,%s,%s,%s)"
        record_to_insert = (id, First_name, Last_name, provincia)
        cursor.execute(query, record_to_insert)
        conn.commit()
    except(Exception, psycopg2.Error) as error:
        print("Error insertando un cliente", error)
    








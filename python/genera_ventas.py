import psycopg2
import random
from random import randrange
from datetime import timedelta,datetime

#Clase que genera ventas sin tener en cuenta los influencers
class genera_ventas_antes_influencer:

    #Función que genera fechas aleatorias entre dos fechas dadas
    def random_date(self,start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    #Función que busca si un producto ya ha sido comprado por el cliente 
    def producto_ya_comprado(self, id_producto, lista_productos):
        encontrado = False
        for p in lista_productos:
            if p == id_producto: 
                encontrado = True
                break
        return encontrado
    
    #Función que crea las facturas
    def insertar_factura(self, id, fecha, numero_productos, total_unidades, importe_total):
        # Abrimos conexión con el servidor de postgresql
        conn = psycopg2.connect(host="postgres", port=5432, database="root",user = "root",password="root")
        cursor = conn.cursor()
        query = "INSERT INTO factura (id, id_venta, fecha, numero_productos, unidades, importe_total) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(id, id, fecha, numero_productos, total_unidades, importe_total))
        conn.commit()
        cursor.close()

    #Función que calcula la información de las ventass y las inserta
    def insert_venta(self, id):

        # Abrimos conexión con el servidor de postgresql
        conn = psycopg2.connect(host="postgres",port=5432, database="root",user = "root",password="root")
        cursor = conn.cursor()

        # Realizamos una consulta para sacar el numero de clientes
        query = "SELECT COUNT(id) FROM cliente"
        cursor.execute(query)
        numero = cursor.fetchall()
        #Elegimos un cliente aleatorio
        id_cliente = random.randint(1,numero[0][0])
        print(f'Cliente: {id_cliente}')

        #Escogemos una fecha random entre el 01/01/2021 al 31/12/2021
        d1 = datetime.strptime('1/1/2021', '%d/%m/%Y')
        d2 = datetime.strptime('31/12/2021', '%d/%m/%Y')
        fecha = self.random_date(d1, d2)
        print(f'La fecha: {fecha}')

        #Generamos un número aleatorio para saber si el cliente solo va a comprar un producto o más de un producto
        numero_productos = random.randint(1,5)
        n = numero_productos
        print(f'El número de productos a comprar es: {numero_productos}')

        #Creamos una lista con los productos comprados por el cliente
        productos_comprados = list()
        #Variable que guarda el total de unidades
        total_unidades = 0
        #Variable que guarda el importe total de la venta
        importe_total = 0

        #Bucle para calcular los datos de cada venta por producto
        while n != 0:

            # Realizamos una consulta para sacar el numero de producto
            query = "SELECT COUNT(id_producto) FROM producto"
            cursor.execute(query)
            numero = cursor.fetchall()
            id_producto = random.randint(1,numero[0][0])
            #Buscamos un producto que aun no haya comprado el cliente
            while self.producto_ya_comprado(id_producto, productos_comprados) is True:
                id_producto = random.randint(1,numero[0][0])
            productos_comprados.append(id_producto)
            print(f'El producto: {id_producto}')

            # Realizamos una consulta para sacar el numero de unidades que se consumen del producto
            unidades_producto = random.randint(1,10)
            print(f'Número de unidades: {unidades_producto}')
            total_unidades += unidades_producto

            #Calculamos el beneficio para IKEA
            cursor.execute("SELECT precio_venta, coste FROM producto WHERE id_producto = %s",[id_producto])
            precio_coste = cursor.fetchall()
            print(f'Con precio: {precio_coste[0][0]} y coste: {precio_coste[0][1]}')
            beneficioIkea = (precio_coste[0][0] - precio_coste[0][1]) * unidades_producto
            print(f'El benefico para IKEA es de: {beneficioIkea}')
            importe_total += precio_coste[0][0]

            #Insertamos esta compra en la tabla venta
            venta = (id, id_cliente, id_producto, unidades_producto, fecha, 0, beneficioIkea)
            cursor.execute("insert into venta (id, id_cliente, id_producto, unidades_producto, fecha, beneficio_influencer, beneficio_ikea) values (%s,%s,%s,%s,%s,%s,%s)",venta )
            conn.commit()

            n -= 1
        #Llamada a la función que inserta la factura de la venta
        self.insertar_factura(id,fecha,numero_productos, total_unidades, importe_total)
        conn.close()

#Clase que genera ventas teniendo en cuenta a los influencers
class genera_ventas_despues_influencer:

    #Función que genera fechas aleatorias entre dos fechas dadas
    def random_date(self,start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    #Función que busca si un producto ya ha sido comprado por el cliente 
    def producto_ya_comprado(self, id_producto, lista_productos):
        encontrado = False
        for p in lista_productos:
            if p == id_producto: 
                encontrado = True
                break
        return encontrado

    #Función que crea las facturas
    def insertar_factura(self, id, fecha, numero_productos, total_unidades, importe_total):
        # Abrimos conexión con el servidor de postgresql
        conn = psycopg2.connect(host="postgres", database="root",user = "root",password="root")
        cursor = conn.cursor()
        query = "INSERT INTO factura (id, id_venta, fecha, numero_productos, unidades, importe_total) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(id, id, fecha, numero_productos, total_unidades, importe_total))
        conn.commit()
        cursor.close()


    def insert_venta(self, id):

        # Abrimos conexión con el servidor de postgresql
        conn = psycopg2.connect(host="postgres", database="root",user = "root",password="root")
        cursor = conn.cursor()

        # Realizamos una consulta para sacar el numero de clientes
        query = "SELECT COUNT(id) FROM cliente"
        cursor.execute(query)
        numero = cursor.fetchall()
        id_cliente = random.randint(1,numero[0][0])
        print(f'Cliente: {id_cliente}')
        
        # Realizamos una consulta para sacar la fecha
        d1 = datetime.strptime('1/1/2022', '%d/%m/%Y')
        d2 = datetime.strptime('3/12/2022', '%d/%m/%Y')
        fecha = self.random_date(d1, d2)
        print(f'La fecha: {fecha}')

        #Generamos un número aleatorio para saber si el cliente solo va a comprar un producto o más de un producto
        numero_productos = random.randint(1,5)
        n = numero_productos
        print(f'El número de productos a comprar es: {numero_productos}')
        productos_comprados = list()
        total_unidades = 0
        importe_total = 0
        while n != 0:

            # Realizamos una consulta para sacar el numero de producto
            query = "SELECT COUNT(id_producto) FROM producto"
            cursor.execute(query)
            numero = cursor.fetchall()
            id_producto = random.randint(1,numero[0][0])
            while self.producto_ya_comprado(id_producto, productos_comprados) is True:
                id_producto = random.randint(1,numero[0][0])
            productos_comprados.append(id_producto)
            print(f'El producto: {id_producto}')

            # Realizamos una consulta para sacar el numero de unidades que se consumen del producto
            unidades_producto = random.randint(1,10)
            print(f'Número de unidades: {unidades_producto}')
            total_unidades += unidades_producto

            #Calculamos el beneficio para el influencer
            cursor.execute("SELECT precio_venta, id_influencer FROM producto WHERE id_producto = %s",[id_producto])
            precio_influencer = cursor.fetchall()
            cursor.execute("SELECT porcentaje FROM influencer WHERE id = %s",[precio_influencer[0][1]])
            porcentaje = cursor.fetchall()
            print(f'Con precio: {precio_influencer[0][0]} y es del influencer: {precio_influencer[0][1]}, y el porcenteje por venta es: {porcentaje[0][0]}')
            beneficioInfluencer = precio_influencer[0][0] * unidades_producto * porcentaje[0][0]
            importe_total += precio_influencer[0][0] * unidades_producto

            #Calculamos el beneficio para IKEA
            cursor.execute("SELECT precio_venta, coste FROM producto WHERE id_producto = %s",[id_producto])
            precio_coste = cursor.fetchall()
            print(f'Con precio: {precio_coste[0][0]} y coste: {precio_coste[0][1]}')
            beneficioIkea = (precio_coste[0][0] - precio_coste[0][1]) * unidades_producto
            print(f'El benefico para IKEA es de: {beneficioIkea}')

            #Insertamos esta compra en la tabla venta
            venta = (id, id_cliente, id_producto, unidades_producto, fecha, beneficioInfluencer, beneficioIkea)
            cursor.execute("insert into venta (id, id_cliente, id_producto, unidades_producto, fecha, beneficio_influencer, beneficio_ikea) values (%s,%s,%s,%s,%s,%s,%s)",venta )
            conn.commit()

            n -= 1
        self.insertar_factura(id,fecha, numero_productos, total_unidades, importe_total)
        conn.close()
    

class numero_venta:
    def numero_ventas(self):
        # Abrimos conexión con el servidor de postgresql
        conn = psycopg2.connect(host="postgres", database="root",user = "root",password="root")
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM venta"
        cursor.execute(query)
        numero_ventas = cursor.fetchall()
        cursor.close()
        return numero_ventas[0][0]



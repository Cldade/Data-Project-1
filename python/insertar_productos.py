import csv
import psycopg2


class insert_in_db_productos:
    def load_csv_Productos(self):
        self.archivo = open(r"csv/Productos.csv", encoding="utf8", errors='ignore')

        self.filas = csv.reader(self.archivo, delimiter = ";")
        self.lista = list(self.filas)
        del (self.lista[0])
        self.productos = tuple(self.lista)
        for rw in self.productos:
            print(rw)


    def insert_productos(self):
        self.connection = psycopg2.connect(host="bbdd_postgresql",port=5433, database="root",user = "root",password="root")
        self.cursor = self.connection.cursor()
        self.cursor.executemany ("insert into producto (id_producto, nombre, stock, color, precio_venta, coste, categoria, id_influencer, link_producto, link_linea) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", self.productos)
        self.connection.commit()
        self.connection.close()
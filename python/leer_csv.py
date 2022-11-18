import csv
import psycopg2

class insert_in_db_influencer:

    def load_csv_Influencers(self):
        self.archivo = open(r"Data-Project-1/csv/Influencers.csv", encoding="utf8", errors='ignore')
        self.filas = csv.reader(self.archivo, delimiter = ";")
        self.lista = list(self.filas)
        del (self.lista[0])
        self.tuplas = tuple (self.lista)
        for rw in self.tuplas:
            print(rw)

    def insert_influencer(self):
        self.connection = psycopg2.connect(host="localhost", database="root",user = "root",password="root")
        self.cursor = self.connection.cursor()
        self.cursor.executemany ("insert into influencer (id, nombre, apellido, porcentaje) values (%s,%s,%s,%s)", self.tuplas)
        self.connection.commit()
        self.connection.close()

ins_db = insert_in_db_influencer()
ins_db.load_csv_Influencers()
ins_db.insert_influencer()

class insert_in_db_productos:
    def load_csv_Productos(self):
        self.archivo = open(r"Data-Project-1/csv/Productos.csv", encoding="utf8", errors='ignore')

        self.filas = csv.reader(self.archivo, delimiter = ";")
        self.lista = list(self.filas)
        del (self.lista[0])
        self.tuplas = tuple (self.lista)
        for rw in self.tuplas:
            print(rw)


    def insert_productos(self):
        self.connection = psycopg2.connect(host="localhost", database="root",user = "root",password="root")
        self.cursor = self.connection.cursor()
        self.cursor.executemany ("insert into producto (id_producto, nombre, stock, color, precioventa, coste, categoria, id_influencer, link_producto, link_linea) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", self.tuplas)
        self.connection.commit()
        self.connection.close()
    
ins_db = insert_in_db_productos()
ins_db.load_csv_Productos()
ins_db.insert_productos()



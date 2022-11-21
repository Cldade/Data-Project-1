import csv
import psycopg2

class insert_in_db_influencer:

    def load_csv_Influencers(self):
        self.archivo = open(r"csv/Influencers.csv", encoding="utf8", errors='ignore')
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

# Esto creo que irá en el main:
ins_db = insert_in_db_influencer()
ins_db.load_csv_Influencers()
ins_db.insert_influencer()



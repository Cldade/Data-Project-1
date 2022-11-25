import csv
import psycopg2

class insert_in_db_influencer:

    def load_csv_Influencers(self):
        self.archivo = open(r"csv/Influencers.csv", encoding="utf8", errors='ignore')
        self.filas = csv.reader(self.archivo, delimiter = ";")
        self.lista = list(self.filas)
        del (self.lista[0])
        self.influencers = tuple(self.lista)
        for rw in self.influencers:
            print(rw)

    def insert_influencer(self):
        while True:
            try:
                self.connection = psycopg2.connect(host="postgres",port=5432, database="root",user = "root",password="root")
                self.cursor = self.connection.cursor()
                self.cursor.executemany ("insert into influencer (id, nombre, apellido, porcentaje) values (%s,%s,%s,%s)", self.influencers)
                self.connection.commit()
                self.connection.close()
                break
            except(Exception, psycopg2.Error) as error:
                print('Unable to connect', error)
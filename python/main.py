<<<<<<< Updated upstream
import psycopg2
=======
import insertar_influencers as influencer
import insertar_productos as producto
import genera_clientes as cliente
import genera_ventas as venta
import genera_factura as factura
>>>>>>> Stashed changes



conn = psycopg2.connect(
    host="localhost",
    database="root",
    user = "root",
    password="root")
#Open a cursor to perform database operations
cursor = conn.cursor()
#Execute a query
query = "INSERT INTO student (id , name) VALUES (%s,%s)"
record_to_insert = (6, 'javi')
cursor.execute(query, record_to_insert)


<<<<<<< Updated upstream

conn.commit()
count = cursor.rowcount
print(count, "Record inserted succesfully into table")
conn.close()
=======
#Guardamos ventas con datos de influencers en bbdd
ventas_despues_influencer = venta.genera_ventas_despues_influencer()
numero_v = venta.numero_venta()
n = 0
id_v_i = numero_v.numero_ventas() + 1
while n < 100:
    ventas_despues_influencer.insert_venta(id_v_i)
    n += 1
    id_v_i += 1

#Guardamos datos en las facturas
factura = factura.genera_factura()
>>>>>>> Stashed changes

import insertar_influencers as influencer
import insertar_productos as producto
import genera_clientes as cliente
import genera_ventas as venta

#Guardamos los influencers en la bbdd
ins_db = influencer.insert_in_db_influencer()
ins_db.load_csv_Influencers()
ins_db.insert_influencer()

#Guardamos los productos en la bbdd
ins_db = producto.insert_in_db_productos()
ins_db.load_csv_Productos()
ins_db.insert_productos()

#Guardamos clientes aleatorios en bbdd
clientes = 1
id_c = 1
while clientes < 1500:
    cliente.insert_clientes(id_c)
    clientes += 1
    id_c += 1

#Guardamos ventas sin datos de los influencers en bbdd
ventas_antes_influencer = venta.genera_ventas_antes_influencer()
n = 0
id_v = 1
while n < 2000:
    ventas_antes_influencer.insert_venta(id_v)
    n += 1
    id_v += 1

#Guardamos ventas con datos de influencers en bbdd
ventas_despues_influencer = venta.genera_ventas_despues_influencer()
numero_v = venta.numero_venta()
n = 0
id_v_i = numero_v.numero_ventas() + 1
while n < 3000:
    ventas_despues_influencer.insert_venta(id_v_i)
    n += 1
    id_v_i += 1
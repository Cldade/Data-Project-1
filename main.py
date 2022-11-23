import psycopg2

conn = psycopg2.connect(host="localhost",database="ejemplodocker",user = "postgres",password="pasword")
#Open a cursor to perform database operations
cursor = conn.cursor()
#Execute a query
query = "INSERT INTO clientes (id , nombre) VALUES (%s,%s)"
record_to_insert = (6, 'javi')
cursor.execute(query, record_to_insert)

conn.commit()
count = cursor.rowcount
print(count, "Record inserted succesfully into table")
conn.close()


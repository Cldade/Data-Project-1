import psycopg2


conn = psycopg2.connect(
    host="postgres",
    database="root",
    user = "root",
    password="root")
#Open a cursor to perform database operations
cursor = conn.cursor()
#Execute a query
query = "INSERT INTO student (id , name) VALUES (%s,%s)"
record_to_insert = (7, 'javi')
cursor.execute(query, record_to_insert)


conn.commit()
count = cursor.rowcount
print(count, "Record inserted succesfully into table")
conn.close()
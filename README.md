
# Data-Project-1

Primer data project del máster en Data Analytics

Cliente : IKEA

Caso de estudio : Nueva línea de negocio basada en la monetización de las ventas de los productos generadas por una serie de influencers en España.

Objetivo:
Generar un programa que permita analizar y proyectar la viabilidad del estudio.

Supuestos:
- Los influencers generan ventas a la compañía y a cambio recibirán una reward o monetización a cambio por producto vendido (en un % asignado).
- Comparativa de las ventas de Ikea con influencers y sin ellos.(Viabilidad)

# Justificación de las herramientas utilizadas:
--Ingestión de datos--
Lenguaje Python 
Herramienta utilizada para el desarrollo de este programa, lenguaje interpretado de fácil uso y comprensión para los técnicos de la compañía.

Se utiliza con el fin de recoger los datos que hay en los csv con la información de los productos e influencers que se han importado,también de generar los datos de los clientes y las facturas así como de simular las ventas e introducir todos estos datos en un contenedor Docker. 

Con el comando docker compose up se levanta el contenedor.

Posteriormente se levanta un servidor y una base de datos en postgreSQL con todo este código introducido en el container de Docker.
Mediante la conexión al puerto localhost:80:80 en el navegador se permite la visualización de todos estos datos en pgadmin.

Se debe introducir el correo y la clave: 
# PGADMIN_DEFAULT_EMAIL: "root@root.com"
# PGADMIN_DEFAULT_PASSWORD: "root"

--Almacenamiento de los Datos--
Docker

El uso de esta herramienta se debe a que sus puntos más fuertes son la portabilidad, el aislamiento, la seguridad y el ahorro de tiempo, por lo que facilita mucho el desarrollo y testeo de aplicaciones.  

PostgreSQL
Base de datos utilizada de software abierto,tiene mucho que ofrecer como sistema de gestión de bases de datos. Se ha ganado su reputación de robustez de funciones, alta fiabilidad, rendimiento, flexibilidad y facilidad de replicación, entre otras cosas. 

--Visualización de los Datos--
Tableau
Mediante una conexión a la base de datos de postgreSQL, se importan los datos a la herramienta Tableau, desde esta plataforma se permite llevar a cabo el uso de los datos y su transformación en gráficos aportando valor a la empresa, visualmente se puede observar la información de una forma clara, sencilla y sintetizada.

# Video explicativo del caso en el siguiente enlace:
# Origen de los datos :
Utilizamos como dataset una muestra del top 5 influencers más influyentes de España.
Utilizamos como dataset una muestra de los 23 productos de IKEA más comprados para realizar nuestro estudio.
Generamos datos aleatorios de los clientes con el fin de simular las ventas de los productos que producen los influencers con el fin de poder ofrecer una respuesta al caso.


# Modelo de datos
Modelo de datos descriptivo - ya que se quiere cuantificar las relaciones en los datos para clasificar variables en grupos.

# Diagrama, diseño arquitectura

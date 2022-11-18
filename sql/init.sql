--
--PostgreSQL database 
--

CREATE TABLE cliente
(
    id bigint NOT NULL,
    nombre varchar(15) ,
    apellido varchar(30),
    CONSTRAINT cliente_pkey PRIMARY KEY (id)
);

CREATE TABLE producto
(
    id bigint NOT NULL,
    nombre varchar(15)
    stock INT NOT NULL,
    color varchar(10) NOT NULL,
    material varchar(10),
    precio decimal NOT NULL,
    CONSTRAINT producto_pkey PRIMARY KEY (id)
);

CREATE TABLE venta
(
    id bigint NOT NULL,
    id_cliente bigint NOT NULL,
    id_producto bigint NOT NULL,
    unidadesProducto INT NOT NULL,
    fecha timestamp NOT NULL,
    CONSTRAINT venta_pkey PRIMARY KEY (id)
);

alter table venta
   add constraint FK_venta_cliente
   foreign key (id_cliente)
   references cliente(id);
   
alter table venta
   add constraint FK_venta_producot
   foreign key (id_producto)
   references producto(id);

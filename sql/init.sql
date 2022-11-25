--
--PostgreSQL database 
--

CREATE TABLE cliente
(
    id bigint NOT NULL,
    nombre varchar(30) ,
    apellido varchar(30),
    CONSTRAINT cliente_pkey PRIMARY KEY (id)
);

CREATE TABLE influencer
(
    id bigint NOT NULL,
    nombre varchar(15) ,
    apellido varchar(30),
    porcentaje decimal NOT NULL,
    CONSTRAINT influencer_pkey PRIMARY KEY (id)
);

CREATE TABLE producto
(
    id_producto bigint NOT NULL,
    nombre varchar(15),
    stock INT NOT NULL,
    color varchar(10) NOT NULL,
    precio_venta decimal NOT NULL,
    coste decimal NOT NULL,
    categoria varchar(20) NOT NULL,
    id_influencer int,
    link_producto varchar(300),
    link_linea varchar(300),
    CONSTRAINT producto_pkey PRIMARY KEY (id_producto)
);

alter table producto
   add constraint FK_venta_cliente
   foreign key (id_influencer)
   references influencer(id);

CREATE TABLE venta
(
    id bigint NOT NULL,
    id_cliente bigint NOT NULL,
    id_producto bigint NOT NULL,
    unidades_producto INT NOT NULL,
    fecha timestamp NOT NULL,
    beneficio_influencer decimal,
    beneficio_ikea decimal,
    CONSTRAINT venta_pkey PRIMARY KEY (id, id_producto)
);

alter table venta
   add constraint FK_venta_cliente
   foreign key (id_cliente)
   references cliente(id);
   
alter table venta
   add constraint FK_venta_producot
   foreign key (id_producto)
   references producto(id_producto);

CREATE TABLE factura
(
    id bigint NOT NULL,
    id_venta int NOT NULL,
    fecha date NOT NULL,
    numero_productos int NOT NULL,
    unidades bigint NOT NULL,
    importe_total decimal NOT NULL,
    CONSTRAINT factura_pkey PRIMARY KEY (id)
);

alter table factura
   add constraint FK_factura_venta
   foreign key (id_venta)
   references venta(id);
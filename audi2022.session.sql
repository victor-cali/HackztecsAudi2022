CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    tipo_usuario varchar(15)  NOT NULL CHECK (tipo_usuario IN ('salida', 'inhouse', 'administrador')), 
    PRIMARY KEY (id_usuario)
);
CREATE TABLE IF NOT EXISTS Contenedor (
    id_contenedor INT NOT NULL AUTO_INCREMENT,
    lt INT,
    alto FLOAT,
    ancho FLOAT,
    largo FLOAT,
    costo FLOAT,
    PRIMARY KEY (id_contenedor)
);
CREATE TABLE IF NOT EXISTS Proveedor (
    duns INT UNIQUE NOT NULL,
    nombre VARCHAR(100),
    pais VARCHAR(10),
    postal INT(10),
    ciudad VARCHAR(30),
    zona INT,
    subzona VARCHAR(15),
    PRIMARY KEY (duns)
);
CREATE TABLE IF NOT EXISTS Parte (
    id_parte INT NOT NULL AUTO_INCREMENT,
    num_parte VARCHAR(20) NOT NULL,
    num_parte_index VARCHAR(20) NOT NULL,
    descripcion VARCHAR(100) NOT NULL,
    alto FLOAT,
    largo FLOAT,
    ancho FLOAT,
    peso FLOAT,
    duns INT,
    FOREIGN KEY (duns) REFERENCES Proveedor(duns),
    PRIMARY KEY (id_parte)
);
CREATE TABLE IF NOT EXISTS Reporte (
    id_reporte INT NOT NULL AUTO_INCREMENT,
    fecha DATE,
    reporte VARCHAR(150),
    PRIMARY KEY (id_reporte)
);
CREATE TABLE IF NOT EXISTS Registro (
    id_registro INT NOT NULL AUTO_INCREMENT,
    id_parte INT,
    partes_por_carro INT,
    ebr INT CHECK (ebr <= 100 AND ebr >= 0),
    carros_por_dia INT,
    duns INT,
    tipo_lt VARCHAR(15),
    lt INT,
    contenedores_por_pallet INT,
    partes_por_contenedor INT,
    gebinde VARCHAR(25),
    pallet INT,
    top INT,
    ftl_o_ltl VARCHAR(3) CHECK (ftl_o_ltl IN ('FTL', 'LTL')),
    pickup_frec INT,
    vollgut FLOAT,
    leergut FLOAT,
    supplier FLOAT,
    inhouse FLOAT,
    trailer_yard FLOAT,
    wh_vollgut FLOAT,
    wh_leergut FLOAT,
    FOREIGN KEY (id_parte) REFERENCES Parte(id_parte),
    FOREIGN KEY (duns) REFERENCES Proveedor(duns),
    PRIMARY KEY (id_registro)
);
CREATE TABLE IF NOT EXISTS Movimiento (
    id_movimiento INT NOT NULL AUTO_INCREMENT,
    fecha DATE NOT NULL,
    tipo_movimiento VARCHAR(25) NOT NULL CHECK (tipo_movimiento IN ('salida', 'entrada')),
    duns INT NOT NULL, 
    cantidad INT NOT NULL,

    FOREIGN KEY (duns) REFERENCES Proveedor(duns),
    PRIMARY KEY (id_movimiento)
)
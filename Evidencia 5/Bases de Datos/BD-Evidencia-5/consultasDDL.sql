-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS SmartHome;
USE SmartHome;

-- Tabla de usuarios
CREATE TABLE Usuario (
    email VARCHAR(100) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contraseña VARCHAR(100) NOT NULL
);

-- Tabla de viviendas
CREATE TABLE Vivienda (
    id_vivienda INT AUTO_INCREMENT PRIMARY KEY,
    nombre_vivienda VARCHAR(100),
    ubicacion VARCHAR(150),
    email_usuario VARCHAR(100),
    FOREIGN KEY (email_usuario) REFERENCES Usuario(email)
);

-- Tabla de dispositivos
CREATE TABLE Dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY,
    nombre_dispositivo VARCHAR(100),
    tipo VARCHAR(50),
    estado VARCHAR(50),
    id_vivienda INT,
    FOREIGN KEY (id_vivienda) REFERENCES Vivienda(id_vivienda)
);


-- Tabla de automatizaciones
CREATE TABLE Automatizacion (
    id_auto INT,
    id_dispositivo INT,
    condicion VARCHAR(150),
    accion VARCHAR(150),
    PRIMARY KEY (id_auto, id_dispositivo),
    FOREIGN KEY (id_auto) REFERENCES Auto(id_auto),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo)
);

-- Tabla de eventos de dispositivos
CREATE TABLE EventoDispositivo (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_dispositivo INT,
    email VARCHAR(100),
    fecha_hora DATETIME,
    detalle VARCHAR(200),
    valor VARCHAR(100),
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
    FOREIGN KEY (email) REFERENCES Usuario(email)
);

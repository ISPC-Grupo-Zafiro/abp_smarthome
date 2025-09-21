INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (1, 'ana@mail.com', '2025-09-10 14:00', 'Temperatura alta', '32°C');
INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (2, 'ana@mail.com', '2025-09-10 20:00', 'Luz encendida', 'ON');
INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (3, 'bruno@mail.com', '2025-09-10 15:30', 'Movimiento detectado', 'Sí');
INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (4, 'carla@mail.com', '2025-09-10 16:00', 'Ventilador encendido', 'ON');
INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (5, 'david@mail.com', '2025-09-10 19:00', 'Gas detectado', 'Sí');
INSERT INTO EventoDispositivo (id_dispositivo, email, fecha_hora, detalle, valor) VALUES (6, 'emma@mail.com', '2025-09-10 07:00', 'Luz apagada', 'OFF');

-- Aquí agregué 6 insert para cada tabla restantes --
INSERT INTO Usuario (email, nombre, contraseña) VALUES ('ana@mail.com', 'Ana', '1234'),('bruno@mail.com', 'Bruno', '1234'),('carla@mail.com', 'Carla', '1234'),('david@mail.com', 'David', '1234'),('emma@mail.com', 'Emma', '1234'),('franco@mail.com', 'Franco', '1234');
INSERT INTO Vivienda (nombre_vivienda, ubicacion, email_usuario) VALUES ('Casa Ana', 'Córdoba Capital', 'ana@mail.com'),('Casa Bruno', 'Rosario Centro', 'bruno@mail.com'),('Casa Carla', 'Mendoza Sur', 'carla@mail.com'),('Casa David', 'Salta Norte', 'david@mail.com'),('Casa Emma', 'Buenos Aires Oeste', 'emma@mail.com'),('Casa Franco', 'La Plata', 'franco@mail.com');
INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado, id_vivienda) VALUES ('Sensor Temperatura Ana', 'Temperatura', 'Activo', 1),('Luz Sala Ana', 'Luz', 'Activo', 1),('Sensor Movimiento Bruno', 'Movimiento', 'Activo', 2),('Ventilador Carla', 'Ventilador', 'Activo', 3),('Detector Gas David', 'Gas', 'Activo', 4),('Luz Cocina Emma', 'Luz', 'Inactivo', 5);
INSERT INTO Automatizacion (id_auto, id_dispositivo, condicion, accion) VALUES (1, 1, 'Temperatura > 30°C', 'Encender ventilador'),(2, 2, 'Movimiento detectado', 'Encender luz'),(3, 3, 'Noche y movimiento', 'Encender alarma'),(4, 4, 'Temperatura < 18°C', 'Apagar ventilador'),(5, 5, 'Gas detectado', 'Enviar alerta'),(6, 6, 'Noche', 'Encender luz automáticamente');

-- Aquí va la consulta para cada tabla --

-- 1) Consulta de usuarios: muestra los nombres y correos de todos los usuarios registrados
SELECT nombre, email 
FROM Usuario;

-- 2) Consulta de viviendas: lista el nombre de la vivienda y su ubicación
SELECT nombre_vivienda, ubicacion 
FROM Vivienda;

-- 3) Consulta de dispositivos: devuelve el nombre, el tipo y el estado de cada dispositivo
SELECT nombre_dispositivo, tipo, estado 
FROM Dispositivo;

-- 4) Consulta de automatizaciones: muestra la condición y la acción configurada para cada automatización
SELECT id_auto, condicion, accion 
FROM Automatizacion;



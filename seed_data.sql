-- Script SQL para MariaDB / MySQL
-- Base de datos: tuchile_db

CREATE DATABASE IF NOT EXISTS tuchile_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE tuchile_db;

-- Insertar Cabañas Iniciales
INSERT INTO portal_cabaña (id, nombre, zona, precio_noche, capacidad) VALUES
(1, 'Cabaña El Litoral 01', 'Costera Central', 65000.00, 4),
(2, 'Cabaña El Litoral 02', 'Costera Central', 85000.00, 6),
(3, 'Cabaña Volcán Villarrica', 'Zona Sur', 110000.00, 5),
(4, 'Palafito Lago Llanquihue', 'Zona Sur', 135000.00, 8);

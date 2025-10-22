CREATE DATABASE IF NOT EXISTS registro_empleados;
USE registro_empleados;

CREATE TABLE IF NOT EXISTS empleados (
    id VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO empleados (id, nombre, sexo, correo) VALUES
('EMP001', 'María González López', 'Femenino', 'maria.gonzalez@empresa.com'),
('EMP002', 'Carlos Rodríguez Pérez', 'Masculino', 'carlos.rodriguez@empresa.com');

-- Ver tablas creadas
SHOW TABLES;

-- Ver datos de empleados
SELECT * FROM empleados;

-- Ver estructura de la tabla
DESCRIBE empleados;

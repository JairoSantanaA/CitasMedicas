CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- ID único de usuario
    nombre VARCHAR(100) NOT NULL,       -- Nombre del usuario
    correo VARCHAR(100) NOT NULL UNIQUE, -- Correo electrónico único
    contrasena VARCHAR(255) NOT NULL,    -- Contraseña encriptada
    tipo_usuario ENUM('Paciente', 'Medico', 'Administrador') NOT NULL, -- Tipo de usuario
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Fecha de creación
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Fecha de última actualización
);

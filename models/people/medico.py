CREATE TABLE medicos (
    id INT PRIMARY KEY,  -- ID del médico (clave foránea que referencia a usuarios.id)
    especialidad VARCHAR(100),  -- Especialidad del médico
    consultorio VARCHAR(100),  -- Consultorio del médico
    disponibilidad TEXT,  -- Horarios de disponibilidad
    FOREIGN KEY (id) REFERENCES usuarios(id) ON DELETE CASCADE -- Relación con usuarios
);

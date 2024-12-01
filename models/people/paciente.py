CREATE TABLE pacientes (
    id INT PRIMARY KEY,  -- ID del paciente (clave foránea que referencia a usuarios.id)
    historial_medico TEXT,  -- Historial médico del paciente
    direccion VARCHAR(255),  -- Dirección del paciente
    telefono VARCHAR(15),  -- Teléfono del paciente
    FOREIGN KEY (id) REFERENCES usuarios(id) ON DELETE CASCADE -- Relación con usuarios
);

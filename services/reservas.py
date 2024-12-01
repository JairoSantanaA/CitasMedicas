CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- ID único de la reserva
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Fecha y hora de la reserva
    estado_reserva ENUM('Confirmada', 'Pendiente', 'Cancelada') DEFAULT 'Pendiente',  -- Estado de la reserva
    cita_id INT,  -- ID de la cita (clave foránea)
    FOREIGN KEY (cita_id) REFERENCES citas(id) ON DELETE CASCADE  -- Relación con citas
);

CREATE TABLE facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- ID único de la factura
    fecha_emision TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Fecha de emisión de la factura
    monto_total DECIMAL(10, 2) NOT NULL,  -- Monto total de la factura
    estado ENUM('Pendiente', 'Pagada', 'Cancelada') DEFAULT 'Pendiente',  -- Estado de la factura
    metodo_pago ENUM('Efectivo', 'Tarjeta', 'Transferencia', 'Otro') NOT NULL,  -- Método de pago
    fecha_pago TIMESTAMP NULL,  -- Fecha de pago (puede ser NULL si no se ha pagado)
    paciente_id INT,  -- ID del paciente (clave foránea)
    FOREIGN KEY (paciente_id) REFERENCES pacientes(id) ON DELETE CASCADE,  -- Relación con el paciente

    -- Relación con citas (una factura puede estar asociada con varias citas)
    citas TEXT,  -- Citas asociadas (puedes usar un campo TEXT o un campo de relación muchos a muchos en una tabla intermedia)
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Fecha de creación
    actualizado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Fecha de última actualización
);

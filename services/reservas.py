class Reserva:
    def __init__(self, paciente, medico, fecha_reserva):
        self.paciente = paciente
        self.medico = medico
        self.fecha_reserva = fecha_reserva
        self.estado = "Pendiente"

    def confirmar_reserva(self):
        self.estado = "Confirmada"
        print(f"Reserva confirmada para {self.paciente.nombre} con el Dr. {self.medico.nombre} para el {self.fecha_reserva}")

    def cancelar_reserva(self):
        self.estado = "Cancelada"
        print(f"Reserva cancelada para {self.paciente.nombre} con el Dr. {self.medico.nombre}")

    def __str__(self):
        return f"Reserva para {self.paciente.nombre} {self.paciente.apellido} con {self.medico.nombre} {self.medico.apellido} el {self.fecha_reserva}. Estado: {self.estado}"

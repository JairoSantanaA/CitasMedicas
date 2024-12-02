class Medico:
    def __init__(self, id, nombre, telefono, especialidad, correo):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.especialidad = especialidad
        self.correo = correo
        self.horarios = []
        self.reservas = []

    def agregar_horario(self, horario):
        self.horarios.append(horario)

    def hacer_reserva(self, fecha, hora, paciente):
        for horario in self.horarios:
            if horario.dia == fecha and horario.hora_inicio <= hora <= horario.hora_fin:
                reserva = reservas(self, fecha, hora, paciente)
                self.reservas.append(reserva)
                return f"Reserva hecha para {paciente} con {self.nombre} el {fecha} a las {hora}."
        return "Horario no disponible."

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(f"Reserva: {reserva.fecha} a las {reserva.hora} para {reserva.paciente}.")
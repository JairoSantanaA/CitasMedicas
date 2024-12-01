class Paciente:
    def __init__(self, nombre, apellido, telefono, email, historial):
        super().__init__(nombre, apellido, telefono, email)
        self.historial = historial

    def agendar_cita(self, cita):
        print(f'{self.nombre} {self.apellido} ha agendado una cita con el Dr. {cita.medico.nombre}')

    def consultar_historial(self):
        return self.historial

    def __str__(self):
        return super().__str__()

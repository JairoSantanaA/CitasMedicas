class Horario:
    def __init__(self, id_horario, empleado, fecha, hora_inicio, hora_fin, disponible=True):
        self.id_horario = id_horario
        self.empleado = empleado
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.disponible = disponible

    def __str__(self):
        return f'{self.empleado.nombre} - {self.fecha} | {self.hora_inicio} - {self.hora_fin} - Disponible: {self.disponible}'

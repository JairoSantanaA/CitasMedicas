class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email, contraseña, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario

    def login(self):
        print(f"Iniciando sesión para {self.nombre} ({self.tipo_usuario})")
    
    def logout(self):
        print(f"Cerrando sesión de {self.nombre}")
    
    def validar_datos(self):
        if '@' not in self.email:
            print("Correo electrónico no válido")
            return False
        return True
    
    def pedir_reserva(self, medico, fecha, hora):
        if not self.validar_datos():
            return "No se puede realizar la reserva, datos no válidos."
        
        return medico.hacer_reserva(fecha, hora, self.nombre)

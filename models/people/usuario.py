class Usuario:
    def __init__(self, id_usuario, nombre, apellido, email, contraseña, tipo_usuario):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña
        self.tipo_usuario = tipo_usuario

    def login(self):
        # Aquí implementarías la autenticación, en este caso solo un placeholder
        print(f"Iniciando sesión para {self.nombre} ({self.tipo_usuario})")
    
    def logout(self):
        # Placeholder para logout
        print(f"Cerrando sesión de {self.nombre}")
    
    def validar_datos(self):
        # Validación de datos del usuario (como el correo electrónico)
        if '@' not in self.email:
            print("Correo electrónico no válido")
            return False
        return True

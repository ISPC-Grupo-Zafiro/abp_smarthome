class Usuario:
    
    def __init__(self, email, nombre, contraseña, rol):
        self.__email = email
        self._nombre = nombre
        self.__contraseña = contraseña
        self._rol = rol
        self._sesion_activa = False
    
    def get_email(self):
        return self.__email

    def get_contraseña(self):
        return self.__contraseña

    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña  

    def iniciar_sesion(self, email, contraseña):
        if self.__email == email and self.__contraseña == contraseña:
            self._sesion_activa = True
            return "Sesión iniciada correctamente."
        return "Email o contraseña incorrectos."
        
    def ver_datos_personales(self):
        return (
            f"Nombre: {self._nombre}\n"
            f"Email: {self.__email}\n"
            f"Contraseña: {self.__contraseña}\n"
            f"Rol: {self._rol}"
        )

    def registrar_nuevo_usuario(self, email, nombre, contraseña, rol):
        return Usuario(email, nombre, contraseña, rol)
    
    def modificar_datos_personales(self, nuevo_email=None, nueva_contraseña=None, nuevo_rol=None):
        if nuevo_email:
            self.__email = nuevo_email
        if nueva_contraseña:
            self.__contraseña = nueva_contraseña
        if nuevo_rol:
            self._rol = nuevo_rol
        return "Datos modificados correctamente"
    
    def eliminar_usuario(self):
        pass    
    
    def gestionar_dispositivos(self, accion, id_dispositivo):
        pass 
    
    def cerrar_sesion(self):
        self._sesion_activa = False
        return "Sesión cerrada."
    

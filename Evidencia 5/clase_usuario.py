class Usuario:
    def __init__(self, email, nombre, contraseña, rol):
        self.__email = email
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol
        
    def get_email(self):
        return self.__email

    def get_nombre(self):
        return self.__nombre

    def get_contraseña(self):
        return self.__contraseña

    def get_rol(self):
        return self.__rol

    def set_email(self, nuevo_email):
        self.__email = nuevo_email

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña    
        
    
    def registrar(self):
        pass
    
    def iniciar_secion (self):
        pass
    
    
    def ver_datos_personales(self):
        return (
            f"Nombre: {self.__nombre}" 
            f"Email: {self.__email}"
            f"Contraseña: {self.__contraseña}"
            f"Rol: {self.__rol}"
        )

   
    
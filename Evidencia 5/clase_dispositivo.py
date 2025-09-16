class Dispositivo:
    def __init__(self, nombre_dispositivo, tipo, estado):
        self.nombre_dispositivo = nombre_dispositivo  
        self.tipo = tipo                              
        self.estado = estado                          
                   

    def __str__(self):
        return f"{self.nombre_dispositivo} ({self.tipo}) - Estado: {self.estado}"

    def activar(self):
        self.estado = "activo"

    def desactivar(self):
        self.estado = "inactivo"

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre_dispositivo = nuevo_nombre
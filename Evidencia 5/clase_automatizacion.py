class Automatizacion:
    def __init__(self, id_auto, id_dispositivo, condicion, accion):
        self.id_auto = id_auto                 
        self.id_dispositivo = id_dispositivo    
        self.condicion = condicion              
        self.accion = accion                   
        self.cambios = []                       

    def agregar_cambio(self, cambio):
        self.cambios.append(cambio)

    def mostrar_info(self):
        print(f"Automatización #{self.id_auto}")
        print(f"Dispositivo: {self.id_dispositivo}")
        print(f"Condición: {self.condicion}")
        print(f"Acción: {self.accion}")
        print(f"Cambios registrados: {len(self.cambios)}")
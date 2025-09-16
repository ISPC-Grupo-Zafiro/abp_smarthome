class Dispositivo:
    def __init__(self, id_dispositivo, nombre_dispositivo, tipo): 
        self._nombre_dispositivo = nombre_dispositivo
        self._tipo = tipo
        self._estado = "apagado"
        self.__id_dispositivo = id_dispositivo

    def get_id_dispositivo(self):
        return self.__id_dispositivo
    
    def registrar_nuevos_dispositivo(self, id_dispositivo, nombre_dispositivo, tipo):
        pass
    
    def modificar_datos_dispositivo(self, id_dispositivo, nombre_dispositivo, tipo):
        pass    
    
    def listar_dispositivos(self):
        pass
    
    def eliminar_dispositivo(self, id_dispositivo):
        pass
    
    def encender(self):
        if self._estado == "apagado":
            self._estado = "encendido"
            print(f"{self._nombre_dispositivo} encendido.")
        

    def apagar(self):
        if self._estado == "encendido":
            self._estado = "apagado"
            print(f"{self._nombre_dispositivo} apagado.")

    def modificarConfiguracion(self, configuracion):
        pass
    
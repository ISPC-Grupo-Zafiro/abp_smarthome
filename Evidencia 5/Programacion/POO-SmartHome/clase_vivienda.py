class Vivienda:
    def __init__(self, id_vivienda, ubicacion, nombre_vivienda):
        self._nombre_vivienda = nombre_vivienda
        self.__ubicacion = ubicacion
        self.__id_vivienda = id_vivienda
        
    def get_ubicacion(self):
        return self.__ubicacion

    def get_id_vivienda(self):
        return self.__id_vivienda  
        
    
    def ver_datos_vivienda(self):
        return (
            f"ID_vivienda: {self.__id_vivienda}\n"
            f"Nombre_vivienda: {self._nombre_vivienda}\n"
            f"Ubicacion: {self.__ubicacion}\n"
        )

    def registrar_nueva_vivienda(self, id_vivienda, ubicacion, nombre_vivienda):
        pass
    
    def modificar_datos_vivienda(self, id_vivienda, ubicacion, nombre_vivienda):
        pass    
    
   
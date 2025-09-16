class Automatizacion:
    def __init__(self, id_auto, condicion, accion):   
        self.__id_auto = id_auto
        self.condicion = condicion              
        self.accion = accion                    
        
    def get_id_auto(self):
        return self.__id_auto
        
    def registrar_nueva_automatizacion(self, id_auto, condicion, accion):
        pass    
    
    def modificar_datos_automatizacion(self, id_auto, condicion, accion):
        pass            
    
    def eliminar_automatizacion(self, id_auto):
        pass    
    
    def activar(self):
        pass    
    
    def desactivar(self):
        pass
    
    def ver_info_automatizacion(self):
        return (
            f"ID Automatizacion: {self.__id_auto}\n"
            f"Condicion: {self.condicion}\n"
            f"Accion: {self.accion}\n"
            ) 
        
        
        
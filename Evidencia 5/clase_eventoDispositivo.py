class EventoDispositivo:
    def __init__(self, fecha_hora, detalle, valor):
        self.fecha_hora = fecha_hora          
        self.detalle = detalle                
        self.valor = valor                    

    def mostrar_evento(self):
        print(f"Fecha y hora: {self.fecha_hora}")
        print(f"Detalle: {self.detalle}")
        print(f"Valor: {self.valor}")
        
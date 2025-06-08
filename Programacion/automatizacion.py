from dispositivos import listar_dispositivos

automatizaciones = [{
    "id_automatizacion": 1,
    "modo": "noche",
    "hora": "19:00",
    "valor": "encendido", # Aca se puede poner el valor que queremos que tenga el dispositivo, por ejemplo, si queremos bajar el brillo de la luz, se puede poner 60%
    "activa": True        # Aquí sabemos si la automatización está activa o no
}, {
    "id_automatizacion": 2,
    "modo": "dia",
    "hora": "10:00",
    "valor": "apagado",
    "activa": True
}]

def listar_automatizaciones():
    return automatizaciones

def activar_automatizacion(modo_automatizacion):
    dispositivos_modificados = []
    for a in automatizaciones:
        if a["modo"].lower() == modo_automatizacion.lower():
            dispositivos = listar_dispositivos()
            for d in dispositivos:
                if d["estado"].lower() == "apagado" and d["tipo"].lower() == "luz exterior":
                    d["estado"] = "Encendido"
                    dispositivos_modificados.append(d["id_dispositivo"])
            return dispositivos_modificados
        

def consultar_automatizaciones_activas():
    activas = [a for a in automatizaciones if a.get("activa")]
    if not activas:
        return"No hay automatizaciones activas."
    else:
        for a in activas:
            return f"ID: {a['id_automatizacion']}, Modo: {a['modo']}, Hora: {a['hora']}, Valor: {a['valor']}"
    


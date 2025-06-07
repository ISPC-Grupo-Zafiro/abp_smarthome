usuarios = [
    {"email": "juanbadia@gmail.com", "nombre": "Juan Badia", "contraseña": "1234", "rool": "estandar"},
    {"email": "adridelosanto@gmail.com", "nombre": "Adriel Delosanto", "contraseña": "ispc444", "rool": "admin"}
]


def ver_datos_personales(email):
    usuario = next((u for u in usuarios if u["email"] == email), None)
    
    if usuario:
        if usuario["rool"] == "admin" or usuario["rool"] == "estandar":
            return f"\nNombre: {usuario['nombre']}\nEmail: {usuario['email']}\nContraseña: {usuario['contraseña'] }\nRool: {usuario['rool']}"
        else:return "\nAcceso restringido: no eres administrador ni usuario estandar."
    return "\n Ingrese nuevamente."


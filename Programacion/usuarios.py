usuarios = [
    {"email": "juanbadia@gmail.com", "nombre": "Juan Badia", "contraseña": "1234", "rool": "estandar"},
    {"email": "adridelosanto@gmail.com", "nombre": "Adriel Delosanto", "contraseña": "ispc444", "rool": "admin"}
]

def iniciar_sesion(email_ingresado, contraseña):
    for u in usuarios:
        if u["email"] == email_ingresado and u["contraseña"] == contraseña:
            return f"Se ha iniciado sesión correctamente como {u['rool']}.\n"
        else: return u
    return "Usuario o contraseña incorrectos.\n"

def ver_datos_personales(email):
    usuario = next((u for u in usuarios if u["email"] == email), None)
    
    if usuario:
        if usuario["rool"] == "admin" or usuario["rool"] == "estandar":
            return f"\nNombre: {usuario['nombre']}\nEmail: {usuario['email']}\nContraseña: {usuario['contraseña'] }\nRool: {usuario['rool']}"
        else:return "\nAcceso restringido: no eres administrador ni usuario estandar."
    return "\n Ingrese nuevamente."



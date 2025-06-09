usuarios = [
    {"email": "juanbadia@gmail.com", "nombre": "Juan Badia", "contraseña": "1234", "rol": "estandar"},
    {"email": "adridelosanto@gmail.com", "nombre": "Adriel Delosanto", "contraseña": "ispc444", "rol": "admin"},
]

def iniciar_sesion(email_ingresado,contraseña):
    for u in usuarios:
        if u["email"] == email_ingresado and u["contraseña"] == contraseña:
            return f"Se ha iniciado sesión correctamente como {u['rool']}.\n"
    return "Usuario o contraseña incorrectos.\n"

def ver_datos_personales(email):
    usuario = next((u for u in usuarios if u["email"] == email), None)
    
    if usuario:
        if usuario["rool"] == "admin" or usuario["rool"] == "estandar":
            return f"\nNombre: {usuario['nombre']}\nEmail: {usuario['email']}\nContraseña: {usuario['contraseña'] }\nRool: {usuario['rool']}"
        else:return "\nAcceso restringido: no eres administrador ni usuario estandar."
    

def agregar_usuario(email,nombre,contraseña):
    if not email or not nombre or not contraseña:
        return "Debe ingresa un Nombre, Email y Contraseña"
    
    usuario= [ {
        "email": email,
        "nombre": nombre,
        "contraseña": contraseña,
        "rool": "estandar"
    }]
    usuarios.append(usuario)
    return f"Se agrego un nuevo usuario:{nombre}."

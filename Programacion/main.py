
from dispositivos import (
    listar_dispositivos,
    agregar_dispositivo,
    buscar_dispositivo,
    editar_dispositivo,
    eliminar_dispositivo,
)
from automatizacion import listar_automatizaciones, activar_automatizacion, consultar_automatizaciones_activas
from usuarios import ver_datos_personales, iniciar_sesion, agregar_usuario
def menu():
    print("\n--- Menu ---")
    print("1. Listar dispositivos")
    print("2. Buscar dispositivo")
    print("3. Agregar dispositivo")
    print("4. Editar dispositivo")
    print("5. Eliminar dispositivo")
    print("6. Ver automatizaciones")
    print("7. Activar automatización")
    print("8. Ver datos personales")
    print("9. Consultar automatizaciones activas")
    print("10. Iniciar sesión")
    print("11. Agregar usuario")
    print("0. Cerrar programa")


def main():
    while True:
        menu()
        opcion = input("Selecciona una opción:")

        if opcion == "1":
            dispositivos = listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos registrados.")
            else:
                print("\nDISPOSITIVOS REGISTRADOS")
                print("-" * 50)
                for d in dispositivos:
                    print(f"   ID: {d['id_dispositivo']}")
                    print(f"   Nombre : {d['nombre']}")
                    print(f"   Tipo   : {d['tipo']}")
                    print(f"   Estado : {d['estado']}")
                    print("-" * 50)

        elif opcion == "2":
            nombre = input("Nombre del dispositivo a buscar (Por ejemplo: Jardin):")
            dispositivo = buscar_dispositivo(nombre)
            if dispositivo:
                print(f"Dispositivo encontrado: {dispositivo}")
            else:
                print("No se encontró el dispositivo.")

        elif opcion == "3":
            nombre = input("Nombre del dispositivo:")
            tipo = input("Tipo de dispositivo:")
            nuevo_dispositivo = agregar_dispositivo(nombre, tipo)
            print(nuevo_dispositivo)

        elif opcion == "4":
            nombre_original = input("Nombre del dispositivo que quieres editar:")
            print("Dejar vacíos los campos que no quieras editar.")
            nuevo_nombre = input("Nombre del dispositivo:")
            nuevo_tipo = input("Tipo de dispositivo:")
            nuevo_estado = input("Estado del dispositivo (encendido/apagado):")
            dispositivo_actualizado = editar_dispositivo(
                nombre_original, nuevo_nombre, nuevo_tipo, nuevo_estado
            )
            print(dispositivo_actualizado)

        elif opcion == "5":
            nombre = input("Nombre del dispositivo a eliminar:")
            dispositivo_eliminado = eliminar_dispositivo(nombre)
            if dispositivo_eliminado:
                print(f"Dispositivo eliminado: {dispositivo_eliminado}")
            else:
                print("No se encontró el dispositivo.")

        elif opcion == "6":
            automatizaciones = listar_automatizaciones()
            if not automatizaciones:
                print("No existen automatizaciones.")
            else:
                print("\n Automatizaciones registradas ")
                for a in automatizaciones:
                    print(
                        f"Automatización (ID {a['id_automatizacion']}) - Modo: {a['modo']}"
                    )

        elif opcion == "7":
            modo_automatizacion = input(
                "Nombre modo de la automatización que quiere activar (Ingrese 'noche'):"
            )
            automatizacion = activar_automatizacion(modo_automatizacion)
            for a in automatizacion:
                print(f"Dispositivo activado ID: {a}")
                
        elif opcion == "8":
            email = input("Ingrese su email: ")
            print(ver_datos_personales(email))
            
        elif opcion == "9":
            print(consultar_automatizaciones_activas())
            
        elif opcion == "10":
            email_ingresado = input("Ingrese email: ")
            contraseña = input("Ingrese contraseña: ")
            print(iniciar_sesion(email_ingresado, contraseña))
        
        elif opcion == "11":
            email = input("Ingrese su email: ")
            nombre = input("Ingrese su nombre: ")
            contraseña = input("Ingrese su contraseña: ")
            print(agregar_usuario(email, nombre, contraseña))
            
        elif opcion == "0":
            print("Se cerró el programa")
            break
        
        else:
            print("Opción no válida. Intenta nuevamente.")


__name__ = "__main__"
main() 
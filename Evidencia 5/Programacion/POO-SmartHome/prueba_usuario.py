import unittest
from clase_usuario import Usuario  # Asumiendo que la clase está en usuario.py


class TestUsuario(unittest.TestCase):

    def setUp(self):
        # Crear un usuario de prueba para los tests
        self.usuario = Usuario("test@email.com", "Leandro", "1234", "admin")

    # 1. Test para obtener email
    def test_get_email(self):
        self.assertEqual(self.usuario.get_email(), "test@email.com")

    # 2. Test para obtener contraseña
    def test_get_contraseña(self):
        self.assertEqual(self.usuario.get_contraseña(), "1234")

    # 3. Test para cambiar contraseña
    def test_set_contraseña(self):
        self.usuario.set_contraseña("4321")
        self.assertEqual(self.usuario.get_contraseña(), "4321")

    # 4. Test para iniciar sesión correctamente
    def test_iniciar_sesion_correcto(self):
        resultado = self.usuario.iniciar_sesion("test@email.com", "1234")
        self.assertEqual(resultado, "Sesión iniciada correctamente.")
        self.assertTrue(self.usuario._sesion_activa)

    # 5. Test para iniciar sesión incorrectamente
    def test_iniciar_sesion_incorrecto(self):
        resultado = self.usuario.iniciar_sesion("test@email.com", "0000")
        self.assertEqual(resultado, "Email o contraseña incorrectos.")
        self.assertFalse(self.usuario._sesion_activa)

    # 6. Test ver datos personales
    def test_ver_datos_personales(self):
        esperado = "Nombre: Leandro\nEmail: test@email.com\nContraseña: 1234\nRol: admin"
        self.assertEqual(self.usuario.ver_datos_personales(), esperado)

    # 7. Test modificar datos personales
    def test_modificar_datos_personales(self):
        self.usuario.modificar_datos_personales(
            nuevo_email="nuevo@email.com",
            nueva_contraseña="abcd",
            nuevo_rol="usuario"
        )
        self.assertEqual(self.usuario.get_email(), "nuevo@email.com")
        self.assertEqual(self.usuario.get_contraseña(), "abcd")
        self.assertEqual(self.usuario._rol, "usuario")

    # 8. Test cerrar sesión
    def test_cerrar_sesion(self):
        self.usuario._sesion_activa = True
        resultado = self.usuario.cerrar_sesion()
        self.assertFalse(self.usuario._sesion_activa)
        self.assertEqual(resultado, "Sesión cerrada.")


if __name__ == "__main__":
    unittest.main()

"""
Explicación de los tests de la clase Usuario:

1. `setUp`: Método que se ejecuta antes de cada test. Aquí se crea un objeto Usuario de prueba para usarlo en todos los tests.

2. `test_get_email`: Verifica que el método `get_email()` devuelva correctamente el email del usuario.

3. `test_get_contraseña`: Verifica que `get_contraseña()` devuelva la contraseña actual.

4. `test_set_contraseña`: Cambia la contraseña usando `set_contraseña()` y comprueba que se haya actualizado correctamente.

5. `test_iniciar_sesion_correcto`: Intenta iniciar sesión con las credenciales correctas y comprueba que la sesión se active y devuelva el mensaje esperado.

6. `test_iniciar_sesion_incorrecto`: Intenta iniciar sesión con credenciales incorrectas y comprueba que la sesión no se active y devuelva el mensaje de error.

7. `test_ver_datos_personales`: Comprueba que el método `ver_datos_personales()` devuelva correctamente todos los datos del usuario en formato de texto.

8. `test_modificar_datos_personales`: Modifica el email, la contraseña y el rol del usuario, y verifica que los cambios se hayan aplicado correctamente.

9. `test_cerrar_sesion`: Fuerza que la sesión esté activa, luego la cierra con `cerrar_sesion()` y verifica que la sesión se desactive y devuelva el mensaje esperado.

En resumen, este conjunto de tests cubre la mayoría de las funcionalidades básicas de la clase `Usuario`, asegurando que la gestión de credenciales, sesión y datos personales funcione correctamente.
"""

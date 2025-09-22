import unittest
from clase_vivienda import Vivienda


class TestVivienda(unittest.TestCase):

    def setUp(self):
        # Creamos una vivienda de prueba
        self.vivienda = Vivienda(1, "Córdoba", "Casa Centro")

    def test_ver_datos_vivienda(self):
        datos = self.vivienda.ver_datos_vivienda()
        self.assertIn("1", datos)
        self.assertIn("Córdoba", datos)
        self.assertIn("Casa Centro", datos)

    def test_modificar_datos_vivienda(self):
        # Modificamos los datos de la vivienda
        self.vivienda.modificar_datos_vivienda(
            2, "Villa Carlos Paz", "Casa de Vacaciones")
        self.assertEqual(self.vivienda.get_id_vivienda(), 2)
        self.assertEqual(self.vivienda.get_ubicacion(), "Villa Carlos Paz")
        self.assertEqual(self.vivienda._nombre_vivienda, "Casa de Vacaciones")

    def test_registrar_nueva_vivienda(self):
        # Probamos que se pueda "registrar" una nueva vivienda
        nueva_vivienda = self.vivienda.registrar_nueva_vivienda(
            3, "La Falda", "Cabaña")
        self.assertEqual(nueva_vivienda.get_id_vivienda(), 3)
        self.assertEqual(nueva_vivienda.get_ubicacion(), "La Falda")
        self.assertEqual(nueva_vivienda._nombre_vivienda, "Cabaña")


if __name__ == "__main__":
    unittest.main()

""" 
*** Explicación

test_ver_datos_vivienda → Verifica que ver_datos_vivienda() devuelve la info correcta.

test_modificar_datos_vivienda → Verifica que modificar_datos_vivienda() realmente cambia los atributos de la instancia.

test_registrar_nueva_vivienda → Verifica que registrar_nueva_vivienda() crea un nuevo objeto Vivienda con los datos proporcionados.

*** 
"""

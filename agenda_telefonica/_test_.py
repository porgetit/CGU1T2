# test_agenda.py
import unittest
from main import agregar_contacto, buscar_contacto, eliminar_contacto, mostrar_contactos

class TestAgendaTelefonica(unittest.TestCase):

    def setUp(self):
        self.agenda = {}

    def test_agregar_contacto(self):
        resultado = agregar_contacto(self.agenda, "Kevin", "123456789")
        self.assertEqual(resultado, "Contacto 'Kevin' agregado.")
        self.assertIn("Kevin", self.agenda)

    def test_agregar_contacto_existente(self):
        agregar_contacto(self.agenda, "Kevin", "123456789")
        resultado = agregar_contacto(self.agenda, "Kevin", "987654321")
        self.assertEqual(resultado, "El contacto 'Kevin' ya existe.")
        self.assertEqual(self.agenda["Kevin"], "123456789")

    def test_buscar_contacto_existente(self):
        agregar_contacto(self.agenda, "Kevin", "123456789")
        resultado = buscar_contacto(self.agenda, "Kevin")
        self.assertEqual(resultado, "123456789")

    def test_buscar_contacto_inexistente(self):
        resultado = buscar_contacto(self.agenda, "Luis")
        self.assertEqual(resultado, "El contacto 'Luis' no existe.")

    def test_eliminar_contacto_existente(self):
        agregar_contacto(self.agenda, "Kevin", "123456789")
        resultado = eliminar_contacto(self.agenda, "Kevin")
        self.assertEqual(resultado, "Contacto 'Kevin' eliminado.")
        self.assertNotIn("Kevin", self.agenda)

    def test_eliminar_contacto_inexistente(self):
        resultado = eliminar_contacto(self.agenda, "Luis")
        self.assertEqual(resultado, "El contacto 'Luis' no existe.")

    def test_mostrar_contactos_vacia(self):
        resultado = mostrar_contactos(self.agenda)
        self.assertEqual(resultado, "La agenda está vacía.")

    def test_mostrar_contactos(self):
        agregar_contacto(self.agenda, "Kevin", "123456789")
        agregar_contacto(self.agenda, "Luis", "987654321")
        resultado = mostrar_contactos(self.agenda)
        esperado = "Kevin: 123456789\nLuis: 987654321"
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()

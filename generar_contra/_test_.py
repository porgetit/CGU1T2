import unittest
import string
from main import generador_contrasena

class TestGeneradorContrasena(unittest.TestCase):

    def test_longitud_correcta(self):
        """Verifica que la contraseña generada tenga la longitud solicitada."""
        for long in [0, 1, 10, 50, 100]:
            contrasena = generador_contrasena(long)
            self.assertEqual(len(contrasena), long, f"Longitud incorrecta para {long}")

    def test_caracteres_validos(self):
        """Verifica que la contraseña solo contenga caracteres válidos."""
        caracteres_validos = string.ascii_letters + string.digits + string.punctuation
        contrasena = generador_contrasena(100)
        for caracter in contrasena:
            self.assertIn(caracter, caracteres_validos, f"Carácter inválido: {caracter}")

    def test_variabilidad(self):
        """Verifica que dos contraseñas consecutivas no sean iguales (muy improbable que lo sean)."""
        contrasena1 = generador_contrasena(20)
        contrasena2 = generador_contrasena(20)
        self.assertNotEqual(contrasena1, contrasena2, "Se generaron dos contraseñas idénticas")

    def test_longitud_cero(self):
        """Verifica que solicitar longitud cero devuelva una cadena vacía."""
        self.assertEqual(generador_contrasena(0), "", "La contraseña debería ser vacía")

    def test_longitud_negativa(self):
        """Verifica que pasar una longitud negativa genere un error."""
        with self.assertRaises(ValueError):
            generador_contrasena(-5)

    def test_tipo_invalido(self):
        """Verifica que pasar un tipo no entero genere un error."""
        for valor in ["10", 10.5, None, [10]]:
            with self.assertRaises(TypeError):
                generador_contrasena(valor)

if __name__ == "__main__":
    unittest.main()

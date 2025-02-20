import unittest
from main import cuentaPalabras

class TestCuentaPalabras(unittest.TestCase):
    def test_frase_vacia(self):
        self.assertEqual(cuentaPalabras(""), 0)
    
    def test_una_palabra(self):
        self.assertEqual(cuentaPalabras("Hola"), 1)
    
    def test_varias_palabras(self):
        self.assertEqual(cuentaPalabras("Hola mundo"), 2)
    
    def test_con_signos_puntuacion(self):
        self.assertEqual(cuentaPalabras("¡Hola, mundo!"), 2)
    
    def test_con_numeros(self):
        self.assertEqual(cuentaPalabras("Tengo 2 perros y 3 gatos"), 6)
    
    def test_con_multiples_espacios(self):
        self.assertEqual(cuentaPalabras("  Esto    es   una   prueba  "), 4)
    
    def test_solo_puntuacion(self):
        self.assertEqual(cuentaPalabras("!!! ??? ,,, ..."), 0)
    
    def test_palabras_con_acentos(self):
        self.assertEqual(cuentaPalabras("camión avión unión"), 3)
    
    def test_palabras_con_guiones(self):
        self.assertEqual(cuentaPalabras("auto-móvil súper-rápido"), 2)

if __name__ == "__main__":
    unittest.main()

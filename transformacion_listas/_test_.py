import unittest
from main import transformar_lista  # Asegúrate de reemplazar 'tu_modulo' con el nombre real del archivo

class TestTransformarLista(unittest.TestCase):
    
    def test_lista_numeros_positivos(self):
        self.assertEqual(transformar_lista([0, 10, 25, 100]), [32, 50, 77, 212])
    
    def test_lista_numeros_negativos(self):
        self.assertEqual(transformar_lista([-40, -10, -1]), [-40, 14, 30.2])
    
    def test_lista_mixta(self):
        self.assertEqual(transformar_lista([-30, 0, 30]), [-22, 32, 86])
    
    def test_lista_vacia(self):
        self.assertEqual(transformar_lista([]), [])
    
    def test_lista_con_decimales(self):
        self.assertEqual(transformar_lista([0.5, -0.5, 10.2]), [32.9, 31.1, 50.36])
    
    def test_lista_con_un_solo_elemento(self):
        self.assertEqual(transformar_lista([37]), [98.6])
    
if __name__ == "__main__":
    unittest.main()

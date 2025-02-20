import unittest
from main import calificacionesNumerosLetras

class TestCalificacionesNumerosLetras(unittest.TestCase):
    
    def test_calificaciones_extremos(self):
        self.assertEqual(calificacionesNumerosLetras([0.0, 5.0]), ['F', 'A'])
    
    def test_calificaciones_intermedias(self):
        self.assertEqual(calificacionesNumerosLetras([1.5, 2.5, 3.5, 4.5]), ['D', 'C', 'B', 'A'])
    
    def test_calificaciones_limites_superiores(self):
        self.assertEqual(calificacionesNumerosLetras([1.0, 2.0, 3.0, 4.0]), ['F', 'D', 'C', 'B'])
    
    def test_calificaciones_limites_inferiores(self):
        self.assertEqual(calificacionesNumerosLetras([1.1, 2.1, 3.1, 4.1]), ['D', 'C', 'B', 'A'])
    
    def test_lista_vacia(self):
        self.assertEqual(calificacionesNumerosLetras([]), [])
    
    def test_calificaciones_decimales(self):
        self.assertEqual(calificacionesNumerosLetras([0.9, 1.9, 2.9, 3.9, 4.9]), ['F', 'D', 'C', 'B', 'A'])
    
if __name__ == '__main__':
    unittest.main()
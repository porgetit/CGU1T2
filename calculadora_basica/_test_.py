import unittest
from main import suma, resta, multiplicacion, division, operacion

class TestOperaciones(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-1, 1), 0)
        self.assertEqual(suma(0, 0), 0)
        self.assertAlmostEqual(suma(2.5, 3.1), 5.6)
    
    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(0, 3), -3)
        self.assertEqual(resta(-3, -3), 0)
        self.assertAlmostEqual(resta(5.5, 2.2), 3.3)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 3), 12)
        self.assertEqual(multiplicacion(-2, 3), -6)
        self.assertEqual(multiplicacion(0, 5), 0)
        self.assertAlmostEqual(multiplicacion(2.5, 2), 5.0)
    
    def test_division(self):
        self.assertEqual(division(6, 2), 3)
        self.assertEqual(division(-6, 3), -2)
        self.assertAlmostEqual(division(7, 2), 3.5)
        with self.assertRaises(ValueError):
            division(5, 0)
    
    def test_operacion(self):
        self.assertEqual(operacion(5, 3, "+"), 8)
        self.assertEqual(operacion(5, 3, "-"), 2)
        self.assertEqual(operacion(5, 3, "*"), 15)
        self.assertEqual(operacion(6, 3, "/"), 2)
        with self.assertRaises(ValueError):
            operacion(5, 3, "%")

if __name__ == "__main__":
    unittest.main()

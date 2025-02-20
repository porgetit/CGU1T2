import unittest
from main import filtroPares

class TestFiltrarLista(unittest.TestCase):
    
    def test_filtroPares(self):
        self.assertEqual(filtroPares([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filtroPares([1, 3, 5, 7]), [])
        self.assertEqual(filtroPares([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(filtroPares([]), [])
        self.assertEqual(filtroPares([0, -2, -3, -4]), [0, -2, -4])
        self.assertEqual(len(filtroPares(list(range(100000)))), 50000)
        
if __name__ == '__main__':
    unittest.main()
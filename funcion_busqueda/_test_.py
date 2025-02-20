import unittest
import numpy as np
from main import busqueda_binaria


class TestBusquedaBinaria(unittest.TestCase):
    def test_arreglo_vacio(self):
        arr = np.array([])
        self.assertEqual(busqueda_binaria(arr, 5), -1)

    def test_arreglo_un_elemento_encontrado(self):
        arr = np.array([10])
        self.assertEqual(busqueda_binaria(arr, 10), 0)

    def test_arreglo_un_elemento_no_encontrado(self):
        arr = np.array([10])
        self.assertEqual(busqueda_binaria(arr, 5), -1)

    def test_arreglo_pequeno_elemento_inicial(self):
        arr = np.array([3, 1, 2])
        self.assertEqual(busqueda_binaria(arr, 1), 0)  # Después de ordenar: [1,2,3]

    def test_arreglo_pequeno_elemento_medio(self):
        arr = np.array([3, 2, 1])
        self.assertEqual(busqueda_binaria(arr, 2), 1)  # Después de ordenar: [1,2,3]

    def test_arreglo_pequeno_elemento_final(self):
        arr = np.array([3, 1, 2])
        self.assertEqual(busqueda_binaria(arr, 3), 2)  # Después de ordenar: [1,2,3]

    def test_arreglo_con_repetidos(self):
        arr = np.array([2, 4, 4, 4, 6, 8])
        indice = busqueda_binaria(arr, 4)
        self.assertIn(indice, [1, 2, 3])  # Cualquiera de las posiciones con 4 es válida

    def test_objetivo_fuera_de_rango(self):
        arr = np.array([10, 20, 30, 40])
        self.assertEqual(busqueda_binaria(arr, 5), -1)   # Menor que todos
        self.assertEqual(busqueda_binaria(arr, 50), -1)  # Mayor que todos

    def test_arreglo_grande_encontrado(self):
        arr = np.arange(0, 1_000_000, 2)  # 500,000 elementos pares
        objetivo = 500_000
        indice = busqueda_binaria(arr, objetivo)
        self.assertNotEqual(indice, -1)
        self.assertEqual(arr[indice], objetivo)

    def test_arreglo_grande_no_encontrado(self):
        arr = np.arange(0, 2_000_000, 3)  # Arreglo grande con pasos de 3
        objetivo = 1_000_001  # No está en la secuencia
        self.assertEqual(busqueda_binaria(arr, objetivo), -1)

    def test_arreglo_extremadamente_grande(self):
        arr = np.linspace(0, 10_000_000, num=10_000_001)  # Arreglo muy grande
        objetivo = 7_654_321
        indice = busqueda_binaria(arr, objetivo)
        self.assertNotEqual(indice, -1)
        self.assertAlmostEqual(arr[indice], objetivo, places=5)


if __name__ == "__main__":
    unittest.main()

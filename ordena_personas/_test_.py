import unittest
from main import ordenar_por_edad_y_nombre

class TestOrdenarPorEdadYNombre(unittest.TestCase):

    def test_ordenar_normal(self):
        personas = [("Ana", 30), ("Luis", 25), ("Pedro", 30), ("Carlos", 25)]
        resultado = ordenar_por_edad_y_nombre(personas)
        esperado = [("Carlos", 25), ("Luis", 25), ("Ana", 30), ("Pedro", 30)]
        self.assertEqual(resultado, esperado)

    def test_ordenar_lista_vacia(self):
        self.assertEqual(ordenar_por_edad_y_nombre([]), [])

    def test_ordenar_un_elemento(self):
        personas = [("Ana", 30)]
        self.assertEqual(ordenar_por_edad_y_nombre(personas), [("Ana", 30)])

    def test_ordenar_mismos_nombres(self):
        personas = [("Ana", 30), ("Ana", 25), ("Ana", 40)]
        esperado = [("Ana", 25), ("Ana", 30), ("Ana", 40)]
        self.assertEqual(ordenar_por_edad_y_nombre(personas), esperado)

    def test_ordenar_mismas_edades(self):
        personas = [("Carlos", 25), ("Ana", 25), ("Luis", 25)]
        esperado = [("Ana", 25), ("Carlos", 25), ("Luis", 25)]
        self.assertEqual(ordenar_por_edad_y_nombre(personas), esperado)

if __name__ == "__main__":
    unittest.main()

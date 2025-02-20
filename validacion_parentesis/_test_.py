import unittest
from main import validar_parentesis


class TestValidarParentesis(unittest.TestCase):
    def test_casos_balanceados(self):
        self.assertTrue(validar_parentesis("()"), "Caso simple balanceado")
        self.assertTrue(validar_parentesis("(())"), "Paréntesis anidados balanceados")
        self.assertTrue(validar_parentesis("()()"), "Múltiples pares de paréntesis")
        self.assertTrue(validar_parentesis("((()))"), "Paréntesis anidados múltiples")
        self.assertTrue(validar_parentesis("()()(()())"), "Combinación compleja balanceada")
        self.assertTrue(validar_parentesis(""), "Cadena vacía (considerada balanceada)")

    def test_casos_no_balanceados(self):
        self.assertFalse(validar_parentesis("("), "Un paréntesis de apertura sin cierre")
        self.assertFalse(validar_parentesis(")"), "Un paréntesis de cierre sin apertura")
        self.assertFalse(validar_parentesis("(()"), "Falta un paréntesis de cierre")
        self.assertFalse(validar_parentesis("())"), "Cierre adicional sin apertura correspondiente")
        self.assertFalse(validar_parentesis(")()("), "Orden incorrecto de paréntesis")
        self.assertFalse(validar_parentesis("(()))("), "Paréntesis desordenados")


if __name__ == "__main__":
    unittest.main()

import numpy as np

def busqueda_binaria(arr: np.ndarray, objetivo: float) -> int:
    """
    Realiza una búsqueda binaria en un arreglo de NumPy ordenado.

    Parámetros:
    - arr (np.ndarray): Arreglo ordenado donde se buscará el objetivo.
    - objetivo (float): Elemento a buscar.

    Retorna:
    - int: Índice del elemento si se encuentra; -1 en caso contrario.
    """
    arr = np.sort(arr)  # Se ordena el arreglo
    izquierda, derecha = 0, arr.size - 1

    while izquierda <= derecha:
        # Cálculo optimizado para el índice medio, evitando desbordamientos
        medio = izquierda + (derecha - izquierda) // 2
        valor_medio = arr[medio]

        if valor_medio == objetivo:
            return medio  # Se encontró el objetivo
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1  # No se encontró el objetivo

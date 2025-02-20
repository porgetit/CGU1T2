from typing import List, Tuple

def ordenar_por_edad_y_nombre(personas: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    """
    Ordena una lista de tuplas (nombre, edad) primero por edad y después por nombre.

    :param personas: Lista de tuplas (nombre, edad)
    :return: Lista ordenada de tuplas
    """
    return sorted(personas, key=lambda x: (x[1], x[0]))
def filtroPares(lista):
    """Función que recibe una lista de números y retorna una lista con los números pares de la lista original.

    Args:
        lista (list): Lista de números.

    Returns:
        list: Lista de números pares.
    """
    return [i for i in lista if i % 2 == 0] # <-- Ahí están el búcle y la condición usados como una compresión de listas.

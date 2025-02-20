def transformar_lista(lista):
    """Transforma una lista de grados celsius a fahrenheit

    Args:
        lista (list): Lista de grados celsius

    Returns:
        list: Lista de grados fahrenheit
    """
    return list(map(lambda celsius: celsius * 9/5 + 32, lista))
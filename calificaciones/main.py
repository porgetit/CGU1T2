def calificacionesNumerosLetras(calificaciones:list):
    """Convierte una lista de calificaciones numéricas a letras.

    Args:
        calificaciones (list): Lista de calificaciones numéricas.

    Returns:
        list: Lista de calificaciones en letras.
    """
    calificacionesLetras = []
    for calificacion in calificaciones:
        if calificacion > 4 and calificacion <= 5:
            calificacionesLetras.append('A')
        elif calificacion > 3:
            calificacionesLetras.append('B')
        elif calificacion > 2:
            calificacionesLetras.append('C')
        elif calificacion > 1:
            calificacionesLetras.append('D')
        else:
            calificacionesLetras.append('F')
    
    return calificacionesLetras
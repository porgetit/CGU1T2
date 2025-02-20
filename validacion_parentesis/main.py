def validar_parentesis(cadena: str) -> bool:
    """Valida si una cadena de paréntesis está balanceada.

    Args:
        cadena (str): Cadena que contiene paréntesis.

    Returns:
        bool: True si la cadena está balanceada, False en caso contrario.
    """
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila:
                return False  # Hay un paréntesis de cierre sin su apertura correspondiente
            pila.pop()  # Empareja un paréntesis de apertura con este cierre

    return len(pila) == 0  # Si la pila está vacía, todos los paréntesis están balanceados

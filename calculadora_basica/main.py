def suma(a:float, b:float):
    """Suma dos números

    Args:
        a (float): Primer operando
        b (float): Segundo operando

    Returns:
        float: Suma de los dos operandos
    """
    return a + b

def resta(a:float, b:float):
    """Resta dos números

    Args:
        a (float): Primer operando
        b (float): Segundo operando

    Returns:
        float: Resta de los dos operandos
    """
    return a - b

def multiplicacion(a:float, b:float):
    """Multiplica dos números

    Args:
        a (float): Primer operando
        b (float): Segundo operando

    Returns:
        float: Multiplicación de los dos operandos
    """
    return a * b

def division(a:float, b:float):
    """Divide dos números

    Args:
        a (float): Dividendo
        b (float): Divisor

    Raises:
        ValueError: Si el divisor es cero

    Returns:
        float: Cociente de la división
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def operacion(a:float, b:float, operador:str):
    """Realiza una operación aritmética

    Args:
        a (float): Primer operando
        b (float): Segundo operando
        operador (str): Operador aritmético

    Raises:
        ValueError: Si el operador no es válido

    Returns:
        float: Resultado de la operación
    """
    if operador == "+":
        return suma(a, b)
    elif operador == "-":
        return resta(a, b)
    elif operador == "*":
        return multiplicacion(a, b)
    elif operador == "/":
        return division(a, b)
    else:
        raise ValueError("Operador no válido")
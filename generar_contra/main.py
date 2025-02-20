def generador_contrasena(long:int):
    if long < 0:
        raise ValueError("La longitud no puede ser negativa")
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(long))
    return contrasena



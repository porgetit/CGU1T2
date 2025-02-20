def cuentaPalabras(frase):
    # Eliminar todo lo que no sea alfanumérico o espacio
    frase = ''.join(e for e in frase if e.isalnum() or e.isspace())
    return len(frase.split())  # split() sin argumentos elimina espacios extra

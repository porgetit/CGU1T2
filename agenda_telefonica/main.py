# agenda.py

def agregar_contacto(agenda, nombre, telefono):
    if nombre in agenda:
        return f"El contacto '{nombre}' ya existe."
    agenda[nombre] = telefono
    return f"Contacto '{nombre}' agregado."

def buscar_contacto(agenda, nombre):
    return agenda.get(nombre, f"El contacto '{nombre}' no existe.")

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        return f"Contacto '{nombre}' eliminado."
    return f"El contacto '{nombre}' no existe."

def mostrar_contactos(agenda):
    if not agenda:
        return "La agenda está vacía."
    return "\n".join([f"{nombre}: {telefono}" for nombre, telefono in agenda.items()])
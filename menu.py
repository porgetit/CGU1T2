import subprocess
import sys

# Opciones del menú con las rutas de los archivos de prueba en cada carpeta
PRUEBAS = {
    "1": ("Calculadora básica", "./calculadora_basica/_test_.py"),
    "2": ("Filtrado de lista", "./filtrado_lista/_test_.py"),
    "3": ("Transformación de listas con Map y Lambda", "./transformacion_listas/_test_.py"),
    "4": ("Sistema de calificaciones", "./calificaciones/_test_.py"),
    "5": ("Conteo de palabras", "./cuenta_palabras/_test_.py"),
    "6": ("Función de búsqueda", "./funcion_busqueda/_test_.py"),
    "7": ("Validación de paréntesis", "./validacion_parentesis/_test_.py"),
    "8": ("Ordenamiento personalizado", "./ordena_personas/_test_.py"),
    "9": ("Generador de contraseñas", "./generar_contra/_test_.py"),
    "10": ("Gestión de agenda telefónica", "./agenda_telefonica/_test_.py"),
    "0": ("Salir", None),
}

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n=== Taller 1: Ejecutar Pruebas ===")
    for key, (nombre, _) in PRUEBAS.items():
        print(f"{key}. {nombre}")

def ejecutar_prueba(opcion):
    """Ejecuta el archivo pruebas.py de la opción seleccionada."""
    if opcion in PRUEBAS:
        nombre, ruta = PRUEBAS[opcion]
        if ruta:
            print(f"\nEjecutando {nombre}...\n")
            subprocess.run([sys.executable, ruta])  # Ejecuta el archivo pruebas.py de la carpeta correspondiente
        else:
            print("\nSaliendo del sistema. ¡Hasta luego!")
            sys.exit(0)
    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")

def main():
    """Bucle principal del menú."""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ").strip()
        ejecutar_prueba(opcion)

if __name__ == "__main__":
    main()

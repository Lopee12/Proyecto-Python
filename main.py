from Paquete_Python.Cliente import Cliente
from Paquete_Python.Usuario import *

# Función para mostrar el menú principal y manejar las opciones de registro e inicio de sesión

def menu_principal():

    print("👋 Bienvenido al sistema de gestión de usuarios y clientes.\n")

    while True:
        print("===== Menú Principal =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        try:
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                registro()
            elif opcion == "2":
                inicio_sesion()
            elif opcion == "3":
                print("👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Por favor, seleccione 1, 2 o 3.\n")
        except Exception as e:
            print(f"❌ Error inesperado: {e}\n")

# Si se desea ejecutar el menú principal, descomentar la siguiente línea:
#menu_principal()

def main():
    print("=== Prueba del módulo Cliente ===\n")

    # Crear cliente
    cliente1 = Cliente(1, "Juan Pérez", "juan@example.com", 1500.0)
    print("👤 Cliente creado:")
    print(cliente1)

    # Usar método actualizar_correo
    print("\n🔄 Actualizando correo:")
    cliente1.actualizar_correo("juanperez@gmail.com")

    # Usar método agregar_saldo
    print("\n💵 Agregando saldo:")
    cliente1.agregar_saldo(500)

    # Crear otro cliente para ver __str__ con más de uno
    cliente2 = Cliente(2, "Ana Gómez", "ana@example.com", 2000.0)
    print("\n👤 Segundo cliente creado:")
    print(cliente2)

    print("\n✅ Fin de prueba.")

if __name__ == "__main__":
    main()


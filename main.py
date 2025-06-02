# Definimos una clase Usuario para manejar los datos de los usuarios registrados.

class Usuario:
    def __init__(self, id, nombre_usuario, contraseña):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

    def __repr__(self):
        return f"ID: {self.id}, Usuario: {self.nombre_usuario}"

# Lista para almacenar los usuarios registrados

usuarios = []

# Funciones para manejar el registro y el inicio de sesión de usuarios

def registro():

    id_usuario = len(usuarios) + 1

    while True:
        try:
            nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
            if not nombre_usuario:
                raise ValueError("❌ El nombre de usuario no puede estar vacío. Inténtelo nuevamente.\n")

            for usuario in usuarios:
                if usuario.nombre_usuario == nombre_usuario:
                    raise ValueError(f"❌ El nombre de usuario '{nombre_usuario}' ya está en uso. Inténtelo con otro.\n")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}. Inténtelo nuevamente.\n")      

    while True:
        try:
            contraseña = input("Ingrese la contraseña: ").strip()
            if not contraseña:
                raise ValueError("❌ La contraseña no puede estar vacía. Inténtelo nuevamente.\n")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}. Inténtelo nuevamente.\n")

    nuevo_usuario = Usuario(id_usuario, nombre_usuario, contraseña)
    usuarios.append(nuevo_usuario)
    print(f"\n✅ Usuario '{nombre_usuario}' registrado con éxito.\n")

def inicio_sesion():

    while True:
        try:
            nombre_usuario = input("Ingrese el nombre de usuario: ").strip()
            if not nombre_usuario:
                raise ValueError("❌ El nombre de usuario no puede estar vacío. Inténtelo nuevamente.\n")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}. Inténtelo nuevamente.\n")

    while True:
        try:
            contraseña = input("Ingrese la contraseña: ").strip()
            if not contraseña:
                raise ValueError("❌ La contraseña no puede estar vacía. Inténtelo nuevamente.\n")
            break
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}. Inténtelo nuevamente.\n")

    for usuario in usuarios:
        if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
            print(f"\n✅ Inicio de sesión exitoso. ¡Bienvenido, {nombre_usuario}!\n")
            mostrar_usuarios()
            menu_post_listado()
            return

    print("\n❌ Usuario o contraseña incorrectos.\n")

# Función para mostrar la lista de usuarios registrados

def mostrar_usuarios():

    if not usuarios:
        print("No hay usuarios registrados.\n")
    else:
        print("👥 Lista de usuarios registrados:")
        for usuario in usuarios:
            print(usuario)
        print()

# Función para mostrar el menú principal y manejar las opciones de registro e inicio de sesión

def menu_principal():

    print("👋 Bienvenido al sistema de gestión de usuarios.\n")

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

def menu_post_listado():

    while True:
        print("====== ¿Qué desea hacer ahora? ======")
        print("1. Volver al menú principal")
        print("2. Salir del programa")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            return  # Vuelve al menú principal
        elif opcion == "2":
            print("👋 ¡Hasta luego!")
            exit()
        else:
            print("❌ Opción no válida. Por favor, seleccione 1 o 2.\n")

# Ejecutar el programa

if __name__ == "__main__":
    menu_principal()

#probamos el programa
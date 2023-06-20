class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.registros = []

    def agregar_registro(self, registro):
        self.registros.append(registro)


class Registro:
    def __init__(self, usuario, tiempo, tipo):
        self.usuario = usuario
        self.tiempo = tiempo
        self.tipo = tipo


class SistemaAsistencia:
    def __init__(self):
        self.usuarios = []

    def agregar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.usuarios.append(usuario)
        print(f"Usuario '{nombre}' agregado.")

    def registrar_entrada(self, nombre):
        usuario = self.buscar_usuario(nombre)
        if usuario:
            registro = Registro(usuario, "now", "entrada")
            usuario.agregar_registro(registro)
            print(f"Registro de entrada para '{nombre}' realizado.")
        else:
            print(f"No se encontró el usuario '{nombre}'.")

    def registrar_salida(self, nombre):
        usuario = self.buscar_usuario(nombre)
        if usuario:
            registro = Registro(usuario, "now", "salida")
            usuario.agregar_registro(registro)
            print(f"Registro de salida para '{nombre}' realizado.")
        else:
            print(f"No se encontró el usuario '{nombre}'.")

    def listar_registros(self):
        for usuario in self.usuarios:
            print(f"Registros de '{usuario.nombre}':")
            for registro in usuario.registros:
                print(f"Tiempo: {registro.tiempo} - Tipo: {registro.tipo}")

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None


def main():
    sistema = SistemaAsistencia()

    while True:
        print("\n--- ☆ Sistema de Asistencia ✩ ---")
        print("1. Agregar usuario")
        print("2. Registrar entrada")
        print("3. Registrar salida")
        print("4. Listar registros")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema.agregar_usuario(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema.registrar_entrada(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            sistema.registrar_salida(nombre)
        elif opcion == "4":
            sistema.listar_registros()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar la función main
main()

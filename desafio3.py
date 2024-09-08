def imprimir_matriz_usuarios(matriz):

    print(f"{'ID':<5} {'Nombre':<10} {'Email':<25} {'Fecha de nacimiento':<15}")
    print("-" * 65)
    for usuario in matriz:
        id_usuario = usuario[0]
        nombre = usuario[1]
        correo = usuario[2]
        fecha_nac = usuario[3]
        print(f"{id_usuario:<5} {nombre:<10} {correo:<25} {fecha_nac:>12}")

def agregar_usuario(matriz_usuarios):
    
    id_usuario = int(input("Ingrese el ID del nuevo usuario: "))
    nombre = input("Ingrese el nombre del nuevo usuario: ")
    email = input("Ingrese el Email del nuevo usuario: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del nuevo usuario (DD/MM/AAAA): ")


    nuevo_usuario = [id_usuario, nombre, email, fecha_nacimiento]
    
    matriz_usuarios.append(nuevo_usuario)

def editar_usuario(matriz_usuarios):
    try:
        id_usuario = int(input("Ingrese el ID del usuario a editar: "))
        for usuario in matriz_usuarios:
            if usuario[0] == id_usuario:
                nuevo_nombre = input(f"Ingrese el nuevo nombre para el usuario (actual: {usuario[1]}): ")
                nuevo_email = input(f"Ingrese el nuevo email para el usuario (actual: {usuario[2]}): ")
                nueva_fecha_nacimiento = input(f"Ingrese la nueva fecha de nacimiento para el usuario (actual: {usuario[3]}): ")

                usuario[1] = nuevo_nombre
                usuario[2] = nuevo_email
                usuario[3] = nueva_fecha_nacimiento

                print("Datos del usuario actualizados exitosamente.")
                return
        print(f"Usuario con ID: {id_usuario} no encontrado.")
    except ValueError:
        print("ID inválido. Debe ser un número entero.")
        

def eliminar_usuario(matriz_usuarios, user_id):
    for i, usuario in enumerate(matriz_usuarios):
        if usuario[0] == user_id:
            del matriz_usuarios[i]
            print(f"Usuario con ID: {user_id} eliminado.")
            return
    print(f"Usuario con ID: {user_id} no encontrado.")


def menu():
    while True:
        print("\nIngrese el número correspondiente a la opción que desea ejecutar: ")
        print("1. Mostrar matriz de usuarios.")
        print("2. Agregar usuarios a la matriz.")
        print("3. Eliminar usuarios de la matriz.")
        print("4. Editar datos de un usuario.")
        print("5. Salir.")

        opcion = input("Opción: ")
        
        if opcion == '1':
            imprimir_matriz_usuarios(matriz_usuarios)
        elif opcion == '2':
            agregar_usuario(matriz_usuarios)
        elif opcion == '3':
            try:
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                eliminar_usuario(matriz_usuarios, user_id)
            except ValueError:
                print("ID inválido. Debe ser un número entero.")
        elif opcion == '4':
            editar_usuario(matriz_usuarios)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


matriz_usuarios = [
    [1, "Francisco", "francilopez@uade.edu.ar", "21/12/2003"],
    [2, "Valentin", "valentin@uade.edu.ar", "16/10/2003"],
    [3, "Gonzalo", "gonzalo12@gmail.com", "27/01/2002"],
    [4, "Sofia", "sofia2@gmail.com", "09/12/2010"],
    [5, "Ciro", "ciro@gmail.com", "11/01/1988"],
    [6, "Valentina", "valentina2@hotmail.com", "21/09/2000"]
]


menu()
import os

USUARIOS = "usuarios.txt"



PERSONAS = "personas.txt"

def pedir_no_vacio(mensaje):
    while True:
        x = input(mensaje).strip()
        if x != " ":
            return x
        print("No puede estar vacío.")


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        x = input(mensaje).strip()
        if not x.isdigit():
            print("Debe ser un número entero.")
            continue
        n = int(x)
        if minimo is not None and n < minimo:
            print(f"Debe ser >= {minimo}.")
            continue
        if maximo is not None and n > maximo:
            print(f"Debe ser <= {maximo}.")
            continue
        return n

def cargar_lista_dict(nombre_archivo):
    datos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            for linea in f:
                linea = linea.strip()
                if linea != "":
                    datos.append(eval(linea))
    return datos

def guardar_lista_dict(nombre_archivo, datos):
    with open(nombre_archivo, "w") as f:
        for d in datos:
            f.write(str(d) + "\n")

def usuario_existe(usuarios, user):
    for u in usuarios:
        if u["user"] == user:
            return True
    return False

def registrar_usuario():
    usuarios = cargar_lista_dict(USUARIOS)
    user = pedir_no_vacio("Usuario: ")
    if usuario_existe(usuarios, user):
        print("Ese usuario ya existe.")
        return
    clave = pedir_no_vacio("Clave: ")
    usuarios.append({"user": user, "clave": clave})
    guardar_lista_dict(USUARIOS, usuarios)
    print("Usuario registrado.")

def login():
    usuarios = cargar_lista_dict(USUARIOS)
    user = pedir_no_vacio("Usuario: ")
    clave = pedir_no_vacio("Clave: ")
    for u in usuarios:
        if u["user"] == user and u["clave"] == clave:
            print("Login correcto.")
            return True
    print("Credenciales incorrectas.")
    return False

def cargar_personas():
    return cargar_lista_dict(PERSONAS)

def guardar_personas(personas):
    guardar_lista_dict(PERSONAS, personas)

def crear_persona(personas):
    nombre = pedir_no_vacio("Nombre: ")
    edad = pedir_entero("Edad: ", minimo=0)
    personas.append({"nombre": nombre, "edad": edad})
    guardar_personas(personas)
    print("Persona creada.")

def listar_personas(personas):
    if len(personas) == 0:
        print("No hay personas registradas.")
        return
    for i, p in enumerate(personas):
        print(f"{i}: Nombre={p['nombre']}, Edad={p['edad']}")

def actualizar_persona(personas):
    if len(personas) == 0:
        print("No hay personas para actualizar.")
        return
    listar_personas(personas)
    idx = pedir_entero("Índice a actualizar: ", minimo=0, maximo=len(personas) - 1)
    nuevo_nombre = pedir_no_vacio("Nuevo nombre: ")
    nueva_edad = pedir_entero("Nueva edad: ", minimo=0)
    personas[idx]["nombre"] = nuevo_nombre
    personas[idx]["edad"] = nueva_edad
    guardar_personas(personas)
    print("Persona actualizada.")

def eliminar_persona(personas):
    if len(personas) == 0:
        print("No hay personas para eliminar.")
        return
    listar_personas(personas)
    idx = pedir_entero("Índice a eliminar: ", minimo=0, maximo=len(personas) - 1)
    eliminado = personas.pop(idx)
    guardar_personas(personas)
    print(f"Persona eliminada: {eliminado['nombre']}")

def menu_crud():
    personas = cargar_personas()
    while True:
        print("\n1 Crear persona")
        print("2 Listar personas")
        print("3 Actualizar por índice")
        print("4 Eliminar por índice")
        print("5 Salir")
        op = input("Opción: ").strip()

        if op == "1":
            crear_persona(personas)
        elif op == "2":
            listar_personas(personas)
        elif op == "3":
            actualizar_persona(personas)
        elif op == "4":
            eliminar_persona(personas)
        elif op == "5":
            break
        else:
            print("Opción inválida.")

def menu_principal():
    while True:
        print("\n1 Registrar")
        print("2 Login")
        print("3 Salir")
        op = input("Opción: ").strip()

        if op == "1":
            registrar_usuario()
        elif op == "2":
            if login():
                menu_crud()
        elif op == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu_principal()

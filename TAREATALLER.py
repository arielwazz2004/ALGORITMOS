import os

# Crear un archivo
with open("archivo.txt", "w") as f:
    f.write("Contenido inicial\n")

# Escribir en un archivo
with open("archivo.txt", "a") as f:
    f.write("Nueva línea\n")

# Escribir en un archivo más líneas
with open("archivo.txt", "a") as f:
    f.write("Otra línea\n")
    f.write("Otra más\n")

# Sobrescribir en un archivo más líneas
with open("sobrescribir.txt", "w") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea\n")

# Seguir escribiendo líneas en un archivo
with open("seguir.txt", "a") as f:
    f.write("Sigo escribiendo\n")

# Abrir un archivo y leerlo
with open("archivo.txt", "r") as f:
    print(f.read())

# Abrir un archivo y leerlo desde otra ruta
ruta = "archivo.txt"
if os.path.exists(ruta):
    with open(ruta, "r") as f:
        print(f.read())

# Abrir un archivo y leerlo línea por línea con while
with open("archivo.txt", "r") as f:
    linea = f.readline()
    while linea != "":
        print(linea.strip())
        linea = f.readline()

# Abrir un archivo y leerlo línea por línea con for
with open("archivo.txt", "r") as f:
    for linea in f:
        print(linea.strip())

# CRUD completo en Python usando archivos
ARCHIVO = "personas.txt"

def cargar():
    personas = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            for linea in f:
                personas.append(linea.strip())
    return personas

def guardar(personas):
    with open(ARCHIVO, "w") as f:
        for p in personas:
            f.write(p + "\n")

def crear(personas):
    nombre = input("Nombre: ")
    personas.append(nombre)
    guardar(personas)

def listar(personas):
    for i, p in enumerate(personas):
        print(i, p)

def actualizar(personas):
    listar(personas)
    i = int(input("Índice: "))
    personas[i] = input("Nuevo nombre: ")
    guardar(personas)

def eliminar(personas):
    listar(personas)
    i = int(input("Índice: "))
    personas.pop(i)
    guardar(personas)

def menu():
    personas = cargar()
    while True:
        print("1 Crear")
        print("2 Listar")
        print("3 Actualizar")
        print("4 Eliminar")
        print("5 Salir")
        op = input("Opción: ")

        if op == "1":
            crear(personas)
        elif op == "2":
            listar(personas)
        elif op == "3":
            actualizar(personas)
        elif op == "4":
            eliminar(personas)
        elif op == "5":
            break
        else:
            print("Opción inválida")

menu()

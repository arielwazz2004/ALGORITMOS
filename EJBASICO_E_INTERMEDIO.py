import os

# 1Crear archivo y escribir 3 líneas
with open("saludo.txt", "w") as f:
    f.write("Hola \n")
    f.write("Bienvenido \n")
    f.write("Ariel\n")


# 2Leer archivo línea por línea
with open("saludo.txt", "r") as f:
    for linea in f:
        print(linea.strip())


# 3Crear archivo solo si no existe
if not os.path.exists("registro.txt"):
    with open("registro.txt", "x") as f:
        f.write("Archivo creado correctamente")
else:
    print("Error: registro.txt ya existe")


# 4Contar líneas con readlines()
with open("saludo.txt", "r") as f:
    lineas = f.readlines()
    print("Cantidad de líneas:", len(lineas))


#5Copiar contenido a otro archivo
with open("saludo.txt", "r") as origen:
    contenido = origen.read()

with open("copia.txt", "w") as destino:
    destino.write(contenido)
# 6Agregar texto a un archivo existente (sin borrar)
with open("saludo.txt", "a") as f:
    f.write("\nNueva línea agregada sin borrar lo anterior")


# 7 Contar cuántas veces aparece una palabra ("Python")
with open("saludo.txt", "r") as f:
    contenido = f.read()
    print("Veces que aparece 'Python':", contenido.count("Python"))


# 8Mostrar solo líneas que contienen una palabra clave 
with open("saludo.txt", "r") as f:
    for linea in f:
        if "Hola" in linea:
            print(linea.strip())


# 9Escribir una lista de nombres en nombres.txt 
nombres_lista = ["Ana", "Luis", "Carlos", "María", "Sofía"]
with open("nombres.txt", "w") as f:
    for nombre in nombres_lista:
        f.write(nombre + "\n")


# 10Leer nombres desde el archivo y mostrarlos en mayúsculas
with open("nombres.txt", "r") as f:
    for nombre in f:
        print(nombre.strip().upper())


# 11Crear y escribir en datos.txt 
with open("datos.txt", "w") as f:
    f.write("Primera línea\n")
    f.write("Segunda línea\n")
    f.write("Tercera línea\n")


# 12Leer e imprimir datos.txt línea por línea sin saltos dobles
with open("datos.txt", "r") as f:
    for linea in f:
        print(linea.strip())


# 13Contar cuántas líneas tiene datos.txt
with open("datos.txt", "r") as f:
    print("Cantidad de líneas en datos.txt:", len(f.readlines()))


# 14Agregar "Cuarta línea" al final de datos.txt
with open("datos.txt", "a") as f:
    f.write("Cuarta línea\n")


# 15Imprimir solo líneas que contienen la palabra línea
with open("datos.txt", "r") as f:
    for linea in f:
        if "línea" in linea:
            print(linea.strip())


# 16Copiar todo el contenido de datos.txt a copia_datos.txt
with open("datos.txt", "r") as origen:
    contenido = origen.read()

with open("copia_datos.txt", "w") as destino:
    destino.write(contenido)


# 17Crear un archivo con nombre personalizado y guardar una línea
nombre_archivo = input("Nombre del archivo: ").strip()
texto = input("Escribe una línea de texto: ")
with open(nombre_archivo, "w") as f:
    f.write(texto + "\n")


# 18Escribir múltiples líneas hasta que el usuario escriba salir
with open("mensajes.txt", "w") as f:
    while True:
        linea = input("Escribe un mensaje: ")
        if linea.lower() == "salir":
            break
        f.write(linea + "\n")


# 19Leer un archivo cuyo nombre lo da el usuario
archivo_leer = input("Nombre del archivo a leer: ").strip()
if os.path.exists(archivo_leer):
    with open(archivo_leer, "r") as f:
        for linea in f:
            print(linea.strip())
else:
    print("Error: el archivo no existe")


# 20Guardar una lista de nombres ingresados por el usuario en nombres.txt
with open("nombres.txt", "w") as f:
    while True:
        nombre = input("Ingresa un nombre: ")
        if nombre.lower() == "salir":
            break
        f.write(nombre + "\n")

print("Proceso terminado correctamente")


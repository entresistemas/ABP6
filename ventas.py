import json
import os
from datetime import datetime


# Verificar si el archivo de clientes existe, y crearlo si no
if not os.path.isfile("clientes.json"):
    with open("clientes.json", "w") as archivo:
        json.dump([], archivo)


# Función para crear un nuevo cliente
def crear_cliente():
    # Ingresar Datos de Cliente
    nombre = input("Ingrese Nombre de Cliente : ")
 
 
    # Cargar los usuarios desde el archivo externo
    with open("clientes.json", "r") as archivo:
        clientes = json.load(archivo)

    # Crear un diccionario con los datos del usuario
    nuevo_cliente = {
        "id": len(clientes) + 1,
        "nombre": nombre,
        
    }

    # Agregar el usuario al diccionario
    clientes.append(nuevo_cliente)

    # Guardar los usuarios en el archivo externo
    with open("clientes.json", "w") as archivo:
        json.dump(clientes, archivo)

    # Mostrar un mensaje de confirmación
    print("Usuario creado con éxito")

# Función para mostrar todos los usuarios
def mostrar_clientes():
    # Cargar los usuarios desde el archivo externo
    with open("clientes.json", "r") as archivo:
        clientes = json.load(archivo)

    # Mostrar los clientes en pantalla
    for cliente in clientes:
        print(cliente)
    print("Presiones Enter para Continuar")
    input()
    os.system("cls" if os.name == "nt" else "clear")



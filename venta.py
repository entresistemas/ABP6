import json
import os
import time
from colorama import Fore, Back
# Cargar los productos desde el archivo externo
with open("clientes.json", "r") as archivo:
    clientes = json.load(archivo)
# Cargar los productos desde el archivo externo
with open("bodega.json", "r") as archivo:
    productos = json.load(archivo)

def valida_stock(id, cant):
    for producto in productos:
        if producto["id"] == id:
            if producto["stock"] >= cant:
                return True
            else:
                return False
            
def valida_numero(num):
    return True if num.isdigit() else False

def valida_venta(num):
    return True if num.isdigit() else False

def compra_producto():
    cantOk = True
    os.system("cls" if os.name == "nt" else "clear")

    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "******* Clientes *******" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)

    # Mostrar los clientes en pantalla
    for cliente in clientes:
        print(f"ID: {cliente['id']}, Nombre: {cliente['nombre']}")

    # Solicitar al usuario que ingrese el ID del cliente comprador
    cliente_id = int(input("Ingrese el ID cliente: "))

    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "*** Productos Venta ****" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)

    # Mostrar los productos en pantalla
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

    # Solicitar al usuario que ingrese el ID del producto a comprar
    producto_id = int(input("Ingrese el ID del producto a comprar: "))

    # Solicitar al usuario que ingrese cantidad a comprar
    while cantOk:
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        producto_cant = input("Ingrese cantidad: ")
        if not valida_numero(producto_cant):
            print('Debes ingresar un número')
            continue
        else:
            cantOk = False
    # Función para validar stock
    os.system("cls" if os.name == "nt" else "clear")
    if valida_stock(producto_id, producto_cant):
        print('Compra aprobada y en camino!!')
    else:
        print('Compra cancelada: no hay suficiente stock para satisfacer el pedido!!')
    time.sleep(3)
    os.system("cls" if os.name == "nt" else "clear")

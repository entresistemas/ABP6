import json
import os
from time import sleep


# Verificar si el archivo de bodega, y crearlo si no
if not os.path.isfile("bodega.json"):
    with open("bodega.json", "w") as archivo:
        json.dump([], archivo)

# Función para crear un nuevo producto
def crear_producto():
    # Pedir  los datos del productos
    nombre = input("Digite Nombre de Producto: ")
    precio = input("Ingrese precio: ")
    stock = input("Ingrese stock: ")
   

    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)

    # Crear un diccionario con los datos del producto
    nuevo_producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        
    }

    # Agregar producto al diccionario
    productos.append(nuevo_producto)

    # Guardar los clientes en el archivo externo
    with open("bodega.json", "w") as archivo:
        json.dump(productos, archivo)

    # Mostrar un mensaje de confirmación
    print("Producto creado con éxito")


#Función Actualizar Stock
def actualizar_stock():
    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)

    # Mostrar los productos en pantalla
    for producto in productos:
        print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")

    # Solicitar al usuario que ingrese el ID del producto a actualizar
    producto_id = int(input("Ingrese el ID del producto a actualizar: "))

    # Buscar el producto por su ID
    for producto in productos:
        if producto['id'] == producto_id:
            # Solicitar al usuario que ingrese el nuevo stock
            nuevo_stock = int(input("Ingrese la nueva cantidad de stock: "))

            # Actualizar el stock del producto
            producto['stock'] = nuevo_stock

            # Guardar los productos actualizados en el archivo externo
            with open("bodega.json", "w") as archivo:
                json.dump(productos, archivo, indent=4)

            print(f"Se ha actualizado el stock del producto {producto['nombre']} a {nuevo_stock} unidades.")
            input("Presione Enter para continuar.")
            return

    # Si no se encontró el producto, mostrar un mensaje de error
    print(f"No se encontró un producto con ID {producto_id}")
    input("Presione Enter para continuar.")


# Función para mostrar Unidades disponibles Todos los Productos
def uni_disp_producto():
    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)

    # Mostrar las unidades disponibles x producto
    for producto in productos:
        print(producto['nombre'], producto['stock'])
    input("Presione Enter para continuar: ")
    os.system("cls" if os.name == "nt" else "clear")

# Función para mostrar Unidades disponibles x Productos Seleccionados 
def uni_disp_producto_sel():
    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)
    
    # Mostrar los productos y su ID
    for producto in productos:
        print(producto['id'],producto['nombre'])
    
    # Solicitar al usuario que ingrese el ID del producto
    producto_id = int(input("Ingrese el ID del producto que desea consultar: "))

    # Buscar el producto seleccionado por ID y mostrar sus unidades disponibles
    for producto in productos:
        if producto['id'] == producto_id:
            print(f"Unidades disponibles de {producto['nombre']}: {producto['stock']}")
            input("Presione Enter para continuar: ")
            os.system("cls" if os.name == "nt" else "clear")
            return
    # Si no se encontró el producto, mostrar un mensaje de error
    print(f"No se encontró un producto con ID {producto_id}")
    input("Presione Enter para continuar: ")
    pass
    

# Función para mostrar Todos los Productos
def mostrar_productos():
    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)

    # Mostrar los productos en pantalla
    for producto in productos:
        print(producto)
    input("Presione Enter para continuar: ")

# Función para mostrar Productos x Stock Mínimo
def mostrar_productos_cant():
    # Cargar los productos desde el archivo externo
    with open("bodega.json", "r") as archivo:
        productos = json.load(archivo)
    
    # Solicitar al usuario que ingrese el Stock Minimo
    stock_min = int(input("Ingrese el Stock Minimo que desee Consultar: "))

    # Mostrar los productos en pantalla
    for producto in productos:
        if int(producto['stock']) >= stock_min:
            print(f"Unidades disponibles de {producto['nombre']}: {producto['stock']}")
            
    input("Presione Enter para continuar: ")
    os.system("cls" if os.name == "nt" else "clear")
    return

    



def eliminar_producto():
    # Cargar los productos desde el archivo externo
    with open("productos.json", "r") as archivo:
        productos = json.load(archivo)

    # Mostrar los productos en pantalla para que el usuario elija cuál eliminar
    for producto in productos:
        print(producto)

    # Pedir al usuario el ID del producto que desea eliminar
    id_producto = int(input("Ingrese el ID del producto que desea eliminar: "))

    # Buscar el producto por su ID y eliminarlo de la lista de productos
    for i, producto in enumerate(productos):
        if producto["id"] == id_producto:
            del productos[i]
            break

    # Guardar los productos actualizados en el archivo externo
    with open("productos.json", "w") as archivo:
        json.dump(productos, archivo)

    # Mostrar un mensaje de confirmación
    print("Producto eliminado con éxito")





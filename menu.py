import json
import os
from colorama import Fore, Back, Style
from bodega import crear_producto, mostrar_productos, uni_disp_producto, uni_disp_producto_sel, mostrar_productos_cant, actualizar_stock
from ventas import compra_producto

# Configurar Colorama
Fore.GREEN = '\033[92m'
Fore.RED = '\033[91m'
Fore.RESET = '\033[0m'
Back.GREEN = '\033[42m'
Back.RED = '\033[41m'
Back.RESET = '\033[0m'


#Menú Clientes
# Función para administrar clientes
def control_ventas():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "** Control de Ventas  **" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Fore.GREEN + "1. Registrar nuevo Cliente" + Fore.RESET)
        print(Fore.GREEN + "2. Mostrar N° de Clientes Registrado" + Fore.RESET)
        print(Fore.GREEN + "3. Comprar" + Fore.RESET)
      
        opcion = input(Fore.YELLOW + "Selecciona una opción: " + Fore.RESET)

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            compra_producto()
        elif opcion == "0":
            break
        else:
            print(Back.RED + Fore.WHITE + "Opción inválida" + Back.RESET + Fore.RESET)

#Menú Control Bodega
# Función para Control de Bodega
def control_bodega():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "**   Control Bodega   **" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Fore.GREEN + "1. Crear nuevo Producto" + Fore.RESET)
        print(Fore.GREEN + "2. Actualizar Stock" + Fore.RESET)
        print(Fore.GREEN + "3. Unidades Disponibles x Producto" + Fore.RESET)
        print(Fore.GREEN + "4. Unidades Disponibles x Producto Seleccionado" + Fore.RESET)
        print(Fore.GREEN + "5. Listar Todos los Productos" + Fore.RESET)
        print(Fore.GREEN + "6. Listar Todos los Productos con + de Cantidad Seleccionada" + Fore.RESET)
        print(Fore.GREEN + "0. Volver" + Fore.RESET)
        opcion = input(Fore.YELLOW + "Selecciona una opción: " + Fore.RESET)

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            uni_disp_producto()
        elif opcion == "4":
            uni_disp_producto_sel()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            mostrar_productos_cant()
            
        elif opcion == "0":
            break
        else:
            print(Back.RED + Fore.WHITE + "Opción inválida" + Back.RESET + Fore.RESET)

def control_venta():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "**   Control Bodega   **" + Back.RESET)
        print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
        print(Fore.GREEN + "1. Crear nuevo Producto" + Fore.RESET)
        print(Fore.GREEN + "2. Actualizar Stock" + Fore.RESET)
        print(Fore.GREEN + "3. Unidades Disponibles x Producto" + Fore.RESET)
        print(Fore.GREEN + "4. Unidades Disponibles x Producto Seleccionado" + Fore.RESET)
        print(Fore.GREEN + "5. Listar Todos los Productos" + Fore.RESET)
        print(Fore.GREEN + "6. Listar Todos los Productos con + de Cantidad Seleccionada" + Fore.RESET)
        print(Fore.GREEN + "0. Volver" + Fore.RESET)
        opcion = input(Fore.YELLOW + "Selecciona una opción: " + Fore.RESET)

        if opcion == "1":
            crear_producto()
        elif opcion == "2":
            actualizar_stock()
        elif opcion == "3":
            uni_disp_producto()
        elif opcion == "4":
            uni_disp_producto_sel()
        elif opcion == "5":
            mostrar_productos()
        elif opcion == "6":
            mostrar_productos_cant()
            
        elif opcion == "0":
            break
        else:
            print(Back.RED + Fore.WHITE + "Opción inválida" + Back.RESET + Fore.RESET)






# Menú principal

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "** Sistema TeloVendo  **" + Back.RESET)
    print(Back.GREEN + Fore.WHITE + "************************" + Back.RESET)
    print(Fore.GREEN + "1. Control de Bodega" + Fore.RESET)
    print(Fore.GREEN + "2. Control Ventas" + Fore.RESET)
    print(Fore.GREEN + "0. Salir" + Fore.RESET)
    opcion = input(Fore.YELLOW + "Selecciona una opción: " + Fore.RESET)

    if opcion == "1":
        control_bodega()
    elif opcion == "2":
        control_ventas()
    elif opcion == "0":
        break
    else:
        print(Back.RED + Fore.WHITE + "Opción inválida" + Back.RESET + Fore.RESET)
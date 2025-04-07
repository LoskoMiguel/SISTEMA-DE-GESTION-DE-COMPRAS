import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from db.conexion import get_conection

def listar_producto_especifico():
    conn = get_conection()
    cursor = conn.cursor()

    nombre = input("Ingrese el Nombre del producto que desea listar: ")

    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()

    if producto:
        print(f"Producto encontrado: ")
        print(f"Nombre: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio: {producto[2]}")
    else:
        print("❌ Producto no encontrado.")

    conn.close()

listar_producto_especifico()
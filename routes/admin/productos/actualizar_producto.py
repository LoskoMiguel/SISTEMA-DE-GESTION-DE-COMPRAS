import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from db.conexion import get_conection

def actualizar_producto():
    conn = get_conection()
    cursor = conn.cursor()

    nombre = input("Ingrese el Nombre del producto que desea actualizar: ")

    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()

    if producto:
        print(f"Producto encontrado: ")
        print(f"Nombre: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio: {producto[2]}")
        print("Ingrese los nuevos datos del producto (deje en blanco para no cambiar):")

        nombre_producto = input("Ingrese el nuevo nombre del producto: ")
        precio_producto = input("Ingrese el nuevo precio del producto: ")
        cantidad_producto = input("Ingrese la nueva cantidad del producto: ")

        cursor.execute("""
            UPDATE productos
            SET producto = ?, stock = ?, price = ?
            WHERE producto = ?
        """, (nombre_producto if nombre_producto else producto[0], 
               cantidad_producto if cantidad_producto else producto[1], 
               precio_producto if precio_producto else producto[2], 
               nombre))

        conn.commit()
        print("✅ Producto actualizado con éxito.")
    else:
        print("❌ Producto no encontrado.")

    conn.close()

actualizar_producto()
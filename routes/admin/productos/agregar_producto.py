import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from db.conexion import get_conection

def agregar_producto():
    conn = get_conection()
    cursor = conn.cursor()

    nombre = input("Nombre del producto: ")

    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()
    
    if producto:
        print ("❌ El producto ya existe en la base de datos.")
        return
    else:
        print("✅ Producto no encontrado, puede agregarlo.")
        nombre = input("Ingrese el nombre del producto: ")
        stock = int(input("Ingrese el stock del producto: "))
        price = float(input("Ingrese el precio del producto: "))

        # Insertar el nuevo producto en la base de datos
        cursor.execute("INSERT INTO productos (producto, stock, price) VALUES (?, ?, ?)", (nombre, stock, price))
        conn.commit()
        print("✅ Producto agregado correctamente.")

    conn.close()


if __name__ == "__main__":
    agregar_producto()
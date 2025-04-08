import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from db.conexion import get_conection

def eliminar_producto():
    conn = get_conection()
    cursor = conn.cursor()

    nombre = input("Ingrese el Nombre del producto que desea eliminar: ")

    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()

    if producto:
        print("✅ Producto encontrado.")

        opcion = input("""opción:
            1. Eliminar Producto  """)

        if opcion == "1":
            cursor.execute("DELETE FROM productos WHERE producto = ?", (nombre,))
            conn.commit()
            print("✅ Producto eliminado con éxito.")

    else:
        print("❌ Producto no encontrado.")
        return


if __name__ == "__main__":
    eliminar_producto()
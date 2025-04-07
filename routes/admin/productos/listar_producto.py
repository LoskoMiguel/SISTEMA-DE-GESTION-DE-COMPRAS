import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from db.conexion import get_conection

def listar_todos_productos():
    conn = get_conection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    for producto in productos:
        print("ID:", producto[0])
        print("Nombre:", producto[1])
        print("Stock:", producto[2])
        print("Precio:", producto[3])
        print()
    cursor.close()
    conn.close()
    return productos

listar_todos_productos()
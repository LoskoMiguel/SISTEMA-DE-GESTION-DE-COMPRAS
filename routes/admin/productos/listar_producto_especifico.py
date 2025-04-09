import sys
import os

# Agregamos al sys.path la ruta del directorio raíz del proyecto para poder importar módulos desde carpetas superiores
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Importamos la función que permite establecer la conexión con la base de datos
from db.conexion import get_conection

# Función que permite listar los datos de un producto específico buscado por su nombre
def listar_producto_especifico():
    # Establecemos conexión a la base de datos y creamos un cursor para ejecutar las consultas SQL
    conn = get_conection()
    cursor = conn.cursor()

    # Solicitamos al usuario el nombre del producto que desea consultar
    nombre = input("Ingrese el Nombre del producto que desea listar: ")

    # Ejecutamos una consulta SQL para buscar el producto en la base de datos por nombre
    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()  # Obtenemos el primer resultado de la consulta

    if producto:
        # Si el producto fue encontrado, mostramos su información en pantalla
        print(f"Producto encontrado: ")
        print(f"Nombre: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio: {producto[2]}")
    else:
        # Si el producto no existe, mostramos un mensaje de error
        print("❌ Producto no encontrado.")

    # Cerramos la conexión a la base de datos
    conn.close()

# Ejecutamos la función listar_producto_especifico()
listar_producto_especifico()
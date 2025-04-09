import sys
import os

# Agregamos al sys.path la ruta del directorio raíz del proyecto para poder importar módulos desde carpetas superiores
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Importamos la función que establece la conexión con la base de datos
from db.conexion import get_conection

# Función que lista todos los productos registrados en la base de datos
def listar_todos_productos():
    # Establecemos la conexión a la base de datos y creamos un cursor para ejecutar consultas
    conn = get_conection()
    cursor = conn.cursor()

    # Ejecutamos una consulta para obtener todos los registros de la tabla 'productos'
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()  # Obtenemos todos los resultados de la consulta

    # Recorremos la lista de productos y mostramos sus datos en consola
    for producto in productos:
        print("ID:", producto[0])
        print("Nombre:", producto[1])
        print("Stock:", producto[2])
        print("Precio:", producto[3])
        print()  # Línea en blanco para separar visualmente los productos

    # Cerramos el cursor y la conexión a la base de datos
    cursor.close()
    conn.close()

    # Retornamos la lista de productos obtenida
    return productos

# Ejecutamos la función para listar todos los productos
listar_todos_productos()
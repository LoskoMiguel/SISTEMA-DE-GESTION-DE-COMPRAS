import sys
import os

# Agregamos al sys.path la ruta del directorio raíz del proyecto para poder importar módulos desde carpetas superiores
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# Importamos la función que nos permite obtener la conexión a la base de datos
from db.conexion import get_conection

# Función encargada de actualizar los datos de un producto existente en la base de datos
def actualizar_producto():
    # Establecemos la conexión a la base de datos y creamos un cursor para ejecutar consultas SQL
    conn = get_conection()
    cursor = conn.cursor()

    # Solicitamos el nombre del producto que se desea actualizar
    nombre = input("Ingrese el Nombre del producto que desea actualizar: ")

    # Buscamos el producto en la base de datos por nombre
    cursor.execute("SELECT producto, stock ,price FROM productos WHERE producto = ?", (nombre,))
    producto = cursor.fetchone()  # Obtenemos el primer resultado de la consulta

    if producto:
        # Si el producto fue encontrado, mostramos sus datos actuales
        print(f"Producto encontrado: ")
        print(f"Nombre: {producto[0]}")
        print(f"Cantidad: {producto[1]}")
        print(f"Precio: {producto[2]}")

        # Indicamos al usuario que puede actualizar los campos dejando en blanco los que no desee cambiar
        print("Ingrese los nuevos datos del producto (deje en blanco para no cambiar):")

        # Pedimos los nuevos valores. Si el usuario deja el campo vacío, se conservará el valor actual
        nombre_producto = input("Ingrese el nuevo nombre del producto: ")
        precio_producto = input("Ingrese el nuevo precio del producto: ")
        cantidad_producto = input("Ingrese la nueva cantidad del producto: ")

        # Ejecutamos la actualización del producto usando los nuevos valores o manteniendo los antiguos si el input está vacío
        cursor.execute("""
            UPDATE productos
            SET producto = ?, stock = ?, price = ?
            WHERE producto = ?
        """, (nombre_producto if nombre_producto else producto[0], 
              cantidad_producto if cantidad_producto else producto[1], 
              precio_producto if precio_producto else producto[2], 
              nombre))

        # Confirmamos los cambios en la base de datos
        conn.commit()
        print("✅ Producto actualizado con éxito.")
    else:
        # Si no se encuentra el producto, mostramos un mensaje de error
        print("❌ Producto no encontrado.")

    # Cerramos la conexión con la base de datos
    conn.close()

# Ejecutamos la función actualizar_producto()
actualizar_producto()
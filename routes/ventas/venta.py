import sys
import os

# Agregamos al sys.path la ruta del directorio raíz del proyecto para poder importar módulos de carpetas superiores
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Importamos la función para obtener la conexión a la base de datos desde el módulo de conexión
from db.conexion import get_conection

# Función principal que ejecuta el flujo de venta de productos
def venta():
    # Datos de prueba para simular una cuenta bancaria y un saldo inicial
    cuenta_bancaria_test = "543677"
    contrasena_cuenta = "1234test"
    saldo = 10000
    
    # Establecemos la conexión a la base de datos y creamos el cursor para ejecutar consultas SQL
    conn = get_conection()
    cursor = conn.cursor()

    # Solicitamos al usuario el nombre del producto que desea comprar
    nombre_producto = input("Nombre del producto: ")

    # Consultamos en la base de datos si el producto existe, obteniendo nombre, stock y precio
    cursor.execute("SELECT producto, stock, price FROM productos WHERE producto = ?", (nombre_producto,))
    producto = cursor.fetchone()  # Obtenemos el primer resultado de la consulta

    if producto:
        # Si el producto fue encontrado, mostramos su información
        print("✅ Producto encontrado.")
        print(f"Producto: {producto[0]}, Stock: {producto[1]}, Precio: {producto[2]}")
        
        # Solicitamos la cantidad que el usuario desea comprar
        cantidad = int(input("Ingrese la cantidad a vender: "))

        # Validamos que la cantidad sea mayor a 0 y menor o igual al stock disponible
        if cantidad > producto[1] or cantidad <= 0:
            print("❌ Cantidad no válida.")
            return
        else:
            # Solicitamos los datos bancarios del usuario para verificar la cuenta
            cuenta_usuario = input("Cuenta Bancaria:  ")
            contrasena_cuenta = input("Contraseña de la cuenta:  ")

            # Verificamos si los datos bancarios coinciden con los de prueba
            if cuenta_usuario == cuenta_bancaria_test and contrasena_cuenta == contrasena_cuenta:
                print("✅ Cuenta verificada.")
                
                # Calculamos el total a pagar por la venta
                total = producto[2] * cantidad
                print(f"Total a pagar: {total}")

                # Validamos si el saldo es suficiente para cubrir el total
                if total > saldo:
                    print("❌ Fondos insuficientes.")
                    return
                else:
                    # Realizamos la venta: descontamos el total del saldo
                    saldo -= total
                    print(f"✅ Venta realizada. Saldo restante: {saldo}")

                    # Actualizamos el stock del producto en la base de datos
                    cursor.execute("UPDATE productos SET stock = stock - ? WHERE producto = ?", (cantidad, nombre_producto))

                    # Registramos la venta en la tabla de ventas
                    cursor.execute("INSERT INTO ventas (nombre_producto, precio_unidad, cantidad_lleva, precio_total, cuenta_usuario) VALUES (?, ?, ?, ?, ?)", (nombre_producto, producto[2], cantidad, total, cuenta_usuario))
                    
                    # Guardamos los cambios en la base de datos
                    conn.commit()
            else:
                # Si la verificación bancaria falla, mostramos mensaje de error
                print("❌ Cuenta o contraseña incorrecta.")
                return

    else:
        # Si el producto no fue encontrado en la base de datos, mostramos mensaje de error
        print("❌ Producto no encontrado.")

# Ejecutamos la función venta()
venta()
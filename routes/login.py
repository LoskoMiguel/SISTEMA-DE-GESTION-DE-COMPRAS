import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.conexion import get_conection

conn = get_conection()
cursor = conn.cursor()

def login():
    intentos = 0

    while intentos < 3:
        username = input("Cual es el nombre de usuario:  ")
        contrasena = input("Cual es la contrasena:  ")

        cursor.execute("SELECT rol FROM users WHERE username = ? AND password = ?", (username, contrasena))
        usuario = cursor.fetchone()

        if usuario:
            print("✅ Bienvenido al sistema")
            break
        else:
            intentos += 1
            print("❌ Usuario o contraseña incorrectos")
            if intentos == 1:
                print("⏳ Te quedan 2 intentos")
            elif intentos == 2:
                print("⏳ Te queda 1 intento")
            elif intentos >= 3:
                print("⛔ Intentos insuficientes. Acceso bloqueado.")
                break

    conn.close()

login()
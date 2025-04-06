import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.conexion import get_conection
from admin.registrar import registrar_usuario

def login():
    conn = get_conection()
    cursor = conn.cursor()
    intentos = 0

    while intentos < 3:
        username = input("Cual es el nombre de usuario: ")
        contrasena = input("Cual es la contrasena: ")

        cursor.execute("SELECT rol FROM users WHERE username = ? AND password = ?", (username, contrasena))
        usuario = cursor.fetchone()
        
        if usuario:
            rol = usuario[0]
            print("✅ Bienvenido al sistema")
            
            if rol == 2:
                print("\n👤 Rol: Administrador")
                while True:
                    opcion = input("""
                    Elige Una Opcion:
                    1. Crear un nuevo usuario
                    Opción: """)
                    
                    if opcion == "1":
                        registrar_usuario()
            else:
                print("\n👤 Rol: Usuario")
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

if __name__ == "__main__":
    login()
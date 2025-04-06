import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from db.conexion import get_conection

def registrar_usuario():
    conn = get_conection()
    cursor = conn.cursor()
    
    while True:
        nombre = input("Nombre: ")
        username = input("Usuario: ")
        password = input("Contraseña: ")
        rol = input("Rol (admin/user): ")

        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        registro = cursor.fetchone()

        if registro:
            print("❌ Nombre de usuario ya existe")
            return

        if rol.lower() == "admin":
            cursor.execute("INSERT INTO users (name, username, password, rol) VALUES (?, ?, ?, ?)", (nombre, username, password, 2))
            conn.commit()
            print("✅ Usuario registrado correctamente")
            break
        
        elif rol.lower() == "user":
            cursor.execute("INSERT INTO users (name, username, password, rol) VALUES (?, ?, ?, ?)", (nombre, username, password, 1))
            conn.commit()
            print("✅ Usuario registrado correctamente")
            break
        
        else:
            print("❌ Rol no válido. Registro fallido.")
            print("Por favor, elige 'admin' o 'user'.")
    
    conn.close()
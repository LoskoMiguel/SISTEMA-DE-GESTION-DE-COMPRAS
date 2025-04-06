import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from db.conexion import get_conection

conn = get_conection()
cursor = conn.cursor()

# Hacer sistema de registro

def registrar_usuario():
    nombre = input("Nombre: ")
    username = input("Usuario: ")
    password = input("Contraseña: ")
    rol = input("Rol: ")

    # Verificar si el username ya existe
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    registro = cursor.fetchone()

    if registro:
        print("❌ Nombre de usuario ya existe")
    else:
        cursor.execute("INSERT INTO users (name, username, password, rol) VALUES (?, ?, ?, ?)", (nombre, username, password, rol,))
        conn.commit()
        print("✅ Usuario registrado correctamente")

registrar_usuario()
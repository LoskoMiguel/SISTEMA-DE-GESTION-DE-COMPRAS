import sqlite3

conn = sqlite3.connect("db/data.db")
cursor = conn.cursor()

# Ver Informacion De Usuarios
# cursor.execute("SELECT * FROM personas")
# personas = cursor.fetchall()
# for persona in personas:
#     id, nombre, numero, edad = persona

#     print(f"""Los Datos Son:
#                 id : {id}
#                 Nombre : {nombre}
#                 Numero De Telefono : {numero}
#                 Edad : {edad}
#           """)

# Ver Informacion De UN Usuario
# cursor.execute("SELECT * FROM personas WHERE nombre = ?", ("losko",))
# persona = cursor.fetchone()

# if persona:
#     id, nombre, numero, edad = persona

#     print(f"""Los Datos Son:
#                 id : {id}
#                 Nombre : {nombre}
#                 Numero De Telefono : {numero}
#                 Edad : {edad}
#           """)
# else:
#     print("Persona NO Encontrada")


#Agregar Persona
# nombre = input("Cual es el nombre:  ")
# celular = int(input("Cual es el numero:  "))
# edad = int(input("Cual es tu edad:  "))
# cursor.execute("INSERT INTO personas (nombre, celular, edad) VALUES (?,?,?)", (nombre, celular, edad,))
# conn.commit()
# print("Usuario Agregado")

#Actualizar Persona
# nombre_actualizar = input("Nombre Persona Para Actualizar:  ")
# cursor.execute("SELECT nombre FROM personas WHERE nombre = ?", (nombre_actualizar,))
# existe = cursor.fetchone()
# if existe:
#     nuevo_nombre = input("Cual es el nuevo nombre:  ")
#     cursor.execute("UPDATE personas SET nombre = ? WHERE nombre = ?", (nuevo_nombre, nombre_actualizar,))
#     conn.commit()
#     print("Nombre Actualizado")
# else:
#     print("Usuario No Encontrado")

# #Eliminar Personas
# nombre_eliminar = input("Nombre Persona Para Eliminar:  ")
# cursor.execute("SELECT nombre FROM personas WHERE nombre = ?", (nombre_eliminar,))
# existe = cursor.fetchone()
# if existe:
#     cursor.execute("DELETE FROM personas WHERE nombre = ?", (nombre_eliminar,))
#     conn.commit()
#     print("Usuario ELiminado")
# else:
#     print("Usuario No Econtrado")

print("lo que sea")
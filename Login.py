nombre =  " "
clave = " "
diccionario_de_usuarios = {"usuario1": {"contrasenia": clave, "saldo": 0}}


print("Bienvenido " + nombre + " a la aplicación de inicio de sesión.")

# print(diccionario_de_usuarios.keys())






# if nombre in diccionario_de_usuarios.keys():
#     print("El usuario existe en el diccionario.")
# else:
#     print("El usuario no existe en el diccionario.")

# diccionario_de_usuarios[nombre[contrasenia]] == clave 


for clave , valor in diccionario_de_usuarios.items():
    print("Clave:", clave)
    print("Valor:", valor)
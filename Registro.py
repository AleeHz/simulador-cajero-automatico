import Login

print("Bienvenido al sistema de registro de usuarios.")
nombre = input("Ingrese su nombre: ")
clave = input("Ingrese su clave: ")
Confirmar_clave = input("Confirme su clave: ")

if clave == Confirmar_clave:
    print("Registro exitoso. Bienvenido, " + nombre + "!")
    Login.diccionario_de_usuarios[nombre] = {"contrasenia": clave, "saldo": 0}
else:
    print("Las claves no coinciden. Por favor, intente de nuevo.")

import datetime

# nombre =  " "
# clave = " "
contador_intentos = 0
perfiles_existentes = {  "usuario1": {                           #esto si el usuario exites y se logea directamente
                            "contraseña": 1234,
                            "saldo": 1000.0,
                            "historial": ["Depósito inicial: $1000"]
                                    },
                        "usuario2": {
                            "contraseña": 5678,
                            "saldo": 2000.0,
                            "historial": ["Depósito inicial: $2000"]
                        },
                         "usuario3": {
                            "contraseña": 2026,
                            "saldo": 3000.0,
                            "historial": ["Depósito inicial: $3000"]
                        }} #esto es de prueba 

perfiles_nuevos = { } #esto es de prueba

def login():

    input_usuario = input("Ingrese su nombre de usuario: ")

    while input_usuario not in perfiles_existentes.keys() or input_usuario not in perfiles_nuevos.keys():
        print("El usuario no existe. Por favor, intente de nuevo.")
        input_usuario = input("Ingrese su nombre de usuario: ")

    input_contraseña = int(input("Ingrese su contraseña: "))

    if input_usuario in perfiles_existentes.keys() or input_usuario in perfiles_nuevos.keys(): 
        if input_usuario in perfiles_existentes.keys():
            if input_contraseña == perfiles_existentes[input_usuario]["contraseña"]:
                print("Inicio de sesión exitoso. Bienvenido, " + input_usuario + "!")
                print("Tu saldo actual es: $" + str(perfiles_existentes[input_usuario]["saldo"]))
                print("Tu historial de transacciones es: " + str(perfiles_existentes[input_usuario]["historial"]))
            else:
                print("Contraseña incorrecta. Por favor, intente de nuevo.")
                contador_intentos += 1
                if contador_intentos >= 3:
                    print("Has excedido el número máximo de intentos. Por favor, inténtalo de nuevo más tarde.")
                    return

        elif input_usuario in perfiles_nuevos.keys():
            if input_contraseña == perfiles_nuevos[input_usuario]["contraseña"]:
                print("Inicio de sesión exitoso. Bienvenido, " + input_usuario + "!")
                print("Tu saldo actual es: $" + str(perfiles_nuevos[input_usuario]["saldo"]))
                print("Tu historial de transacciones es: " + str(perfiles_nuevos[input_usuario]["historial"]))
            else:
                print("Contraseña incorrecta. Por favor, intente de nuevo.")
                contador_intentos += 1
                if contador_intentos >= 3:
                    print("Has excedido el número máximo de intentos. Por favor, inténtalo de nuevo más tarde.")
                    return



# print(diccionario_de_usuarios.keys())





# if nombre in diccionario_de_usuarios.keys():
#     print("El usuario existe en el diccionario.")
# else:
#     print("El usuario no existe en el diccionario.")

# diccionario_de_usuarios[nombre[contrasenia]] == clave 


# for clave , valor in perfiles_existentes.items():
#     print("Clave:", clave)
#     print("Valor:", valor)
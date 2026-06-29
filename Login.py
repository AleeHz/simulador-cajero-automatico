import datetime
##hay q meter una opcion para ingresar plata y otra para retirar plata, y q se vayan sumando o restando al saldo, y q se vayan guardando en el historial de transacciones
# nombre =  " "
# clave = " "

base_usuarios = {  
    'usuario1': {                            
        "contraseña": "123",
        "saldo": 1000.0,
        "historial": ["Depósito inicial: $1000"]
    },
    'usuario2': {
        "contraseña": "5678",
        "saldo": 2000.0,
        "historial": ["Depósito inicial: $2000"]
    },
    'usuario3': {
        "contraseña": "2026",
        "saldo": 3000.0,
        "historial": ["Depósito inicial: $3000"]
    }
}


def login():
    contador_intentos = 0

    input_usuario = input("Ingrese su nombre de usuario: ")

    while input_usuario not in base_usuarios:
        print("El usuario no existe. Por favor, intente de nuevo.")
        input_usuario = input("Ingrese su nombre de usuario: ")

    

   
    while contador_intentos< 3:   
        input_contraseña = input("Ingrese su contraseña: ").strip()
        
        if input_contraseña == base_usuarios[input_usuario]["contraseña"]:
            print("Inicio de sesión exitoso. Bienvenido, " + input_usuario + "!")
                    # print("Tu saldo actual es: $" + str(base_usuarios[input_usuario]["saldo"]))
                    # print("Tu historial de transacciones es: " + str(base_usuarios[input_usuario]["historial"]))
            return input_usuario
        else:
            print("Contraseña incorrecta. Por favor, intente de nuevo.")
            contador_intentos += 1
        
        if contador_intentos == 3:
            print("Has excedido el número máximo de intentos. Por favor, inténtalo de nuevo más tarde.")
            #break
            return False
    return False
            
    
 


# print(diccionario_de_usuarios.keys())





# if nombre in diccionario_de_usuarios.keys():
#     print("El usuario existe en el diccionario.")
# else:
#     print("El usuario no existe en el diccionario.")

# diccionario_de_usuarios[nombre[contrasenia]] == clave 


# for clave , valor in perfiles_existentes.items():
#     print("Clave:", clave)
#     print("Valor:", valor)
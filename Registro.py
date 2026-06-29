import Login

def registro():
    print("Bienvenido al sistema de registro de usuarios.")
    input_usuario = input("Ingrese su nombre: ")

    if input_usuario in Login.base_usuarios:
        print("El usuario ya existe. Por favor, elija otro nombre de usuario.")
        return 


    input_contraseña = input("Ingrese su clave: ")
    Confirmar_clave = input("Confirme su clave: ")

    while input_contraseña != Confirmar_clave:
        print("Las claves no coinciden. Por favor, intente de nuevo.")
        print("\n")

        input_contraseña = input("Ingrese su clave: ")
        Confirmar_clave = input("Confirme su clave: ")
        

    if input_contraseña == Confirmar_clave:
        print("Registro exitoso. Bienvenido, " + input_usuario + "!")
        Login.base_usuarios[input_usuario]={"contraseña": input_contraseña, "saldo": 0, "historial": []}
        
        return Login.base_usuarios
        
  




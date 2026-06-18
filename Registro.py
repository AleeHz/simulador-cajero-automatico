import Login

def registro():
    print("Bienvenido al sistema de registro de usuarios.")
    input_usuario = input("Ingrese su nombre: ")
    input_contraseña = input("Ingrese su clave: ")
    Confirmar_clave = input("Confirme su clave: ")

    while input_contraseña != Confirmar_clave:
        print("Las claves no coinciden. Por favor, intente de nuevo.")
        print("\n")

        input_contraseña = input("Ingrese su clave: ")
        Confirmar_clave = input("Confirme su clave: ")
        

    if input_contraseña == Confirmar_clave:
        print("Registro exitoso. Bienvenido, " + input_usuario + "!")
        Login.perfiles_nuevos[input_usuario]={"contraseña": input_contraseña, "saldo": 0, "historial": []}
        
        return Login.perfiles_nuevos
        
  




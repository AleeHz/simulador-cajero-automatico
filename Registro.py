import Login

def registro():
    print("Bienvenido al sistema de registro de usuarios.")
    nombre_n = input("Ingrese su nombre: ")
    clave_n = input("Ingrese su clave: ")
    Confirmar_clave = input("Confirme su clave: ")

    while clave_n != Confirmar_clave:
        print("Las claves no coinciden. Por favor, intente de nuevo.")
        print("\n")

        clave_n = input("Ingrese su clave: ")
        Confirmar_clave = input("Confirme su clave: ")

    if clave_n == Confirmar_clave:
        print("Registro exitoso. Bienvenido, " + nombre_n + "!")
        Login.perfiles_nuevos[nombre_n] = {"contrasenia": clave_n, "saldo": 0, "historial": []}
        Login.login()

   




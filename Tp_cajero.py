import Registro
import Login

#menu de incio de login y registro
while True:
    print("BIENVENIDO AL CAJERO AUTOMÁTICO")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Ingrese un numero para realizar una accion ")
    print("Elegiste la opción:", opcion)

    if opcion == "1":
        while True:
            usuario_actual = Login.login()
            if usuario_actual != False:
                print("Has iniciado sesión correctamente, ahora puedes acceder a las opciones del cajero automático.")
                break
        break
        
    elif opcion == "2":
        Registro.registro()
        # break
    elif opcion == "3":
        print("Adios")
        break
    else:
        print("Opción no válida, por favor ingrese un número del 1 al 3")
        






while True:  #bucle principal del programa, se repetirá hasta que el usuario decida salir
    
    if opcion == "3":
        print("Gracias por usar el cajero automático, vuelva pronto")
        break

    print("BIENVENIDO AL CAJERO AUTOMÁTICO")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Extraer")
    print("4. Transferir")
    print("5. Ver historial")
    print("6. Salir") 
    opcion = input ("Ingrese un numero para realizar una accion ")
    print("Elegiste la opción:", opcion)


    if opcion == "1":
        print("Elegiste consultar saldo")
        if usuario_actual in Login.perfiles_existentes.keys():
            saldo = Login.perfiles_existentes[usuario_actual]["saldo"]
        else:
            saldo = Login.perfiles_nuevos[usuario_actual]["saldo"]
        print("Tu saldo actual es: $" + str(saldo))
    
    elif opcion == "2":
        print("Elegiste depositar") 


    elif opcion == "3":
        print("Elegiste extraer")
      

    elif opcion == "4": 
        print("Elegiste transferir")
      

      


    elif opcion == "5":
        print("Elegiste ver historial")
        if usuario_actual in Login.perfiles_existentes.keys():
            historial = Login.perfiles_existentes[usuario_actual]["historial"]
        else:
            historial = Login.perfiles_nuevos[usuario_actual]["historial"]
        print("Fin del historial")
        print("------------------------------------------------")

       

    
    
    elif opcion == "6":
        print("Gracias por usar el cajero automático, vuelva pronto")
        break
    else:
        print("Opción no válida, por favor ingrese un número del 1 al 6")


    print("¿Desea continuar navegando? ")   #un bucle q le pregunta al usuario si quiere seguir usando el cajero o si ya termino
    respuesta = input("Ingrese 's' para sí o 'n' para no: ")
    
    if respuesta.lower() != 's':
        print("Gracias por usar el cajero automático, vuelva pronto")
        break
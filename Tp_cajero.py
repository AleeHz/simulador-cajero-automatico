import Registro
import Login

#menu de incio de login y registro
while True:
    print("BIENVENIDO AL CAJERO AUTOMÁTICO")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input ("Ingrese un numero para realizar una accion ")
    print("Elegiste la opción:", opcion)

    if opcion == "1":
        Login.login()
        break
    elif opcion == "2":
        Registro.registro()
        break
    elif opcion == "3":
        print("Adios")
        break
    else:
        print("Opción no válida, por favor ingrese un número del 1 al 3")
        






while opcion == "1" or opcion=="2":  #bucle principal del programa, se repetirá hasta que el usuario decida salir

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
     
    
    elif opcion == "2":
        print("Elegiste depositar") 


    elif opcion == "3":
        print("Elegiste extraer")
      

    elif opcion == "4": 
        print("Elegiste transferir")
      

      


    elif opcion == "5":
        print("Elegiste ver historial")
        # for movimiento in historial:
        #     print("-", movimiento)
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
historial = ["Depósito: $1000", "Extracción: $500", "Transferencia a M: $200"]  #esto es de ejemplo para ver si podia usarlo en el pto 5 q me muestre los elementos de la lista, pero no se si es correcto o no, lo deje para probarlo y ver si funciona, si no lo borro despues

while True:
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
        for movimiento in historial:
            print("-", movimiento)
        print("Fin del historial")
        print("------------------------------------------------")

       

    
    
    elif opcion == "6":
        print("Gracias por usar el cajero automático, vuelva pronto")
        break
    else:
        print("Opción no válida, por favor ingrese un número del 1 al 6")


    print("¿Desea continuar navegando? ")
    respuesta = input("Ingrese 's' para sí o 'n' para no: ")
    
    if respuesta.lower() != 's':
        print("Gracias por usar el cajero automático, vuelva pronto")
        break
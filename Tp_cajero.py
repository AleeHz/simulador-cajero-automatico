# historial = ["Depósito: $1000", "Extracción: $500", "Transferencia a M: $200"]  #esto es de ejemplo para ver si podia usarlo en el pto 5 q me muestre los elementos de la lista, pero no se si es correcto o no, lo deje para probarlo y ver si funciona, si no lo borro despues

perfiles_exitentes = {  "usuario1": {                           #esto si el usuario exites y se logea directamente
                            "contraseña": 1234,
                            "saldo": 1000,
                            "historial": ["Depósito inicial: $1000"]
                                    },
                        "usuario2": {
                            "contraseña": 5678,
                            "saldo": 2000,
                            "historial": ["Depósito inicial: $2000"]
                        },
                         "usuario3": {
                            "contraseña": 2026,
                            "saldo": 3000,
                            "historial": ["Depósito inicial: $3000"]
                        }}


#si se registra un nuevo usario, se le asigna un nuevo perfil con su contraseña y saldo inicial de 0

nuevo_usuario = input("Ingrese un nuevo nombre de usuario para registrarse: ")
nueva_contrasena = input("Ingrese una nueva contraseña para registrarse: ")
perfiles_nuevo_usuario = {nuevo_usuario: {
                        "contraseña": nueva_contrasena,
                        "saldo": 0,
                        "historial": []
}
}

#esto es para verificar si el nuevo usuario ya existe en los perfiles existentes, si es asi, se le da la bienvenida, sino se le dice que el usuario o contraseña son incorrectos. Es prueba esto
if nuevo_usuario in perfiles_exitentes and perfiles_exitentes[nuevo_usuario]["contraseña"] == nueva_contrasena:
    print("Bienvenido de nuevo, ", nuevo_usuario)
else:
   
    print("Usuario o contraseña incorrectos, por favor intente nuevamente o regístrese si no tiene una cuenta.")

while True:  #bucle principal del programa, se repetirá hasta que el usuario decida salir

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
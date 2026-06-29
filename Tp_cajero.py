import Registro
import Login

#menu de incio de login y registro
while True:
    while True:
        print("BIENVENIDO AL CAJERO AUTOMÁTICO")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Ingrese un numero para realizar una accion ")
        print("Elegiste la opción:", opcion)

        if opcion == "1":
            usuario_actual = Login.login()
            if usuario_actual != False:
                print("Has iniciado sesión correctamente, ahora puedes acceder a las opciones del cajero automático.")
                break
       
        
        elif opcion == "2":
            Registro.registro()
        # break
        
        elif opcion == "3":
            print("Adios")
            exit() #cierra el programa
        else:
            print("Opción no válida, por favor ingrese un número del 1 al 3")
        






    while True:  #bucle principal del programa, se repetirá hasta que el usuario decida salir
    
   
        print("BIENVENIDO AL CAJERO AUTOMÁTICO")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Extraer")
        print("4. Transferir")
        print("5. Ver historial")
        print("6. Cerrar sesión")
        opcion = input("Ingrese un numero para realizar una accion ")
        print("Elegiste la opción:", opcion)


        if opcion == "1":
            print("Elegiste consultar saldo")
            saldo=Login.base_usuarios[usuario_actual]["saldo"]
            print("Tu saldo actual es: $" + str(saldo))
    
        elif opcion == "2":
            print("Elegiste depositar") 
            monto = float(input("Ingrese el monto a depositar: $"))

            if monto >0:
                #vamos al diccionario de login y sumamos el monto al saldo del usuario actual
                Login.base_usuarios[usuario_actual]["saldo"] += monto

                #armamos el texto para el historial. El ':.2f' es para que muestre siempre 2 decimales
                registro = f"Depósito: ${monto:.2f}"
                #guardamos este texto en la lista de historial de este usuario
                Login.base_usuarios[usuario_actual]["historial"].append(registro)

                print(f"Depósito exitoso. Tu nuevo saldo es: ${monto:.2f}")
                print(f"Tu nuevo saldo es: ${Login.base_usuarios[usuario_actual]['saldo']:.2f}")
            else:
                # si el usuario puso 0 o un número negativo, lo rebotamos
                print("Monto inválido. Por favor, ingrese un monto positivo.")
           
        elif opcion == "3":
            print("Elegiste extraer")

            #pedimos el monto a extraer
            monto = float(input("Ingrese el monto a extraer: $"))

            #guardamos el saldo en una variable para no tener que escribir tanto
            saldo_actual = Login.base_usuarios[usuario_actual]["saldo"]

            #el monto tiene q ser mayor a cero
            if monto > 0:

                #el usaurio debe tener plata para extraer
                if monto <= saldo_actual:
                    #restamos el monto al saldo del usuario actual
                    Login.base_usuarios[usuario_actual]["saldo"] -= monto
            
                    #el texto para el historial
                    registro = f"Extracción: ${monto:.2f}"

                    #guardamos este texto en la lista de historial de este usuario
                    Login.base_usuarios[usuario_actual]["historial"].append(registro)

                    print(f"\n¡Operación exitosa! Has retirado ${monto:.2f}")
                    print(f"Tu nuevo saldo es: ${Login.base_usuarios[usuario_actual]['saldo']:.2f}")
                else:
                    print("Fondos insuficientes. No puedes extraer más de lo que tienes en tu cuenta.")
            else:
                print("Monto inválido. Por favor, ingrese un monto positivo.")

        elif opcion == "4": 
            print("Elegiste transferir")

            destinatario = input("Ingrese el nombre de usuario del destinatario: ")

            #verificamos si exite el usuario destinatario
            if destinatario in Login.base_usuarios: 
                #evitamos q el usuario se transfiera a si mismo
                if destinatario !=usuario_actual:
                    monto =  float(input("Ingrese el monto a transferir: $"))
                    saldo_actual = Login.base_usuarios[usuario_actual]["saldo"]

                    #el monto tiene q ser mayor a cero
                    if monto > 0:
                        #debe tener saldo suficiente para transferir
                        if monto <= saldo_actual:

                            #restamos el monto al saldo del usuario actual
                            Login.base_usuarios[usuario_actual]["saldo"] -= monto

                            #sumamos el monto al saldo del destinatario
                            Login.base_usuarios[destinatario]["saldo"] += monto

                            #registramos la transferencia en el historial de ambos usuarios
                            historial_salida = f"Transferencia a {destinatario}: ${monto:.2f}"
                            historial_entrada = f"Transferencia de {usuario_actual}: ${monto:.2f}"

                            #guardamos cada regristro
                            Login.base_usuarios[usuario_actual]["historial"].append(historial_salida)
                            Login.base_usuarios[destinatario]["historial"].append(historial_entrada)

                            print(f"\n¡Transferencia exitosa! Has transferido ${monto:.2f} a {destinatario}.")
                            print(f"Tu nuevo saldo es: ${Login.base_usuarios[usuario_actual]['saldo']:.2f}")
                        else:
                            print("Fondos insuficientes. No puedes transferir más de lo que tienes en tu cuenta.")
                    else:
                        print("Error: El monto a transferir debe ser mayor a cero.")
                else:
                    print("Error: No podés transferirte dinero a tu propia cuenta.")
            else:
                print("Error: El usuario destino no existe en nuestra base de datos.")
      

      


        elif opcion == "5":
            print("Elegiste ver historial")
            print("\n--- HISTORIAL DE OPERACIONES ---")
            historial = Login.base_usuarios[usuario_actual]["historial"]
        
            if len(historial) == 0:
                print("No hay operaciones registradas.")
            else:
                for movimiento in historial:
                    print("-", movimiento)
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
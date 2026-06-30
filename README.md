# simulador-cajero-automtico


*Integrantes del grupo:* 

Santillan Gonzalo Emmanuel

Hernandez Jose  Alejandro 


*Comision:* 1.2 


*Descripcion general del sistema*

<!-- las estructuras utilizadas;
las validaciones realizadas;
el manejo de errores;
y el funcionamiento general del sistema. -->

ejecutamos el programa seguido a ello se ingresa a un bucle  donde se muestra por pantalla 3 opciones del menu de inicio las cuales son: 

1. Iniciar sesion
2. Registrarse 
3. Salir 

el bucle finaliza cuando  se selecciona la opcion 3 que ejecuta la funcion "exit" que cierra el programa

si el usuario decide "Iniciar sesion" presinando 1 entonces nos movemos al archivo "Login.py"  donde alli se encuentra una estructura de datos llamada Dictionary(Diccionario) Los diccionarios en Python son *estructuras de datos mutables* que almacenan elementos en forma de *pares clave-valor*, permitiendo organizar información de manera eficiente y accesible.

Por ejemplo para acceder a un *"valor"* se hace de la siguiente manera 

nombre_diccionario[clave]

en nuestro caso seria

base_usuarios[usuario1]

esto nos devolveria el siguiente *"valor"*

{ *"contraseña"*: "123", *"saldo"*: 1000.0, *"historial"*: ["Depósito inicial: $1000"] }


una vez aclarado esto. el usuario al momento de ingresar a la opcion de "Iniciar sesion" ingresa en un bucle manejado por contador que cuenta la cantidad de intentos realizados. el usuario contara con  3 intentos  antes de que el sistema le informe por pantalla que se han excedido la cantidad maxima de intentos permitidos y sacarlo de la ventana de inicio de sesion. en caso de que el Inicio de sesion sea exitoso ingresa al bucle menu y alli se le pedira al usuario que ingrese un numero de acuerdo a la opcion que quiera realizar  el cual tiene el siguiente formato 

1. Consultar el dinero disponible 
2. Depositar dinero 
3. Extraer el dinero
4. Transferir dinero a otra cuenta
5. Ver el historial de movimientos de la cuenta 
6. Cerrar sesion de la cuenta 

con 1 consulta el saldo actual despues de realizada la consulta se le preguntara al usuarion si desea seguir realizando alguna accion dando la opcion de seguir presionando *"s"* o no presinando *"n"*

a 2 le permite depositar dinero al usuario  despues de realizado el deposito se le preguntara al usuarion si desea seguir realizando alguna accion dando la opcion de continuar depositando presionando *"s"* para si o *"n"* para no una vez realizada la accion se actulizan los datos guardados en el diccionario ¨*"base_usuarios"* con el nuevo valor de saldo.

la 3 es para extraer el dinero disponible de la cuenta en caso de contar con el mismo  una vez hecha la accion se actualiza los datos  guardados en el diccionario "*base_usuarios*"

la 4 le permite al usuario transferir el dinero de una cuenta A  a una cuenta B  ingresando el nombre de usuario de la cuenta B una vez hecha la accion se actualiza los datos  guardados en el diccionario "*base_usuarios*" restando el valor transferido al usuario *A* y sumando dicho valor a la cuenta *B*  

con la opcion 5 el usuario puede ver  el historial de movimientos realizados de la cuenta ya  sea para ver depositos, extracciones o transferencias.

con la opcion 6 sale del bucle menu principal  y vuelve  al menu de inicio  donde si quiere salir del cajero presionara 3 

    
*IA utilizada en el proyecto*

    *Gemini*
    *Codex*

*Para*

para explicarnos como utilizar ciertas funciones y para ayudarnos a destrabarnos en caso de no saber como resolver algun error en el codigo. 


*Como*

como ayuda  al momento de escribir el codigo facilitandonos el acceso a funciones que no conociamos como por ejemplo exit() el como definir funciones,el manejo de estructuras de control repetitivas y condicionales en python el manejo de estructuras como el diccionario,la sintaxis a seguir para escribir codigo en python
la modularizacion del codigo como por ejemplo cuando usamos "Registro.registro()" lo mismo para "Login" 


*Intrucciones de ejecucion*


primero verificamos que tenemos instalado python escribiendo en la consola "python --version" una vez verificado vamos  y descargamos/clonamos  el repositorio despues tenemos 2 opciones.

*1°* Si contamos con Visual Studio Code podemos simplemente ir a la parte superior derecha de la pantalla alli habra un boton con la leyenda "Run" los presionamos y el codigo se ejecutara.

*2°* Si no contamos con el "Visual" entonces hacemos lo siguiente si nuestro sistema operativo es Windows abrimos la consola y nos posicionamos en la carpeta  que contenga a *"Tp_cajero.py"* *"Login.py"* y *"Registro.py"* con "cd [nombre de nuestra carpeta] " una vez alli escribimos en la consola *"python Tp_cajero.py"*  y listo nuestro programa se ejecutara por consola.

*En caso de que nuestro sistema operativo sea macOS entonces hacemos lo siguiente*  

proseguimos de la misma manera primero verificamos que tenemos instalado python escribiendo en la terminal"python --version" una vez verificado vamos a la carpeta donde se encuentra "Tp_cajero.py"

*1°* Si contamos con Visual Studio Code podemos simplemente ir a la parte superior derecha de la pantalla alli habra un boton con la leyenda "Run" los presionamos y el codigo se ejecutara.


*2°* Si no contamos con el "Visual" entonces hacemos lo siguiente abrimos la terminal y nos posicionamos en la carpeta  que contenga a *"Tp_cajero.py"* una vez alli escribimos en la terminal *"python3 Tp_cajero.py"* o *"pythonw Tp_cajero"*  y listo nuestro programa se ejecutara por la terminal de MacOS.

Para ir a una carpeta específica en MacOS: Escribimos "*cd*" en la terminal seguido de un espacio y el nombre de la carpeta. Por ejemplo, "*cd Documentos*" o "*cd ~/Descargas*".


Eso seria todo  gracias por leer.

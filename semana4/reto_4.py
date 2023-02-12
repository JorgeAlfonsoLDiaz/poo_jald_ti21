"""
    Reto_4
    Nombre:" Jorge Alfonso Luqueño Díaz
    Fecha: 07/02/2023
    Descripción: Código en Python que lee la entrada de datos para 3 números enteros, y luego imprime el mayor, si es el         caso.
"""
numero1 = int(input("Número 1: "))  # Guarda una entrada de datos del usuario en la variable numero1.
numero2 = int(input("Número 2: "))  # Guarda una entrada de datos del usuario en la variable numero2.
numero3 = int(input("Número 3: "))  # Guarda una entrada de datos del usuario en la variable numero3.

if numero1 > numero2 and numero1 > numero3:  # Evalúa varias condiciones a la vez con una sentencia if para verificar si numero1 es mayor a los demás.
  print("El número mayor es ",numero1,".")  # Imprime el resultado en un mensaje en pantalla. Mayor: numero1
elif numero2 > numero1 and numero2 > numero3:  # Evalúa varias condiciones a la vez con una sentencia if para verificar si numero2 es mayor a los demás.
  print("El número mayor es ",numero2,".")  # Imprime el resultado en un mensaje en pantalla. Mayor: numero2
elif numero3 > numero1 and numero3 > numero2:  # Evalúa varias condiciones a la vez con una sentencia if para verificar si numero3 es mayor a los demás.
  print("El número mayor es ",numero3,".")  # Imprime el resultado en un mensaje en pantalla. Mayor: numero3
elif numero1 == numero2 and numero1 == numero3:  # Evalúa si todos los números son iguales.
  print("Todos los números son iguales.")  # Imprime el resultado en un mensaje en pantalla, en el que menciona que todos los números fueron iguales.
else:  # Uso de la sentencia else para ejecutar código en caso de ninguna condición anterior devuelva "True".
  print("Hay dos números iguales.")  # Imprime en pantalla el mensaje "Hay dos números iguales."

respuesta = input("Y... ¿Eso es todo? ")  # Se guarda en la variable 'respuesta' la respuesta del usuario a la pregunta "Y... ¿Eso es todo?"

if respuesta == "si" or respuesta == "Si" or respuesta == "Claro." or respuesta == "¿Que mas esperabas?":  # Evalúa la respuesta anterior del usuario.
  print("Bueno")  # En caso de que la respuesta haya cumplido con alguna de las anteriores condiciones, el programa            responderá con "Bueno".
else:  # Se utiliza la sentencia else para ejecutar código en caso de que las condiciones anteriores no se hayan cumplido.
  print("Ah.")  # Imprime un mensaje de confirmación en pantalla: "Ah.".
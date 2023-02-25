"""
    Reto_16"
    Nombre: Jorge Alfonso Luqueño Díaz"
    Fecha: 23/02/2023
    Descripción: Código que pide dos números al usuario, e imprime la suma de ambos, la mayoría del tiempo.
"""
import numpy as np  # Importa la biblioteca "numpy" y le da un alias "np".

user_choice = input("¿Cara o cruz? (1 / 2) > ")  # Guarda en la variable user_choice el número que introduzca el usuario, que puede ser 1 (cara) o 2 (cruz).

program_choice = np.random.choice([1, 2], size = 1, p=[0.5,0.5])  # Guarda en la variable "program_choice" la elección del programa de elegir cara o cruz (1 / 2)

print("Resultado: ",int(program_choice))  # Imprime en pantalla el valor de program_choice, con un mensaje.

if int(user_choice) == int(program_choice):  # Evalúa si user_choice es igual a program_choice, con una sentencia if.
  print("Ganaste!")  # Imprime en pantalla el mensaje "Ganaste!".

elif int(user_choice) == 1 or int(user_choice) == 2:  # Evalúa si user_choice es igual a 1 o a 2, con una sentencia elif.
  print("Suerte para la próxima!")  # Imprime un mensaje "Suerte para la próxima!".

else:  # Evalúa si ninguna de las condiciones anteriores fue verdadera, con una sentencia else. Este procedimiento se lleva a cabo para verificar si el usuario introdujo 1 o 2.
  print("Ya no juego :(")  # Imprime un mensaje "Ya no juego :(".

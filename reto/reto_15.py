"""
    Reto_15"
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 22/02/2023
    Descripción: Código que pide dos números al usuario, e imprime la suma de ambos, la mayoría del tiempo.
"""
import numpy as np  # Importa la biblioteca "numpy" y le da un alias "np".

numero1 = input("Introduzca el primer número: ")  # Guarda en la variable "numero1" el valor de la entrada de datos del usuario.
numero2 = input("Introduzca el segundo número: ")  # Guarda en la variable "numero2" el valor de la entrada de datos del usuario.

resultado = int(numero1) + int(numero2)  # Guarda en la variable "resultado" la suma de numero1 y numero2.
concatenacion = numero1 + numero2  # Guarda en la variable "concatenacion" la cadena resultante de concatenar numero1 y numero2.

obtencion = np.random.choice([resultado, concatenacion], size = 1, p=[0.9,0.1])  # Guarda en la variable "obtencion" el resultado de escoger el valor de resultado (90% de probabilidades) o el valor de concatenacion (10% de probabilidades)

if obtencion == concatenacion:  # Evalúa si el valor de "obtencion" coincide con el de "concatenacion", usando una sentencia if.
  print(int(obtencion),"                    Oops!")  # Imprime un mensaje con el valor de "obtencion" (que es igual al de "concatenacion") y hace saber al usuario de su "error".
else:  # Evalúa si la condición anterior no se cumplió, con el uso de una sentencia else.
  print(int(obtencion))  # Imprime el valor de la variable "obtencion" (que es igual al de "resultado").

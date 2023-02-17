"""
    Programa5
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 26/01/2023
    Descripción: Uso de input() para pedir entrada de datos al usuario y "casting" de la respuesta para poder realizar operaciones con números enteros.
"""
numero1 = input("Número1 (suma): ")  # Se pide al usuario que introduzca el primer número, a través de un input.
numero2 = input("Número2 (suma): ")  # Se crea la variable numero2 que guarda el segundo número de la suma.
suma = int(numero1) + int(numero2)  # Se realiza la suma correspondiente, realizando el "casting" necesario para que se sumen ambos números enteros.
print(suma)  # Se imprime el valor de la variable 'suma'.

numero1 = input("Número1 (resta): ")  # Se pide al usuario que introduzca el primer número, a través de un input.
numero2 = input("Número2 (resta): ")  # Se crea la variable numero2 que guarda el segundo número de la resta.
resta = int(numero1) - int(numero2)  # Se realiza la resta correspondiente, realizando el "casting" necesario para que se resten ambos números enteros.
print(resta)  # Se imprime el valor de la variable 'resta'.

numero1 = input("Número1 (multiplicación): ")  # Se pide al usuario que introduzca el primer número, a través de un input.
numero2 = input("Número2 (multiplicación): ")  # Se crea la variable numero2 que guarda el segundo número de la multiplicación.
producto = int(numero1) * int(numero2)  # Se realiza la multiplicación correspondiente, realizando el "casting" necesario para que se multipliquen ambos números enteros.
print(producto)  # Se imprime el valor de la variable 'producto'.

numero1 = input("Número1 (división): ")  # Se pide al usuario que introduzca el dividendo, a través de un input.
numero2 = input("Número2 (división): ")  # Se crea la variable numero2 que guarda el divisor.
cociente = int(numero1) / int(numero2)  # Se realiza la suma correspondiente, realizando el "casting" necesario para que se pueda obtener el cociente de la división.
print(cociente)  # Se imprime el valor de la variable 'cociente'.

numero1 = input("Número1 (potencia): ")  # Se pide al usuario que introduzca el primer número, a través de un input.
numero2 = input("Número2 (potencia): ")  # Se crea la variable numero2 que guarda el valor del exponente.
potencia = int(numero1) ** numero2  # Se realiza la potenciación correspondiente, realizando el "casting" necesario para que se pueda elevar al cuadrado.
print(potencia)  # Se imprime el valor de la variable 'potencia'.

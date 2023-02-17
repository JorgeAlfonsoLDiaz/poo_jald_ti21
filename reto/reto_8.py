"""
    Reto_8"
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 12/02/2023
    Descripción: Código que pide una entrada de dos cadenas, las concatena y las imprime juntas usando una función.
"""

def concat(a, b):  # Define la función concat, con dos parámetros.
  return a + b  # Devuelve el valor de la concatenación de las fos cadenas y termina la función.

a = input("Palabra 1: ")  # Guarda en la variable 'a' la entrada de datos del usuario.
b = input("Palabra 2: ")  # Guarda en la variable 'b' la entrada de datos del usuario.
print(concat(a, b))  # Imprime en pantalla el valor que devuelve la función concat con el valor de 'a' y 'b' como argumentos.

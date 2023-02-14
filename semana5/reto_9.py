"""
    Reto_9"
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 13/02/2023
    Descripción: Código que pide una entrada de dos cadenas, las concatena y las imprime juntas usando una función.
"""

def happyBDay(nombre):  # Define la función happyBDay, con un parámetro "nombre".
  return "Feliz cumpleaños, "+nombre+"!"  # Devuelve una cadena con el mensaje "Feliz cumpleaños, " concatenado con la variable "nombre".

nombre = input("¡Hola! Cuál es tu nombre? > ")  # Guarda en la variable 'nombre' la entrada de datos del usuario.
print(happyBDay(nombre))  # Felicita al usuario por el día de su cumpleaños :D!

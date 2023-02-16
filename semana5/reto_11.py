"""
    Reto_11"
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 15/02/2023
    Descripción: Código que pide la entrada de una cadena para verificarla como contraseña, y luego proporcionar "acceso" al usuario.
"""

password = "por_favor"  # Se define la variable "password" con una cadena "por_favor", la cual será la contraseña.

palabra = input("¡Hola! Si desea obtener acceso al sistema, introduzca la contraseña: > ")  # Guarda en la variable "palabra" la entrada de datos del usuario (una cadena).

if palabra == password:  # Evalúa si la variable "palabra" es igual a "password", con una sentencia if.
  print("Bienvenido, gracias por ser amable.")  # Imprime en pantalla un texto que notifica al usuario del acceso al sistema. También le agradece su amabilidad.
else:  # Evalúa si la condición anterior no se cumplió, con una sentencia else.
  print("Acceso denegado.")  # Imprime en pantalla el texto "Acceso denegado."

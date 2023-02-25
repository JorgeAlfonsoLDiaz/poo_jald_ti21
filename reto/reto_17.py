"""
    Reto_17"
    Nombre: Jorge Alfonso Luqueño Díaz"
    Fecha: 24/02/2023
    Descripción: Código que pide el día de la semana al usuario, e imprime el mensaje correspondiente para motivarlo.
"""

dia = input("¡Hola! ¿Qué día es? > ")  # Guarda en la variable "dia" el valor de la respuesta del usuario.

if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves":  # Evalúa si la variable "dia" coincide con alguno de los días hábiles de la semana, exceptuando viernes.

  print("¡A trabajar duro se ha dicho!")  # Imprime un mensaje en pantalla "¡A trabajar duro se ha dicho!"

elif dia == "viernes":  # Evalúa si la variable "dia" coincide con la cadena "viernes".

  print("Ya falta poco, ¡tú puedes!")  # Imprime un mensaje en pantalla "Ya falta poco, ¡tú puedes!"

elif dia == "sabado" or dia == "domingo":  # Evalúa si la variable "dia" coincide con las cadenas "sabado" o "domingo".
  print("Descansa, ¡te lo mereces!")  # Imprime un mensaje en pantalla "Descansa, ¡te lo mereces!"

"""
    Reto_12"
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 16/02/2023
    Descripción: Código que pide la entrada de un número de tipo flotante, y realiza la conversión de galones a litros.
"""

galones = float(input("Por favor, introduzca la cantidad de galones que desea convertir a litros: "))  # Se guarda en la variable "galones" el valor de la entrada de datos del usuario, de tipo flotante.

litros = galones * 3.78541  # Se establece el valor de litros como la cantidad de galones multiplicada por 3.78541 (se realiza la conversión de galones a litros).

print("{} galones es igual a {} litros.".format(galones, litros))  # Imprime en pantalla el resultado de la conversión, dentro de un mensaje.

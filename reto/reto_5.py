"""
    Reto_5
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 08/02/2023
    Descripción: Código en Python que calcula la hipotenusa de un triángulo rectángulo a partir de la medida de sus          catetos.
"""
print("Bienvenido, aquí podrá calcular el valor de la hipotenusa de un triángulo rectángulo a partir de la medida de sus catetos. \n")  # Imprime en pantalla un mensaje de bienvenida al usuario
a = int(input("Introduzca el valor del primer cateto del triángulo: "))  # Guarda en la variable "a" la entrada de datos del usuario para la medida del primer cateto.
b = int(input("Ahora, introduzca el valor del segundo cateto del triángulo: \n"))  # Guarda en la variable "b" la entrada de datos del usuario para la medida del segundo cateto.

c = (a**2 + b**2)**0.5  # Guarda en la variable "c" el resultado de aplicar el Teorema de Pitágoras con las medidas obtenidas anteriormente

print("La medida de la hipotenusa es de {}.".format(c))  # Imprime el resultado del cálculo, haciendo uso de la variable "c".

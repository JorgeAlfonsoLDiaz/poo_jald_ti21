"""
    Programa7
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 31/01/2023
    Descripción: Código que hace uso de input() y otras funciones para calcular el perímetro y el área de            un          círculo y un cuadrado.
"""
PI = 3.1416  # Se asigna el valor de 3.1416 a la constante 'PI'
radio = input("Bienvenido. Por favor, introduzca el valor del radio del círculo: > ")  # Se pide al usuario que introduzca un valor al radio del círculo,

area = PI * float(radio)**2  # Se calcula el área del círculo con la fórmula correspondiente.
perimetro = PI * (float(radio) * 2)  # Se calcula el perímetro (circunferencia) del círculo con la fórmula correspondiente.

print("El área de un círculo de {} de radio es {} ".format(radio, area))  # Se imprime en pantalla un mensaje: 'El área de un círculo de (radio) de radio es (area)'
print("El perímetro de un círculo de {} de radio es {} ".format(radio, perimetro))  # Se imprime en pantalla un mensaje: 'El perímetro de un círculo de (radio) de radio es (perimetro)'

lado = input("Ahora, por favor ingrese la medida de los lados del cuadrado: > ")  # Se pide al usuario
area = float(lado) ** 2  # Se hace la conversión de la variante 'lado' a tipo flotante para calcular el área con la fórmula correspondiente. 
perimetro = float(lado) * 4  # Se hace nuevamente la conversión de la variable 'lado' a tipo flotante para poder calcular el perímetro con la formula correspondiente

print("El área de un cuadrado de {} por lado es {} ".format(lado, area))  # Se imprime en pantalla el mensaje "El área de un cuadrado de (lado) por lado es (area) haciendo uso de los valores correspondientes"
print("El perímetro de un cuadrado de {} por lado es {} ".format(lado, perimetro))  # Se imprime en pantalla el mensaje "El perímetro de un cuadrado de (lado) por lado es (perimetro) "

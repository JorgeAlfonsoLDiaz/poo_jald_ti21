"""
    Programa6
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 30/01/2023
    Descripción: Código que hace uso de input() y otras funciones para calcular el perímetro y      el área de       un triángulo (equilátero o isósceles).
"""

opcion = input("Bienvenido/a. Introduzca 'a' para obtener el área de un triángulo. Introduzca 'p' para obtener el perímetro de un triángulo. > ")  # Pide al usuario una entrada de datos entre 'a' y 'p'

if opcion == 'a':  # Evalúa si la respuesta del usuario fue 'a', para poder continuar con el proceso del cálculo de área.
  base = input("Introduzca la base: ")  # Pide al usuario introducir el valor de la variable 'base' y lo guarda en esta.
  altura = input("Introduzca la altura: ")  # Pide al usuario introducir el valor de la variable 'altura' y lo guarda en esta.
  area = (int(base) * int(altura))/2  # Se guarda en la variable 'area' el resultado de la fórmula: (base * altura) / 2  para obtener el área de un triángulo.
  print("Área: {}".format(area))  # Se imprime en pantalla el siguiente mensaje: "Área: " seguido por el valor de la variable 'area'.
elif opcion == 'p':  # Evalúa si la respuesta del usuario fue 'p', para poder continuar con el proceso del cálculo de perímetro.
  lado1 = input("Introduzca el primer lado: ")  # Pide al usuario introducir el valor de la variable 'lado1' y lo guarda en esta.
  lado2 = input("Introduzca el segundo lado: ")  # Pide al usuario introducir el valor de la variable 'lado2' y lo guarda en esta.
  lado3 = input("Introduzca el tercer lado: ")  # Pide al usuario introducir el valor de la variable 'lado3' y lo guarda en esta.
  perimetro = int(lado1) + int(lado2) + int(lado3)  # Realiza el cálculo del perímetro sumando el valor de los tres lados, y guarda el resultado en 'perimetro'

  print("Perímetro: {}".format(perimetro))  # Se imprime en pantalla el siguiente mensaje: "Perímetro: " seguido por el valor de la variable 'perimetro'.
else:
  print("Error 404 Not found: Por favor, elija una opción válida. > ")  # Se imprime en pantalla el siguiente mensaje de error: "Error 404 Not found: Por favor, elija una opción válida. > ".

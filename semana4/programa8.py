"""
    Programa8
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 07/02/2023
    Descripción: Código que compila un total de 11 maneras diferentes de resolver el problema "Crear una          aplicación que lea 2 números enteros, los compare y muestre el número mayor, en caso de que sean             iguales      mostrar None."
"""
numero1 = int(input("Número 1 "))
numero2 = int(input("Número 2 "))

if numero1 > numero2:
  print(numero1)
if numero2 > numero1:
  print(numero2)
if numero1 == numero2:
  print(None)


numero1 = int(input("Número 1 "))
numero2 = int(input("Número 2 "))

if numero2 > numero1:
  print(numero2)
if numero1 > numero2:
  print(numero1)
else:
  print(None)


numero1 = int(input("Número 1 "))
numero2 = int(input("Número 2 "))

if numero1 > numero2:
  print(numero1)
elif numero2 > numero1:
  print(numero2)
else:
  print(None)


numero1 = int(input("Número 1 "))
numero2 = int(input("Número 2 "))

if numero1 == numero2:
  print(None)
elif numero1 > numero2:
  print(numero1)
elif numero2 > numero1:
  print(numero2)


numero1 = int(input("Número 1 "))
numero2 = int(input("Número 2 "))

if numero1 < numero2:
  print(numero2)
if numero2 < numero1:
  print(numero1)
if numero1 == numero2:
  print(None)




"""
    Programa8
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 07/02/2023
    Descripción: Código que compila un total de 11 maneras diferentes de resolver el problema "Crear una aplicación que lea 2 números enteros, los compare y muestre el número mayor, en caso     de que sean iguales mostrar None."
"""
numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
if numero2 > numero1:  # Evalúa si numero2 es mayor que numero1, con una sentencia if.
  print(numero2)  # Imprime en pantalla el valor de numero2.
if numero1 == numero2:  # Evalúa si numero1 es igual que numero2, con una sentencia if.
  print(None)  # Imprime en pantalla el valor "None".
  

numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero2 > numero1:  # Evalúa si numero2 es mayor que numero1, con una sentencia if.
  print(numero2)  # Imprime en pantalla el valor de numero2.
if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
else:  # Evalúa si ninguna de las condiciones anteriores se cumplió, con una sentencia else.
  print(None)  # Imprime en pantalla el valor "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
elif numero2 > numero1:  # Evalúa si numero2 es mayor que numero1, con una sentencia elif.
  print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 == numero2:  # Evalúa si numero1 y numero2 son iguales, con una sentencia if.
  print(None)  # Imprime en pantalla el valor de "None".
elif numero1 > numero2:  # Evalúa si numero1 es mayor que numero2, con una sentencia elif.
  print(numero1)  # Imprime en pantalla el valor de numero1.
elif numero2 > numero1:  # Evalúa si numero2 es mayor que numero1, con 
  print(numero2)


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 < numero2:  # Evalúa si numero1 es menor que numero2, con una sentencia if.
  print(numero2)  # Imprime en pantalla el valor de numero2.
if numero2 < numero1:  # Evalúa si numero2 es menor que numero1, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
if numero1 == numero2:  # Evalúa si numero1 y numero2 son iguales, con una sentencia if.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero2 > numero1:  # Evalúa si numero2 es mayor que numero1, con una
  print(numero2)  # Imprime en pantalla el valor de numero2.
if numero2 < numero1:  # Evalúa si numero2 es menor que numero1, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if(numero2<numero1>numero2):  # Evalúa si numero2 es menor que numero1 y si numero1 es mayor que numero2, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
elif(numero1<numero2>numero1):  # Evalúa si numero1 es menor que numero2 y si numero2 es mayor que numero1, con una sentencia elif.
  print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 <= numero2:  # Evalúa si numero1 es menor o igual que numero2, con una sentencia if.
  if numero1 == numero2:  # Evalúa si numero1 y numero2 son iguales, con una sentencia if.
    print(None)  # Imprime en pantalla el valor de "None".
  else:  # Evalúa si no se cumplió la condición anterior, con una sentencia else.
    print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(numero1)  # Imprime en pantalla el valor de numero1.


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if (numero1 - numero2) > 0:  # Evalúa si la resta de numero2 a numero1 es mayor que 0, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
elif (numero2 - numero1) > 0:  # Evalúa si la resta de numero1 a numero2 es mayor que 0, con una sentencia elif.
  print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if numero1 > numero2 and numero2 < numero1:  # Evalúa si numero1 es mayor que numero2 y numero2 es menor que numero1, con una sentencia if.
  print(numero1)  # Imprime en pantalla el valor de numero1.
elif numero1 < numero2 and numero2 > numero1:  # Evalúa si numero1 es menor que numero2 y numero2 es mayor que numero1, con una sentencia elif.
  print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".


numero1 = int(input("Número 1 "))  # Guarda en "numero1" el valor de la entrada de datos del usuario.
numero2 = int(input("Número 2 "))  # Guarda en "numero2" el valor de la entrada de datos del usuario.

if (numero1 - numero2) not in [0]:  # Evalúa si la resta de numero2 a numero1 no pertenece al vector [0], para saber si no son iguales, con una sentencia if.
  if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2, con una sentencia if.
    print(numero1)  # Imprime en pantalla el valor de numero1.
  else:  # Evalúa si no se cumplió la condición anterior, con una sentencia else.
    print(numero2)  # Imprime en pantalla el valor de numero2.
else:  # Evalúa si no se cumplió ninguna de las condiciones anteriores, con una sentencia else.
  print(None)  # Imprime en pantalla el valor de "None".

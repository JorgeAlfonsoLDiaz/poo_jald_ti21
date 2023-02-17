"""
    Programa4
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 26/01/2023
    Descripción: Print y str.format llamándolas por sus posiciones y por sus nombres.
"""
numero1 = 10  # Se guarda en la variable numero1 un dato de tipo int.
numero2 = 5  # Se guarda en la variable numero2 un dato de tipo int.
print("{} + {} = {}".format(numero1, numero2, numero1+numero2))  # Imprime los valores de numero1, numero2 y la suma de ambos por su posición.
print("{} + {} = ".format(numero1, numero2, numero1+numero2))  # Imprime los valores de los índices 0 y 1, pero el 2 no se imprimió, sin necesidad de que surja un error.
print("{n1} + {n2} = {suma}".format(n1=numero1, n2=numero2, suma=numero1+numero2))  # Imprime variables llamándolas por su nombre.
print("{numero1} + {numero2} = {suma}".format(numero1=numero1, numero2=numero2, suma=numero1+numero2))  # Imprime el mismo resultado sin problemas, utilizando sus mismos nombres para crear las variables.
print("{numero1} + {numero2} = {}".format(numero1, numero2, numero1+numero2))  # Una línea que genera un error, debido a que no se están creando variables para colocarlas entre las llaves.

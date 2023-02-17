"""
    Programa10
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 09/02/2023
    Descripción: Código que utiliza un método y typing para resolver un problema y verificarlo con un "Unit test"
"""

def mayor(numero1:int, numero2:int)->int|None:  # define la función "mayor", y se hace uso del casting para los tipos de las variables con las que se trabajarán.
  result = None  # Se guarda en la variable result el valor "None".
  if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2 con una sentencia if.
    result = numero1  # Se guarda en la variable result el valor de numero1, indicando que fue el número mayor.
  elif numero2 > numero1:  # Evalúa si numero2 es mayor que numero1 con una sentencia elif.
    result = numero2  # Se guarda en la variable result el valor de numero2, indicando que fue el número mayor.
  return result  # La función devuelve el valor de la variable return y concluye.

print(mayor(2,1))  # 2
print(mayor(1,2))  # 2
print(mayor(2,2))  # None
print(mayor(2,-1))  # 2
print(mayor(-1,2))  # 2
print(mayor(-1,-1))  # None
print(mayor(-2,-1))  # -1
print(mayor(-1,-2))  # -2

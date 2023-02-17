"""
    Programa9
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 09/02/2023
    Descripción: Código que utiliza un método para resolver un problema y verificarlo con un      "Unit test".
"""

def mayor(numero1, numero2):  # Define el método 'mayor' con las variables numero1 y numero2 como parámetros.
  result = None  # Asigna el valor 'None' a la variable result, con el propósito de darle un valor posteriormente.
  if numero1 > numero2:  # Evalúa si numero1 es mayor que numero2 con el uso de una sentencia if.
    result = numero1  # Se guarda en la variable result el valor de numero1, indicando que fue el número mayor.
  elif numero2 > numero1:  # Evalúa si numero2 es mayor que numero1 con el uso de una sentencia if.
    result = numero2  # Se guarda en la variable result el valor de numero2, indicando que fue el número mayor.
  return result  # Devuelve el valor de la variable result y termina la función.

print(mayor(2,1))  # 2
print(mayor(1,2))  # 2
print(mayor(2,2))  # None
print(mayor(2,-1))  # 2
print(mayor(-1,2))  # 2
print(mayor(-1,-1))  # None
print(mayor(-2,-1))  # -1
print(mayor(-1,-2))  # -2

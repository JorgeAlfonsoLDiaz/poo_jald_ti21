"""
    Reto_6
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 09/02/2023
    Descripción: Código en Python que utiliza una función para calcular el resultado de potenciar un número, en este         caso el número 2, coincidiendo con los valores de las posiciones de los bits en código binario, de derecha a             izquierda.
"""

def potencia(base:float, exponente:int)->float|int:  # Define la función "potencia", teniendo como argumentos las variables base (tipo flotante) y exponente (tipo entero), haciendo uso de typing.
  resultado = base ** exponente  # Guarda el resultado de la variable "base" potenciada al valor de la variable "exponente", en la variable "resultado".
  return resultado  # Devuelve el valor de la variable "resultado" en la función.

print(potencia(2,0))  # 1
print(potencia(2,1))  # 2
print(potencia(2,2))  # 4
print(potencia(2,3))  # 8
print(potencia(2,4))  # 16
print(potencia(2,5))  # 32
print(potencia(2,6))  # 64
print(potencia(2,7))  # 128

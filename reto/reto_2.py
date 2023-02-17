"""
    Reto_2
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 05/02/2023
    Descripción: Código en Python que verifica la respuesta del usuario para calcular el resultado de una rifa.
"""
numero = input("Elija un número del 1 al 10: > ")  # 
print("Gracias por participar en esta rifa!")
if int(numero) in [4,2,9]:
  print("¡Felicidades! ¡Usted es el ganador oficial del fabuloso premio de 5 pesos!")
elif int(numero) <= 10:
  print("¡Vaya! ¡Parece que hoy no fue su día de suerte, gracias por participar!")
else:
  print("Por favor, inténtelo otra vez con un número válido.")
  
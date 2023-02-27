"""
    Reto_19"
    Nombre: Jorge Alfonso Luqueño Díaz"
    Fecha: 26/02/2023
    Descripción: Código que saluda al usuario, siempre que éste lo hace también. También se despide del usuario cuando este hace lo mismo.
"""
respuesta = input(". . .")  # Imprime un mensaje en pantalla y espera una respuesta del usuario, para guardarla en la variable respuesta.

while respuesta == "hola" or respuesta == "Hola":  # Se crea un bucle while que se repite mientras la variable respuesta coincida con alguna de las dos formas de saludo que contempla el programa.
  print("Hola")  # Imprime en pantalla un saludo al usuario.
  respuesta = input()  # Asigna a la variable respuesta un nuevo valor introducido por el usuario.

  if respuesta == "adios" or respuesta == "Adios" or respuesta == "adiós" or respuesta == "Adiós":  # Evalúa si la variable respuesta coincide con alguna de las 4 formas que tiene el usuario para despedirse.
    print("Adiós")  # Imprime en pantalla una despedida para el usuario.

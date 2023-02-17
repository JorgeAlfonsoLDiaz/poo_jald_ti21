"""
    Reto_3
    Nombre: Jorge Alfonso Luqueño Díaz
    Fecha: 06/02/2023
    Descripción: Código en Python que simula el funcionamiento de una tienda de objetos en Final Fantasy I.
"""
activo = True
dinero = 500

while activo == True:
  if dinero < 500:
    print("\n|1 -> Poción - 60 G \n|2 -> Antídoto - 75 G \n|3 -> Saco de dormir - 75 G \n| \n| Dinero: {} G \n \n| > Salir".format(dinero))
    compra = input("> ")
  else:
    print("\nBienvenidos!")
    print("¿Qué necesitáis?")
    print("\n|1 -> Poción - 60 G \n|2 -> Antídoto - 75 G \n|3 -> Saco de dormir - 75 G \n| \n| Dinero: {} G \n \n| > Salir".format(dinero))
    compra = input("> ")
  
  if compra == "1":
    if dinero < 60:
      print("Lo siento, pero no tienes el dinero suficiente.")
    else:
      confirmar = input("¿Estáis seguros de querer comprar Poción por 60 G? (si / no) \n>")
      if confirmar == "si":
        dinero -= 60
        print("\n¡Gracias por comprar!")
      
  elif compra == "2":
    if dinero < 75:
      print("Lo siento, pero no tienes el dinero suficiente.")
    else:
      confirmar = input("¿Estáis seguros de querer comprar Antídoto por 75 G? (si / no) \n>")
      if confirmar == "si":
        dinero -= 75
        print("\n¡Gracias por comprar!")
      
  elif compra == "3":
    if dinero < 75:
      print("Lo siento, pero no tienes el dinero suficiente.")
    else:
      confirmar = input("¿Estáis seguros de querer comprar Saco de dormir por 75 G? (si / no) \n>")
      if confirmar == "si":
        dinero -= 75
        print("\n¡Gracias por comprar!")

  elif compra == "salir" or "exit" or "cancelar":
    break
    
  else:
    print("¿Qué? Lo siento, no conozco ese producto.")

  if confirmar == "si":
    print("¿Algo más?\n")
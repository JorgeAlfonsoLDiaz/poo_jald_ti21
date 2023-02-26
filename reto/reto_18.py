"""
    Reto_17"
    Nombre: Jorge Alfonso Luqueño Díaz"
    Fecha: 24/02/2023
    Descripción: Código que pide el día de la semana al usuario, e imprime el mensaje correspondiente para motivarlo.
"""
import datetime
import zoneinfo

zona_horaria = zoneinfo.ZoneInfo("America/Chihuahua")

hora = datetime.datetime.now(zona_horaria)

print("Son las ",hora,"\n \n \n")

if hora.hour > 5 and hora.hour < 13:

  print("¡Buenos días! ¡Te espera un día muy productivo y lleno de éxito ^-^ !")

elif hora.hour > 13 and hora.hour < 19:

  print("¡Buenas tardes! ¿Ya realizaste tu código diario?")

else:

  print("¡Buenas noches! ¿Ya vas a descansar? Si es así, descansa, ¡Mañana será un gran día y necesitas despertar lleno de energía! Si no, seguro es por tus tareas, ¡Ánimo, que tu puedes! ")

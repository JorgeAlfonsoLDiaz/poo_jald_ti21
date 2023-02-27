"""
    Reto_18"
    Nombre: Jorge Alfonso Luqueño Díaz"
    Fecha: 25/02/2023
    Descripción: Código que pide el día de la semana al usuario, e imprime el mensaje correspondiente para motivarlo.
"""
import datetime  # Se importa la librería datetime.
import zoneinfo  # Se importa la librería zoneinfo.

zona_horaria = zoneinfo.ZoneInfo("America/Chihuahua")  # Se guarda en la variable zona_horaria la zona horaria en la que se basará la obtención de la hora.

hora = datetime.datetime.now(zona_horaria)  # Se guarda en la variable hora la hora actual de acuerdo con la variable zona_horaria.

print("Son las ",hora,"\n \n \n")  # Imprime en pantalla un mensaje, que le indica al usuario cuál es la hora actual.

if hora.hour > 5 and hora.hour < 13:  # Evalúa si la hora actual es mayor que 5 y menor que 13, con una sentencia if.

  print("¡Buenos días! ¡Te espera un día muy productivo y lleno de éxito ^-^ !")  # Imprime un mensaje en pantalla, en caso de que sea de mañana.

elif hora.hour > 13 and hora.hour < 19:  # Evalúa si la hora actual es mayor que 13 y menor que 19, con una sentencia if.

  print("¡Buenas tardes! ¿Ya realizaste tu código diario?")  # Imprime un mensaje en pantalla, en caso de que sea en la tarde.

else:  # Evalúa si no se cumplió ninguna de las anteriores condiciones, con una sentencia else.

  print("¡Buenas noches! ¿Ya vas a descansar? Si es así, descansa, ¡Mañana será un gran día y necesitas despertar lleno de energía! Si no, seguro es por tus tareas, ¡Ánimo, que tu puedes! ")  # Imprime un mensaje en pantalla, en caso de que ya sea de noche,

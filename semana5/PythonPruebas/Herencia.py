"""
   Descripción: Código que crea una clase Persona y una clase hija Alumno que hereda las características de la superclase Persona.
"""


class Persona:  # Clase Persona.
  
  __nombre = None  # Asigna el valor "None" al atributo privado __nombre
  __edad = None  # Asigna el valor "None" al atributo privado __edad

  def __init__(self):  # Constructor de la clase Persona.
    print("Persona")  # Imprime en pantalla el mensaje "Persona"
  
  
  def setNombre(self, nombre):  # Método para modificar el valor de la variable privada __nombre .
    self.__nombre = nombre  #Asigna el valor de nombre a la variable privada __nombre .


class Alumno (Persona):  # Clase hija Alumno (de Persona)

  __nombre = None  # Asigna el valor "None" al atributo privado __nombre
  __matricula = None  # Asigna el valor "None" al atributo privado __matricula

  def __init__(self):  # Constructor de la clase hija Alumno
    super().__init__()  # Llama al constructor de la clase Persona
    print("Alumno")  # Muestra el mensaje "Alumno"


objeto_persona = Persona()  # Crea un objeto de la clase Persona
objeto_alumno = Alumno()  # Crea un objeto de la clase Alumno  # Crea un objeto de la clase Alumno

print(dir(objeto_persona))  # Imprime en pantalla todas las propiedades y atributos del objeto objeto_persona  # Impr
print(dir(objeto_alumno))  # Imprime en pantalla todas las propiedades y atributos del objeto objeto_alumno

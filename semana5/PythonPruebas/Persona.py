class Persona:  # Clase Persona.

  __nombre = None  # Le asigna el valor "None" al atributo privado __nombre
  __email = None  # Le asigna el valor "None" al atributo privado __email

  def __init__(self):  # Constructor de la clase Persona
    print("Persona")  # Muestra el mensaje "Persona"

  def setNombre(self, nombre):  # Método para modificar el valor de la variable privada __nombre .
    self.__nombre = nombre  # Asigna el valor de nombre a la variable privada __nombre .
  
  def getNombre(self):
    return self.__nombre

  def setEmail(self, nombre):
    self.__email = email
  
  def getEmail(self):
    return self.__email


Dejah = Persona()  # Crea el objeto Dejah de la clase Persona
Dejah.setNombre("Dejah")
print(Dejah.getNombre())

Dejah.setEmail()


  
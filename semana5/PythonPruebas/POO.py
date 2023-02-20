"""
   Descripción: Código que crea varias clases hijas que heredan los atributos de una clase padre "Persona".
"""
class Persona:  # Crea la clase.
  
  __nombre = None  # Crea la variable privada "nombre" y le asigna un valor 'None'.
  __edad = None  # Crea la variable privada "edad" y le asigna un valor 'None'.

  def __init__(self):  # Define la función __init__ tomando como argumento a "self"
    print("Persona")  
  
  
  def setNombre(self, nombre):
    self.__nombre = nombre

class Alumno (Persona):

  __nombre = None
  __matricula = None

  def __init__(self):
    super().__init__()
    print("Alumno")

  def setNombre(self, nombre:str):
    self.__nombre = nombre
  
  def getNombre(self):
    return self.__nombre

class Profesor(Persona):

  __no_nomina = None

  def __init__(self):
    super().__init__()
    print("Profesor")

  def setNoNomina(self, no_nomina:str):
    self.__noNomina = noNomina

  def getNoNomina(self):
    return self___noNomina

  def setNombre(self, nombre:str):
    self.__nombre = nombre
  
  def getNombre(self):
    return self.__nombre


class Coordinador(Persona):

  __no_nomina = None
  __carrera_cargo = None

  def __init__(self):
    super().__init__()
    print("Coordinador")

  def setNoNomina(self, no_nomina:str):
    self.__noNomina = noNomina

  def getNoNomina(self):
    return self___noNomina

  def setCarreraCargo(self, carrera_cargo:str):
    self.__carreraCargo = carreraCargo

  def getCarreraCargo(self):
    return self___carreraCargo

  def setNombre(self, nombre:str):
    self.__nombre = nombre
  
  def getNombre(self):
    return self.__nombre

objeto_persona = Persona()
objeto_alumno = Alumno()
objeto_profesor = Profesor()
objeto_coordinador = Coordinador()

objeto_alumno._Alumno__nombre = "Alumno nombre"
objeto_alumno._Persona__nombre = "Persona nombre"

objeto_profesor._Profesor__nombre = "Profesor nombre"
objeto_profesor._Persona__nombre = "Persona nombre"

objeto_coordinador._Coordinador__nombre = "Coordinador nombre"
objeto_coordinador._Persona__nombre = "Persona nombre"

print(objeto_alumno._Alumno__nombre)
print(objeto_alumno._Persona__nombre)
print(objeto_alumno.getNombre())


print(objeto_profesor._Profesor__nombre)
print(objeto_profesor._Persona__nombre)
print(objeto_profesor.getNombre())


print(objeto_coordinador._Coordinador__nombre)
print(objeto_coordinador._Persona__nombre)
print(objeto_coordinador.getNombre())


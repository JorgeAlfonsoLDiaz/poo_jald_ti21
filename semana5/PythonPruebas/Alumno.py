class Alumno:  # Clase Alumno
    __nombre = None  # Asigna el valor "None" al atributo privado __nombre
    __matricula = None  # Asigna el valor "None" al atributo privado __matricula
    __carrera = None  # Asigna el valor "None" al atributo privado __carrera

    def __init__(self):  # Constructor de la clase Alumno.
      print("Alumno")  # Imprime en pantalla el mensaje "Alumno"

    def setNombre(self,nombre):  # Método para modificar el valor de la variable privada __nombre .
      self.__nombre = nombre  # Asigna el valor de nombre a la variable privada __nombre .

    def getNombre(self):  # Método para regresar el valor de la variable privada __nombre .
      return self.__nombre  # Regresa el valor de la variable privada __nombre .

    def setMatricula(self,matricula):  # Método para modificar el valor de la variable privada __matricula .
      self.__matricula = matricula  # Asigna el valor de nombre a la variable privada __matricula .

    def getMatricula(self):  # Método para regresar el valor de la variable privada __matricula .
      return self.__matricula  # Regresa el valor de la variable privada __matricula .

    def setCarrera(self,carrera): # Método para modificar el valor de la variable privada __carrera .
      self.__carrera = carrera  # Asigna el valor de nombre a la variable privada __carrera .

    def getCarrera(self):  # Método para regresar el valor de la variable privada __carrera .
      return self.__carrera   # Regresa el valor de la variable privada __carrera .
        
Alfonso = Alumno()  # Crea un objeto de la clase Alumno e invoca al constructor.
Alfonso.setNombre("Jorge Alfonso Luqueno Díaz")  # Llama al método setNombre de la clase Alumno y le pasa el parámetro "Jorge Alfonso Luqueno Díaz".
print(Alfonso.getNombre())  # Llama al método getNombre e imprime el valor del nombre.

Alfonso.setMatricula("1722110431")  # Llama al método setMatricula de la clase Alumno y le pasa el parámetro "1722110431".
print(Alfonso.getMatricula())  # Llama al método getMatricula e imprime el valor de la matrícula.

Alfonso.setCarrera("Tecnologías de la Información área Desarrollo de Software Multiplataforma")  # Llama al método setCarrera de la clase Alumno y le pasa el parámetro "Tecnologías de la Información área Desarrollo de Software Multiplataforma".
print(Alfonso.getCarrera())  # Llama al método getCarrera e imprime el nombre de la carrera.

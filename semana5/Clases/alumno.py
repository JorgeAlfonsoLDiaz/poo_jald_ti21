from persona import Persona  # Importa del archivo persona.py la clase Persona

class Alumno(Persona):  # Crea la clase Alumno y hereda de la clase Persona

    def __init__(self) -> None:  # Constructor de la clase Alumno
        super().__init__()   # Llama al constructor de la clase Persona
        print("Constructor Alumno")  # Muestra el mensaje "Constructor Alumno"

objeto_alumno = Alumno()  # Crea un objeto de la clase Alumno e invoca al constructor.
objeto_alumno.setNombre("Dejah")  # Llama al método setNombre de la clase Persona y le pasa el parámetro "Dejah".
print(objeto_alumno.getNombre())  # Llama al método getNombre e imprime el valor del nombre.

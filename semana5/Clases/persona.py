class Persona:  # Clase Persona.

    __nombre = None  # Asigna el valor "None" al atributo privado __nombre

    def __init__(self) -> None:  # Constructor de la clase Persona.
        print("Constructor Persona")  #  Imprime el texto "Contructor Persona".

    def setNombre(self, nombre:str) -> None:  # Método para modificar el valor de la variable privada __nombre .
        self.__nombre = nombre  # Asigna el valor de nombre a la variable privada __nombre .

    def getNombre(self) -> str:  # Método para regresar el valor de la variable privada __nombre .
        return self.__nombre  # Regresa el valor de la variable privada __nombre .

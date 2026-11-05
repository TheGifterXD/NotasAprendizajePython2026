# ================================
# CONCEPTO: CLASES Y OBJETOS
# ================================
# Una clase es un plano de instrucciones que permite
# definir la estructura y el comportamiento de objetos únicos.

# 1. CREAR UNA CLASE
# - Se usa la palabra clave 'class' seguida del nombre.
# - '__init__' es el método constructor que inicializa los atributos.
# - 'self' hace referencia a la instancia actual del objeto.
# - Los métodos son funciones dentro de la clase que usan esos datos.

class ClassName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sample_method(self):
        print(self.name.upper())

# 2. CREAR OBJETOS Y LLAMAR MÉTODOS
# - Sintaxis de instanciación: object1 = ClassName(attribute_1, attribute_2)
# - Llamada a métodos: object1.method_name()

# Ejemplo práctico:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog("Jack", 3)
dog_2 = Dog("Thatcher", 5)

dog_1.bark()  # JACK says woof woof! I'm 3 years old!
dog_2.bark()  # THATCHER says woof woof! I'm 5 years old!

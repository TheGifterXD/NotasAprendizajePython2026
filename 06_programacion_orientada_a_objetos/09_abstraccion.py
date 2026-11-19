# ========================
# CONCEPTO: ABSTRACCIÓN
# ========================
# Es el proceso de ocultar los detalles complejos de implementación
# y mostrar únicamente las características esenciales de un objeto.
# En otras palabras, se enfoca en qué hace el programa en vez de cómo lo hace.

# 1. MÓDULO ABC
# Este módulo proporciona la clase base ABC y el decorador @abstractmethod.
# Una clase abstracta que contiene métodos abstractos no puede instanciar objetos
# directamente; debe ser heredada por subclases que sobrescriban TODOS los
# métodos abstractos definidos en la clase padre para poder instanciarse.

from abc import ABC, abstractmethod

# Definición de una clase base abstracta
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Subclase concreta que implementa el método abstracto
class ConcreteClassOne(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassOne')

# Otra subclase concreta
class ConcreteClassTwo(AbstractClass):
    def abstract_method(self):
        print('Implementation in ConcreteClassTwo')


# Ejemplo práctico:
class Animal(ABC):
    @abstractmethod
    def make_sound(self):  # Método que las subclases están obligadas a sobrescribir
        pass

class Dog(Animal):
    def make_sound(self):
        print('Woof!')

class Cat(Animal):
    def make_sound(self):
        print('Meow!')

class Monkey(Animal):
    def make_sound(self):
        print('Ooh ooh aah aah!')

# Instanciación de las clases concretas
animals = [Dog(), Cat(), Monkey()]

# Llamada polimórfica al método implementado
for animal in animals:
    animal.make_sound()

# Output:
# Woof!
# Meow!
# Ooh ooh aah aah!


# Ejemplo de error al intentar instanciar la clase abstracta directamente:
# dog = Animal()
# TypeError: Can't instantiate abstract class Animal
# without an implementation for abstract method 'make_sound'

# Ejemplo de error al instanciar una subclase que no sobrescribe los métodos abstractos:
# class Bird(Animal):
#     pass
#
# bird = Bird()
# TypeError: Can't instantiate abstract class Bird
# without an implementation for abstract method 'make_sound'


# Ejemplo de clase abstracta con atributos de instancia (__init__):
class TalkingToy(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class RobotToy(TalkingToy):
    def speak(self):
        print(f'{self.name} says beep boop! I am a robot!')

class TeddyBearToy(TalkingToy):
    def speak(self):
        print(f"{self.name} says hug me! I'm cuddly!")

class DinosaurToy(TalkingToy):
    def speak(self):
        print(f'{self.name} says ROOOOAR!')

rusty = RobotToy('Rusty')
fluffy = TeddyBearToy('Fluffy')
rex = DinosaurToy('Rex')

toys = [rusty, fluffy, rex]
for toy in toys:
    toy.speak()

# Output:
# Rusty says beep boop! I am a robot!
# Fluffy says hug me! I'm cuddly!
# Rex says ROOOOAR!

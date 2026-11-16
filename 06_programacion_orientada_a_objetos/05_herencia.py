# ======================
# CONCEPTO: HERENCIA
# ======================
# La herencia permite que una subclase (clase hija) acceda a los atributos
# y métodos de una clase base (clase padre), facilitando la reutilización de código.

# 1. HERENCIA SIMPLE
# Sintaxis básica:
class Parent:
    pass

class Child(Parent):
    pass

# Ejemplo práctico:
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    bark = 'woof! woof!! woof!!!'

    # Sobrescribe sound() llamando primero al método de la clase padre con super()
    def sound(self):
        base = super().sound()
        return f'{base}, then {self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())  # Jack makes a sound, then Jack barks woof! woof!! woof!!!


# 2. HERENCIA MÚLTIPLE
# Permite que una subclase herede de dos o más clases independientes al mismo tiempo.
# Sintaxis básica:
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

# Ejemplo práctico:
class Walker:
    def walk(self):
        return 'it can walk on land'

class Swimmer:
    def swim(self):
        return 'it can swim in water'

# Amphibian hereda tanto de Walker como de Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"It is {self.name} the frog; {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: It is Freddy the frog; it can walk on land and it can swim in water.

# ==============================================
# CONCEPTO: ATRIBUTOS DE CLASE Y DE INSTANCIA
# ==============================================
# - Atributos de clase: Variables compartidas por todas las instancias de la clase.
# - Atributos de instancia: Variables únicas y particulares para cada objeto creado.

class Dog:
    # Atributo de clase (universal para todos los objetos de esta clase)
    species = "French Bulldog"

    def __init__(self, name):
        # Atributo de instancia (único para cada objeto)
        self.name = name

print(Dog.species)  # French Bulldog

dog_1 = Dog("Jack")
print(dog_1.name)     # Jack (Atributo de instancia)
print(dog_1.species)  # French Bulldog (Heredado de la clase)

dog_2 = Dog("Tom")
print(dog_2.name)     # Tom (Atributo de instancia)
print(dog_2.species)  # French Bulldog (Heredado de la clase)

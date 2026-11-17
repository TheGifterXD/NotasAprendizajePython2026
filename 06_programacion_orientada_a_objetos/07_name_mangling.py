# ==========================
# CONCEPTO: NAME MANGLING
# ==========================
# Es el proceso mediante el cual Python reescribe internamente el nombre
# de un atributo o método para evitar sobrescrituras accidentales,
# especialmente al trabajar con herencia.

# - Un guion bajo (_): Convención que indica que el atributo o método
#   es de uso interno y no debería accederse desde fuera de la clase.
# - Doble guion bajo (__): Activa el name mangling y renombra el elemento así:
#   __attribute -> _ClassName__attribute


# Ejemplo SIN name mangling:
class Parent:
    def __init__(self):
        self.data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.data = 'Child data'

c = Child()
print(c.__dict__)  # {'data': 'Child data'}
# El atributo definido en Parent se sobrescribe y se pierde al heredar.


# Ejemplo CON name mangling:
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__)  # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
# Ambos atributos coexisten sin colisionar gracias al renombrado interno.

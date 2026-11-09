# ========================================
# CONCEPTO: MANEJO DINÁMICO DE ATRIBUTOS
# ========================================
# Permite acceder, modificar, verificar o eliminar atributos
# usando sus nombres como cadenas de texto mediante funciones integradas.

# 1. GETATTR()
# Permite leer un atributo de un objeto cuando no se conoce su nombre de antemano.
# Si el atributo no existe, devuelve un AttributeError, a menos que se especifique un valor por defecto.
# Sintaxis: getattr(object, attribute_name, default_value)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)

print(getattr(person, 'name'))                  # John Doe
print(getattr(person, 'age'))                   # 30
print(getattr(person, 'city', 'Milano'))        # Milano (valor por defecto)

# Uso práctico con variables:
attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))


# 2. LISTAR ATRIBUTOS CON DIR()
# La función dir() permite inspeccionar los atributos disponibles en un objeto.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John Doe', 30)

# Filtrar atributos ignorando métodos dunder y métodos ejecutables
for attr in dir(person):
    if not attr.startswith('__') and not callable(getattr(person, attr)):
        value = getattr(person, attr)
        print(f'{attr}: {value}')

# Output:
# age: 30
# name: John Doe
# NOTA: callable() verifica si un atributo/método puede ser invocado.


# 3. SETATTR()
# Permite crear o actualizar un atributo existente de forma dinámica.
# Sintaxis: setattr(object, attribute_name, value)

class Configuration:
    pass

# Datos cargados en tiempo de ejecución (ej. archivo de configuración o variables de entorno)
settings_data = {
    'server_url': 'https://api.example.com',
    'timeout_sec': 30,
    'max_retries': 5
}

config_obj = Configuration()

# Asignación dinámica de atributos usando las claves y valores del diccionario
for attr_name, attr_value in settings_data.items():
    setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)   # https://api.example.com
print(config_obj.timeout_sec)  # 30


# 4. HASATTR()
# Permite comprobar si un atributo existe en un objeto, devolviendo un booleano.
# Sintaxis: hasattr(object, attribute_name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product_a = Product('T-Shirt', 25)
required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
    if not hasattr(product_a, attr):
        print(f"ERROR: Product is missing the required attribute: '{attr}'")
    else:
        print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'


# 5. DELATTR()
# Permite eliminar un atributo de un objeto si ya no se necesita.
# Sintaxis: delattr(object, attribute_name)

class UserSession:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.auth_token = token    # sensible / privado
        self.temp_counter = 0      # temporal

session = UserSession(101, 'a1b2c3d4e5')

# Lista de atributos a limpiar antes de "guardar" o serializar la sesión
attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
    if hasattr(session, attr):
        delattr(session, attr)
        print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session, attr)):
        print(f' - {attr}: {getattr(session, attr)}')

# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter
# Final attributes remaining:
#  - user_id: 101

# ===========================
# CONCEPTO: DICCIONARIOS
# ===========================
# Estructuras de datos mutables que almacenan colecciones de pares clave-valor.
# Las claves deben ser de tipos inmutables (str, int, float, tuple) y únicas.

# 1. SINTAXIS BÁSICA Y CREACIÓN
# Sintaxis literal con llaves: {[clave]: [valor]}
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250,
    'toppings': ['mozzarella', 'basil']
}

# Constructor dict() pasando un iterable de tuplas (clave, valor):
pizza_alt = dict([
    ('name', 'Margherita Pizza'),
    ('price', 8.9),
    ('calories_per_slice', 250),
    ('toppings', ['mozzarella', 'basil'])
])


# 2. ACCEDER A UN VALOR
# Notación de corchetes: [diccionario][[clave]]
print(pizza['name'])  # Imprime: 'Margherita Pizza'
# Nota: Si la clave no existe, lanza un KeyError.


# 3. ACTUALIZAR Y AÑADIR ELEMENTOS
# Si la clave existe, actualiza el valor; si no existe, crea el nuevo par:
pizza['name'] = 'Margherita'
print(pizza['name'])  # Imprime: 'Margherita'

pizza['is_vegetarian'] = True  # Añade clave nueva al final


# 4. MÉTODOS DE DICCIONARIOS

# 4.1 .GET([clave], [default])
# Recupera el valor de la clave de forma segura sin lanzar KeyError si no existe.
print(pizza.get('toppings', []))  # Imprime: ['mozzarella', 'basil']
print(pizza.get('size', 'Medium')) # Imprime: 'Medium' (no existe 'size')


# 4.2 .KEYS() Y .VALUES()
# Devuelven objetos de vista (dictionary views) iterables de claves y valores:
print(pizza.keys())    # dict_keys(['name', 'price', 'calories_per_slice', ...])
print(pizza.values())  # dict_values(['Margherita', 8.9, 250, ...])


# 4.3 .ITEMS()
# Devuelve un objeto de vista con tuplas de la forma (clave, valor):
print(pizza.items())   # dict_items([('name', 'Margherita'), ('price', 8.9), ...])


# 4.4 .CLEAR()
# Elimina todos los pares clave-valor dejando el diccionario vacío.
# pizza.clear() -> {}


# 4.5 .POP([clave], [default])
# Elimina la clave especificada y devuelve su valor.
price = pizza.pop('price', None)
print(price)  # Imprime: 8.9
# Nota: Si la clave no existe y no se define [default], lanza KeyError.


# 4.6 .POPITEM()
# Elimina y devuelve el último par (clave, valor) insertado como tupla.
last_item = pizza.popitem()
print(last_item)  # Imprime: ('is_vegetarian', True)


# 4.7 .UPDATE([otro_diccionario])
# Actualiza los valores existentes y añade las claves nuevas que no estaban:
pizza.update({'price': 15.0, 'total_time': 25})
print(pizza)
# Imprime:
# {
#     'name': 'Margherita',
#     'calories_per_slice': 250,
#     'toppings': ['mozzarella', 'basil'],
#     'price': 15.0,
#     'total_time': 25
# }

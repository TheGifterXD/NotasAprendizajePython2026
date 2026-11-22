# ==============================================
# CONCEPTO: MAPAS, TABLAS HASH Y CONJUNTOS
# ==============================================

# 1. TIPO ABSTRACTO DE DATOS (ADT)
# Modelo conceptual que define qué operaciones admite una estructura y sus reglas,
# sin especificar cómo se implementa internamente (separa interfaz de implementación).


# 2. MAPAS (ADT) Y HASH MAPS (TABLAS HASH)
# - Map: ADT que almacena pares clave-valor donde cada clave es única (los valores sí
#   pueden repetirse).
# - Hash Map: Implementación concreta de un mapa. Usa una función hash sobre la clave
#   para calcular un índice en un arreglo interno donde se guarda el dato.
# - Colisiones: Ocurren cuando dos claves generan el mismo índice. Se resuelven con:
#   * Encadenamiento (Chaining): Cada índice apunta a una lista enlazada con los pares.
#   * Direccionamiento abierto (Open Addressing): Busca el siguiente índice libre.
# - Complejidad (insertar, buscar, eliminar):
#   * Tiempo: O(1) en promedio; O(n) en el peor caso (múltiples colisiones).
#   * Espacio: O(1) en promedio; O(n) al redimensionar la tabla interna.

# En Python, 'dict' está implementado como un Hash Map:
my_dictionary = {'A': 1, 'B': 2, 'C': 3}
my_dictionary = dict(A=1, B=2, C=3)

print(my_dictionary['A'])       # 1 (Obtener valor)
my_dictionary['A'] = 4          # Actualizar valor
del my_dictionary['A']          # Eliminar par clave-valor
print('C' in my_dictionary)     # True (Verificar existencia de clave)

print(my_dictionary.keys())     # dict_keys(['B', 'C'])
print(my_dictionary.values())   # dict_values([2, 3])
print(my_dictionary.items())    # dict_items([('B', 2), ('C', 3)])


# 3. CONJUNTOS (SETS)
# - Colecciones dinámicas y desordenadas de elementos únicos (sin duplicados ni índices).
# - Internamente funcionan como una tabla hash que solo almacena claves (sin valores).
# - Solo admiten elementos inmutables/hasheables (números, cadenas, tuplas; no listas ni dicts).
# - Complejidad (agregar, eliminar, verificar pertenencia):
#   * Tiempo: O(1) en promedio; O(n) en el peor caso (colisiones).
#   * Espacio: O(1) en promedio; O(n) al redimensionar.

empty_set = set()        # {} crea un diccionario vacío, no un set
numbers = {1, 2, 3, 4}

numbers.add(5)           # Agrega elemento: {1, 2, 3, 4, 5}
numbers.remove(5)        # Elimina elemento (lanza KeyError si no existe)
numbers.discard(5)       # Elimina elemento (no lanza error si no existe)
print(3 in numbers)      # True
numbers.pop()            # Elimina y devuelve un elemento arbitrario
numbers.clear()          # Vacía el conjunto por completo


# 4. OPERACIONES MATEMÁTICAS DE CONJUNTOS
set_a = {1, 2, 3, 4}
set_b = {2, 3, 4, 5, 6}

print(set_a | set_b)     # Unión: {1, 2, 3, 4, 5, 6} -> set_a.union(set_b)
print(set_a & set_b)     # Intersección: {2, 3, 4} -> set_a.intersection(set_b)
print(set_a - set_b)     # Diferencia: {1} -> set_a.difference(set_b)
print(set_a ^ set_b)     # Diferencia simétrica: {1, 5, 6} -> set_a.symmetric_difference(set_b)

print(set_a.issubset(set_b))    # False
print(set_a.issuperset(set_b))  # False

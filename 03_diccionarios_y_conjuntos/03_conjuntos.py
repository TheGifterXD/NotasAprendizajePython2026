# =======================
# CONCEPTO: CONJUNTOS (SETS)
# =======================
# Estructuras de datos integradas, mutables y NO ordenadas.
# Almacenan únicamente elementos ÚNICOS e INMUTABLES (hashables como int, str, tuple).
# Se utilizan para eliminar duplicados y realizar operaciones matemáticas de teoría de conjuntos.

# 1. CREACIÓN DE CONJUNTOS
# Sintaxis literal utilizando llaves con elementos:
my_set = {1, 2, 3, 4, 5}

# NOTA CLAVE: Para crear un conjunto vacío, DEBES usar la función set().
# Usar solo llaves {} creará un diccionario vacío (dict).
empty_set = set()   # Instancia de set
empty_dict = {}      # Instancia de dict


# 2. AGREGAR ELEMENTOS
# Método .add([elemento]): Añade un solo elemento al conjunto si no existe previamente.
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)  # Imprime: {1, 2, 3, 4, 5, 6}


# 3. ELIMINAR ELEMENTOS
my_set = {1, 2, 3, 4, 5, 6}

# A) .remove([elemento]): Elimina un elemento. Lanza KeyError si el elemento NO existe.
# my_set.remove(7)  # Lanza KeyError: 7

# B) .discard([elemento]): Elimina el elemento si existe. Si NO existe, se ignora sin lanzar error.
my_set.discard(2)
print(my_set)  # Imprime: {1, 3, 4, 5, 6}

# C) .clear(): Vacía completamente el conjunto.
my_set.clear()
print(my_set)  # Imprime: set()


# 4. COMPARAR CONJUNTOS (MÉTODOS BOOLEANOS)
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

# 4.1 .issubset([otro_conjunto])
# Devuelve True si todos los elementos del conjunto actual están contenidos en el otro:
print(your_set.issubset(my_set))  # Imprime: False ({6} no está en my_set)

# 4.2 .issuperset([otro_conjunto])
# Devuelve True si el conjunto actual contiene todos los elementos del otro:
print(my_set.issuperset(your_set))  # Imprime: False

# 4.3 .isdisjoint([otro_conjunto])
# Devuelve True si los dos conjuntos no comparten NINGÚN elemento en común:
print(my_set.isdisjoint(your_set))  # Imprime: False (comparten 2, 3, 4)


# 5. OPERADORES DE CONJUNTOS
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

# 5.1 UNIÓN (|): Combina todos los elementos de ambos conjuntos (sin duplicados).
print(my_set | your_set)  # Devuelve: {1, 2, 3, 4, 5, 6}

# 5.2 INTERSECCIÓN (&): Mantiene únicamente los elementos comunes.
print(my_set & your_set)  # Devuelve: {2, 3, 4}

# 5.3 DIFERENCIA (-): Mantiene elementos presentes en el primer conjunto pero NO en el segundo.
print(my_set - your_set)  # Devuelve: {1, 5}

# 5.4 DIFERENCIA SIMÉTRICA (^): Mantiene los elementos que están en uno u otro conjunto, pero NO en ambos.
print(my_set ^ your_set)  # Devuelve: {1, 5, 6}


# 6. COMPROBAR PERTENENCIA
# El operador 'in' en conjuntos es extremadamente rápido (complejidad O(1) constante):
print(5 in my_set)  # Imprime: True

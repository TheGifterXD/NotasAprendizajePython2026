# ===============================
# CONCEPTO: MÉTODOS DE TUPLAS
# ===============================

# 1. COUNT()
# Indica cuántas veces aparece un elemento en una tupla:
prog_langs = ('Rust', 'Java', 'C++', 'Rust')
print(prog_langs.count('Rust'))    # Imprime: 2

# Si el elemento no existe, devuelve 0:
print(prog_langs.count('python'))  # Imprime: 0
# Nota: Llamarlo sin argumentos lanza TypeError.


# 2. INDEX()
# Devuelve el índice de la primera aparición de un elemento:
print(prog_langs.index('Java'))  # Imprime: 1

# Segundo argumento (start): Define desde dónde inicia la búsqueda:
print(prog_langs.index('Rust', 2))  # Imprime: 3

# Tercer argumento (stop): Define el límite superior exclusivo [start:stop]:
print(prog_langs.index('C++', 0, 3))  # Imprime: 2
# Nota: Si el elemento no se encuentra dentro del rango especificado, lanza ValueError.


# 3. FUNCIÓN INTEGRADA SORTED()
# No es un método de tupla, sino una función integrada que ordena iterables.
# NOTA CLAVE: Siempre devuelve una LISTA nueva, no modifica la tupla original.

# Parámetros opcionales:
# - reverse=True: Orden descendente.
# - key=función: Transforma el elemento antes de comparar (e.g., len, str.lower, abs).

print(sorted(prog_langs, reverse=True))  # Imprime: ['Rust', 'Rust', 'Java', 'C++']
print(sorted(prog_langs, key=len))       # Imprime: ['C++', 'Java', 'Rust', 'Rust']

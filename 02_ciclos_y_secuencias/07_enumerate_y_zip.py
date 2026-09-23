# ========================================
# CONCEPTO: FUNCIONES ENUMERATE() Y ZIP()
# ========================================

# 1. FUNCIÓN ENUMERATE()
# Mantiene un seguimiento del índice y del elemento de un iterable en cada iteración.
# Devuelve un objeto de tipo enumerate que genera tuplas (índice, elemento).
langs = ['Spanish', 'English', 'Russian', 'Chinese']
print(list(enumerate(langs)))
# Imprime: [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# Iteración con desempaquetado de índice y elemento:
for index, lang in enumerate(langs):
    print(f'Index {index} and Language {lang}')
# Imprime:
# Index 0 and Language Spanish
# Index 1 and Language English
# Index 2 and Language Russian
# Index 3 and Language Chinese


# 2. ARGUMENTO START
# Parámetro opcional para cambiar el valor inicial del contador/índice (por defecto es 0):
for index, lang in enumerate(langs, start=1):
    print(f'Index {index} and Language {lang}')
# Imprime:
# Index 1 and Language Spanish
# Index 2 and Language English
# Index 3 and Language Russian
# Index 4 and Language Chinese


# 3. FUNCIÓN ZIP()
# Agrupa elementos en la misma posición de dos o más iterables en tuplas.
devs = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]
print(list(zip(devs, ids)))
# Imprime: [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]

# Iteración en paralelo con desempaquetado:
for name, dev_id in zip(devs, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')
# Imprime:
# Name: Naomi
# ID: 1
# Name: Dario
# ID: 2
# Name: Jessica
# ID: 3
# Name: Tom
# ID: 4

# NOTA CLAVE SOBRE ZIP():
# Si las secuencias tienen diferentes longitudes, zip() se detiene al agotar la más corta.

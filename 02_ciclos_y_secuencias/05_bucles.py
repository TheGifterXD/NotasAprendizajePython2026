# ========================
# CONCEPTO: BUCLES
# ========================
# Permiten ejecutar repetidamente un bloque de código mientras se cumpla una condición 
# o se recorran los elementos de un iterable.

# 1. BUCLE FOR
# Utilizado para iterar sobre secuencias (listas, tuplas, cadenas, etc.).
prog_langs = ['Rust', 'Java', 'Python', 'C++']

for language in prog_langs:
    print(language)
# Imprime:
# Rust
# Java
# Python
# C++

# Iteración sobre cadenas de texto:
for char in 'code':
    print(char)
# Imprime:
# c
# o
# d
# e


# 2. BUCLES ANIDADOS
# Permiten ejecutar un bucle interno completo por cada iteración del bucle externo.
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot']

for category in categories:
    for food in foods:
        print(category, food)
# Imprime:
# Fruit Apple
# Fruit Carrot
# Vegetable Apple
# Vegetable Carrot


# 3. BUCLE WHILE
# Ejecuta su bloque de código mientras la condición evaluada sea True.
secret_number = 3
guess = 0

# Nota: Asegurar siempre una condición de salida para evitar bucles infinitos.
while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')


# 4. SENTENCIA BREAK
# Interrumpe y sale inmediatamente del bucle actual.
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer) 
# Imprime solo: Jess


# 5. SENTENCIA CONTINUE
# Omite el resto del código en la iteración actual y pasa inmediatamente a la siguiente.
for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)
# Imprime:
# Jess
# Tom


# 6. CLÁUSULA ELSE EN BUCLES (Opcional)
# Se ejecuta solo si el bucle termina todas sus iteraciones de forma natural (sin break).
for developer in developer_names:
    if developer == 'Alex':
        print('Found!')
        break
else:
    print('Developer not found in list')  # Se ejecuta esta línea

# ==========================================
# CONCEPTO: MÉTODOS COMUNES DE CADENAS
# ==========================================
# Un método es una función asociada a un objeto especifico.
# Sintaxis: objeto.método(argumentos)

# 1. UPPER()
# Convierte todos los caracteres de una cadena a mayúsculas.
str1 = 'Hello world'
uppercase_str1 = str1.upper()
print(uppercase_str1)  # Imprime: HELLO WORLD

# 2. LOWER()
# Convierte todos los caracteres de una cadena a minúsculas.
lowercase_str1 = str1.lower()
print(lowercase_str1)  # Imprime: hello world

# 3. STRIP()
# Elimina los caracteres especificados solo de los extremos (por defecto borra espacios en blanco).
trimmed_str1 = str1.strip('Hello')
print(trimmed_str1)  # Imprime: ' world' (mantiene el espacio intermedio)

# 4. REPLACE(OLD, NEW)
# Reemplaza apariciones de la subcadena 'old' por 'new'.
replaced_str1 = str1.replace('Hello', 'Hi')
print(replaced_str1)  # Imprime: Hi world

# 5. SPLIT()
# Divide una cadena en una lista según el separador indicado (por defecto divide por espacios).
split_words = str1.split()
print(split_words)  # Imprime: ['Hello', 'world']

# 6. JOIN(ITERABLE)
# Une elementos de un iterable (como una lista) en una sola cadena usando el separador indicado.
list1 = ['Hello', 'world']
joined_list = ' '.join(list1)
print(joined_list)  # Imprime: Hello world

# 7. STARTSWITH(PREFIX) y ENDSWITH(SUFFIX)
# Retornan un valor booleano indicando si la cadena empieza o termina con dicho texto.
check_start_str1 = str1.startswith('Hello')
print(check_start_str1)  # Imprime: True
check_end_str1 = str1.endswith('Hello')
print(check_end_str1)    # Imprime: False

# 8. FIND(SUBSTRING)
# Devuelve el índice de la primera coincidencia de la subcadena. Si no existe, devuelve -1.
find_index_true = str1.find('world')
print(find_index_true)   # Imprime: 6
find_index_false = str1.find('planet')
print(find_index_false)  # Imprime: -1

# 9. COUNT(SUBSTRING)
# Devuelve el número de veces que aparece una subcadena en el texto.
o_count = str1.count('o')
print(o_count)  # Imprime: 2

# 10. CAPITALIZE()
# Convierte solo el primer carácter de la cadena a mayúscula y el resto a minúsculas.
cap_str1 = str1.capitalize()
print(cap_str1)  # Imprime: Hello world

# 11. ISUPPER()
# Evalúa si todos los caracteres alfabéticos de la cadena están en mayúsculas.
str2 = 'HELLO WORLD'
upper_check_str2 = str2.isupper()
print(upper_check_str2)  # Imprime: True

# 12. ISLOWER()
# Evalúa si todos los caracteres alfabéticos de la cadena están en minúsculas.
lower_check_str2 = str2.islower()
print(lower_check_str2)  # Imprime: False

# 13. TITLE()
# Convierte el primer carácter de cada palabra a mayúscula.
title_str1 = str1.title()
print(title_str1)  # Imprime: Hello World

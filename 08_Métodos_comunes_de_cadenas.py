# ==========================================
# CONCEPTO: MÉTODOS COMUNES DE CADENAS
# ==========================================
# Un método es una función que pertenece a una clase u objeto específico
# Se usa la sintaxis objeto.método

# 1. UPPER()
# Convierte todos los carácteres de una cadena a mayúsculas
str1 = 'Hello world'
uppercase_str1 = str1.upper()
print(uppercase_str1) # Imprime: HELLO WORLD

# 2. LOWER()
# Convierte todos los carácteres de una cadena a minúsculas
lowercase_str1 = str1.lower()
print(lowercase_str1) # Imprime: hello world

# 3. STRIP()
# Elimina los carácteres especificados, si no hay, solo borra los espacios
trimmed_str1 = str1.strip('Hello')
print(trimmed_str1) # Imprime:  World

# 4. REPLACE(OLD, NEW)
# Intercambia los carácteres específicados en el parámetro 'old' por los de 'new'
replaced_str1 = str1.replace('Hello', 'Hi')
print(replaced_str1) # Imprime: Hi world

# 5. SPLIT()
# Divide una cadena en una lista basada en el separador asignado
# Sin parámetros solo divide por cada espacio
split_words = str1.split()
print(split_words) # Imprime: ['Hello', 'world']

# 6. JOIN()
# Une los elementos de una iterable en una sola cadena
list1 = ['Hello', 'world']
joined_list = ' '.join(list1)
print(joined_list) # Imprime: Hello world

# 7. STARTSWITH(PREFIX) y ENDSWITH(SUFFIX)
# Dan un valor booleano si un carácter esta o no en un índice espefíficado
check_start_str1 = str1.startswith('Hello')
print(check_start_str1) # Imprime: True
check_end_str1 = str1.endswith('Hello')
print(check_end_str1) # Imprime: False

# 8. FIND(SUBSTRING)
# 

# ==================================
# CONCEPTO: CONCATENACIÓN E INTERPOLACIÓN
# ==================================

# 1. CONCATENACIÓN
# Combina cadenas usando el operador (+).
# Solo funciona entre tipos de datos 'str'.
str1 = 'hello'
str2 = 'world'
str1_plus_str2 = str1 + ' ' + str2
print(str1_plus_str2)  # Imprime: hello world

# 2. CONCATENACIÓN CON ENTEROS
# Para concatenar enteros se usa la función str() para convertirlos previamente.
name = 'John'
age = 28
john_age = name + ' ' + str(age)
print(john_age)  # Imprime: John 28

# Uso del operador de asignación aumentada (+=)
text = name + ' '  # Inicializamos la cadena con 'John '
text += str(age)   # Equivale a: text = text + str(age)
print(text)        # Imprime: John 28

# 3. INTERPOLACIÓN (f-strings)
# Proceso para insertar variables directamente dentro de un texto, facilitando la lectura.
# Se antepone una 'f' antes de las comillas y las variables van entre llaves {}.
# No requiere convertir tipos de datos manualmente con str().
name = 'Jane'
age = 25
print(f'{name} is {age} years old')  # Imprime: Jane is 25 years old

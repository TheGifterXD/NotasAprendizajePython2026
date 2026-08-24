# =====================================
# CONCEPTO: STRING SLICING
# =====================================
# El String slicing permite extraer una porción de una cadena.
# Las cadenas son inmutables en Python, por lo que el slicing no modifica la versión original.

# 1. NOTACIÓN BÁSICA
# Se usa la sintaxis var_name[start:stop]
# El parámetro 'start' es inclusivo y 'stop' es exclusivo.
str1 = 'hello'
# Índices: h(0), e(1), l(2), l(3), o(4)
print(str1[1:4])  # Imprime: ell

# 2. OMISIÓN DE ÍNDICES
# Si se omite 'start', inicia desde el índice 0.
# Si se omite 'stop', lee hasta el último carácter de la cadena.
print(str1[:4])  # Imprime: hell
print(str1[1:])  # Imprime: ello

# 3. PARÁMETRO STEP (PASO)
# Dicta el salto entre caracteres: var_name[start:stop:step]
str2 = 'hello world'
print(str2[0:11:2])  # Imprime: hlowrd

# 4. ÍNDICES NEGATIVOS
# Un valor negativo en 'step' invierte la dirección.
# Al dejar 'start' y 'stop' vacíos, invierte la cadena completa.
print(str2[::-1])  # Imprime: dlrow olleh

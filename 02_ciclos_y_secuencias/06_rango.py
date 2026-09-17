# ==========================
# CONCEPTO: FUNCIÓN RANGE()
# ==========================
# Genera una secuencia inmutable de números enteros de forma eficiente (lazy evaluation).

# Sintaxis básica:
# range(stop)
# range(start, stop[, step])

# 1. ARGUMENTO ÚNICO (STOP)
# El único argumento obligatorio es 'stop' (exclusivo).
# 'start' por defecto es 0 y 'step' por defecto es 1.
for num in range(3):
    print(num)
# Imprime:
# 0
# 1
# 2


# 2. ARGUMENTOS START Y STOP
# 'start' define el número inicial (inclusivo).
for num in range(1, 5):
    print(num)
# Imprime:
# 1
# 2
# 3
# 4


# 3. ARGUMENTO STEP (PASO POSITIVO)
# Incremento aplicado en cada iteración.
for even_num in range(2, 11, 2):
    print(even_num)
# Imprime:
# 2
# 4
# 6
# 8
# 10


# 4. PASO NEGATIVO (SECUENCIA DECRECIENTE)
# 'start' debe ser mayor que 'stop' y 'step' debe ser negativo.
for number in range(40, 0, -10):
    print(number)
# Imprime:
# 40
# 30
# 20
# 10


# 5. CONVERSIÓN A LISTA Y ERRORES COMUNES
# Un objeto range() se puede convertir a una lista mutable mediante list():
pair_numbers = list(range(2, 11, 2))
print(pair_numbers)  # Imprime: [2, 4, 6, 8, 10]

# NOTAS SOBRE ERRORES:
# - Llamar a range() sin argumentos lanza TypeError.
# - Usar flotantes como argumentos lanza TypeError.
# - Usar 0 como argumento 'step' lanza ValueError (range() arg 3 must not be zero).

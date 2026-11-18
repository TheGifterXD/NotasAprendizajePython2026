# =======================================
# CONCEPTO: FUNCIONAMIENTO DE FUNCIONES
# =======================================
# Son bloques de código reutilizables que solo se ejecutan cuando son llamados.

# 1. PRINT()
# Muestra un valor o resultado en la consola.
name = 'John'
print(name)  # Imprime: John

# 2. INPUT()
# Solicita una entrada al usuario desde la consola (siempre devuelve un 'str').
user_name = input('What is your name? ')  # Ejemplo de entrada: Gifter
print('Hello', user_name)                # Imprime: Hello Gifter

# 3. INT()
# Convierte números flotantes, cadenas válidas o booleanos a un tipo entero.
print(int(3.14))   # Imprime: 3
print(int('42'))   # Imprime: 42
print(int(True))   # Imprime: 1
print(int(False))  # Imprime: 0

# 4. FUNCIONES PERSONALIZADAS
# Se definen con la palabra clave 'def', seguida del nombre, paréntesis () y dos puntos :
# El código interno debe ir indentado.

# Función básica sin parámetros:
def hello():
    print('Hello World')

hello()  # Imprime: Hello World

# Función con parámetros (las variables declaradas dentro del paréntesis):
def print_sum(a, b):
    print(a + b)

print_sum(3, 1)  # Imprime: 4 (los valores 3 y 1 son los argumentos)

# Nota: Pasar un número incorrecto de argumentos lanza un TypeError.

# 5. RETORNO DE VALORES (RETURN VS PRINT)
# Si una función no tiene una instrucción 'return', devuelve implícitamente 'None'.
# 'None' representa la ausencia de un valor y se evalúa como Falsy.

def sum_without_return(a, b):
    print(a + b)

my_sum1 = sum_without_return(3, 1)  # Imprime: 4 (por el print interno)
print(my_sum1)                       # Imprime: None

# Uso adecuado de 'return':
def sum_with_return(a, b):
    return a + b

my_sum2 = sum_with_return(3, 1)
print(my_sum2)                       # Imprime: 4

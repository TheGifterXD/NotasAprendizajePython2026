# =============================
# CONCEPTO: FUNCIONES LAMBDA
# =============================
# Son funciones anónimas de una sola línea.
# Sintaxis: lambda [parámetros]: [expresión]
# Se utilizan principalmente como argumentos para funciones de orden superior como map() y filter().

# NOTA: Una función de orden superior es aquella que recibe una función como argumento
# y/o devuelve una función como resultado.


# 1. USO BÁSICO DE FUNCIONES LAMBDA
# Función tradicional:
def square(num):
    return num ** 2

print(square(4))  # Imprime: 16

# Refactorización con función lambda dentro de filter():
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Imprime: [2, 4]


# 2. BUENAS PRÁCTICAS Y PEP 8

# A) Evitar asignar funciones lambda a variables:
# PEP 8 recomienda no hacer esto porque destruye el propósito de ser anónima
# y dificulta el rastreo de errores en el traceback:
# square = lambda x: x ** 2  # NO RECOMENDADO

# Forma correcta con lambda (pasándola directamente sin variable intermedia):
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Imprime: [1, 4, 9, 16, 25]

# Forma correcta con def (si la lógica se va a reutilizar):
def square(num):
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Imprime: [1, 4, 9, 16, 25]


# B) Evitar lambdas complejas u oscuras:
# Difícil de leer y mantener:
result = (lambda x: (x**2 + 2*x - 1) if x > 0 else (x**3 - x + 4))(3)
print(result)  # Imprime: 14

# Mucho más legible definiendo una función explícita:
def calculate_expression(x):
    if x > 0:
        return x**2 + 2*x - 1
    else:
        return x**3 - x + 4

print(calculate_expression(3))  # Imprime: 14

# CONCLUSIÓN:
# Usa expresiones lambda para operaciones simples, de una sola línea y de uso único.
# Si necesitas reutilizar la función o incluye lógica compleja, utiliza 'def'.

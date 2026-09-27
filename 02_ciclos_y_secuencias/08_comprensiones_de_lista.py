# ========================================
# CONCEPTO: COMPRENSIONES DE LISTA, MAP, FILTER Y SUM
# ========================================
# Permiten crear y transformar listas de forma concisa y expresiva.

# 1. COMPRENSIONES DE LISTA (LIST COMPREHENSIONS)
# Sintaxis básica con condición opcional: 
# [[expresión] for [elemento] in [iterable] if [condición]]

# Bucle tradicional:
even_numbers = []
for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # Imprime: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Equivalente con comprensión de lista (más conciso):
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)  # Imprime: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Comprensión con condicional if-else (operador ternario):
# Sintaxis: [[expresión_if] if [condición] else [expresión_else] for [elemento] in [iterable]]
numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)  # Imprime: [(1, 'Odd'), (2, 'Even'), (3, 'Odd'), (4, 'Even'), (5, 'Odd')]


# 2. FUNCIÓN FILTER()
# Filtra elementos de un iterable evaluando una función que devuelve un booleano (True/False).
# Sintaxis: filter([función], [iterable])
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

# Nota: filter() devuelve un objeto ejecutable (iterador), por lo que se convierte a list():
long_words = list(filter(is_long_word, words))
print(long_words)  # Imprime: ['mountain', 'river', 'cloud']


# 3. FUNCIÓN MAP()
# Aplica una función a cada elemento de un iterable y devuelve los resultados transformados.
# Sintaxis: map([función], [iterable])
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit)  # Imprime: [32.0, 50.0, 68.0, 86.0, 104.0]


# 4. FUNCIÓN SUM()
# Devuelve la suma de todos los elementos numéricos de un iterable.
# Sintaxis: sum([iterable], [start=0])
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total)  # Imprime: 50

# Uso con valor inicial opcional [start] (se pasa como segundo argumento posicional):
nums = [5, 10, 15, 20]
total = sum(nums, 10)  # Inicia la suma desde 10 ([start] = 10 + 5 + 10 + 15 + 20)
print(total)  # Imprime: 60

# ====================================
# CONCEPTO: LISTAS
# ====================================
# Son secuencias ordenadas de elementos mutables basadas en índice 0.
# Pueden contener tipos de datos heterogéneos (cadenas, números, booleanos y otras listas).

# 1. ACCESO Y MODIFICACIÓN
cities = ['Los Angeles', 'London', 'Tokyo']

# Acceso mediante índice positivo y negativo:
print(cities[0])   # Imprime: Los Angeles
print(cities[-1])  # Imprime: Tokyo

# La función list() convierte cualquier iterable a una lista:
developer = 'Jessica'
print(list(developer))  # Imprime: ['J', 'e', 's', 's', 'i', 'c', 'a']

# Con len() se obtiene la cantidad total de elementos:
prog_langs = ['JavaScript', 'Java']
print(len(prog_langs))  # Imprime: 2

# Las listas son mutables; se pueden modificar directamente sus elementos:
prog_langs[0] = 'Python'
print(prog_langs)  # Imprime: ['Python', 'Java']
# Nota: Intentar acceder o modificar un índice inexistente lanza un IndexError.


# 2. INSTRUCCIÓN DEL
# Elimina un elemento de la lista en una posición específica:
dev_profile = ['Jane Doe', 23, 'Python Developer']
del dev_profile[1]
print(dev_profile)  # Imprime: ['Jane Doe', 'Python Developer']


# 3. OPERADOR DE PERTENENCIA (IN)
# Devuelve un valor booleano indicando si un elemento está presente en la lista:
print('JavaScript' in prog_langs)  # Imprime: False
print('Python' in prog_langs)      # Imprime: True


# 4. LISTAS ANIDADAS
# Listas que contienen otras listas como elementos:
dev = ['Alice', 25, ['Python', 'Rust', 'C++']]

# Acceso al elemento que contiene la lista anidada:
print(dev[2])        # Imprime: ['Python', 'Rust', 'C++']

# Acceso a un elemento interno de la lista anidada:
print(dev[2][1])     # Imprime: Rust


# 5. DESEMPAQUETADO DE VALORES (UNPACKING)
# Asigna elementos de una lista a múltiples variables independientes:
develop = ['Alice', 34, 'Rust Developer']
name, age, job = develop
print(name)  # Imprime: Alice
print(age)   # Imprime: 34
print(job)   # Imprime: Rust Developer

# Uso del operador asterisco (*) para capturar los elementos sobrantes en una sublista:
name, *rest = develop
print(name)  # Imprime: Alice
print(rest)  # Imprime: [34, 'Rust Developer']

# Nota: Si el número de variables no coincide con los elementos (y no se usa *), lanza un ValueError.


# 6. SLICING DE LISTAS
# Permite obtener una sublista de elementos utilizando [start:stop:step]:
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
print(desserts[1:4])  # Imprime: ['Cookies', 'Ice Cream', 'Pie']

# Slicing con paso (step):
nums = [1, 2, 3, 4, 5, 6]
print(nums[1::2])  # Imprime: [2, 4, 6]

# ====================================
# CONCEPTO: MÉTODOS COMUNES DE LISTAS
# ====================================
# La mayoría de métodos de listas modifican la lista original 'in-place'
# y devuelven 'None'. Para ver los cambios se debe imprimir la lista después.

# 1. APPEND()
# Añade un único elemento al final de la lista.
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)  # Imprime: [1, 2, 3, 4, 5, 6]

# Si le pasas una lista, la añade como un elemento anidado:
even_nums = [8, 10]
numbers.append(even_nums)
print(numbers)  # Imprime: [1, 2, 3, 4, 5, 6, [8, 10]]


# 2. EXTEND()
# Desempaqueta y añade los elementos de un iterable al final de la lista.
letters = ['a', 'b']
letters.extend(['c', 'd'])
print(letters)  # Imprime: ['a', 'b', 'c', 'd']


# 3. INSERT()
# Inserta un elemento en el índice indicado: list.insert(index, element)
numbers_list = [1, 2, 4, 5]
numbers_list.insert(2, 3)  # En el índice 2 coloca el valor 3
print(numbers_list)  # Imprime: [1, 2, 3, 4, 5]


# 4. REMOVE()
# Elimina la primera coincidencia del valor especificado.
# Lanza un ValueError si el elemento no existe en la lista.
nums = [10, 20, 30, 40, 50, 50]
nums.remove(50)
print(nums)  # Imprime: [10, 20, 30, 40, 50]


# 5. POP()
# Elimina y DEVUELVE el elemento en el índice dado.
# Si no se pasa un índice, elimina y devuelve el último elemento.
items = ['a', 'b', 'c', 'd']
removed_item = items.pop(1)  # Extrae el valor en índice 1 ('b')
print(removed_item)  # Imprime: 'b'
print(items)         # Imprime: ['a', 'c', 'd']


# 6. CLEAR()
# Vacía todos los elementos de la lista dejándola en [].
demo_list = [1, 2, 3]
demo_list.clear()
print(demo_list)  # Imprime: []


# 7. SORT()
# Ordena la lista original 'in-place' (de menor a mayor por defecto).
unsorted_nums = [1, 7, 4, 2]
unsorted_nums.sort()
print(unsorted_nums)  # Imprime: [1, 2, 4, 7]


# 8. FUNCIÓN BUILT-IN SORTED()
# No modifica la lista original; crea y devuelve una NUEVA lista ordenada.
original = [5, 2, 9, 1]
new_sorted = sorted(original)
print(original)    # Imprime: [5, 2, 9, 1] (Sigue intacta)
print(new_sorted)  # Imprime: [1, 2, 5, 9]


# 9. REVERSE()
# Invierte el orden de los elementos 'in-place'.
rev_nums = [1, 2, 3, 4]
rev_nums.reverse()
print(rev_nums)  # Imprime: [4, 3, 2, 1]


# 10. INDEX()
# Devuelve el índice de la primera coincidencia del elemento indicado.
# Lanza un ValueError si el elemento no se encuentra.
prog_langs = ['Python', 'Java', 'C++']
idx = prog_langs.index('Java')
print(idx)  # Imprime: 1

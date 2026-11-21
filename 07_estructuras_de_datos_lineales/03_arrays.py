# ==================================================
# CONCEPTO: ARREGLOS ESTÁTICOS Y ARREGLOS DINÁMICOS
# ==================================================
# Los arrays almacenan colecciones ordenadas de datos en ubicaciones
# de memoria adyacentes, lo que permite acceder a cualquier elemento
# mediante su índice en tiempo constante O(1).


# 1. ARRAYS ESTÁTICOS
# - Tienen un tamaño fijo definido al momento de inicializarse y no pueden crecer ni reducirse.
# - Ideales cuando se conoce de antemano la cantidad exacta de elementos y se prioriza
#   el acceso rápido sin sobrecosto de memoria.
# - Python no cuenta con arreglos estáticos nativos tradicionales (a diferencia de lenguajes
#   como Java: int[] numbers = new int[3];).


# 2. ARRAYS DINÁMICOS (LISTAS EN PYTHON)
# - Pueden crecer o reducirse automáticamente en tiempo de ejecución.
# - Cuando alcanzan su capacidad máxima, asignan un bloque de memoria más grande
#   y copian los elementos existentes de forma automática.
# - Ideales cuando el número de elementos es desconocido o varía constantemente.

# En Python, la estructura 'list' funciona como un arreglo dinámico:
numbers = [3, 4, 5, 6]


# 3. OPERACIONES Y COMPLEJIDAD TEMPORAL (BIG O)
# - Acceso por índice: O(1) -> Cálculo directo de dirección en memoria.
print(numbers[0])  # 3
print(numbers[3])  # 6

# - Actualización por índice: O(1)
numbers[2] = 16    # [3, 4, 16, 6]

# - Inserción al final (.append): O(1) amortizado (O(n) solo cuando requiere redimensionar).
numbers.append(7)  # [3, 4, 16, 6, 7]

# - Inserción en posición específica (.insert): O(n) -> Desplaza los elementos posteriores.
numbers.insert(3, 15)  # [3, 4, 16, 15, 6, 7]

# - Eliminación por índice (.pop): O(n) en posiciones intermedias; O(1) al final sin índice.
numbers.pop(2)  # Elimina el 16 -> [3, 4, 15, 6, 7]
numbers.pop()   # Elimina el último elemento (7) -> [3, 4, 15, 6]

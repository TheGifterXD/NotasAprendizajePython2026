# ======================================
# CONCEPTO: ALGORITMOS Y NOTACIÓN BIG O
# ======================================
# Un algoritmo es un conjunto ordenado de instrucciones
# que sirven para solucionar un problema o realizar una tarea.

# 1. CARACTERÍSTICAS CLAVE
# - Debe tener un número finito de pasos.
# - Los pasos deben ser precisos y no ambiguos.
# - Pueden expresarse en pseudocódigo o implementarse en un lenguaje de programación.
# - Pueden tener 0 o más entradas (inputs) y 1 o más salidas (outputs).

# 2. CORRECCIÓN Y EFICIENCIA
# Un algoritmo correcto es aquel que devuelve la salida esperada para cualquier entrada válida.
# Un algoritmo eficiente es aquel que cumple su función usando el mínimo tiempo y memoria posibles.

# 3. NOTACIÓN BIG O
# Mide qué tan rápido crece el costo de un algoritmo cuando aumenta el tamaño de los datos.
# Describe el límite superior asintótico (el rendimiento en el peor escenario posible).

# 4. TAMAÑO DE LA ENTRADA (n)
# El término que domina el comportamiento de un algoritmo es n.
# Los factores constantes y términos menores pierden peso conforme crece n.
# Por ejemplo: en 7n + 20, el 20 y el 7 se ignoran cuando n tiende a infinito -> O(n).

# 5. COMPLEJIDADES DE TIEMPO
# Miden cómo escala la cantidad de operaciones cuando la entrada (n) es mayor.

# 5.1 COMPLEJIDAD TEMPORAL CONSTANTE O(1)
# El algoritmo tarda el mismo tiempo en ejecutarse independientemente del tamaño de la entrada.
def check_even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Este código siempre ejecuta las mismas 2 operaciones, sin importar si 'number' es 2 o 999,999,999.


# 5.2 COMPLEJIDAD TEMPORAL LOGARÍTMICA O(log n)
# El programa descarta una fracción constante (ej. la mitad) de los datos en cada paso.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# En cada iteración del while se elimina la mitad de la lista restante,
# por lo que duplicar los datos apenas suma 1 paso extra.


# 5.3 COMPLEJIDAD TEMPORAL LINEAL O(n)
# El tiempo aumenta proporcionalmente al tamaño de la entrada.
for grade in grades:  # grades es una lista de tamaño n
    print(grade)

# El ciclo for recorre uno por uno todos los elementos de grades.
# Si los elementos de grades se duplican, las operaciones también se duplican.


# 5.4 COMPLEJIDAD TEMPORAL LOG-LINEAL O(n log n)
# Es la complejidad estándar de los algoritmos de ordenamiento eficientes (ej. Timsort, Merge Sort).
sorted_grades = sorted(grades)

# Python divide la lista repetidamente (log n) y luego mezcla/ordena cada elemento (n),
# resultando en una combinación de n * log n operaciones.


# 5.5 COMPLEJIDAD TEMPORAL CUADRÁTICA O(n²)
# El tiempo crece al cuadrado respecto al tamaño de la entrada.
for i in range(n):
    for j in range(n):
        print("Hello, World!")

# Un ciclo anidado dentro de otro: el ciclo interno itera n veces
# por cada una de las n iteraciones del ciclo principal (n * n = n²).


# 5.6 COMPLEJIDAD TEMPORAL EXPONENCIAL O(2ⁿ) Y FACTORIAL O(n!)
# El tiempo se duplica con cada nuevo dato O(2ⁿ) o crece por permutaciones O(n!).
# Son inviables para entradas grandes (ej. fuerza bruta de contraseñas o el problema del viajante).


# 6. COMPLEJIDADES DE ESPACIO
# Miden cómo escala el uso de memoria RAM adicional cuando la entrada es mayor.

# 6.1 COMPLEJIDAD ESPACIAL CONSTANTE O(1)
# Requiere una cantidad fija de memoria independientemente de la entrada.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Sin importar si 'numbers' tiene 10 o 1,000,000 de elementos,
# la función solo crea dos variables simples ('total' y 'num') en memoria.


# 6.2 COMPLEJIDAD ESPACIAL LINEAL O(n)
# El uso de memoria crece proporcionalmente al tamaño de la entrada.
def double_values(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return result

# Se crea una lista nueva ('result') que almacenará exactamente n elementos,
# ocupando tanta memoria nueva como el tamaño de la entrada.


# 6.3 COMPLEJIDAD ESPACIAL CUADRÁTICA O(n²)
# El uso de memoria crece cuadráticamente en función del tamaño de la entrada.
def create_grid(n):
    return [[0 for _ in range(n)] for _ in range(n)]

# Se genera una matriz (lista de listas) de n filas por n columnas,
# reservando n * n = n² espacios en memoria.

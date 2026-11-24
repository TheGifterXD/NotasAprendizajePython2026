# ================================================
# CONCEPTO: BÚSQUEDA LINEAL Y BÚSQUEDA BINARIA
# ================================================
# Algoritmos fundamentales para localizar un target dentro de una
# colección. Ambos devuelven el índice del elemento si lo encuentran, o -1 como valor
# centinela si no existe (en Python se debe validar que el retorno no sea -1 antes de
# indexar, ya que arr[-1] accedería por error al último elemento).


# 1. BÚSQUEDA LINEAL (LINEAR SEARCH)
# - Funcionamiento: Recorre la lista secuencialmente desde el inicio hasta el final
#   comparando cada elemento con el objetivo.
# - Requisito: Funciona en listas ordenadas y desordenadas.
# - Complejidad:
#   * Tiempo: O(n) -> En el peor caso revisa todos los elementos.
#   * Espacio: O(1) -> Solo usa variables de control constantes.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


nums = [13, 4, 7, 9, 10]
print(linear_search(nums, 9))  # 3
print(linear_search(nums, 5))  # -1


# 2. BÚSQUEDA BINARIA (BINARY SEARCH)
# - Funcionamiento: Divide el rango de búsqueda (low a high) por la mitad en cada paso:
#   * Si arr[mid] == target -> Devuelve mid.
#   * Si arr[mid] < target  -> Descarta la mitad izquierda (low = mid + 1).
#   * Si arr[mid] > target  -> Descarta la mitad derecha (high = mid - 1).
# - Requisito obligatorio: La lista debe estar previamente ordenada.
# - Complejidad:
#   * Tiempo: O(log n) -> Descarta la mitad de los elementos restantes en cada iteración.
#   * Espacio: O(1) -> Solo usa tres punteros enteros (low, high, mid).

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_nums = [4, 7, 9, 10, 13]
print(binary_search(sorted_nums, 9))  # 2
print(binary_search(sorted_nums, 5))  # -1

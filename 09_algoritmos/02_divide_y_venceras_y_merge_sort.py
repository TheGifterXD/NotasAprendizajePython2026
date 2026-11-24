# ================================================
# CONCEPTO: DIVIDE Y VENCERÁS Y MERGE SORT
# ================================================

# 1. PARADIGMA DIVIDE Y VENCERÁS (DIVIDE AND CONQUER)
# Técnica algorítmica que descompone recursivamente un problema grande en subproblemas
# más pequeños e independientes hasta alcanzar un caso base trivial, para luego combinar
# sus soluciones y resolver el problema original.


# 2. MERGE SORT (ORDENAMIENTO POR MEZCLA)
# Algoritmo de ordenamiento basado en Divide y Vencerás:
# - Dividir: Parte la lista por la mitad recursivamente hasta obtener sublistas
#   de 1 o 0 elementos (caso base, ya que están ordenadas por defecto).
# - Vencer (Mezclar): Compara y fusiona las sublistas ordenadas en pares hasta
#   reconstruir la lista completa en orden.
# - Complejidad:
#   * Tiempo: O(n log n) en todos los casos (log n divisiones por n comparaciones).
#   * Espacio: O(n) -> No ordena in-place; requiere memoria adicional para las sublistas.

def merge_sort(arr):
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(arr) <= 1:
        return arr

    # Fase de división
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Fase de mezcla (combinación ordenada)
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Agregar los elementos restantes de la sublista que no se haya agotado
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


numbers = [42, 37, 53, 17]
print(merge_sort(numbers))  # [17, 37, 42, 53]

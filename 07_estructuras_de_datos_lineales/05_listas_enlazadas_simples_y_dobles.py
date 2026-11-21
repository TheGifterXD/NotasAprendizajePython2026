# ==============================================================
# CONCEPTO: LISTAS ENLAZADAS SIMPLES Y LISTAS ENLAZADAS DOBLES
# ==============================================================
# Una lista enlazada es una estructura de datos lineal formada por una cadena de nodos.
# A diferencia de los arreglos, no ocupa memoria contigua ni tiene tamaño fijo;
# crece o se reduce dinámicamente modificando las referencias entre nodos.


# 1. LISTA ENLAZADA SIMPLE (SINGLY LINKED LIST)
# - Estructura: Cada nodo guarda su dato y una única referencia al siguiente nodo ('next').
# - Puntos clave: El primer nodo se llama 'head' (cabeza) y el último 'tail' (cola, apunta a None).
# - Recorrido: Unidireccional (solo avanza desde 'head' hasta 'tail').
# - Complejidad temporal (sin puntero tail):
#   * Insertar/eliminar al inicio (head): O(1) -> Solo actualiza la referencia de 'head'.
#   * Insertar/eliminar en medio o al final (tail): O(n) -> Requiere recorrer la lista.
#   * Complejidad espacial de inserción/eliminación: O(1).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Construcción manual básica: A -> B -> C -> None
head = Node('A')
head.next = Node('B')
head.next.next = Node('C')

# Insertar al inicio (O(1)): E -> A -> B -> C -> None
new_node = Node('E')
new_node.next = head
head = new_node

# Eliminar del inicio (O(1)): A -> B -> C -> None
head = head.next


# 2. LISTA ENLAZADA DOBLE (DOUBLY LINKED LIST)
# - Estructura: Cada nodo guarda su dato y dos referencias: al siguiente nodo ('next')
#   y al nodo anterior ('prev').
# - Recorrido: Bidireccional (puede avanzar desde 'head' o retroceder desde 'tail').
# - Ventaja: Permite recorrer en ambos sentidos y operar al final en O(1) si se mantiene
#   una referencia directa a 'tail'.
# - Desventaja (Trade-off): Consume más memoria que la lista simple al almacenar dos punteros
#   por nodo y exige actualizar ambas referencias al insertar o eliminar.

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Construcción manual básica: None <- A <-> B -> None
node_a = DoublyNode('A')
node_b = DoublyNode('B')

node_a.next = node_b
node_b.prev = node_a

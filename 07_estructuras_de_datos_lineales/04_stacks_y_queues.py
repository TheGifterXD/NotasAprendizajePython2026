# ===========================
# CONCEPTO: STACKS Y QUEUES
# ===========================
# Son estructuras de datos lineales que restringen el orden en que se agregan
# y eliminan elementos.


# 1. STACKS - LIFO (Last-In, First-Out)
# - Principio: El último elemento en entrar es el primero en salir.
# - Extremos: Cima (top) y base (bottom). Todas las operaciones ocurren en la cima.
# - Operaciones principales (ambas con complejidad temporal y espacial O(1)):
#   * Push: Agrega un elemento a la cima.
#   * Pop: Elimina y devuelve el elemento de la cima.

stack = []

# Push (.append)
stack.append('plato_1')
stack.append('plato_2')
stack.append('plato_3')  # ['plato_1', 'plato_2', 'plato_3']

# Pop (.pop)
print(stack.pop())  # plato_3
print(stack)        # ['plato_1', 'plato_2']


# 2. QUEUES - FIFO (First-In, First-Out)
# - Principio: El primer elemento en entrar es el primero en salir.
# - Extremos: Frente (front) y final (back).
# - Operaciones principales (ambas con complejidad temporal y espacial O(1)):
#   * Enqueue: Agrega un elemento al final (back) de la cola.
#   * Dequeue: Elimina y devuelve el elemento del frente (front) de la cola.
# - En Python se usa 'collections.deque' porque usar list.pop(0) costaría O(n).

from collections import deque

queue = deque()

# Enqueue (.append)
queue.append('persona_1')
queue.append('persona_2')
queue.append('persona_3')  # deque(['persona_1', 'persona_2', 'persona_3'])

# Dequeue (.popleft)
print(queue.popleft())  # persona_1
print(queue)            # deque(['persona_2', 'persona_3'])

# ==============================================
# CONCEPTO: RECURSIÓN Y CALL STACK
# ==============================================
# La recursión es una técnica en la que una función se llama a sí misma para resolver
# versiones más pequeñas de un problema hasta alcanzar una condición de parada.
# Es útil en problemas de profundidad desconocida (como árboles de archivos o grafos).


# 1. ANATOMÍA DE UNA FUNCIÓN RECURSIVA
# Toda función recursiva requiere dos elementos obligatorios:
# - Caso base: Condición que detiene las llamadas recursivas. Sin un caso base
#   alcanzable, ocurre una recursión infinita y Python lanza 'RecursionError'.
# - Caso recursivo: Llamada a la misma función modificando el argumento para
#   acercarlo progresivamente al caso base.

def recursive_countdown(number):
    if number < 1:                    # Caso base
        return
    print(number)
    recursive_countdown(number - 1)   # Caso recursivo

recursive_countdown(5)  # Imprime: 5, 4, 3, 2, 1


# 2. ORDEN DE EJECUCIÓN EN LA RECURSIÓN
# La ubicación de las instrucciones respecto a la llamada recursiva altera el resultado:
# - Antes de la llamada recursiva: Se ejecuta mientras se desciende hacia el caso base.
# - Después de la llamada recursiva: Se ejecuta al retornar desde el caso base hacia arriba.

def recursive_countup(number):
    if number < 1:
        return
    recursive_countup(number - 1)
    print(number)  # Se ejecuta al desapilar cada llamada

recursive_countup(5)  # Imprime: 1, 2, 3, 4, 5


# 3. LA PILA DE LLAMADAS (CALL STACK)
# Python gestiona las llamadas activas mediante una pila LIFO (Last-In, First-Out):
# - Cada llamada crea un marco (stack frame) con sus argumentos y variables locales,
#   pausando la ejecución de la llamada anterior hasta que la nueva termine.
# - Al alcanzarse el caso base, los marcos se eliminan en orden inverso y cada
#   función reanuda las líneas pendientes después de su llamada recursiva.

def trace_countdown(number):
    print(f'Function call started for number: {number}')
    if number < 1:
        print('Base case reached')
        return
    print(f'Calling recursive_countdown with number: {number - 1}')
    trace_countdown(number - 1)
    print(f'Function call completed for number: {number}')

trace_countdown(3)
# Salida:
# Function call started for number: 3
# Calling recursive_countdown with number: 2
# Function call started for number: 2
# Calling recursive_countdown with number: 1
# Function call started for number: 1
# Calling recursive_countdown with number: 0
# Function call started for number: 0
# Base case reached
# Function call completed for number: 1
# Function call completed for number: 2
# Function call completed for number: 3

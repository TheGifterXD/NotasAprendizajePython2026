# =================================
# CONCEPTO: MANEJO DE EXCEPCIONES
# =================================
# Fundamental para escribir programas tolerantes a fallos.
# Permite anticipar, capturar y responder a errores de manera estructurada.

# 1. BLOQUES TRY Y EXCEPT
# - try: Bloque de código donde se anticipa que puede ocurrir un error.
# - except: Bloque que se ejecuta si se genera la excepción especificada.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
# Imprime: You can't divide by zero!


# 2. BLOQUES ELSE Y FINALLY
# - else: Se ejecuta únicamente si el bloque try NO lanza ninguna excepción.
# - finally: Se ejecuta siempre, ocurra o no una excepción (ideal para cerrar archivos o conexiones).
try:
    x = 10 / 2
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print('Division successful:', x)
finally:
    print('This block always runs')
# Imprime: Division successful 5.0
#          This block always runs


# 3. EXCEPCIONES MÚLTIPLES
# Se pueden capturar diferentes errores con bloques except separados:
try:
    number = int('abc')
    result = 10 / number
except ValueError:
    print('That was not a valid number')
except ZeroDivisionError:
    print("You can't divide by zero!")
# Imprime: Error occurred: ValueError

# O agruparlas en una misma línea utilizando una tupla:
try:
    number = int('abc')
except (ValueError, ZeroDivisionError) as e:
    print(f'Error occurred: {e}')
# Imprime: Error occurred: ValueError


# 4. CAPTURAR EL OBJETO DE EXCEPCIÓN (ALIAS)
# Se utiliza la palabra clave 'as' para almacenar la instancia del error y analizar su mensaje:
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f'Error occurred: {e}')
# Imprime: Error occurred: ZeroDivisionError

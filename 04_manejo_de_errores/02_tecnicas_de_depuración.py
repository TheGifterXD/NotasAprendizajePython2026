# ==================================
# CONCEPTO: TÉCNICAS DE DEPURACIÓN
# ==================================
# Son técnicas fundamentales para solucionar errores más rápido

# 1. FUNCIÓN PRINT() Y F-STRINGS
# Usar la función print() y f-strings puede ayudar a entender el flujo
# Y estados de las variables si se ponen en varios puntos del código
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

add(3, 7) # Imprime: Adding 3 and 7 gives 10

# 2. MÓDULO PDB
# Es el depurador interactivo de Python
# Permite pausar la ejecución de un script, examinar variables, ejecutar
# Código línea por línea y encontrar errores
import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2)) # Imprime: 5.0

# Con el comando .set_trace() se establece un prompt interactivo de pdb

# 3. HERRAMIENTAS DE DEPURACIÓN DEL IDE
# Muchos entornos integrados de desarrollo cuentan con herramientas
# Avanzadas de depuración

# ==================================
# CONCEPTO: ÁMBITO (SCOPE)
# ==================================
# Determina la visibilidad y accesibilidad de una variable en diferentes partes del código.

# 1. ÁMBITO GLOBAL
# Variables definidas fuera de cualquier función. Son accesibles desde cualquier lugar del módulo.

# 2. ÁMBITO LOCAL
# Variables declaradas dentro de una función (incluyendo sus parámetros).
# Solo existen y se pueden usar durante la ejecución de esa función.

tax_rate = 0.1  # Variable global

def calculate_tax(price):  # 'price' es un parámetro (variable local)
    tax = price * tax_rate  # 'tax' es una variable local
    return tax

print(calculate_tax(50))  # Imprime: 5.0
print(tax_rate)           # Imprime: 0.1

# Intentar acceder a una variable local fuera de su función lanza un NameError:
# print(tax)  # NameError: name 'tax' is not defined

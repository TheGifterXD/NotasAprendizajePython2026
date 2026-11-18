# ==========================================
# CONCEPTO: ASIGNACIONES AUMENTADAS
# ==========================================
# Aplican una operación a una variable y almacenan su resultado en ella misma.
# Su función es aumentar la legibilidad y reducir la redundancia y los errores tipográficos.

# La sintaxis básica es:
# var_name <operator>= value

# Que es la versión abreviada de:
# var_name = var_name <operator> value

# 1. OPERACIONES ARITMÉTICAS CON NÚMEROS

# Suma equivalente: var1 = var1 + 5
var1 = 10
var1 += 5
print(var1)  # Imprime: 15

# Resta equivalente: count = count - 3
count = 14
count -= 3
print(count)  # Imprime: 11

# Multiplicación equivalente: product = product * 7
product = 65
product *= 7
print(product)  # Imprime: 455

# División explícita (siempre devuelve float): price = price / 4
price = 100
price /= 4
print(price)  # Imprime: 25.0

# División entera: total_pages = total_pages // 5
total_pages = 23
total_pages //= 5
print(total_pages)  # Imprime: 4

# Módulo: bits = bits % 2
bits = 35
bits %= 2
print(bits)  # Imprime: 1

# Potencia: power = power ** 3
power = 2
power **= 3
print(power)  # Imprime: 8

# 2. OPERACIONES CON CADENAS
# Algunos operadores funcionan con cadenas gracias a la sobrecarga de operadores.

# Concatenación acumulativa:
greet1 = 'Hello'
greet1 += ' World'
print(greet1)  # Imprime: Hello World

# Repetición acumulativa:
greet2 = 'Hi'
greet2 *= 3
print(greet2)  # Imprime: HiHiHi

# Nota: Los operadores '-=', '/=', '//=', '%=' y '**=' generan un TypeError al usarse con cadenas.

# ==========================================
# CONCEPTO: OPERACIONES ARITMÉTICAS
# ==========================================
# Se usan variables de tipo 'int' y 'float'

# 1. OPERACIONES CON ENTEROS
# Una variable de tipo int es un número entero, sin decimales.

int1 = 56
int2 = 12

sum_ints = int1 + int2
print(sum_ints)  # Imprime: 68

diff_ints = int1 - int2
print(diff_ints)  # Imprime: 44

product_ints = int1 * int2
print(product_ints)  # Imprime: 672

# En Python 3, la división con (/) siempre devuelve un tipo 'float'
div_ints = int1 / int2
print(div_ints)  # Imprime: 4.666666666666667

# 2. OPERACIONES CON FLOTANTES
# Una variable de tipo float representa números reales (con decimales).

float1 = 5.4
float2 = 12.0

sum_floats = float1 + float2
print(sum_floats)  # Imprime: 17.4

diff_floats = float1 - float2
print(diff_floats)  # Imprime: -6.6

product_floats = float1 * float2
print(product_floats)  # Imprime: 64.8

div_floats = float1 / float2
print(div_floats)  # Imprime: 0.45

# 3. OPERADOR DE MÓDULO (%)
# Devuelve el residuo de la división entre el operando izquierdo y el derecho.
mod_ints = int1 % int2
mod_floats = float1 % float2
print(mod_ints)    # Imprime: 8
print(mod_floats)  # Imprime: 5.4

# 4. DIVISIÓN ENTERA (//)
# Devuelve la parte entera del cociente (redondea hacia abajo al entero más cercano).
floor_ints = int1 // int2
floor_floats = float1 // float2
print(floor_ints)    # Imprime: 4
print(floor_floats)  # Imprime: 0.0

# 5. EXPONENCIACIÓN (**)
# Eleva la base a la potencia indicada.
exp_ints = int1 ** int2
exp_floats = float1 ** float2
print(exp_ints)    # Imprime: 951166013805414055936
print(exp_floats)  # Imprime: 614787626.1765089

# Nota sobre flotantes:
# 0.1 + 0.2 da 0.30000000000000004 debido a la representación binaria IEEE 754 de punto flotante.

# 6. FUNCIONES INT() Y FLOAT()
# Conversión explícita de tipos de datos (casting).
int3 = 56
float3 = float(int3)
print(float3, type(float3))  # Imprime: 56.0 <class 'float'>

float4 = 12.92
int4 = int(float4)           # Trunca la parte decimal (no redondea)
print(int4, type(int4))      # Imprime: 12 <class 'int'>

str1_int = '45'
str2_float = '7.8'
int5 = int(str1_int)
float5 = float(str2_float)
print(int5, type(int5))      # Imprime: 45 <class 'int'>
print(float5, type(float5))  # Imprime: 7.8 <class 'float'>

# 7. ROUND()
# Redondea al número de decimales especificado (por defecto al entero más cercano).
# Utiliza redondeo al par más cercano (Banker's rounding).
float7 = 4.798
rounded_float7 = round(float7)
print(rounded_float7)  # Imprime: 5

float8 = 4.253
rounded_float8 = round(float8, 1)
print(rounded_float8)  # Imprime: 4.3

# 8. ABS()
# Devuelve el valor absoluto de un número.
num = -15
absol_value = abs(num)
print(absol_value)  # Imprime: 15

# 9. POW()
# pow(base, exp) equivale a base ** exp.
# pow(base, exp, mod) realiza (base ** exp) % mod de forma más eficiente en memoria.
result_1 = pow(2, 3)
print(result_1)  # Imprime: 8

result_2 = pow(2, 3, 5)
print(result_2)  # Imprime: 3

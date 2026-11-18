# ==========================================
# CONCEPTO: CONDICIONALES Y OPERADORES LÓGICOS
# ==========================================
# Permiten controlar el flujo de un programa evaluando expresiones relacionales.

# 1. OPERADORES DE COMPARACIÓN
# Retornan un valor booleano (True o False).

# Igualdad (==)
print(3 == 4)  # Imprime: False
print(3 == 3)  # Imprime: True

# Desigualdad (!=)
print(3 != 4)  # Imprime: True

# Mayor que (>) y Menor que (<)
print(3 > 4)   # Imprime: False
print(3 < 4)   # Imprime: True

# Mayor o igual que (>=) y Menor o igual que (<=)
print(3 >= 4)  # Imprime: False
print(3 <= 4)  # Imprime: True


# 2. CONDICIONAL IF
# Evalúa una condición. Si el resultado es True, se ejecuta el bloque de código indentado.
# Sintaxis:
# if condición:
#     código...

age = 18
if age >= 18:
    print('You are an adult')  # Imprime: You are an adult


# 3. CONDICIONAL ELSE
# Se ejecuta si ninguna de las condiciones previas del bloque resultaron verdaderas.
# Nota: Si se coloca código sin indentar entre el 'if' y el 'else', Python lanzará un SyntaxError.
age = 12
if age >= 18:
    print('You are an adult')
else:
    print('You are not an adult yet')  # Imprime: You are not an adult yet


# 4. CONDICIONAL ELIF
# Permite evaluar múltiples condiciones en secuencia.
# Tan pronto como una condición resulta True, se ejecuta su bloque y se omiten las demás.
age = 12
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
else:
    print('You are a child')  # Imprime: You are a child

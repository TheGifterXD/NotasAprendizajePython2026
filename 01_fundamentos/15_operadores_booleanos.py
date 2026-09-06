# ==========================================
# CONCEPTO: OPERADORES BOOLEANOS
# ==========================================
# Se usan para evaluar múltiples condiciones dentro del flujo de control.

# 1. SENTENCIAS ANIDADAS
# Permiten evaluar condiciones dependientes, aunque a menudo se simplifican con 'and'.
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('You are eligible to vote')  # Imprime: You are eligible to vote
    else:
        print('You are not old enough to vote')
else:
    print('You are not a citizen')


# 2. VALORES TRUTHY Y FALSY
# En Python, todo objeto tiene un valor booleano implícito.

# Los valores Falsy principales son:
# - False y None
# - El número 0 (int: 0, float: 0.0)
# - Cadenas y colecciones vacías ('', [], (), {})

# Los valores Truthy son:
# - Cualquier número distinto de 0
# - Cadenas y colecciones con al menos un elemento

# Se evalúa el valor booleano de un objeto con bool()
print(bool(False))  # Imprime: False
print(bool(0))      # Imprime: False
print(bool(''))     # Imprime: False
print(bool(None))   # Imprime: False

print(bool(True))   # Imprime: True
print(bool(1))      # Imprime: True
print(bool('Hi'))   # Imprime: True


# 3. OPERADORES LOGICOS (AND, OR, NOT)

# OPERADOR AND
# Evalúa de izquierda a derecha. Devuelve el primer valor Falsy que encuentra.
# Si todos son Truthy, devuelve el último valor.
is_citizen = True
age = 25
print(is_citizen and age)  # Imprime: 25

# Mismo ejemplo simplificado sin anidamiento:
if is_citizen and age >= 18:
    print('You are eligible to vote')


# OPERADOR OR
# Evalúa de izquierda a derecha. Devuelve el primer valor Truthy que encuentra.
# Si todos son Falsy, devuelve el último valor.
age = 19
is_unemployed = False
print(age or is_unemployed)  # Imprime: 19

is_student = True
if age < 18 or is_student:
    print('You are eligible for a student discount')  # Imprime esta línea
else:
    print('You are not eligible for a student discount')

# Nota: 'and' y 'or' evalúan con cortocircuito (short-circuiting), deteniendo
# la ejecución en cuanto se confirma el resultado final.


# OPERADOR NOT
# Invierte el valor booleano del operando. Siempre devuelve un valor bool (True o False).
is_admin = False
if not is_admin:
    print('Access denied for non-administrators')  # Imprime esta línea
else:
    print('Welcome, Administrator!')

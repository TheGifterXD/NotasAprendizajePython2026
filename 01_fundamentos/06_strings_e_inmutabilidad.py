# ==================================
# CONCEPTO: STRINGS E INMUTABILIDAD
# ==================================

# 1. COMILLAS SIMPLES Y DOBLES
# En algunos lenguajes se tratan distinto, pero en Python funcionan exactamente igual.
msssimple = "It's raining"
msgdoble = 'He said: "Hi!"'

# Se puede usar la barra invertida (\) como carácter de escape si se repiten comillas.
msg2 = 'It\'s raining'

# 2. STRINGS MULTILÍNEA
# Se escriben con comillas triples ('''...''' o """...""").
# Permiten escribir en varios renglones sin usar explícitamente '\n'.
msg = """Este es un string
que ocupa múltiples líneas
usando comillas triples."""

# 3. PERTENENCIA (in)
# Comprueba si un carácter o subcadena está dentro del string.
msg3 = "Hello"
print("Hello" in msg3)  # Imprime: True
print("e" in msg3)      # Imprime: True
print("Hi" in msg3)     # Imprime: False

# 4. LONGITUD (len)
# Muestra el número total de caracteres (incluyendo espacios).
print(len(msg3))  # Imprime: 5

# 5. INDEXACIÓN
# Permite acceder a un carácter específico usando corchetes [...].
# Los índices van de 0 hasta (longitud - 1).
print(msg3[0])  # Imprime: H (primer carácter)
print(msg3[4])  # Imprime: o (último carácter)

# Índices negativos: cuentan desde el final hacia atrás.
print(msg3[-1]) # Imprime: o (último)
print(msg3[-2]) # Imprime: l (penúltimo)

# 6. INMUTABILIDAD
# Un string NO se puede modificar una vez creado.
# Además de str, los tipos de datos int, float, bool, tuple y range también son inmutables.

# 7. F-STRINGS
# Permiten interpolar variables y expresiones dentro de un string de forma clara anteponiendo una 'f' y usando llaves {}.
nombre = "Gifter"
print(f"Hola, {nombre}. Tienes {10 + 6} años.") # Imprime: Hola, Gifter. Tienes 16 años.

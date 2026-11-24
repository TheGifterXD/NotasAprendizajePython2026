# ===================================
# CONCEPTO: OPERADORES DE IDENTIDAD
# ===================================
# Verifican si dos operandos apuntan exactamente al mismo objeto en memoria
# (es decir, si comparten la misma identidad o dirección de memoria).
# Se emplean los operadores 'is' e 'is not' y funcionan con cualquier tipo
# de objeto, aunque su uso principal es comparar contra singletons como None,
# True y False.

# Ejemplo básico con None:
response = None

print(response is None)      # True
print(response is not None)  # False

# 'is None' comprueba la ausencia de un valor;
# 'is not None' verifica que exista un valor asignado.


# Ejemplo diferenciando None de False:
response = False

if response is None:
    print('No answer yet')
else:
    print('An answer was given')  # An answer was given

# Una evaluación con 'if not response' trataría tanto a None como a False
# como falsos. El uso de 'is None' permite distinguir entre una respuesta
# no proporcionada (None) y una respuesta explícitamente negativa (False).


# Ejemplo comprobando identidad exacta:
response = False

print(response is True)      # False
print(response is False)     # True
print(response is not None)  # True

# 'is' evalúa si la referencia en memoria es idéntica, sin limitarse
# exclusivamente a valores booleanos.
# NOTA: Para evaluaciones booleanas estándar o banderas comunes, resulta
# más práctico utilizar operadores lógicos o condicionales directos

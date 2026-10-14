# ============================
# CONCEPTO: MENSAJES DE ERROR COMUNES
# ============================
# Guía rápida para identificar las excepciones más frecuentes en Python.

# 1. SYNTAXERROR
# Se genera cuando el código no cumple con la sintaxis formal del lenguaje.
# Ejemplo:
# print('Hello, world!'
# SyntaxError: unmatched '(' / '(' was never closed


# 2. NAMEERROR
# Se genera cuando intentas utilizar una variable, función o módulo que 
# no ha sido definida o declarada previamente en el ámbito actual.
# Ejemplo:
# print(undefined_variable)
# NameError: name 'undefined_variable' is not defined


# 3. TYPEERROR
# Se genera cuando una operación o función se aplica a un objeto de un tipo 
# inapropiado o incompatible (por ejemplo, sumar un entero y un texto).
# Ejemplo:
# 5 + '5'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


# 4. INDEXERROR
# Se genera al intentar acceder a un índice que está fuera de los límites 
# válidos de una secuencia (como listas o tuplas).
# Ejemplo:
# my_list = [1, 2, 3]
# print(my_list[5])
# IndexError: list index out of range


# 5. ATTRIBUTEERROR
# Se genera cuando intentas acceder o invocar un atributo o método que 
# no existe para el tipo de dato del objeto.
# Ejemplo:
# num = 42
# num.append(5)
# AttributeError: 'int' object has no attribute 'append'

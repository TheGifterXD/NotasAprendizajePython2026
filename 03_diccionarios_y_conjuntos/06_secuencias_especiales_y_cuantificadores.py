# ========================================================
# CONCEPTO: SECUENCIAS ESPECIALES Y CUANTIFICADORES
# ========================================================
import re

# 1. RAW STRINGS
# Se crean anteponiendo 'r' o 'R' a las comillas (ej. r'\d').
# Hacen que Python trate las barras invertidas (\) como caracteres literales
# en lugar de secuencias de escape (como \n o \t), evitando conflictos en regex.

print('Tab:\tdone')   # Tab:    done
print(r'Tab:\tdone')  # Tab:\tdone


# 2. SECUENCIAS ESPECIALES
# Representan grupos comunes de caracteres mediante una barra invertida (\):
# - \d: Cualquier dígito decimal (0-9).
# - \w: Cualquier carácter de palabra (letras, dígitos y guion bajo _).
# - \s: Cualquier espacio en blanco (espacio, tabulación, salto de línea).
# - \D, \W, \S: Lo opuesto a sus versiones en minúscula (ej. \D = no dígito).

room = 'Room 42B'
print(re.search(r'\d', room))  # <re.Match object; span=(5, 6), match='4'>


# 3. CUANTIFICADORES
# Indican cuántas veces puede repetirse el carácter o secuencia anterior:
# - +    : 1 o más veces.
# - *    : 0 o más veces.
# - ?    : 0 o 1 vez (hace el carácter opcional).
# - {n}  : Exactamente n veces.
# - {n,m}: Entre n y m veces.

print(re.search(r'\d+', room))                        # <re.Match object; span=(5, 7), match='42'>
print(re.search(r'go*al', 'What a goooal!'))          # <re.Match object; span=(7, 13), match='goooal'>
print(re.search(r'colou?r', 'My favorite color is blue'))  # <re.Match object; span=(12, 17), match='color'>
print(re.search(r'\d{4}', 'Room 42, built in 1987'))  # <re.Match object; span=(18, 22), match='1987'>


# 4. COMBINACIÓN DE ELEMENTOS
# Se pueden unir texto literal, secuencias especiales, cuantificadores y banderas.

cart = 'You have 3 ITEMS in your cart.'
print(re.search(r'\d+ items', cart, re.IGNORECASE))
# <re.Match object; span=(9, 16), match='3 ITEMS'>

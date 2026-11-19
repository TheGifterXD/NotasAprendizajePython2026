# ===============================================
# CONCEPTO: FUNCIONES PRINCIPALES DEL MÓDULO RE
# ===============================================
import re

# 1. RE.MATCH()
# Busca el patrón únicamente al inicio de la cadena.
# Devuelve un objeto 're.Match' si coincide al principio, o 'None' en caso contrario.

print(re.match(r'\d+', '42 apples'))   # <re.Match object; span=(0, 2), match='42'>
print(re.match(r'\d+', 'apples: 42'))  # None


# 2. RE.FULLMATCH()
# Verifica que la cadena completa cumpla exactamente con el patrón (ideal para validaciones).
# Devuelve 're.Match' si todo el texto coincide, o 'None' si sobran o faltan caracteres.

print(re.fullmatch(r'\d+:\d+', '10:30pm'))  # None
print(re.fullmatch(r'\d+:\d+', '10:30'))    # <re.Match object; span=(0, 5), match='10:30'>


# 3. RE.FINDALL()
# Busca todas las coincidencias del patrón en el texto y las devuelve en una lista.
# Si no encuentra ninguna, devuelve una lista vacía ([]).

menu = 'Coffee costs 3 dollars, tea costs 2, and cake costs 5.'
print(re.findall(r'\d+', menu))              # ['3', '2', '5']
print(re.findall(r'\d+', 'No numbers here')) # []


# 4. RE.SUB()
# Reemplaza las coincidencias del patrón por una nueva cadena y devuelve el texto resultante.
# Sintaxis: re.sub(patrón, reemplazo, texto, count=0, flags=0)
# - count: Limita el número máximo de reemplazos (pasar siempre como argumento con nombre).
# - flags: Modifica el comportamiento de búsqueda, como 're.IGNORECASE' (pasar con nombre).

message = 'My phone number is 555 0123'
print(re.sub(r'\d', '*', message))           # My phone number is *** ****
print(re.sub(r'\d', '*', message, count=3))  # My phone number is *** 0123

sentence = 'Cat and cat'
print(re.sub('cat', 'dog', sentence, flags=re.IGNORECASE))  # dog and dog

# =================================
# CONCEPTO: EXPRESIONES REGULARES 
# =================================
# Son patrones usados para buscar, validar o extraer texto según su estructura,
# sin necesidad de conocer la cadena exacta. Se manejan con el módulo estándar 're'.

import re

# 1. RE.SEARCH()
# Busca la primera coincidencia del patrón en el texto.
# Devuelve un objeto 're.Match' si lo encuentra, o 'None' si no existe.

sentence = 'The cat sat on the mat.'
print(re.search('cat', sentence))  # <re.Match object; span=(4, 7), match='cat'>
print(re.search('dog', sentence))  # None


# 2. MÉTODOS DEL OBJETO MATCH
# - .group(): Devuelve el texto exacto encontrado.
# - .span(): Devuelve una tupla con los índices (inicio, fin) de la coincidencia.

result = re.search('cat', sentence)
print(result.group())  # cat
print(result.span())   # (4, 7)


# 3. BANDERAS (FLAGS)
# Por defecto distingue entre mayúsculas y minúsculas.
# La bandera 're.IGNORECASE' desactiva esa distinción.

print(re.search('Cat', sentence))                 # None
print(re.search('Cat', sentence, re.IGNORECASE))  # <re.Match object; span=(4, 7), match='cat'>

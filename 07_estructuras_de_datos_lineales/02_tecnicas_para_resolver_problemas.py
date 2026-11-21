# ==============================================
# CONCEPTO: TÉCNICAS PARA RESOLVER PROBLEMAS
# ==============================================
# Metodología estructurada para analizar, diseñar y optimizar algoritmos.
# Caso práctico:
# "Dada una cadena, escribir un algoritmo que devuelva una nueva cadena
# con los caracteres en orden inverso."


# 1. ENTENDER EL PROBLEMA
# Leer y analizar el enunciado hasta identificar con claridad el objetivo,
# las restricciones y las reglas del problema antes de escribir código.


# 2. DESGLOSAR EL PROBLEMA
# Dividir el reto en tres componentes fundamentales:
# - Entrada (Input): Una cadena de texto (ej. "python").
# - Salida esperada (Output): Una nueva cadena invertida (ej. "nohtyp").
# - Transformación: Recorrer los caracteres de fin a inicio o insertar
#   cada carácter al principio de una nueva estructura.


# 3. PLANIFICAR EN PSEUDOCÓDIGO
# Redactar la lógica en lenguaje natural estructurado para validar el flujo
# sin preocuparse aún por la sintaxis exacta del lenguaje:
#
# GET original_string
# SET reversed_string = ""
#
# FOR EACH character IN original_string:
#     ADD character TO THE BEGINNING OF reversed_string
#
# RETURN reversed_string


# 4. ELEGIR EL ALGORITMO ADECUADO
# Evaluar distintas alternativas priorizando la eficiencia en tiempo y memoria (Big O):
# - Bucle con concatenación manual: O(n²) en tiempo (al ser las cadenas inmutables,
#   Python crea una nueva cadena en memoria en cada iteración).
# - Slicing con paso negativo [::-1]: O(n) en tiempo y espacio; opción más directa.
# - Función reversed() + "".join(): O(n) en tiempo y espacio; ideal para iteradores.


# 5. CONSIDERAR ESTRUCTURAS DE DATOS Y CASOS LÍMITE (EDGE CASES)
# Evaluar las herramientas adecuadas y prever entradas atípicas:
# - ¿Qué estructura de datos ofrece mejor rendimiento? (ej. listas para mutar datos
#   frente a cadenas inmutables).
# - ¿La solución contempla casos límite como una cadena vacía (""), un solo
#   carácter ("a"), espacios o caracteres especiales?


# 6. IMPLEMENTAR, PROBAR Y PERFECCIONAR LA SOLUCIÓN
# Traducir el diseño a código funcional, verificar con casos límite y refactorizar
# para obtener la versión más limpia, legible y eficiente.

def reverse_string_slicing(text: str) -> str:
    """Invierte una cadena utilizando slicing en tiempo O(n)."""
    return text[::-1]

def reverse_string_join(text: str) -> str:
    """Invierte una cadena combinando reversed() y join() en tiempo O(n)."""
    return "".join(reversed(text))

# Pruebas de funcionamiento y casos límite:
print(reverse_string_slicing("python"))  # nohtyp
print(reverse_string_join("python"))     # nohtyp
print(reverse_string_slicing(""))        # "" (caso límite: cadena vacía)
print(reverse_string_slicing("a"))       # a  (caso límite: un solo carácter)

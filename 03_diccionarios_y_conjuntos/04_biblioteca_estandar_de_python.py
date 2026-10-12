# ==========================================
# CONCEPTO: BIBLIOTECA ESTÁNDAR DE PYTHON
# ==========================================
# Una biblioteca estándar es un conjunto de módulos preescritos (funciones, clases 
# y estructuras de datos) integrados en Python listos para ser utilizados.

# Ejemplos de áreas cubiertas por la biblioteca estándar:
# - Sistema operativo y rutas (os, sys, pathlib)
# - Manipulación de fechas y horas (datetime)
# - Matemáticas (math, statistics)
# - Expresiones regulares (re)
# - Generación de números aleatorios (random)


# 1. IMPORTAR MÓDULOS COMPLETOS
# Sintaxis básica: import [module_name]
import math

# Para invocar una función del módulo importado, se utiliza la notación de punto:
# [module_name].[module_function]()
print(math.sqrt(36))  # Imprime: 6.0


# 1.1 USO DE ALIAS EN MÓDULOS
# Sintaxis: import [module_name] as [alias]
# Se usa para acortar nombres largos o evitar conflictos de nombres en el código:
import math as m

print(m.sqrt(36))  # Imprime: 6.0


# 2. IMPORTAR FUNCIONES ESPECÍFICAS
# Si solo necesitas elementos concretos sin cargar todo el módulo:
# Sintaxis: from [module_name] import [name1], [name2]
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

print(sin(angle_radians))  # Imprime: 0.6427876096865393
print(cos(angle_radians))  # Imprime: 0.766044443118978
# Nota: Al usar 'from', las funciones se llaman directamente SIN el prefijo del módulo.


# 2.1 IMPORTACIÓN CON COMODÍN (*)
# Sintaxis: from [module_name] import *
# Importa absolutamente todas las funciones y variables al espacio de nombres global.
from math import *
print(sqrt(36))  # Imprime: 6.0
print(pow(5, 2)) # Imprime: 25.0

# POR QUÉ SE DESACONSEJA:
# - Contamina el espacio de nombres (namespace).
# - Dificulta enormemente saber de qué módulo proviene cada función.
# - Puede sobrescribir funciones integradas de Python (built-ins) por accidente.


# 3. EL IDIOMA: if __name__ == '__main__':
# ¿Qué es '__name__'? Es una variable interna especial de Python.
# - Si ejecutas el script directamente en la terminal, Python le asigna el valor '__main__'.
# - Si el archivo es importado como módulo en otro script, '__name__' toma el nombre del archivo.

def main():
    print('Executing main script workflow...')

if __name__ == '__main__':
    # Este bloque de código SOLO se ejecuta si el script se corre directamente.
    # Si este archivo es importado desde otro script, este código se omite.
    main()

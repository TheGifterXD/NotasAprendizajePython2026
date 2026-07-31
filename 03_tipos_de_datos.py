# ==========================================
# CONCEPTO: TIPOS DE DATOS
# ==========================================

# Python es un lenguaje de tipado dinámico.
# Lo cual significa que interpreta las variables basado en el valor que se les asigne.
name = 'John Doe' # Es una variable de tipo string.
age = 25 # Es una variable de tipo integer.

# También existen los lenguajes de tipado estático.
# Por ejemplo: C#, que necesita que se indique el tipo de variable.
# string name = 'John Doe'
# int age = 25

# Los tipos de datos principales en Python son los siguientes:
mi_entero = 20 # integer o int: número entero.
mi_flotante = 15.5 # float: número con decimales.
mi_texto = 'Hola' # string o str: caracteres encerrados por comillas ('...' / "...").
mi_booleano = True # boolean o bool: representa valores lógicos (True / False).

# ESTRUCTURA Y COLECCIONES DE DATOS:

# set: colección de elementos únicos y no ordenados (se usan llaves {...}).
mi_set = {'Hola', 20, 15.5} 

# dictionary (dict): colección de pares clave: valor (se usan llaves y dos puntos {:}).
mi_diccionario = {'clave_1': 'Hola', 'clave_2': 15.5} 
# El set comprueba si existe un elemento; el dict asocia una clave a un valor.

# tuple: colección de datos inmutables y ordenados (se usan paréntesis (...)).
mi_tupla = ('Hola', 20, 15.5) 

# list: colección de datos ordenados y mutables (se usan corchetes [...]).
mi_lista = ['Hola', 20, 15.5]

# range: genera una secuencia inmutable de números.
rango = range(5)
print(rango) # Imprime: range(0, 5)

# Convertir una secuencia a lista con la función list():
secuencia = range(10)
print(list(secuencia)) # Imprime: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

# ==============================================
# CONCEPTO: FORMATEO DE NÚMEROS EN F-STRINGS
# ==============================================
# Las f-strings permiten controlar la presentación visual de un número sin alterar
# su valor numérico original ni su precisión en memoria.


# 1. ESPECIFICACIÓN DE FORMATO (.nf)
# Sintaxis: f"{valor:.2f}"
# - ':'  -> Introduce la especificación de formato.
# - '.2' -> Indica la cantidad exacta de decimales a mostrar (rellena con ceros o redondea).
# - 'f'  -> Representación de punto fijo (notación decimal estándar).

value = 12.5
print(f"{value:.2f}")  # 12.50 (rellena con cero)
print(value)           # 12.5  (el valor original no cambia)

value = 12.3456
print(f"{value:.2f}")  # 12.35 (redondea al mostrar)
print(value)           # 12.3456


# 2. TIPO DE DATO RESULTANTE
# Formatear con una f-string devuelve siempre una cadena (str), por lo que
# la variable original (int o float) sigue disponible para cálculos matemáticos.

display = f"{value:.2f}"
print(type(display))  # <class 'str'>
print(type(value))    # <class 'float'>


# 3. DIFERENCIA ENTRE F-STRING Y ROUND()
# - round(valor, n): Devuelve un número redondeado útil para cálculos posteriores,
#   pero omite ceros finales no significativos al imprimirse.
# - f"{valor:.nf}": Devuelve texto formateado garantizando la cantidad fija de decimales.

value = 12.5
rounded_value = round(value, 2)
formatted_value = f"{value:.2f}"

print(rounded_value)    # 12.5
print(formatted_value)  # 12.50


# 4. IMPRECISIÓN DE PUNTO FLOTANTE
# Permite ocultar los residuos de aproximación binaria de los floats al imprimir
# sin modificar el dato real almacenado.

total = 0.1 + 0.2
print(total)            # 0.30000000000000004
print(f"{total:.2f}")   # 0.30

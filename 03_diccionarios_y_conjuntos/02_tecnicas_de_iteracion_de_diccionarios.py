# ==============================================
# TÉCNICAS COMUNES DE ITERACIÓN DE DICCIONARIOS
# ==============================================

# Diccionario base para los ejemplos:
products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}


# 1. ITERAR SOBRE VALORES CON .VALUES()
# Recorre directamente los valores del diccionario:
for price in products.values():
    print(price)
# Imprime:
# 990
# 600
# 250
# 70


# 2. ITERAR SOBRE CLAVES CON .KEYS()
# Por defecto, iterar directamente sobre un diccionario o usar .keys() da el mismo resultado:
for product in products.keys():  # O simplemente: for product in products:
    print(product)
# Imprime:
# Laptop
# Smartphone
# Tablet
# Headphones


# 3. ITERAR SOBRE PARES CLAVE-VALOR CON .ITEMS()
# Retorna cada par empaquetado en una tupla (clave, valor):
for product in products.items():
    print(product)
# Imprime:
# ('Laptop', 990)
# ('Smartphone', 600)
# ('Tablet', 250)
# ('Headphones', 70)


# 4. DESEMPAQUETADO DE CLAVE Y VALOR
# Separa la clave y el valor en variables independientes dentro del bucle:
for product, price in products.items():
    print(product, price)
# Imprime:
# Laptop 990
# Smartphone 600
# Tablet 250
# Headphones 70


# 5. MODIFICAR VALORES DURANTE LA ITERACIÓN
# Para aplicar cambios al diccionario original, se reasignan las claves usando la sintaxis [clave]:
for product, price in products.items():
    products[product] = round(price * 0.8)  # Aplica un 20% de descuento

print(products)
# Imprime:
# {
#     'Laptop': 792, 
#     'Smartphone': 480, 
#     'Tablet': 200, 
#     'Headphones': 56
# }


# 6. ENUMERATE() CON DICCIONARIOS
# Mantiene un índice contador junto a las claves:
for index, product in enumerate(products):
    print(index, product)
# Imprime:
# 0 Laptop
# 1 Smartphone
# 2 Tablet
# 3 Headphones


# 7. ENUMERATE() CON .VALUES()
# Asocia un índice a cada valor del diccionario:
for index, price in enumerate(products.values()):
    print(index, price)
# Imprime:
# 0 792
# 1 480
# 2 200
# 3 56


# 8. ENUMERATE() CON .ITEMS() (DESEMPAQUETADO COMPLETO)
# Opción A: Desempaquetado simple (retorna tupla para el par clave-valor):
for index, product_item in enumerate(products.items()):
    print(index, product_item)
# Imprime: 0 ('Laptop', 792)

# Opción B: Desempaquetado anidado (separa índice, clave y valor individualmente):
for index, (product, price) in enumerate(products.items()):
    print(f'#{index + 1}: {product} costs ${price}')
# Imprime:
# #1: Laptop costs $792
# #2: Smartphone costs $480
# #3: Tablet costs $200
# #4: Headphones costs $56


# 9. PERSONALIZAR EL ÍNDICE INICIAL EN ENUMERATE()
# Se pasa el valor [start] como argumento (ej. start=1):
for index, (product, price) in enumerate(products.items(), start=1):
    print(index, product, price)
# Imprime:
# 1 Laptop 792
# 2 Smartphone 480
# 3 Tablet 200
# 4 Headphones 56

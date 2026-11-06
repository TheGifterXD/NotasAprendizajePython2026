# ==============================
# CONCEPTO: MÉTODOS ESPECIALES
# ==============================
# Conocidos también como métodos mágicos o métodos dunder.
# El programa los ejecuta internamente cuando una acción los requiere.

# 1. MÉTODOS ESPECIALES COMUNES
# 1.1. Operaciones aritméticas: __add__(), __sub__(), __mul__(), __truediv__()
# 1.2. Operaciones de cadenas: __str__(), __repr__()
# 1.3. Operaciones de comparación: __eq__(), __lt__(), __gt__()
# 1.4. Iteración: __iter__(), __next__()

# 2. ¿POR QUÉ SON NECESARIOS?
# Permiten que las clases personalizadas funcionen con funciones integradas de Python.

# Ejemplo SIN métodos:
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

book1 = Book("Build Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

try:
    print(len(book1))
except TypeError:
    print("TypeError: object of type 'Book' has no len()")

print(str(book1))      # <__main__.Book object>
print(book1 == book2)  # False


# Ejemplo CON métodos:
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book("Build Wealth Like a Boss", 420)
book2 = Book("Be Your Own Start", 420)

print(len(book1))      # 420
print(len(book2))      # 420
print(str(book1))      # 'Build Wealth Like a Boss' has 420 pages
print(str(book2))      # 'Be Your Own Start' has 420 pages
print(book1 == book2)  # True

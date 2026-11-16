# =================================
# CONCEPTO: GETTERS Y SETTERS
# =================================
# Son métodos que permiten controlar cómo se acceden y modifican
# los atributos de una clase.
# - Getters: Recuperan o leen valores.
# - Setters: Establecen o modifican valores (con validaciones opcionales).

# 1. PROPIEDADES
# Conectan los getters con los setters para dar acceso controlado a los datos:
# - Actúan como atributos pero se comportan como métodos.
# - Se llaman mediante la notación de punto (ej. objeto.propiedad).
# - Ejecutan lógica adicional al obtener, establecer o eliminar valores.


# 2. DECORADOR @PROPERTY
# Modifica la funcionalidad de una función para convertirla en una propiedad.

# 2.1. GETTER
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Getter para obtener el radio."""
        return self._radius
  
    @property
    def area(self):
        """Getter calculado dinámicamente."""
        return 3.14 * (self._radius ** 2)

my_circle = Circle(3)
print(my_circle.radius)  # 3
print(my_circle.area)    # 28.26

# NOTA: _radius se usa con guion bajo por convención como atributo de uso interno.


# 2.2. SETTER
# Sintaxis: @<property_name>.setter
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Llama al setter automáticamente al instanciar

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value  # Se asigna a _radius para evitar recursión infinita

my_circle = Circle(3)
print('Initial radius:', my_circle.radius)  # Initial radius: 3

my_circle.radius = 8
print('After modifying:', my_circle.radius)  # After modifying: 8


# 3. LLAMAR GETTERS Y SETTERS
# Python los invoca automáticamente al usar la sintaxis de atributos:
# my_circle.radius      -> Llama al getter
# my_circle.radius = 4  -> Llama al setter
#
# IMPORTANTE: Dentro del setter no es recomendable usar self.radius = value, 
# ya que se llamaría a sí mismo infinitamente provocando un RecursionError.
# Siempre se debe usar la variable interna con guion bajo: self._radius = value.


# 4. DELETER
# Sintaxis: @<property_name>.deleter
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius

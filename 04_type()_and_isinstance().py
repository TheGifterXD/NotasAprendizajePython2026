# =====================================
# CONCEPTO: TYPE() E ISINSTANCE()
# =====================================

# type() es una función que indica qué tipo de dato contiene una variable:
developer = 'Devin'
print(type(developer)) # Imprime: <class 'str'>
# Los símbolos <...> indican que es una representación interna de clase de Python.

# type() muestra el nombre abreviado de cada tipo de dato:
  # entero = int
  # float = float
  # string = str
  # boolean = bool
  # set = set
  # dictionary = dict
  # tuple = tuple
  # range = range
  # list = list
  # none = NoneType

# None es un valor especial que denota la ausencia de valor (sirve para dejar una variable "vacía").

# isinstance() comprueba si una variable pertenece a un tipo de dato específico (devuelve True o False):
account_balance = "12"
# account_balance / 2  # Produce un TypeError (no se puede dividir un string entre un entero).

print(isinstance(account_balance, int)) # Imprime: False (porque "12" es un string).

account_balance = 12
print(isinstance(account_balance, int)) # Imprime: True (porque ahora 12 sí es un integer).

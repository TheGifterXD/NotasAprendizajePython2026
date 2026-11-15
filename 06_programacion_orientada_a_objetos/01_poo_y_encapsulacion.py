# ============================================================
# CONCEPTO: PROGRAMACIÓN ORIENTADA A OBJETOS Y ENCAPSULACIÓN
# ============================================================
# La POO es un paradigma de programación basado en el concepto de "objetos".
# Sus 4 principios clave son: Encapsulación, Herencia, Polimorfismo y Abstracción.

# 1. ENCAPSULACIÓN
# Es la agrupación de atributos y métodos dentro de una clase,
# ocultando el estado interno y permitiendo la interacción controlada.


# 2. PREFIJO DE GUIÓN BAJO SIMPLE (_)
# Sirve como convención para indicar que un atributo o método es de uso interno.
class Wallet:
    def __init__(self, balance):
        self._balance = balance  # Uso interno por convención

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

# NOTA: Aunque Python permite acceder a _balance desde fuera, se considera una
# mala práctica ya que rompe el principio de encapsulación.


# 3. PREFIJO DE DOBLE GUIÓN BAJO (__)
# Activa el "name mangling": Python renombra internamente el atributo
# para evitar colisiones en subclases (ej. __balance -> _Wallet__balance).
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acct_one = Wallet(100)
acct_one.deposit(50)
print(acct_one.get_balance())  # 150

acct_two = Wallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance())  # 422


# 4. MÉTODOS PRIVADOS
# Los métodos también pueden llevar '__' para ser utilizados
# exclusivamente de forma interna por otros métodos de la clase.
class Wallet:
    def __init__(self):
        self.__balance = 0

    def __validate(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be positive')

    def deposit(self, amount):
        self.__validate(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.__validate(amount)
        if amount > self.__balance:
            raise ValueError('Insufficient funds')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

acct_one = Wallet()
acct_one.deposit(50)
print(acct_one.get_balance())  # 50

# acct_one.deposit(-4)  # ValueError: Amount must be positive

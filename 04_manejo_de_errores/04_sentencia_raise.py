# ===========================
# CONCEPTO: SENTENCIA RAISE
# ===========================
# Permite activar manualmente excepciones en el código,
# crear condiciones de error personalizadas y hacer cumplir comportamientos.

# 1. USO BÁSICO DE RAISE
# Permite lanzar una excepción predefinida cuando se cumple una condición no deseada:
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error capturado: {e}')
# Imprime: Error capturado: Age cannot be negative


# 1.1 RE-LANZAR EXCEPCIONES (Re-raising)
# Útil para registrar (loggear) un error localmente antes de propagarlo:
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print('Logging interno: Invalid data received')
        raise  # Vuelve a lanzar exactamente el mismo ValueError hacia arriba

try:
    process_data('abc')
except ValueError:
    print('Excepción manejada a un nivel superior del programa')
# Imprime:
# Logging interno: Invalid data received
# Excepción manejada a un nivel superior del programa


# 2. EXCEPCIONES PERSONALIZADAS
# Se pueden crear excepciones propias heredando de la clase base Exception:
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f'Insufficient funds: ${balance} available, ${amount} requested')

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(f'Transaction failed -> {e}')
# Imprime: Transaction failed -> Insufficient funds: $100 available, $150 requested


# 3. ENCADENAMIENTO DE EXCEPCIONES (RAISE ... FROM)
# Permite controlar cómo se muestran los rastreos (tracebacks) al relacionar errores:
def parse_config(content):
    try:
        # Simulamos un error interno de conversión
        return int(content)
    except ValueError as e:
        # 'from e' vincula explícitamente ambas excepciones en el reporte de error
        raise ValueError('Invalid configuration format') from e

try:
    parse_config('abc')
except ValueError as err:
    print(f'Error de configuración detectado: {err}')
# Imprime: Error de configuración detectado: Invalid configuration format

# Nota sobre modificadores:
# - raise ... from e  -> Muestra la causa raíz y el error nuevo en el Traceback.
# - raise ... from None -> Suprime la excepción original por completo en el Traceback.


# 4. ASSERT (ASERCIONES)
# Es una forma abreviada de lanzar un AssertionError si una condición es falsa.
# Se utiliza principalmente para depuración y validación interna de supuestos lógicos.
def calculate_square_root(number):
    assert number >= 0, 'Cannot calculate square root of negative number'
    return number ** 0.5

try:
    result = calculate_square_root(-4)
except AssertionError as e:
    print(f'Assertion failed: {e}')
# Imprime: Assertion failed: Cannot calculate square root of negative number

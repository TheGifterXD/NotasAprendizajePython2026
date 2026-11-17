# =========================
# CONCEPTO: POLIMORFISMO
# =========================
# Permite que métodos de diferentes clases compartan el mismo nombre
# y se comporten de manera distinta según el objeto que los invoque.

# Estructura básica:
class A:
    def action(self): ...

class B:
    def action(self): ...

class C:
    def action(self): ...

A().action()
B().action()
C().action()

# Ejemplo práctico (sin herencia / Duck Typing):
class Twitter:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"🐦 Tweet: '{self.content}' (280 chars max)"

class Instagram:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"📸 Instagram Post: '{self.content}' + ✨ filters"

class LinkedIn:
    def __init__(self, content):
        self.content = content

    def post(self):
        return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

def start(social_media):
    print(social_media.post())  # Llama a .post() en cualquier objeto compatible

# Instancias
tweet = Twitter('Just learned Python polymorphism!')
photo = Instagram('Sunset vibes 🌅')
article = LinkedIn('Why OOP matters in 2024')

# Llamadas polimórficas: misma función, diferentes salidas
start(tweet)    # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
start(photo)    # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
start(article)  # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)


# 1. POLIMORFISMO BASADO EN HERENCIA
# Una clase base define un método y las subclases lo sobrescriben según sus necesidades.
class Animal:
    def speak(self):
        return 'Some generic sound'

class Cat(Animal):
    def speak(self):
        return 'A cat meows'

class Dog(Animal):
    def speak(self):
        return 'A dog barks woof woof'

class Monkey(Animal):
    def speak(self):
        return 'A monkey ooh ooh aah aah ooh ooh aah aah'

print(Cat().speak())     # A cat meows
print(Dog().speak())     # A dog barks woof woof
print(Monkey().speak())  # A monkey ooh ooh aah aah ooh ooh aah aah
print(Animal().speak())  # Some generic sound

#1. Создать класс **`IdCounter`** (в котором хранятся генератор значений id (обычный инкремент на 1))
    #* в нем должен быть реализован простой интерфейс хранения значения и получения нового значения
class IdCounter:
    def __init__(self):
        self.counter = 0

    def get_id(self):
        self.counter += 1
        return self.counter

#2 Создать класс **`Password`** (который ответственен за выдачу хэш-значения пароля и проверке пароля с его хэш значением)
#* реализовать методы `get` и `check`
#* `get` - выдаёт хэш-значение. Можно возпользоваться модулем [hashlib](https://docs.python.org/3/library/hashlib.html#hash-algorithms).
#Как пример и для упрощения предлагаю воспользоваться данным выражением `hashlib.sha256(password.encode()).hexdigest()`, которое вернёт хэш-значение по переданной строке `password`.
#Однако вы сами вольны выбирать каким методом и как возвращать хэш-значение.
#* Для передаваемого пароля перед получением хэш-значения должны быть произведены проверки, что пароль строкового типа и пароль соответствует минимальным правилам (проверить можно как при помощи re, так и обычных строковых методов) пароля:
#* Длина не менее 8 символов
#* В пароле есть как цифры так и буквы
#* `check` - проверяет соотносится ли передаваемый пароль с его хэш-значением

import hashlib
import re

class Password:
    def __init__(self, password):
        if isinstance(password, str):
            if re.search("[a-zA-Z]+", password) and re.search("[0-9]+", password) and len(password) >= 8:
                self.password = password
                self.hashed_password = self.get()
            else:
                raise ValueError("Пароль содержит буквы и цифры должен содерджать хотя бы 8 символов")
        else:
            raise TypeError("Пароль должен быть строкой")

    def get(self):
        return hashlib.sha256(self.password.encode()).hexdigest()

    def check(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.hashed_password


#3 Создать класс **`Product`** (в котором хранится информация о продукте)
#* в классе должны быть атрибуты (`id`, `name`, `price`, `rating`)
#* `id` **не должен** передаваться как входной аргумент. При инициализации он должен сам определяться.
#* `id` и `name` не должны иметь возможность измениться из вне
#* `price`, `rating` могут меняться из вне (можно сделать как свойствами, так и обычными методами, на ваше усмотрение)
#* для тех атрибутов, которым это необходимо проведите проверку корректности значений при инициализации, если проверка не пройдена вызываем `raise ValueError`
#* для атрибутов, необходимо провести проверку типов, если проверка не пройдена вызываем `raise TypeError`
#* среди открытых методов не должно быть методов, которые явно позволяют изменять атрибуты
#(т.е. если у вас есть защищенный атрибут и вы не хотите, чтобы пользователь его менял, то сделайте защищенный метод, который будете вызывать вы как разработчик)
#* реализуйте \_\_str__ и \_\_repr__ методы. В \_\_str__ вывести строку вида {id}_{name}
class Product:
    _next_id = 1

    def __init__(self, name, price, rating):
        self._id = Product._next_id
        Product._next_id += 1

        if not isinstance(name, str):
            raise TypeError("Name строка")
        self._name = name

        if not isinstance(price, float) and not isinstance(price, int):
            raise TypeError("Price float or an integer")
        if price <= 0:
            raise ValueError("Price положительное значение")
        self._price = float(price)

        if not isinstance(rating, float) and not isinstance(rating, int):
            raise TypeError("Rating float or an integer")
        if rating < 0 or rating > 5:
            raise ValueError("Rating в диапанозоне [0, 5]")
        self._rating = float(rating)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Price float or an integer")
        if value <= 0:
            raise ValueError("Price положительное значение")
        self._price = float(value)

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Rating float or an integer")
        if value < 0 or value > 5:
            raise ValueError("Rating в диапазоне [0, 5]")
        self._rating = float(value)

    def __str__(self):
        return f"{self._id}_{self._name}"

    def __repr__(self):
        return f"Product(id={self._id}, name='{self._name}', price={self._price}, rating={self._rating})"

#4 Создать класс **`Cart`** (корзина в котором хранится информация о списке товаров)
#* должны быть методы добавления и удаления товара из корзины
class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("The argument should be an instance of the Product class.")
        self.products.append(product)

    def remove_product(self, product):
        if product not in self.products:
            raise ValueError("Product удален.")
        self.products.remove(product)

#5. Создать класс **`User`** (в котором хранится информация о пользователе)
   #* в классе должны быть атрибуты (id, username, password)
   #* id **не должен** передаваться как входной аргумент. При инициализации он должен сам определяться.
   #* при инициализации пользователя должна создаваться корзина для этого пользователя, но изменить её из вне не должно получаться, она доступна только для чтения (возвращения объекта корзины)
   #* атрибут username можно задать при инициализации, но возможность его изменить должна отсутствовать
   #* атрибут password должен храниться в хэш-значение пароля и должен быть закрытым. Хранение пароля в открытом виде **запрещено**
   #* должны быть реализованы проверки при инициализации для атрибута username
   #* реализуйте \_\_str__ и \_\_repr__ методы. Однако теперь реальный password не должен выводится на экран, вместо него поставим заглушку `'password1'`.
import hashlib


class User:
    next_id = 1

    def __init__(self, username, password):
        self.id = User.next_id
        User.next_id += 1
        self._username = username
        self.__password = hashlib.sha256(password.encode()).hexdigest()
        self._cart = []

    @property
    def username(self):
        return self._username

    @property
    def cart(self):
        return self._cart

    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', password='password1')"

    def __repr__(self):
        return self.__str__()

#№8. Создайте генераторы для создания продуктов (выбрал стойматериалы). Постарайтесь чтобы генератор выдавал хотя бы приближенные значения с реальностью.
#Можете использовать как стронние библиотеки, так и просто брать случайное значение из сформированного вами списка.
#Значения цены и рейтинга округлите до 2-ух знаков.

import random
import names
import string

class BuildingMaterial:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.rating:.2f} stars)"

    def __repr__(self):
        return f"BuildingMaterial({self.name!r}, {self.price!r}, {self.rating!r})"

def generate_building_materials(n=10):
    product_names = [''.join(random.choices(string.ascii_uppercase + string.digits, k=6)) for i in range(n)]
    for name in product_names:
        price = round(random.uniform(10, 100), 2)
        rating = round(random.uniform(0, 5), 2)
        yield BuildingMaterial(name, price, rating)

building_materials = list(generate_building_materials(20))
print(building_materials)

#9. Создайте класс `Store`.
   #* Реализуйте в нём аутентификацию (упростим задачу, чтобы не хранить список пользователей, под аутентификацией будем понимать создание пользователя) пользователя через консоль(логин и пароль будут вводиться через консоль)
   #* Реализуйте метод позволяющий пользователю добавить случайный продукт в корзину
   #* Реализуйте метод позволяющий пользователю просмотреть свою корзину
import random

class Store:
    def __init__(self):
        self.products = []
        self.cart = []

    def authenticate(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("User authenticated.")
        return username, password

    def add_product(self):
        product = random.choice(self.products)
        self.cart.append(product)
        print("Product added to the cart.")

    def view_cart(self):
        print("Products in the cart:")
        for i, product in enumerate(self.cart):
            print(f"{i+1}. {product}")

store = Store()
store.products = [("Cement", 20.0), ("Bricks", 30.0), ("Sand", 10.0), ("Iron Rods", 50.0), ("Doors", 40.0)]

username, password = store.authenticate()
store.add_product()
store.view_cart()

#10. В блоке `if __name__ == '__main__'` проверьте функциональность добавления продуктов в корзину и отображения корзины пользователя.
if __name__ == '__main__':
    store = Store()
    store.authenticate()
    store.add_product_to_cart()
    store.view_cart()
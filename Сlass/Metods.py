class MyClass:
    def method(self):
        return 'вызван метод экземпляра', self

    @classmethod
    def classmethod(cls):
        return 'вызван метод класса', cls

    @staticmethod
    def staticmethod():
        return 'вызван статический метод'


obj = MyClass()

print(obj.method())

print(MyClass.method(obj))

print(MyClass.classmethod())

print(MyClass.staticmethod())

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['моцарелла', 'помидоры'])

    @classmethod
    def prosciutto(cls):
        return cls(['моцарелла', 'помидоры', 'ветчина'])

Pizza   (['сыр', 'помидоры'])
Pizza(['сыр', 'помидоры'])

import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r},'
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


"""
>>> from collections import namedtuple
>>> from sys import getsizeof
>>> p1 = namedtuple('Point', 'x y z')(1, 2, 3)
>>> p2 = (1, 2, 3)
>>> getsizeof(p1)
64
>>> getsizeof(p2)
64
"""
"""
typing.NamedTuple — усовершенствованные именованные кортежи
>>> from typing import NamedTuple
class Car(NamedTuple):
    цвет: str
    пробег: float
    автомат: bool
>>> car1 = Car('красный', 3812.4, True)
# Экземпляры имеют хороший метод repr:
>>> car1 Car(цвет='красный', пробег=3812.4, автомат=True)
# Доступ к полям:
>>> car1.пробег 3812.4
# Поля неизменяемы:
>>> car1.пробег = 12
AttributeError: "can't set attribute"
>>> car1.лобовое_стекло = 'треснутое'
AttributeError:
"'Car' object has no attribute 'лобовое_стекло'"
# Аннотации типа не поддерживаются без отдельного
# инструмента проверки типов, такого как mypy:
>>> Car('красный', 'НЕВЕЩЕСТВЕННЫЙ', 99)
Car(цвет='красный', пробег='НЕВЕЩЕСТВЕННЫЙ', автомат=99)
"""
"""
struct.Struct — сериализованные С-структуры
>>> from struct import Struct
>>> MyStruct = Struct('i?f')
>>> data = MyStruct.pack(23, False, 42.0)
# Вы получаете двоичный объект данных (blob):
>>> data
b'x17x00x00x00x00x00x00x00x00x00(B'
# BLOB-объекты можно снова распаковать:
>>> MyStruct.unpack(data)
(23, False, 42.0)
"""
"""
types.SimpleNamespace — причудливый атрибутивный доступ

>>> from types import SimpleNamespace
>>> car1 = SimpleNamespace(цвет='красный',
пробег=3812.4,
автомат=True)
# Метод repr по умолчанию:
>>> car1
namespace(автомат=True, пробег=3812.4, цвет='красный')
# Экземпляры поддерживают атрибутивный доступ и могут изменяться:
>>> car1.пробег = 12
>>> car1.лобовое_стекло = 'треснутое'
>>> del car1.автомат
>>> car1
namespace(лобовое_стекло='треснутое', пробег=12, цвет='красный')
"""
"""
У вас есть всего несколько (2–3) полей: использование обыкновенного объекта-кортежа может подойти, если порядок следования полей легко запоминается или имена полей излишни. Например, представьте точку (x, y, z) в трехмерном пространстве.
Вам нужны неизменяемые поля: в данном случае обыкновенные кортежи, collections.namedtuple и typing.NamedTuple, дадут неплохие возможности для реализации этого типа объекта данных.
Вам нужно устранить имена полей, чтобы избежать опечаток: вашими друзьями здесь будут collections.namedtuple и typing.NamedTuple.
Вы не хотите усложнять: обыкновенный объект-словарь может быть хорошим вариантом из-за удобного синтаксиса, который сильно напоминает JSON.
Вам нужен полный контроль над вашей структурой данных: самое время написать собственный класс с методами-модификаторами (сеттерами) и методами-получателями (геттерами) @property.
Вам нужно добавить в объект поведение (методы): вам следует написать собственный класс с нуля либо путем расширения collections.namedtuple или typing.NamedTuple.
Вам нужно плотно упаковать данные, чтобы сериализовать их для записи на жесткий диск или отправить их по Сети: самое время навести справки по поводу struct.Struct, потому что этот объект представляет собой превосходный вариант использования.

"""
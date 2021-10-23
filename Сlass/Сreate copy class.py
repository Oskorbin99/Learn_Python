# Shallow copy  -- означает конструирование нового объекта-коллекции
# и затем его заполнение ссылками на дочерние объекты, найденные в оригинале.

# Deep copy -- выполняет процесс копирования рекурсивно.
# Это означает конструирование сначала нового объекта коллекции,
# а затем рекурсивное его заполнение копиями дочерних объектов, найденных в оригинале.

# Shallow copy
print('Shallow copy')
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs) # Сделать мелкую копию

xs.append(['новый подсписок'])

print(xs)

print(ys)

xs[1][0] = 'X'

print(xs)

print(ys)


# Deep copy
print('Deep copy')
import copy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

xs.append(['новый подсписок'])

print(xs)

print(zs)

xs[1][0] = 'X'

print(xs)

print(zs)

# For class


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


a = Point(23, 42)
b = copy.copy(a)

print(f'{a}, {b}, {a is b}')


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r},'
            f'{self.bottomright!r})')


a = Rectangle(Point(0, 1), Point(5, 6))
b = copy.copy(a)

print(f'{a}, {b}, {a is b}')

a.topleft.x = 999

print(f'{a}\n{b}')

drect = copy.deepcopy(a)

drect.topleft.x = 222

print(f'{a}\n{drect}')

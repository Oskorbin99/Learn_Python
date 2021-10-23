from collections import namedtuple

# First element is name namedtuple and all.
Car = namedtuple('Авто', 'цвет пробег')

my_car = Car('красный', 3812.4)

print(my_car.пробег)

color, mileage = my_car

print(color, mileage)

print(*my_car)

# is not good
Car = namedtuple('Авто', 'цвет пробег')


class MyCarWithMethods(Car):

    def hexcolor(self):
        if self.цвет == 'красный':
            return '#ff0000'
        else:
            return '#000000'


c = MyCarWithMethods('красный', 1234)


print(c.hexcolor())

Car = namedtuple('Авто', 'цвет пробег')
ElectricCar = namedtuple(
                'ЭлектрическоеАвто', Car._fields + ('заряд',))

# this is vocabulary!
print(my_car._asdict())
# for copy tuple but you can change value
print(my_car._replace())
# Наконец, метод класса _make()
# может использоваться для создания новых экземпляров класса namedtuple из (итерируемой) последовательности:
print(my_car._make(['красный', 999]))


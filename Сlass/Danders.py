class Car:
    def __init__(self, name):
        self.name_car = name

    def __str__(self):
        return self.name_car + ' str'

    def __repr__(self):
        return self.name_car + ' repr'

my_car = Car("Mersedes")

print(my_car)

my_car
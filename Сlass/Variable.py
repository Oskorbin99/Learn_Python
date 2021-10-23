class Dog:
    num_legs = 4 # <- Переменная класса

    def __init__(self, name):
        self.name = name # <- Переменная экземпляра


jack = Dog('Джек')
jill = Dog('Джилл')

print(jack.name, jill.name)
print(jack.num_legs, jill.num_legs)
Dog.num_legs = 3
print(jack.num_legs, jill.num_legs)


# True way edit class variables
class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances += 1
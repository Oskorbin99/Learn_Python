from random import randrange
# Simple decorator


def pidor_decorator(func):
    def wrapper():
        if randrange(2) == 1:
            zrada = func() + " You is pidor!"
        else:
            zrada = func() + " Very cool! You is idiot!"
        return zrada
    return wrapper


@pidor_decorator
def greet():
    return 'Hello!'


print(greet())

# Multi use decorators


def zrada(func):
    def wrapper():
        return func() + ' Zrada'
    return wrapper


def peremoga(func):
    def wrapper():
        return 'Peremoga ' + func()
    return wrapper


@zrada
@peremoga
def dzen():
    return 'is'


print(dzen())

# Decorator with arguments


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
            f'с {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() '
            f'вернула {original_result!r}')
        return original_result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('zrada', 'peremoga'))


# functools is .... можно использовать в своих собственных декораторах для того, чтобы копировать потерянные
# метаданные из недекорированной функции в замыкание декоратора.
import functools


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet_functools():
    return 'Hello!'


# decorator from first chapter file "Decorator"
print(greet.__name__ )

print(greet_functools.__name__)
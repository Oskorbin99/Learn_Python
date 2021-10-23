# Simple lambda-functions
# add = lambda x, y: print(x+y)
# add(5, 4)


# But it is not good because do not assign a lambda expression, use a def
def add_def(x, y): print(x+y)


add_def(5, 4)
# Use lambda for sort
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))
print(sorted(range(-5, 6), key=lambda x: x * x))


# Use lambda for lexical closures
def make_adder(n): return lambda x: x+n


plus_3 = make_adder(3)
print(plus_3(4))
print(make_adder(3)(4))

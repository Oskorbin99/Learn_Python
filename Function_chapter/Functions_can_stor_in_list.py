def yell(text):
    return text.upper() + '!'


bark = yell

# Functions can be stored in list
funcs = [bark, str.lower, str.capitalize]

print(funcs)

for funcs_value in funcs:
    print(funcs_value, funcs_value('All Hi'))

print(funcs[0]("zrada"))

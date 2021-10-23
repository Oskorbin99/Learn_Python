def yell(text):
    return print(text.upper() + '!')


# Function - is object
bark = yell

bark("Gav")

# Delete function yell
del yell

# If call yell -- Error
try:
    yell("hmm")
except NameError:
    print("yell is not exist")

# But is call bark -- Ok

bark(f"Gav. Funk name is {bark.__name__}")

from string import Template

a = "Zrada"
b = "Peremoga"

# Classical format
print("Classical -- %s is %s" % (a, b))

# Modern format
print("Modern -- {} is {}".format(a, b))

# String interpolation Format
print(f"Interpolation -- {a} is {b}")

# Sample format -- for user input data because it is safe
f = Template("Sample -- $a is $b")
print(f.substitute(a=a, b=b))

# hz Format
print("hz -- " + a + " is " + b)

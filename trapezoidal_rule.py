import math

def f(x):
    return math.sqrt(1 + x)

a = 0
b = 1
h = 1/3

integral = (f(a) + f(b)) / 2
for i in range(1, int((b - a) / h)):
    integral += f(a + i * h)
integral *= h

print("Wartość całki:", integral)


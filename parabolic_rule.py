import math

def f(x):
    return math.sin(x) * math.exp(-3 * x) + x**3

a = -3
b = 1
n = 1000  # liczba podprzedziałów

h = (b - a) / n
integral = f(a) + f(b)
for i in range(1, n):
    xi = a + i * h
    if i % 2 == 0:
        integral += 2 * f(xi)
    else:
        integral += 4 * f(xi)
integral *= h / 3

print("Wartość całki:", integral)

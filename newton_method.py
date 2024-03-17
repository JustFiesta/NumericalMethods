# ex4

import math

def f(x):
    return math.sin(x) - 1 / (2 * x)

def f_prime(x):
    return math.cos(x) + 1 / (2 * x**2)

def newton_method(f, f_prime, x0, tolerance, max_iterations=1000):
    iterations = 0
    while True:
        x1 = x0 - f(x0) / f_prime(x0)
        iterations += 1
        if abs(x1 - x0) < tolerance or iterations >= max_iterations:
            break
        x0 = x1
    return x1, iterations

x0 = math.pi / 2
tolerance = 0.01

root, iterations = newton_method(f, f_prime, x0, tolerance)

print("Pierwiastek równania:", root)
print("Liczba iteracji:", iterations)

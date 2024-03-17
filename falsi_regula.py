# ex 6

import math

def f(x):
    return 3 * x - math.cos(x) - 1

def regula_falsi(f, a, b, tolerance, max_iterations=1000):
    if f(a) * f(b) >= 0:
        print("Nie można zagwarantować istnienia pierwiastka w zadanym przedziale.")
        return None
    iterations = 0
    while True:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tolerance or iterations >= max_iterations:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return c, iterations

a = 0.25
b = 0.75
tolerance = 0.00001

root, iterations = regula_falsi(f, a, b, tolerance)

print("Pierwiastek równania:", root)
print("Liczba iteracji:", iterations)

# ex 5

def f(x):
    return x**3 + x**2 - 3*x - 3

def secant_method(f, x0, x1, tolerance, max_iterations=1000):
    iterations = 0
    while True:
        if abs(f(x1) - f(x0)) < tolerance or iterations >= max_iterations:
            break
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
        iterations += 1
    return x2, iterations

x0 = 1
x1 = 2
tolerance = 0.0001

root, iterations = secant_method(f, x0, x1, tolerance)

print("Pierwiastek równania:", root)
print("Liczba iteracji:", iterations)

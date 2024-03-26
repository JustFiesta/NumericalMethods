a = 1
b = 4
n = 1000  # liczba podprzedziałów

integral = 0
h = (b - a) / n
for i in range(n):
    x = a + i * h
    integral += 0.06 * x**2 + 2
integral *= h

print("Wartość całki:", integral)

"""
Número de Fibonacci:
Pide al usuario un número entero positivo 'n'. Calcula el enésimo número de Fibonacci 
utilizando un bucle for
"""

n = int(input("Ingresa un número entero positivo: "))

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print(f"El número Fibonacci en la posición {n} es: {a}")

"""
Conjetura de Collatz:
Pide al usuario un número entero positivo. Aplica la conjetura de Collatz: si el número es par,
divídelo por 2; si es impar, multiplícalo por 3 y suma 1. Repite el proceso hasta que el número
llegue a 1. Utiliza un bucle while e imprime la secuencia de números generada
"""
n = int(input("Ingresa un número entero positivo: "))

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

print(1)


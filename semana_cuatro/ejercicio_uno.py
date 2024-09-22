"""
Suma de Números Pares:
Pide al usuario un número entero positivo 'n'. Calcula la suma de todos los números pares desde
2 hasta 'n' (inclusive) utilizando un bucle while
"""

n = int(input("Ingresa un número entero positivo: "))
suma_pares = 0
i = 2

while i <= n:
    if i % 2 == 0:
        suma_pares += i
    i += 1

print(f"La suma de todos los números pares hasta {n} es: {suma_pares}")

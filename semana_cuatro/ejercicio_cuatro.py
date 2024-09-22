"""
Imprimir Patrón de Triángulo:
Pide al usuario un número entero positivo 'n'. Imprime un triángulo de asteriscos con 'n' filas
utilizando un bucle for anidado
"""

n = int(input("Ingresa un número entero positivo: "))

for i in range(1, n + 1):
    print("*" * i)


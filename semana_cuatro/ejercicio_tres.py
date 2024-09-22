"""
Tabla de Multiplicar con for:
Pide al usuario un número entero positivo. Imprime la tabla de multiplicar de ese número 
utilizando un bucle for.
"""

n = int(input("Ingresa un número entero positivo: "))

print(f"Tabla de multiplicar del {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

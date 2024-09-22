"""
Escribe un script en Python que muestre la siguiente tabla
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

# Solución
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

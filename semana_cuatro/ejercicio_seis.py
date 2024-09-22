"""
Suma de Dígitos:
Pide al usuario un número entero positivo. Calcula la suma de sus dígitos utilizando un bucle 
while
"""

n = int(input("Ingresa un número entero positivo: "))
suma_digitos = 0

while n > 0:
    suma_digitos += n % 10
    n = n // 10

print(f"La suma de los dígitos es: {suma_digitos}")

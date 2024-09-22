"""
¿Par o Impar?
Pide al usuario un número entero y utiliza una estructura if...else para determinar si es par o
impar. Imprime el resultado
"""

numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")
"""
Número Positivo, Negativo o Cero:
Pide al usuario un número y utiliza una estructura if...elif...else para determinar si es positivo,
negativo o cero
"""

numero = float(input("Introduce un número: "))

if numero > 0:
    print("El número", numero, "es positivo.")
elif numero < 0:
    print("El número", numero, "es negativo.")
else:
    print("El número es cero.")
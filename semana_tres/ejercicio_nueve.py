"""
Año Bisiesto:
Pide al usuario un año y utiliza una estructura if...elif...else para determinar si es bisiesto. Un año
es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400.
"""

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año", año, "es bisiesto.")
else:
    print("El año", año,  "no es bisiesto.")
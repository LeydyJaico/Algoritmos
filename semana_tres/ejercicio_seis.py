"""
Mayor de Tres:
Pide al usuario tres números y utiliza estructuras if...elif...else anidadas para determinar cuál es
el mayor.
"""

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

if num1 >= num2:
    if num1 >= num3:
        print("El mayor es:", num1)
    else:
        print("El mayor es:", num3)
else:
    if num2 >= num3:
        print("El mayor es:", num2)
    else:
        print("El mayor es:", num3)

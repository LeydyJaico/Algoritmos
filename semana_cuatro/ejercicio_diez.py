"""
Calculadora de Promedio:
Pide al usuario una serie de números separados por comas. Calcula el promedio de esos 
números utilizando un bucle for
"""

numeros = input("Ingresa una serie de números separados por comas: ").split(',')
suma = 0

for numero in numeros:
    suma += float(numero)

promedio = suma / len(numeros)
print(f"El promedio de los números ingresados es: {promedio}")


#EJERCICIO_4
"""
El radio de un círculo es de 30 metros.
▪ Calcula el área de un círculo y asigna el valor a una variable llamada area_of_circle
▪ Calcula la circunferencia de un círculo y asigna el valor a una variable llamada
circum_of_circle
▪ Tome el radio como entrada del usuario y calcule el área.
"""
import math as M
radio= 30
#calculamos area
area_of_circle=M.pi*(radio**2)
print("El área es:", area_of_circle)
#calculamos circuferencia
circum_of_circle= 2 * M.pi * radio
print("La circuferencia es:", circum_of_circle)
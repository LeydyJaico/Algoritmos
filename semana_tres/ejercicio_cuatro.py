"""
Calculadora Simple:
Escribe un programa que realice operaciones aritméticas básicas (suma, resta, multiplicación,
división) con dos números ingresados por el usuario
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == '+':
    resultado = num1 + num2
elif operacion == '-':
    resultado = num1 - num2
elif operacion == '*':
    resultado = num1 * num2
elif operacion == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operación no válida."

print("El resultado es:", resultado)
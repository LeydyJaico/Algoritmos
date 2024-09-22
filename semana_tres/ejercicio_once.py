"""
Calculadora de IMC:
Pide al usuario su peso en kilogramos y su altura en metros. Calcula su índice de masa corporal
(IMC = peso / altura^2) y utiliza una estructura if...elif...else para determinar su categoría (bajo
peso, normal, sobrepeso, obesidad).
"""

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "bajo peso"
elif 18.5 <= imc < 24.9:
    categoria = "normal"
elif 25 <= imc < 29.9:
    categoria = "sobrepeso"
else:
    categoria = "obesidad"

print(f"Tu IMC es {imc:.2f}, lo que indica {categoria}")





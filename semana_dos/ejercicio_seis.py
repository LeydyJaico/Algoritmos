"""
Escribe un script que solicite al usuario que introduzca las horas y la tarifa por hora. ¿Cuál es el
pago de la persona?
Introduce las horas: 40
Introduce la tarifa por hora: 28
Tu salario semanal es 1120
"""

horas = int(input("Introduce las horas: "))
tarifa = int(input("Introduce la tarifa por hora: "))
salario = horas * tarifa
print("Tu salario semanal es: ", salario)
"""
Calculadora de Descuento:
Pide al usuario el precio original de un producto y la categoría del descuento ("estudiante",
"jubilado", "empleado" u "otro"). Aplica un descuento del 10% para estudiantes, 15% para
jubilados, 5% para empleados y 0% para otros. Imprime el precio final
"""

precio = float(input("Ingresa el precio original del producto: "))
categoria = input("Ingresa la categoría (estudiante, jubilado, empleado, otro): ").lower()

if categoria == "estudiante":
    descuento = 0.10
elif categoria == "jubilado":
    descuento = 0.15
elif categoria == "empleado":
    descuento = 0.05
else:
    descuento = 0

precio_final = precio * (1 - descuento)
print("El precio final es:", precio_final)

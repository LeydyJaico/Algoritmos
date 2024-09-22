"""
Los números pares son divisibles por 2 y el residuo es cero. ¿Cómo comprobarías si un número es
par o no usando python?
"""

numero = int(input("Introduce un número: "))
es_par = numero % 2 == 0
print(es_par)
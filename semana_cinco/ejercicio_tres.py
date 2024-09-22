"""
Considera tres listas de números enteros, una con números del 1 al 10, otra con números del 5 al 
15, y la última con números del 10 al 20. (5ptos)
a. Convierte las listas en conjuntos.
b. Encuentra el conjunto de todos los números que están presentes en las tres listas.
c. Encuentra el conjunto de todos los números que están presentes en al menos una de las listas.
d. Encuentra el conjunto de todos los números que están presentes en la primera lista, pero no en 
la última.
e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
"""
# listas
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convierte las listas en conjuntos
set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

# b. Conjunto de todos los números presentes en las tres listas
conjunto_comun = set1.intersection(set2, set3)
print(f"Números comunes en las tres listas: {conjunto_comun}")

# c. Conjunto de todos los números presentes en al menos una de las listas
conjunto_union = set1.union(set2, set3)
print(f"Números presentes en al menos una lista: {conjunto_union}")

# d. Conjunto de números presentes en la primera lista pero no en la última
conjunto_diferencia = set1.difference(set3)
print(f"Números en la primera lista pero no en la última: {conjunto_diferencia}")

# e. Convierte los conjuntos obtenidos en tuplas y suma el primer y último elemento de cada tupla
tupla_comun = tuple(conjunto_comun)
tupla_union = tuple(conjunto_union)
tupla_diferencia = tuple(conjunto_diferencia)

if tupla_comun:
    suma_comun = tupla_comun[0] + tupla_comun[-1]
else:
    suma_comun = 0

suma_union = tupla_union[0] + tupla_union[-1]
suma_diferencia = tupla_diferencia[0] + tupla_diferencia[-1]

print(f"Suma de primer y último elemento (común): {suma_comun}")
print(f"Suma de primer y último elemento (unión): {suma_union}")
print(f"Suma de primer y último elemento (diferencia): {suma_diferencia}")

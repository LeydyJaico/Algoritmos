"""
Contar vocales: Escribe un programa que cuente el número de vocales en una cadena dada por
el usuario.
"""

cadena = input("Introduce una cadena: ")
vocales = 'aeiouAEIOU'
contador_vocales=0
for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

print(contador_vocales)



cadena = input("Introduce una cadena: ")
vocales = "aeiouAEIOU"
contador = sum(1 for letra in cadena if letra in vocales)
print("Número de vocales:", contador)


##OJOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
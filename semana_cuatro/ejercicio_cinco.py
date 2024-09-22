"""
Contar Vocales en una Frase:
Pide al usuario una frase y cuenta el número total de vocales (mayúsculas y minúsculas) 
utilizando un bucle for.

"""

frase = input("Ingresa una frase: ").lower()
vocales = "aeiou"
contador_vocales = 0

for letra in frase:
    if letra in vocales:
        contador_vocales += 1

print(f"El número total de vocales es: {contador_vocales}")

"""
Verificar si una Cadena es Palíndromo:
Pide al usuario una cadena y verifica si es un palíndromo (se lee igual de izquierda a derecha 
que de derecha a izquierda) utilizando un bucle for.

"""

cadena = input("Ingresa una cadena: ").lower().replace(" ", "")
es_palindromo = True

for i in range(len(cadena)):
    if cadena[i] != cadena[-(i+1)]:
        es_palindromo = False
        break

if es_palindromo:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")

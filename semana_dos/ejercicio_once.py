"""
Palíndromo: Escribe un programa que verifique si una cadena dada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
cadena = input("Introduce una cadena: ")
es_palindromo = cadena == cadena[::-1]
print(es_palindromo)





"""
Contar palabras: Escribe un programa que cuente el número de palabras en una cadena dada
por el usuario
"""
cadena = input("Introduce una cadena: ")
contador_palabras = len(cadena.split())
print("Número de palabras:", contador_palabras)

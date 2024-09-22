"""
Invertir una Cadena:
Pide al usuario una cadena e inviértela utilizando un bucle for.
"""
cadena = input("Ingresa una cadena: ")
cadena_invertida = ""

for letra in cadena:
    cadena_invertida = letra + cadena_invertida

print(f"La cadena invertida es: {cadena_invertida}")


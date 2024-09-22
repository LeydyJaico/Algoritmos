"""
Conversor de Unidades de Longitud:
Pide al usuario una longitud en metros y la unidad a la que desea convertir ("pies", "pulgadas"
o "yardas"). Realiza la conversión e imprime el resultado.

"""


#lower-----minúscula
longitud = float(input("Introduce una longitud en metros: "))
unidad = input("Introduce la unidad a la que deseas convertir (pies, pulgadas, yardas): ").lower()

if unidad == "pies":
    conversion = longitud * 3.28084
elif unidad == "pulgadas":
    conversion = longitud * 39.3701
elif unidad == "yardas":
    conversion = longitud * 1.09361
else:
    conversion = "Unidad no válida."

print(longitud,"metros son",conversion, unidad)
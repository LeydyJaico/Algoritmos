"""
Clasificación de Triángulos:
Escribe un programa que pida al usuario las longitudes de tres lados de un triángulo y
determine si es equilátero, isósceles o escaleno.

"""

lado1 = float(input("Introduce la longitud del primer lado: "))
lado2 = float(input("Introduce la longitud del segundo lado: "))
lado3 = float(input("Introduce la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
    
    
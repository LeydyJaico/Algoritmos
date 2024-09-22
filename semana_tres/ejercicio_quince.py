"""
Número de Teléfono con Formato:
Pide al usuario un número de teléfono de 10 dígitos y utiliza slicing y concatenación para darle
el formato "(###) ###-####"
"""

telefono = input("Ingresa un número de teléfono de 10 dígitos: ")

if len(telefono) == 10 and telefono.isdigit():
    formato = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número de teléfono con formato es: {formato}")
else:
    print("Número no válido.")
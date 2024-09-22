"""
Promedio de Notas:
Escribe un programa que calcule el promedio de una lista de notas ingresadas por el usuario.

"""

notas = input("Introduce las notas separadas por espacios: ").split()
notas = [float(nota) for nota in notas]
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")


# Solicitar lista de notas
notas = input("Introduce las notas separadas por comas: ")
notas = [float(nota) for nota in notas.split(',')]  # Convertir las notas a flotantes

# Calcular el promedio
promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio}")

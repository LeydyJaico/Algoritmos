#EJERCICIO_2
"""
Compara la longitud de tu nombre y tu apellido
"""
print("EJERCICIO 2:")
#variables
nombre = "Leydy"
longitud_n = len(nombre)
apellido = "Jaico"
longitud_a= len(apellido)

#mostramos los datos
print("Nombre:", nombre, "\nLa longitud es de:", longitud_n, "letras.")
print("Apellido:", apellido, "\nLa longitud es de:", longitud_a, "letras.")

#comparando
print("Comparamos las longitudes")
if longitud_a==longitud_n:
    print("la longitud del apellido y nombre son iguales")
else:
    print("Las longitudes del apellido y nombre son distintas")

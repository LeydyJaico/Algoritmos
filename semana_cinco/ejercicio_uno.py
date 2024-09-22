"""1) La siguiente es una lista de las edades de 10 estudiantes:
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24] (4ptos)
a. Ordena la lista y encuentra la edad mínima y máxima
b. Añade de nuevo la edad mínima y máxima a la lista
c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por 
dos)
d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)
e. Encuentra el rango de las edades (máximo menos mínimo)
f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()"""


# Lista de edades
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordena la lista y encuentra la edad mínima y máxima
edades.sort()         #no olvide sort y sorted son similares
edad_minima = min(edades)
edad_maxima = max(edades)
print(f"Edades ordenadas: {edades}")
print(f"Edad mínima: {edad_minima}, Edad máxima: {edad_maxima}")

# b. Añade de nuevo la edad mínima y máxima a la lista
edades.append(edad_minima)
edades.append(edad_maxima)
print(f"Lista con edades mínima y máxima añadidas: {edades}")

# c. Encuentra la edad mediana
longitud = len(edades)
if longitud % 2 == 0:
    mediana = (edades[longitud // 2 - 1] + edades[longitud // 2]) / 2
else:
    mediana = edades[longitud // 2]
print(f"Mediana de las edades: {mediana}")

# d. Encuentra la edad promedio
promedio = sum(edades) / len(edades)
print(f"Edad promedio: {promedio}")

# e. Encuentra el rango de las edades
rango = edad_maxima - edad_minima
print(f"Rango de edades: {rango}")

# f. Comparaaaa
diferencia_min_promedio = abs(edad_minima - promedio)
diferencia_max_promedio = abs(edad_maxima - promedio)
print(f"Min-Promedio: {diferencia_min_promedio}, Max-Promedio: {diferencia_max_promedio}")

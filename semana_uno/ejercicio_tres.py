#EJERCICIO_3
"""
Declara 5 como num_one y 4 como num_two
▪ Sume num_one y num_two y asigne el valor a una variable total
▪ Resta num_two de num_one y asigna el valor a una variable diff
▪ Multiplica num_two y num_one y asigna el valor a una variable producto
▪ Dividir num_one por num_two y asignar el valor a una variable división
▪ Utilice la división de módulo para encontrar num_two dividido por num_one y asigne el valor a
un resto variable
▪ Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
▪ Encuentra la división del piso de num_one por num_two y asigna el valor a una variable
floor_division
"""   

#Declaramos variables
num_one=5
num_two=4
print("num_one:", num_one, "\nnum_two:", num_two)
#suma
Total=num_one+num_two
print("La suma de ambos numeros es:", Total) 
#resta
diff=num_one-num_two
print("La resta de ambos numeros es:", diff) 
#multiplicacion
producto=num_one*num_two
print("La multiplicación de ambos numeros es:", producto)
#division
division= num_one/num_two
print("La division de ambos numeros es:",float(division))
#division modulo
resto = num_two % num_one
print("La división modulo es:", resto)
#potencia
exp = num_two ** num_one
print("La respuesta es:", exp)
#division piso
floor_division = num_two // num_one
print("La división piso es:", floor_division)
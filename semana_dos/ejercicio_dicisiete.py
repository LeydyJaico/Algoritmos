"""
Verificar prefijo y sufijo: Escribe un programa que verifique si una cadena dada por el usuario
comienza con un prefijo específico y termina con un sufijo específico.
"""
cadena = input("Introduce una cadena: ")
prefijo = input("Introduce el prefijo: ")
sufijo = input("Introduce el sufijo: ")
especifico = cadena.startswith(prefijo) and cadena.endswith(sufijo) 
print(especifico)
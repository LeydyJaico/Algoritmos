"""
Escribe un script que solicite al usuario que introduzca el número de años. Calcula el número de
segundos que una persona puede vivir. Supongamos que una persona puede vivir cien años.
Introduce el número de años que has vivido: 100
Has vivido durante 3153600000 segundos
"""
años = int(input("Introduce el número de años que has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print("Has vivido durante :",segundos, " segundos")
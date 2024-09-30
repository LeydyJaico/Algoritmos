"""2) Calculadora Simple: Crea una calculadora simple que pueda realizar operaciones básicas como suma,
resta, multiplicación y división. La calculadora debe aceptar dos números del usuario y el tipo de
operación que desea realizar. Maneja excepciones en caso de errores de entrada."""
def calculadora(num1, num2, operacion):
    try:
        if operacion == '+':
            return num1 + num2
        elif operacion == '-':
            return num1 - num2
        elif operacion == '*':
            return num1 * num2
        elif operacion == '/':
            return num1 / num2
        else:
            raise ValueError("Operación no válida. Use +, -, * o /.")
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
    except Exception as e:
        return f"Error: {e}"

# Entrada
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    resultado = calculadora(num1, num2, operacion)
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Entrada inválida. Asegúrese de ingresar números válidos.")

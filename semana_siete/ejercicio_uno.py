"""1) Conversor de Temperatura: Escribe un programa que convierta entre Celsius y Fahrenheit. El
programa debe permitir al usuario ingresar una temperatura y la unidad en la que está (C o F). Luego,
realiza la conversión y muestra el resultado. Utiliza funciones y control de flujo para realizar las
conversiones y manejar excepciones en caso de entradas incorrectas."""
def convertir_temperatura(temperatura, unidad):
    try:
        if unidad.upper() == "C":
            # Celsius a Fahrenheit
            return (temperatura * 9/5) + 32
        elif unidad.upper() == "F":
            # Fahrenheit a Celsius
            return (temperatura - 32) * 5/9
        else:
            raise ValueError("Unidad no válida. Use 'C' para Celsius o 'F' para Fahrenheit.")
    except Exception as e:
        return f"Error: {e}"

# Entrada
try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad de la temperatura (C o F): ")
    resultado = convertir_temperatura(temperatura, unidad)
    print(f"La temperatura convertida es: {resultado}")
except ValueError:
    print("Entrada inválida. Asegúrese de ingresar un número para la temperatura.")

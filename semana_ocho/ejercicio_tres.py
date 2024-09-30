"""3) Generador de Contraseñas: Crea una función que genere contraseñas aleatorias. La función debe
aceptar parámetros como longitud de la contraseña y si debe incluir letras mayúsculas, minúsculas,
números y caracteres especiales. Utiliza funciones lambda para generar caracteres aleatorios y maneja
excepciones si se proporcionan parámetros inválidos."""
import random
import string

def generar_contraseña(longitud, mayusculas=True, minusculas=True, numeros=True, especiales=True):
    try:
        caracteres = ""
        if mayusculas:
            caracteres += string.ascii_uppercase
        if minusculas:
            caracteres += string.ascii_lowercase
        if numeros:
            caracteres += string.digits
        if especiales:
            caracteres += string.punctuation
        
        if caracteres == "":
            raise ValueError("Debe seleccionar al menos un tipo de caracteres.")

        # Aleatorio
        return ''.join(random.choice(caracteres) for _ in range(longitud))
    except Exception as e:
        return f"Error: {e}"

# Entrada al usuario
try:
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    incluir_mayusculas = input("¿Incluir mayúsculas? (S/N): ").upper() == "S"
    incluir_minusculas = input("¿Incluir minúsculas? (S/N): ").upper() == "S"
    incluir_numeros = input("¿Incluir números? (S/N): ").upper() == "S"
    incluir_especiales = input("¿Incluir caracteres especiales? (S/N): ").upper() == "S"

    contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_especiales)
    print(f"La contraseña generada es: {contraseña}")
except ValueError:
    print("Entrada inválida. Asegúrese de ingresar un número válido para la longitud.")

"""Ejercicio Complejo:
Generador de Contraseñas Seguras
Descripción: Vamos a crear un generador de contraseñas seguras utilizando los conceptos
que hemos aprendido hasta ahora, incluyendo funciones, módulos y control de flujo. La idea
es que el programa genere una contraseña aleatoria con una longitud específica y asegure
que cumple con ciertos requisitos de seguridad.
Requisitos de seguridad de la contraseña:
La contraseña debe tener al menos 8 caracteres.
Debe incluir al menos una letra mayúscula y una letra minúscula.
Debe contener al menos un número.
Debe contener al menos un carácter especial (por ejemplo, !, @, #, $, %, etc.)."""

import random
import string

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud mínima de la contraseña debe ser 8 caracteres")

    # Caracteres
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiales = string.punctuation

    # caracter de cada tipo
    contraseña = [
        random.choice(letras_mayusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiales)
    ]

    # aleatorio
    todos_los_caracteres = letras_mayusculas + letras_minusculas + numeros + caracteres_especiales
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # mezcla
    random.shuffle(contraseña)

    # 
    return ''.join(contraseña)

# Solicitar la longitud de la contraseña al usuario
longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): "))
contraseña_segura = generar_contraseña(longitud)
print("Contraseña generada:", contraseña_segura)


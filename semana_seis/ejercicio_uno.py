import random
import string

def generamos_contraseña(longitud):
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return  

    # caracteres que debe tener
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # aleatorio para la seguidad
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    print("Tu contraseña segura es", contraseña)

# Solicitar al usuario la longitud de la contraseña
longitud = int(input("Introduce la longitud de la contraseña: "))
generamos_contraseña(longitud)

8
#if name??




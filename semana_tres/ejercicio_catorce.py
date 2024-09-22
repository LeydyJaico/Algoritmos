"""
Piedra, Papel o Tijera:
Pide al usuario que elija "piedra", "papel" o "tijera". Genera una elección aleatoria para la
computadora y determina quién gana.
"""

import random

opciones = ["piedra", "papel", "tijera"]
usuario = input("Elige piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)

print(f"La computadora eligió: {computadora}")

if usuario == computadora:
    print("Es un empate.")
elif (usuario == "piedra" and computadora == "tijera") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
    print("Ganaste.")
else:
    print("Perdiste.")

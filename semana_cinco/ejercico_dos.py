"""
“Soy profesor y me encanta inspirar y enseñar a la gente”. ¿Cuántas palabras únicas se han 
utilizado en la frase? Usa los métodos de split y sets para obtener las palabras únicas. (4pto)

"""

# Frase del profesor
frase = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras_unicas = set(frase.split())
print(f"Palabras únicas: {palabras_unicas}")
print(f"Cantidad de palabras únicas: {len(palabras_unicas)}")

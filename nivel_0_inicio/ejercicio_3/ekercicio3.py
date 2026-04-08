# Clasificador de Candidatos (Misión Selección)

añosExperiencia = int(input("Ingrese sus años de experiencia: "))
python = input("¿Domina Python? (si/no): ").lower()
tituloMaestria = input("¿Tiene título de Maestría? (si/no): ").lower()
ingles = input("¿Habla Inglés? (si/no): ").lower()

ruta1 = añosExperiencia > 5 and python == "si"
ruta2 = tituloMaestria == "si" and ingles == "si"

if ruta1 and ruta2:
    print("Candidato PRE-SELECCIONADO")
else:
    print("Candidato DESCARTADO por antecedentes éticos")
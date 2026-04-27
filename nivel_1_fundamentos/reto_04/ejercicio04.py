contA = 0
contB = 0
contVIP = 0

numeroDturnos = input("Numero de turnos: ")
turnos = [int(x) for x in input("Ingrese los turnos separados por espacio: ").split()]

print("Turnos ingresados: ")
for t in turnos:
    print (t)

for turno in turnos:
    if turno % 10 == 0:
        print(f"Turno {turno} -> Ventanilla Especial (VIP)")
        contVIP += 1
    elif turno % 2 == 0:
        print(f"Turno {turno} -> Ventanilla A")
        contA += 1
    else:
        print(f"Turno {turno} -> Ventanilla B")
        contB += 1

print("\nTotales:")
print(f"Ventanilla A: {contA} cliente(s)")
print(f"Ventanilla B: {contB} cliente(s)")
print(f"Ventanilla Especial: {contVIP} cliente(s)")
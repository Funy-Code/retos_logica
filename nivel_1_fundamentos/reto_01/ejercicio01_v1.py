
# codigo version1
N = int(input("Ingrese la cantidad de instrucciones (N): "))

girosIzq = 0
girosDer = 0
avanza = 0

for i in range(N):
    instruccion = input(f"Instrucción {i+1}: ").strip().upper()
    
    
    if instruccion == "AVANZA":
        avanza += 1
        
    elif instruccion == "GIRA_IZQ":
        girosIzq += 1
        
    elif instruccion == "GIRA_DER":
        girosDer += 1

pasos =  girosDer + girosIzq + avanza

print("\n--- Resultados del Robot ---")
print(f"Total de pasos recorridos: {avanza}")
print(f"Giros a la izquierda: {girosIzq}")
print(f"Giros a la derecha: {girosDer}")
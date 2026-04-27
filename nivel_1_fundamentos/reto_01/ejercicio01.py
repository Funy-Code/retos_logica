# 1. Leer N (cantidad de instrucciones)
N = int(input("Ingrese la cantidad de instrucciones (N): "))

pasos = 0
girosIzq = 0
girosDer = 0

for i in range(N):
    instruccion = input(f"Instrucción {i+1}: ").strip().upper()
    
    
    if instruccion.startswith("AVANZA"):
        partes = instruccion.split()
        if len(partes) > 1:
            valor_x = int(partes[1])
            pasos += valor_x
            
    elif instruccion == "GIRA_IZQ":
        girosIzq += 1
        
    elif instruccion == "GIRA_DER":
        girosDer += 1

# 5. Mostrar los 3 contadores
print("\n--- Resultados del Robot ---")
print(f"Total de pasos recorridos: {pasos}")
print(f"Giros a la izquierda: {girosIzq}")
print(f"Giros a la derecha: {girosDer}")
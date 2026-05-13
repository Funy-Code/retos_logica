
while True:
  inicio = int(input("Ingresa el número de inicio para la cuenta regresiva (entre 0 y 30): "))
  if 0 <= inicio <= 30:
    break
  else:
    print("Por favor, ingresa un número entre 0 y 30.")

consecutivosPares = 0
abortado = False

for numero in range(inicio, -1, -1):
    print(numero)
    
    if numero == 7:
        print("¡Revisión de sistemas!")
        print("Esperando 2 segundos...", end="")
        for _ in range(4):
            print(".", end="")
        print()
    elif numero == 5:
        print("¡Punto de no retorno!")
    elif numero == 3:
        print("¡Ignición encendida!")
    
    if numero % 2 == 0:
        consecutivosPares += 1
        if consecutivosPares == 3:
            print("⚠️ Lanzamiento abortado por 3 números pares consecutivos")
            abortado = True
            break
    else:
        consecutivos_pares = 0

if not abortado:
    print("🚀 ¡DESPEGUE!")
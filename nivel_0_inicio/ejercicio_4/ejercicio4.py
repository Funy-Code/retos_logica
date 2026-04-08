# Central Hidroeléctrica - Lógica de Alerta

nivelDeAgua = float(input("Ingrese el nivel de agua en metros: "))
velocidadLlenado = input("Ingrese la velocidad de llenado (bajo/medio/alto): ").lower()

if nivelDeAgua > 120:
    print("Nivel crítico: Abrir COMUERTA A y COMUERTA B")
    print("SONAR ALARMA GENERAL")
elif nivelDeAgua > 100 and velocidadLlenado == "alto":
    print("Abrir COMUERTA A")
elif nivelDeAgua > 100 and velocidadLlenado == "medio":
    print("Abrir COMUERTA B")
else:
    print("Comuertas cerradas, situación normal")
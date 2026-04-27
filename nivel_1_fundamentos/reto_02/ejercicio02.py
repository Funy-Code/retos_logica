verde = int(input("Ingrese tiempo en verde (segundos): "))
amarillo = int(input("Ingrese tiempo en amarillo (segundos): "))
rojo = int(input("Ingrese tiempo en rojo (segundos): "))

duracion_ciclo = verde + amarillo + rojo

total_segundos_turno = 8 * 60 * 60

ciclos_completos = total_segundos_turno // duracion_ciclo
segundos_sobrantes = total_segundos_turno % duracion_ciclo

print("\nResultados:")
print(f"Ciclo completo: {duracion_ciclo} segundos")
print(f"Ciclos en 8 horas: {ciclos_completos}")
print(f"Segundos sobrantes: {segundos_sobrantes}")
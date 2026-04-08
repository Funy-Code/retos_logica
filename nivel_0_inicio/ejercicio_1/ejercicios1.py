# Control de Acceso al Laboratorio Químico
fugaDeGas = ""
identificacion = ""
traje = ""

fugaDeGas = input("¿Hay fuga de gas? (si/no): ")
identificacion = input("¿Tienes identificaion? (si/no): ")
traje = input("¿Tienes el traje? (si/no): ")


if fugaDeGas == "si":
    print("Acceso Denegado por Seguridad")
elif (identificacion == "si") and (traje == "si"):
    print("Acceso Autorizado")
else:
    print("Equipo Incompleto")
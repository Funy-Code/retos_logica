anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))
anio_consulta = int(input("Ingrese el año que desea consultar: "))
    
edad_actual = anio_actual - anio_nacimiento
print(f"Edad actual: {edad_actual} años")


if anio_consulta > anio_actual:
    edad = anio_consulta - anio_nacimiento
    print(f"Edad en el año {anio_consulta}: {edad} años")
elif anio_consulta == anio_actual:
    print(f"Edad en el año {anio_consulta}: {edad_actual} años")
else:
    if anio_consulta >= anio_nacimiento:
        edad = anio_consulta - anio_nacimiento
        print(f"Edad en el año {anio_consulta}: {edad} años")
    else:
        print(f"En el año {anio_consulta}, aún no había nacido")
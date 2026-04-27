precio = 0
pago = 0
denominaciones = [500, 200, 100, 50, 20, 10, 5, 1]

precio = int(input("Ingrese precio de toda la compra: "))
pago = int(input("Ingrese el monto entregado: "))

cambio = (pago - precio)

if cambio < 0:
    print("Monto insuficiente. No se puede realizar compra.")
else:
    print(f"Cambio total: {cambio} pesos")
    
    cambioDetallado = {}
    
    for d in denominaciones:
        if cambio >= d:
            cantidad = cambio // d
            cambio = cambio % d
            cambioDetallado[d] = cantidad
            
    print("Entregar al cliente: ")
    for denom, cant in cambioDetallado.items():
        print(f"{cant} billete(s)/moneda(s) de {denom} pesos")
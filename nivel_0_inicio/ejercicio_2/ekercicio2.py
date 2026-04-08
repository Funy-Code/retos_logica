# Sistema de Descuentos "Cliente VIP"

montoCompra = float(input("Ingrese el valor de su compra en pesos: "))
vip = input("¿Es cliente VIP? (si/no): ").lower()
descuento = 0

if vip == "si":
    if montoCompra > 500000:
        descuento = 0.30
    else:
        descuento = 0.10
else: 
    if montoCompra > 500000:
        descuento = 0.20
    else:
        descuento = 0.0

precio_final = montoCompra * (1 - descuento)

print("Descuento aplicado:", int(descuento * 100), "%")
print("Precio final a pagar: $", precio_final)
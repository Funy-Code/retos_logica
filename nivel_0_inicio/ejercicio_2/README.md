# 🛍️ Sistema de Descuentos "Cliente VIP"

## 🔹 Escenario

Una **tienda tecnológica** desea premiar la fidelidad de sus clientes **sin comprometer sus ganancias**.

## 🔹 Reglas de Descuento

1. 💰 Si la compra es **mayor a $500.000**:
   - Cliente normal: **20% de descuento**
   - Cliente VIP: **30% de descuento**

2. 💳 Si la compra es **menor a $500.000**:
   - Cliente VIP: **10% de descuento**
   - Cliente normal: **0% de descuento**

## 🔹 Problema

Un cliente recibe un 20% de descuento si su compra es mayor a $500.000. Pero si el cliente es miembro VIP, el descuento sube al 30% siempre que la compra supere los 500.000. Si la compra es menor a esa cifra, los miembros VIP solo reciben un 10% y los clientes normales nada.

## 🔹 Reto

Estructurar los **condicionales** para calcular el **precio final** según:

- Tipo de cliente (VIP o normal) 🏷️
- Monto de la compra 💵

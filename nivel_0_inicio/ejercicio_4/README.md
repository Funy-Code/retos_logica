# 🌊 Central Hidroeléctrica (Lógica de Alerta)

## 🔹 Escenario

Una **represa** necesita un sistema de **alerta temprana** para prevenir inundaciones, controlando el nivel de agua y la velocidad de llenado.

## 🔹 Reglas del Sistema

1. ⚡ **Nivel > 120m**
   - Abrir **ambas compuertas** 🚪🚪
   - Sonar la **Alarma General** 🔔

2. 💧 **Nivel > 100m y velocidad alta**
   - Abrir **Compuerta A** 🚪

3. 💧 **Nivel > 100m y velocidad media**
   - Abrir **Compuerta B** 🚪

4. ⬇️ **Cualquier otro caso**
   - Las compuertas permanecen **cerradas** 🔒

## 🔹 Problema

El sistema monitorea el nivel de agua (en metros) y la velocidad de llenado (bajo, medio, alto).
Si el nivel es mayor a 100m y la velocidad es "alta", se debe abrir la Comuerta A.
Si el nivel es mayor a 100m pero la velocidad es "media", se abre la Comuerta B.
Si el nivel es mayor a 120m, no importa la velocidad, se deben abrir AMBAS comuertas y sonar la Alarma General.
En cualquier otro caso, las comuertas permanecen cerradas.

## 🔹 Reto

Manejar **rangos numéricos** y **variables de texto** para controlar múltiples salidas usando **condicionales anidados o lógicos**.

# 🧪 Control de Acceso al Laboratorio Químico

## 🔹 Escenario

El laboratorio de **alta seguridad** tiene un protocolo de entrada estricto para **prevenir accidentes** y garantizar la seguridad del personal.

## 🔹 Reglas de Acceso

1. ✅ El acceso se permite **solo si el usuario**:
   - Posee una **identificación válida** 🆔
   - Porta correctamente el **traje de protección** 🥼

2. ⚠️ **Excepción de seguridad**:
   - Si el sensor detecta una **fuga de gas** 💨, el acceso se deniega automáticamente para todos, sin importar la identificación o el equipo.

## 🔹 Mensajes del Sistema

- 🟢 **Acceso Autorizado**: Usuario cumple todos los requisitos y no hay peligro.
- 🔴 **Acceso Denegado por Seguridad**: Se detecta fuga de gas.
- 🟡 **Equipo Incompleto**: Usuario no cumple con algún requisito de identificación o traje.

## 🔹 Problema

El sistema permite la entrada si el usuario tiene una identificación válida y porta su traje de protección. Sin embargo, si el sensor detecta que hay una fuga de gas en el interior, nadie puede entrar, sin importar su identificación o equipo.

## 🔹 Reto

Determinar cuál mensaje imprimir según el estado de cada variable (**identificación, traje, sensor de gas**) usando **lógica condicional**.

---

> 💡 Tip: Puedes usar condicionales `if-else` en Python (o cualquier otro lenguaje) para evaluar estas reglas de manera eficiente.

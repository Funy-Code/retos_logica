# 👨‍💼 Clasificador de Candidatos (Misión Selección)

## 🔹 Escenario

Recursos Humanos necesita **filtrar perfiles automáticamente** para el cargo de **Ingeniero Senior**, asegurando que solo los candidatos más calificados pasen a la pre-selección.

## 🔹 Reglas de Pre-selección

1. 🏆 **Ruta 1**:
   - Más de **5 años de experiencia**
   - Domina **Python** 🐍

2. 🎓 **Ruta 2**:
   - Tiene un **título de Maestría**
   - Habla **Inglés** 🗣️

3. ⚠️ **Descarte prioritario**:
   - Cualquier candidato con **antecedentes de faltas éticas** es **descartado inmediatamente**, sin importar experiencia o estudios.

## 🔹 Problema

Para ser pre-seleccionado, el candidato debe cumplir al menos una de estas dos rutas:
Tener más de 5 años de experiencia y dominar Python.
Tener un título de Maestría y hablar Inglés.
Nota Crítica: Si el candidato tiene antecedentes de faltas éticas, queda descartado inmediatamente, sin importar sus estudios o experiencia.

## 🔹 Reto

Identificar el uso correcto de los **operadores lógicos**:

- `AND` (Y) ✅
- `OR` (O) ✅
- Condicional de **descarte prioritario** ❌

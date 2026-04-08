# 📐 Cómo Resolver los Retos

Esta guía te explica la metodología step-by-step para resolver cada ejercicio del repositorio.

---

## La Regla de Oro

> **Nunca escribas código sin antes tener un diagrama.**

El código es la traducción de un plan. Si no tienes plan, tu código será confuso, lleno de errores y difícil de mantener. Los ingenieros profesionales diseñan antes de codificar.

---

## Paso a Paso

### Paso 1 — Lee el Problema Completo (sin saltearte nada)

Antes de pensar en soluciones, lee el enunciado **dos veces**:
- La primera vez para entender la historia.
- La segunda vez para identificar: ¿qué entra?, ¿qué sale?, ¿qué condiciones hay?

### Paso 2 — Identifica los Componentes Clave

Anota en papel o en texto:

```
📥 ENTRADAS: ¿qué datos recibo?
📤 SALIDAS:  ¿qué debo producir?
⚙️  PROCESO:  ¿qué transformaciones ocurren?
🚦 CONDICIONES: ¿qué decisiones debo tomar?
🔁 REPETICIONES: ¿hay algo que deba repetirse?
```

### Paso 3 — Dibuja el Diagrama de Flujo

Usa los símbolos estándar:

| Símbolo | Forma | Uso |
|---------|-------|-----|
| **Inicio/Fin** | Óvalo / Cápsula | Marca dónde empieza y termina el proceso |
| **Proceso** | Rectángulo | Operaciones, asignaciones, cálculos |
| **Decisión** | Rombo | Preguntas con respuesta Sí/No |
| **Entrada/Salida** | Paralelogramo | Leer datos o mostrar resultados |
| **Flujo** | Flecha | Indica la dirección del proceso |
| **Conector** | Círculo | Conecta partes del diagrama |

#### Reglas para un buen diagrama:
- ✅ Siempre comienza con **INICIO** y termina con **FIN**
- ✅ Cada rombo (decisión) debe tener exactamente **dos salidas**: Sí y No
- ✅ Usa flecha de regreso para los **ciclos**
- ✅ Sé específico en los rombos: escribe la condición completa (ej: `¿edad >= 18?`)
- ❌ No uses código dentro del diagrama — usa lenguaje natural

### Paso 4 — Valida el Diagrama con los Casos de Prueba

Cada ejercicio tiene **casos de prueba**. Antes de codificar, recorre tu diagrama manualmente con esos casos:

1. Toma el primer caso de prueba
2. Sigue las flechas de tu diagrama paso a paso
3. ¿Llegaste al resultado esperado? ✅ Continúa al siguiente
4. ¿No llegaste? ❌ Corrige el diagrama y repite

> Esto se llama **"ejecutar el diagrama a mano"** o *dry run*.

### Paso 5 — Traduce a Código (Fase 2)

Una vez que el diagrama pasa todos los casos de prueba, **traduce símbolo por símbolo**:

| Símbolo del diagrama | Se convierte en... |
|---------------------|-------------------|
| Rectángulo | Instrucción / asignación |
| Rombo | `if / else` |
| Flecha de regreso | `while / for` |
| Paralelogramo de entrada | `input()` / `readline()` |
| Paralelogramo de salida | `print()` / `console.log()` |

### Paso 6 — Prueba el Código

Ejecuta el código con los mismos casos de prueba del ejercicio. Si falla, vuelve al diagrama — el error está ahí.

---

## Ejemplo Rápido

**Problema:** Dado un número, di si es par o impar.

**Paso 2 — Componentes:**
```
📥 ENTRADA: un número entero N
📤 SALIDA:  "Par" o "Impar"
⚙️  PROCESO:  calcular N % 2
🚦 CONDICIÓN: si el residuo es 0 → Par, si no → Impar
```

**Paso 3 — Diagrama:**
```
[INICIO]
    ↓
[Leer N]
    ↓
¿N % 2 == 0?
   /      \
 Sí        No
  ↓         ↓
[Mostrar  [Mostrar
  "Par"]   "Impar"]
    ↓         ↓
        [FIN]
```

**Paso 5 — Código (Python):**
```python
n = int(input("Ingresa un número: "))
if n % 2 == 0:
    print("Par")
else:
    print("Impar")
```

---

## Consejos de Oro

- 🧩 **Divide y vencerás**: si el problema es grande, divídelo en partes pequeñas
- 🔄 **Itera**: no intentes hacer el diagrama perfecto de una sola vez
- 🗣️ **Explícalo en voz alta**: si puedes explicar la solución a alguien, el diagrama será fácil
- 📝 **Usa papel**: a veces el papel es más rápido que cualquier herramienta digital
- ❓ **Si te atascas**: lee las pistas del ejercicio (están al final de cada `.md`)

---

*"Un buen programador no es el que recuerda más sintaxis, sino el que sabe descomponer problemas."*

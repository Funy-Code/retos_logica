# ⭐⭐⭐⭐⭐ Nivel 5 — Funciones y Modularidad

> **Conceptos:** Definición de funciones, parámetros, valor de retorno, alcance (scope), reutilización, diseño modular

---

## ¿Qué aprenderás en este nivel?

Una función es un bloque de código reutilizable que hace una tarea específica. En lugar de repetir código, lo encapsulas en una función y la llamas cuando la necesitas. En este nivel practicarás:

- 📦 **Definir funciones**: darle nombre, parámetros y cuerpo
- 🔄 **Llamar funciones**: invocarlas con argumentos
- 📤 **Retornar valores**: devolver resultados desde una función
- 🧩 **Diseño modular**: dividir un problema grande en funciones pequeñas
- 🔗 **Componer funciones**: usar el resultado de una función como entrada de otra
- 🌍 **Alcance (scope)**: variables locales vs. globales

---

## 🎯 Los Retos

| # | Nombre | Dificultad | Descripción breve |
|---|--------|------------|-------------------|
| 01 | [El Cocinero Modular](./reto_01_cocinero_modular.md) | 🟡 Medio | Diseña una receta como conjunto de sub-funciones |
| 02 | [La Calculadora de Planetas](./reto_02_calculadora_de_planetas.md) | 🟡 Medio | Calcula el peso de una persona en diferentes planetas |
| 03 | [La Fábrica de Contraseñas](./reto_03_fabrica_de_contrasenas.md) | 🟠 Difícil | Genera y valida contraseñas con reglas de seguridad |
| 04 | [El Validador de Formularios](./reto_04_validador_de_formularios.md) | 🟠 Difícil | Valida campos de un formulario usando funciones especializadas |
| 05 | [El Generador de Reportes](./reto_05_generador_de_reportes.md) | 🔴 Muy Difícil | Genera resúmenes académicos a partir de datos crudos |

---

## 💡 Consejos para este Nivel

- **Una función = una responsabilidad**: si una función hace más de una cosa, divídela
- **Nombra bien tus funciones**: `calcularPeso()` es mejor que `cp()`
- **En el diagrama, las funciones se dibujan como sub-diagramas separados**
- **Primero diseña la interfaz**: ¿qué recibe y qué devuelve la función? Luego el cuerpo
- **Reutiliza**: si copias y pegas código, probablemente debería ser una función

---

## 📐 Función en diagrama de flujo

```
Diagrama principal:          Sub-diagrama (función):
                             ┌──────────────────┐
[Llamar calcular(a, b)] ──►  │ calcular(a, b)   │
        ↓                    │   INICIO          │
[Usar resultado]             │   [proceso...]    │
                             │   [Retornar valor]│
                             │   FIN             │
                             └──────────────────┘
```

---

*Cuando termines los 5 retos de este nivel, pasa al [Nivel 6 → Lógica Avanzada](../nivel_6_logica_avanzada/)*

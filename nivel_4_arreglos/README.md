# ⭐⭐⭐⭐ Nivel 4 — Listas y Arreglos

> **Conceptos:** Arreglos/listas, recorrido (traversal), búsqueda, filtrado, inserción, eliminación, ordenamiento básico

---

## ¿Qué aprenderás en este nivel?

Un arreglo es una colección ordenada de elementos. En lugar de tener 10 variables para 10 valores, tienes una lista. En este nivel practicarás:

- 📦 **Crear y recorrer** una lista elemento por elemento
- 🔍 **Buscar** un elemento dentro de una lista
- 🧹 **Filtrar** elementos que cumplan una condición
- ➕ **Agregar y eliminar** elementos
- 📊 **Calcular** estadísticas sobre una colección (suma, promedio, mínimo, máximo)
- 🗂️ **Ordenamiento básico** de una lista

---

## 🎯 Los Retos

| # | Nombre | Dificultad | Descripción breve |
|---|--------|------------|-------------------|
| 01 | [El Inventario Pirata](./reto_01_inventario_pirata.md) | 🟡 Medio | Gestiona el botín de un barco con una lista de items |
| 02 | [El Ranking de Héroes](./reto_02_ranking_de_heroes.md) | 🟠 Difícil | Ordena heroínas y héroes por puntuación de batalla |
| 03 | [El Filtro de Sabores](./reto_03_filtro_de_sabores.md) | 🟡 Medio | Filtra helados según las alergias del cliente |
| 04 | [Duplicados en el Mapa](./reto_04_duplicados_en_el_mapa.md) | 🟠 Difícil | Detecta coordenadas repetidas en un mapa del tesoro |
| 05 | [El Promedio de las Aldeas](./reto_05_promedio_de_aldeas.md) | 🔴 Muy Difícil | Analiza temperaturas de múltiples aldeas y emite alertas |

---

## 💡 Consejos para este Nivel

- **Recorrer una lista = ciclo + índice**: siempre tendrás un contador `i` que va de 0 a N-1
- **El diagrama de búsqueda tiene un rombo dentro del ciclo**: ¿encontré el elemento?
- **Piensa en el "caso vacío"**: ¿qué pasa si la lista está vacía?
- **Para ordenar**: piensa en comparar pares de elementos → eso lleva a ciclos anidados

---

## 📐 Recorrido de lista en diagrama

```
[i = 0]
    ↓
◇ ¿i < longitud?
  |         |
  Sí        No → (salida)
  ↓
[Procesar lista[i]]
  ↓
[i = i + 1]
  ↑ (regresa a ◇)
```

---

*Cuando termines los 5 retos de este nivel, pasa al [Nivel 5 → Funciones](../nivel_5_funciones/)*

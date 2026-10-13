# Plan de trabajo — Isolation Forest dengue Perú

## Fase 1 — Exploración (completada)
- Notebook 01: 1 029 421 registros, 14 columnas, periodo 2000–2024.
- Revisiones de faltantes, categorías, duplicados exactos, distribución nacional y análisis de Ayacucho.

## Fase 2 — Tratamiento inicial (completada)
- Notebook 02: validación de `ubigeo`, `ano`, `semana`; estandarización textual.
- Agregación por `(ubigeo, ano, semana)` y unión geográfica validada.
- Salida: 81 196 observaciones, 12 columnas, suma de conteos igual al total validado.

## Fase 3 — Ingeniería de características (pendiente)
1. Auditar semanas epidemiológicas 53 y posibles lagunas temporales.
2. Distinguir explícitamente ausencia de registros, semanas sin notificación y cero observado; documentar las decisiones.
3. Ordenar cada serie territorial y construir rezagos sin usar semanas futuras.
4. Calcular, donde sea válido, `casos_lag_1`, media móvil de 4 semanas (solo pasado), cambio semanal y desviación frente al historial territorial.
5. Analizar sesgo por distritos con diferente volumen de registros y comparar alternativas como `log1p(casos_semanales)`.
6. Guardar dataset de características y un reporte de calidad.

**Criterio de aceptación:** sin duplicados en clave temporal; ausencia de fuga de información; reglas de semanas faltantes justificadas y testadas.

## Fase 4 — Isolation Forest (pendiente)
1. Definir ventana histórica de entrenamiento y validación temporal (sin barajar semanas).
2. Elegir características numéricas, tratamiento de valores faltantes y escalas.
3. Entrenar `sklearn.ensemble.IsolationForest`, registrar `random_state`, `n_estimators`, `max_samples` y `contamination`.
4. Comparar sensibilidad a parámetros y enfoques global versus territorial.
5. Guardar puntajes, hiperparámetros y versiones del entorno.

**Criterio de aceptación:** modelo reproducible, puntuaciones por territorio-semana y decisiones de hiperparámetros documentadas.

## Fase 5 — Evaluación, interpretación e informe (pendiente)
1. Inspeccionar semanas y distritos más inusuales sin identificarlos automáticamente como brotes.
2. Comparar los periodos relevantes con referencias oficiales solo cuando las ventanas y definiciones sean compatibles.
3. Presentar sensibilidad, estabilidad y limitaciones; no inventar precisión, recall ni F1 sin etiquetas verificadas.
4. Preparar tablas, gráficas, anexos y conclusiones del informe APA 7.

# Detección de anomalías epidemiológicas del dengue en Perú mediante Isolation Forest

Proyecto final de **Inteligencia Artificial I (IS-484)**, Universidad Nacional de San Cristóbal de Huamanga (UNSCH).

**Enfoque:** aprendizaje no supervisado, análisis espaciotemporal del dengue en Perú, con énfasis en Ayacucho.

> **Estado (octubre de 2026):** exploración y agregación epidemiológica inicial realizadas. La ingeniería de características, el entrenamiento de Isolation Forest y la evaluación están pendientes. Una anomalía estadística no equivale a un brote confirmado.

## Objetivo

Analizar registros históricos de vigilancia epidemiológica del dengue a escala distrito-semana y, en una etapa posterior, detectar observaciones inusuales mediante Isolation Forest para apoyar el análisis exploratorio de patrones temporales y territoriales.

## Resultados verificados del avance

| Indicador | Resultado |
|---|---:|
| Periodo del CSV | 2000–2024 |
| Registros individuales | 1 029 421 |
| Variables originales | 14 |
| Registros excluidos por validaciones iniciales | 0 |
| Observaciones agrupadas por UBIGEO, año y semana | 81 196 |
| Variables del dataset agrupado | 12 |
| Registros correspondientes a Ayacucho | 9 946 |

Estos resultados proceden de los notebooks 01 y 02 y de las verificaciones del dataset procesado; aún no constituyen resultados del algoritmo Isolation Forest. La suma de `casos_semanales` es igual a 1 029 421, y la tabla resultante no presenta claves duplicadas en `(ubigeo, ano, semana)`.

## Fuente de los datos

- [Vigilancia epidemiológica de dengue — Plataforma Nacional de Datos Abiertos](https://www.datosabiertos.gob.pe/dataset/vigilancia-epidemiol%C3%B3gica-de-dengue). Archivo local esperado: `datos_abiertos_vigilancia_dengue_2000_2024.csv`.
- [CDC-MINSA — Sala de situación del dengue, SE 14 de 2026](https://www.dge.gob.pe/portal/docs/vigilancia/sala/2026/SE14/dengue.pdf). Referencia contextual; no es el archivo de entrada al modelo ni debe compararse sin considerar diferencias de periodo y definiciones.

## Estructura

```text
isolation-forest-dengue-peru/
├── data/
│   ├── dataset/           # CSV original local (ignorado por Git)
│   └── processed/         # CSV agregado generado (ignorado por Git)
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_tratamiento_datos.ipynb
│   ├── 03_ingenieria_caracteristicas.ipynb
│   ├── 04_isolation_forest.ipynb
│   └── 05_evaluacion_visualizacion.ipynb
├── docs/
│   ├── PLAN_TRABAJO.md
│   └── DICCIONARIO_DATOS.md
├── tests/
│   └── test_processed_dataset.py
├── results/              # gráficos y tablas generados localmente
├── .gitignore
├── requirements.txt
└── README.md
```

## Preparar el entorno (Windows + VS Code)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name dengue-if --display-name "Python (Dengue IF)"
```

Seleccionar el intérprete de `.venv` o el kernel `Python (Dengue IF)` en VS Code. Ejecutar desde el directorio raíz del repositorio o verificar que los notebooks localicen correctamente la raíz del proyecto.

## Ejecutar el flujo

1. Descargar el CSV oficial y guardarlo en `data/dataset/datos_abiertos_vigilancia_dengue_2000_2024.csv`.
2. Ejecutar `01_exploracion_datos.ipynb`: revisar estructura, faltantes, temporalidad y distribución territorial.
3. Ejecutar `02_tratamiento_datos.ipynb`: limpiar, validar y agrupar por UBIGEO-año-semana. Se genera `data/processed/dengue_distrito_semanal.csv`.
4. Validar la exportación desde la raíz del repositorio:

```powershell
python -m unittest discover -s tests -v
```

5. Más adelante: construir variables temporales (03), entrenar Isolation Forest (04) y evaluar/visualizar resultados (05).

## Precauciones metodológicas

- `diagnostic` contiene códigos como `A97.0`, `A97.1` y `A97.2`; **no** es un campo de confirmación `C/P/S`. El CSV mostrado no contiene un campo `tipo_dx` para filtrar probables y confirmados.
- Hay filas idénticas, pero no se eliminan automáticamente: no existe un identificador único que permita afirmar que sean duplicados erróneos.
- Las 81 196 filas corresponden a semanas **con registros**. Una semana ausente no debe convertirse en cero sin justificar la cobertura de vigilancia.
- Una semana epidemiológica 53 puede existir y deberá validarse respecto al calendario correspondiente.
- El conteo de registros no equivale automáticamente a incidencia poblacional ni a brote confirmado.
- Evitar fuga temporal de información al calcular medias históricas y al separar entrenamiento y evaluación.

## Hoja de ruta

Consultar [PLAN_TRABAJO.md](docs/PLAN_TRABAJO.md) y [DICCIONARIO_DATOS.md](docs/DICCIONARIO_DATOS.md).

## Repositorio y resultados

Los datos originales y procesados están excluidos por `.gitignore`, por lo que **GitHub contiene el procedimiento reproducible, no el CSV original**. Las salidas guardadas de notebooks son evidencias exploratorias; los resultados posteriores del modelo se documentarán cuando hayan sido calculados y contrastados.

# Detección de anomalías epidemiológicas del dengue en Perú mediante Isolation Forest

**Curso:** Inteligencia Artificial I (IS-484) · UNSCH
**Enfoque:** Aprendizaje no supervisado; análisis nacional y énfasis en Ayacucho.
**Estado:** Estructura inicial para trabajo en equipo. El análisis y el modelado están pendientes; todavía no hay resultados.

## Objetivo
Preparar registros históricos del CDC-MINSA para analizar patrones inusuales por distrito y semana epidemiológica y, en una etapa posterior, detectar anomalías con Isolation Forest. Las anomalías no son automáticamente brotes confirmados.

## Fuente
- CSV histórico de vigilancia epidemiológica de dengue: https://www.datosabiertos.gob.pe/dataset/vigilancia-epidemiol%C3%B3gica-de-dengue
- `dengue.pdf`: sala de situación CDC-MINSA a la semana epidemiológica 14 de 2026, documento de referencia contextual (no insumo tabular primario).

## Carpetas
```text
isolation-forest-dengue-peru/
├── data/
│   ├── dataset/                 # CSV original, no se sube a GitHub
│   └── processed/               # CSV transformado, generado
├── notebooks/
│   ├── 01_exploracion_datos.ipynb            # verificación básica del entorno
│   ├── 02_tratamiento_datos.ipynb            # plantilla pendiente
│   ├── 03_ingenieria_caracteristicas.ipynb   # plantilla pendiente
│   ├── 04_isolation_forest.ipynb             # plantilla pendiente
│   └── 05_evaluacion_visualizacion.ipynb     # plantilla pendiente
├── results/
│   ├── figures/
│   └── tables/
├── docs/
│   └── REFERENCIAS.md
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación (Windows PowerShell + VS Code)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name dengue-if --display-name "Python (Dengue IF)"
code .
```
Seleccionar kernel **Python (Dengue IF)** en VS Code o Jupyter. Si PowerShell bloquea la activación, usar `.venv\Scripts\python.exe -m pip install -r requirements.txt` y seleccionar ese intérprete como kernel sin activar el entorno.

## Datos y ejecución
El flujo de análisis todavía no está implementado. Cuando se complete, cada integrante debe descargar el CSV oficial y guardarlo en `data/dataset/` con el nombre `datos_abiertos_vigilancia_dengue_2000_2024.csv`; luego podrá ejecutar los notebooks en orden. Los datos procesados y resultados se guardarán localmente en `data/processed/` y `results/`.

## Decisiones y precauciones
- El notebook conserva filas idénticas, porque sin un identificador de caso no hay prueba de que correspondan a duplicados erróneos.
- Se seleccionan diagnósticos `C` y `P` como criterio inicial sujeto a verificación con el diccionario del CSV.
- Se separan registros incompletos para revisión.
- No se rellena automáticamente como cero cada semana sin notificaciones.
- El reporte CDC-MINSA 2026 tiene cortes y definiciones que pueden diferir del CSV 2000–2024.
- `data/dataset/` se excluye de Git para mantener ligero el repositorio. Cada integrante debe descargar el CSV oficial y guardarlo en esa carpeta.

## Avance actual
- [x] Estructura del repositorio
- [x] Verificación básica del entorno en Jupyter
- [ ] Exploración y tratamiento del CSV
- [ ] Características temporales y entrenamiento Isolation Forest
- [ ] Evaluación, gráficos finales e informe APA 7

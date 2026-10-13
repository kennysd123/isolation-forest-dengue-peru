# Diccionario de datos y trazabilidad

## Dataset fuente (CSV de vigilancia 2000–2024)

Columnas observadas: `departamento`, `provincia`, `distrito`, `localidad`, `enfermedad`, `ano`, `semana`, `diagnostic`, `diresa`, `ubigeo`, `localcod`, `edad`, `tipo_edad`, `sexo`.

- `ubigeo`: identificador territorial, leer como texto para conservar ceros iniciales.
- `ano`, `semana`: periodo epidemiológico; semana dentro de 1–53, con validación de calendario pendiente.
- `enfermedad`: formas clínicas encontradas: dengue sin signos de alarma, dengue con signos de alarma, dengue grave.
- `diagnostic`: código CIE (`A97.0`, `A97.1`, `A97.2`); no confundir con confirmación del caso.
- `tipo_edad`: se observaron `A`, `M`, `D`; convertir edad solo tras confirmar la codificación del campo.
- `sexo`: `F` y `M` en la exploración reportada.
- `localidad`, `localcod`, `diresa`: campos con valores faltantes; no son necesarios para la clave agregada.

## Dataset procesado — `dengue_distrito_semanal.csv`

| Campo | Descripción |
|---|---|
| `ubigeo` | Código de distrito, texto |
| `ano` | Año epidemiológico |
| `semana` | Semana epidemiológica |
| `casos_semanales` | Número de registros agrupados |
| `casos_graves` | Conteo con `enfermedad == DENGUE GRAVE` |
| `casos_con_alarma` | Conteo con `enfermedad == DENGUE CON SIGNOS DE ALARMA` |
| `casos_femeninos` | Conteo con `sexo == F` |
| `proporcion_graves` | `casos_graves / casos_semanales` |
| `proporcion_alarma` | `casos_con_alarma / casos_semanales` |
| `departamento` | Nombre geográfico |
| `provincia` | Nombre geográfico |
| `distrito` | Nombre geográfico |

## Interpretación y límites

Cada fila procesada indica una combinación distrito-año-semana **con al menos un registro**. No implica que semanas ausentes sean cero. La suma de `casos_semanales` conserva los registros validados; esta comprobación no sustituye auditorías de subregistro o calidad epidemiológica.

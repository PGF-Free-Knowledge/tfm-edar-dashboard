# Análisis Técnico Inicial de Datos EDAR

## Proyecto

TFM – Comparación de Plantas EDAR mediante Python y Dashboard Interactivo

---

# 1. Introducción

El presente análisis corresponde a la evaluación comparativa de dos estaciones depuradoras de aguas residuales (EDAR):

* EDAR Cerceda
* EDAR Vedra

Los datos fueron obtenidos desde planillas Excel operacionales y posteriormente procesados mediante herramientas de análisis de datos en Python.

La arquitectura desarrollada considera:

* Procesamiento automático de datos
* Limpieza y normalización
* Visualización interactiva
* Dashboard técnico mediante Streamlit
* Comparación dinámica entre ambas plantas

---

# 2. Objetivo del análisis

El objetivo principal consiste en comparar el comportamiento operacional y las cargas contaminantes de ambas EDAR, identificando:

* Diferencias de escala operacional
* Variabilidad temporal
* Tendencias mensuales
* Comportamiento hidráulico
* Relación entre parámetros contaminantes
* Estabilidad operacional

---

# 3. Parámetros analizados

Los principales parámetros considerados son:

| Parámetro   | Descripción                  |
| ----------- | ---------------------------- |
| Caudal      | Volumen diario tratado       |
| DBO5        | Demanda biológica de oxígeno |
| DQO         | Demanda química de oxígeno   |
| SST         | Sólidos suspendidos totales  |
| NT          | Nitrógeno total              |
| PT          | Fósforo total                |
| pH          | Potencial hidrógeno          |
| A y G       | Aceites y grasas             |
| Det. Anion. | Detergentes aniónicos        |

---

# 4. Procesamiento de datos

El flujo de procesamiento implementado considera:

1. Lectura automática desde Excel
2. Extracción de bloques relevantes
3. Limpieza de datos
4. Normalización de columnas
5. Conversión de meses a formato estándar
6. Generación automática de gráficos
7. Construcción de dashboard interactivo

Tecnologías utilizadas:

* Python
* Pandas
* Plotly
* Streamlit
* Matplotlib
* OpenPyXL

---

# 5. Resultados preliminares

## 5.1 Diferencia de escala operacional

Los datos muestran diferencias muy significativas entre ambas EDAR.

### Caudal medio aproximado

| EDAR    | Caudal medio |
| ------- | ------------ |
| Cerceda | ~485 m3/d    |
| Vedra   | ~16 m3/d     |

Esto permite inferir que:

* Cerceda opera a una escala considerablemente superior.
* Vedra corresponde probablemente a una planta de menor capacidad.
* Las cargas contaminantes de Cerceda son mucho más elevadas.

---

## 5.2 Cargas contaminantes

Los parámetros DBO5, DQO y SST muestran diferencias importantes.

### DBO5 media aproximada

| EDAR    | DBO5     |
| ------- | -------- |
| Cerceda | ~65 kg/d |
| Vedra   | ~4 kg/d  |

### DQO media aproximada

| EDAR    | DQO       |
| ------- | --------- |
| Cerceda | ~240 kg/d |
| Vedra   | ~9 kg/d   |

### SST media aproximada

| EDAR    | SST      |
| ------- | -------- |
| Cerceda | ~99 kg/d |
| Vedra   | ~2 kg/d  |

---

# 6. Interpretación técnica

## 6.1 Variabilidad operacional

Cerceda presenta una variabilidad considerablemente mayor.

Se observan:

* Picos mensuales elevados
* Oscilaciones importantes
* Cambios bruscos en carga contaminante

Esto podría asociarse a:

* Aportes industriales
* Variabilidad hidráulica
* Influencia estacional
* Cambios operacionales
* Eventos de infiltración o lluvias

Por otro lado, Vedra presenta un comportamiento más estable y homogéneo.

---

## 6.2 Relación DBO5/DQO

La relación DBO5/DQO constituye un indicador importante de biodegradabilidad.

Interpretación típica:

| Ratio     | Interpretación          |
| --------- | ----------------------- |
| > 0.4     | Alta biodegradabilidad  |
| 0.2 – 0.4 | Biodegradabilidad media |
| < 0.2     | Baja biodegradabilidad  |

En Cerceda se observan variaciones importantes entre meses, lo cual podría indicar cambios en la composición del afluente.

---

# 7. Dashboard interactivo

Se desarrolló un dashboard interactivo utilizando Streamlit.

Características implementadas:

* KPIs principales
* Comparación EDAR
* Gráficos interactivos
* Series temporales
* Filtros dinámicos
* Visualización comparativa

El dashboard permite:

* Identificar tendencias
* Comparar parámetros
* Detectar anomalías
* Analizar estabilidad operacional
* Facilitar interpretación técnica

---

# 8. Arquitectura del proyecto

El proyecto fue estructurado modularmente.

## Estructura principal

```text
app/
scripts/
data/
outputs/
docs/
diagrams/
notebooks/
```

---

# 9. Conclusiones preliminares

Los resultados obtenidos permiten concluir preliminarmente que:

1. Las EDAR presentan escalas operacionales significativamente distintas.
2. Cerceda posee mayores cargas hidráulicas y contaminantes.
3. Cerceda presenta mayor variabilidad operacional.
4. Vedra exhibe comportamiento más estable.
5. El dashboard desarrollado permite visualizar tendencias y apoyar el análisis técnico.
6. La arquitectura implementada permite escalabilidad futura.

---

# 10. Líneas futuras de desarrollo

Se propone continuar el proyecto incorporando:

* Diagramas de flujo EDAR
* Indicadores de eficiencia
* Balance de masas
* Modelos predictivos
* Exportación automática de reportes
* Análisis estadístico avanzado
* Machine Learning para predicción de cargas
* Despliegue web completo

---

# 11. Repositorio del proyecto

Repositorio GitHub:

`tfm-edar-dashboard`

El repositorio incluye:

* Código fuente
* Dashboard
* Scripts de análisis
* Procesamiento automático
* Visualizaciones
* Documentación técnica

---

# 12. Estado actual del proyecto

Estado actual:

* Dashboard funcional
* Procesamiento automático operativo
* Arquitectura modular implementada
* Visualización interactiva activa
* Integración GitHub completada
* Proyecto listo para expansión futura

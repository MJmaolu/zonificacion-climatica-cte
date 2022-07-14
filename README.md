[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/curso-reproducibilidad-team4/zonificacion-climatica-cte/HEAD)
[![Snakemake](https://img.shields.io/badge/snakemake-≥5.6.0-brightgreen.svg?style=flat)](https://snakemake.readthedocs.io)

# Zonificación climática del CTE

- [Zonificación climática del CTE](#zonificación-climática-del-cte)
  - [Acerca de este proyecto](#acerca-de-este-proyecto)
    - [Zonificación climática localidades españolas según severidades del Código Técnico de la Edificación](#zonificación-climática-localidades-españolas-según-severidades-del-código-técnico-de-la-edificación)
    - [Propuesta](#propuesta)
  - [Cómo replicar el flujo de trabajo](#cómo-replicar-el-flujo-de-trabajo)
    - [Opción 1. Mediante un entorno de conda](#opción-1-mediante-un-entorno-de-conda)
    - [Opción 2. Mediante Snakemake](#opción-2-mediante-snakemake)
    - [Opción 3. Mediante Binder](#opción-3-mediante-binder)
  - [Software necesario](#software-necesario)
  - [Fuentes de datos](#fuentes-de-datos)
    - [Pasos a ejecutar](#pasos-a-ejecutar)
    - [Resultados](#resultados)
  - [Proceso de análisis](#proceso-de-análisis)

## Acerca de este proyecto

### Zonificación climática localidades españolas según severidades del Código Técnico de la Edificación

El _Código Técnico de la Edificación (CTE)_ permite asignar a cada localidad una zona climática, que se obtiene a partir de su capital de provincia y la altitud sobre el nivel del mar.

Las [tablas del Anejo B](https://www.codigotecnico.org/pdf/Documentos/HE/DccHE.pdf) del _Documento básico de Ahorro de Energía del CTE (CTE DB-HE)_ recogen esta zonificación y se elaboraron a partir de datos climáticos correspondientes a las capitales de provincia, realizando interpolación geométrica y calculando dos indicadores, la severidad climática de invierno (SCI) y la severidad climática de verano (SCV). Dichas severidades se codifican como zonas climáticas mediante una letra (zona climática de invierno, ZCI) y un número (zona climática de verano, ZCV) que, combinadas, definen una zona climática (ZC).

Esta zonificación climática está vinculada a las exigencias reglamentarias de eficiencia energética de los edificios, especificadas en el _CTE DB-HE_, pero también se utilizan para cuantificar el bono social térmico, etc.

### Propuesta

Con la disponibilidad de datos de satélite más precisos para cualquier punto georeferenciado, se plantea el ejercicio de obtener con esa información la zonificación climática y comparar los resultados con la zonificación actualmente existente del CTE DB-HE 2019.

Este análisis se propone como un caso de ciencia reproducible.

## Cómo replicar el flujo de trabajo

- Si quieres hacerlo en tu máquina local: ejecuta desde el 1 al 3 y luego elige entre hacerlo con [conda](#creando-un-conda-environment) o con [snakemake](#con-snakemake)
- También puedes ejecutarlo directamente con [binder](#con-binder)

Para reproducir el análisis realizado debe seguir el siguiente flujo de trabajo:

1. Clonar el repositorio

```shell
  git clone https://github.com/curso-reproducibilidad-team4/zonificacion-climatica-cte.git
```

1. Acceder al directorio

```shell
  cd zonificacion-climatica-cte
```

3. Asignar permisos de ejecución para los scripts

```shell
  chmod -R +x ./src
```

### Opción 1. Mediante un entorno de conda

Si no tienes _conda_, puedes ver cómo instalártelo [aquí](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

4a. Generamos un entorno de conda

```shell
conda env create -f environment.yml
```

5a. Activamos el entorno

```shell
conda activate zonificacion-climatica-env
```

6a. Ejecutamos los scripts del apartado [Pasos a ejecutar](#pasos-a-ejecutar)

### Opción 2. Mediante Snakemake

Para la instalación de [Snakemake](https://snakemake.readthedocs.io/en/stable/index.html#) consulte su [documentación](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html).

```shell
  snakemake -c1
```

### Opción 3. Mediante Binder

Puede ejecutar el análisis de este proyecto usando [Binder](https://mybinder.org)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/curso-reproducibilidad-team4/zonificacion-climatica-cte/HEAD)

1. Siga en una consola los pasos del apartado [Pasos a ejecutar](#pasos-a-ejecutar)

## Software necesario

[Python](https://www.python.org) para el tratamiento previo de datos

- `Python versión 3`

Dependencias relevantes de Python:

```yaml
- numpy == 1.19
- pandas == 1.2
- requests == 2.25
```

## Fuentes de datos

Municipios y geolocalizción:

- Fuente:
  - [Nomenclator oficial del Centro Nacional de Información Geográfica (CNIG)](https://datos.gob.es/gl/catalogo/e00125901-spaignngbe)
  - [Centro de descargas](http://centrodedescargas.cnig.es/CentroDescargas/catalogo.do?Serie=NGMEN)
- Licencia: Compatible CC BY 4.0
- Formato: archivo de datos separados por comas .csv
- Ruta en el repositorio: `datos/ign/MUNICIPIOS.csv`

Información climática

- Fuente: Joint Research Center (JRC)
  - [PV-GIS (JRC)](https://re.jrc.ec.europa.eu/pvg_tools/en/)
  - Descarga a través de API para obtener TMY:
    - [API Support page](https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system/getting-started-pvgis/api-non-interactive-service_en)
    - Estructura de URL: `https://re.jrc.ec.europa.eu/api/v5_2/tmy?lat=40.409&lon=-3.724&usehorizon=1&browser=1&outputformat=csv&startyear=2005&endyear=2020&userhorizon=&js=1&period=1`
- Licencia: CC BY 4.0. [Notal legal EU](https://ec.europa.eu/info/legal-notice_en)
- Formato: Año meteorológico tipo (TMY) en formato .csv
- Ruta de descarga en el repositorio: `datos/output/tmy

### Pasos a ejecutar

- Definición de la secuencia de tareas

  1. Generación de los datos para la descarga de archivos climáticos:

     `python3 src/select_input.py`

  2. Descarga de archivos climáticos (8130)

     `python3 src/download_TMY.py`

  3. Cálculo de indicadores

     `python3 src/compute_indicators.py`

  4. Representación gráfica

     `jupyter nbconvert --to notebook --execute --allow-errors notebooks/graficas.ipynb`

### Resultados

- Archivo con datos de municipios:
  - `data/output/Municipios.csv`
- Archivos climáticos:
  - `data/output/tmy/*.csv`
- Archivo de datos de zonificación:
  - `data/output/Results.csv`
- Gráficas:
  - `data/output/plots/*.png`
- Descripción de los resultados y conclusiones
  - `...TODO`

## Proceso de análisis

- Obtención de datos:
  - Latitud y longitud de municipios a partir del nomenclator oficial del Centro Nacional de Información Geográfica (CNIG):
    - https://datos.gob.es/gl/catalogo/e00125901-spaignngbe
    - http://centrodedescargas.cnig.es/CentroDescargas/catalogo.do?Serie=NGMEN
  - Información climática (radiación y temperatura)
    - Año meteorológico tipo (TMY):
    - [PV-GIS (JRC)](https://re.jrc.ec.europa.eu/pvg_tools/en/)
    - API para obtener TMY:
      - `https://re.jrc.ec.europa.eu/api/v5_2/tmy?lat=40.409&lon=-3.724&usehorizon=1&browser=1&outputformat=csv&startyear=2005&endyear=2020&userhorizon=&js=1&period=1`
      - `https://re.jrc.ec.europa.eu/api/v5_2/tmy?lat=40.409&lon=-3.724&usehorizon=1&browser=1&outputformat=json&startyear=2005&endyear=2020&userhorizon=&js=1&period=1`
- Cálculo de indicadores
  - índices de severidad climática de invierno (SCI) y verano (SCV)
  - zonas climáticas de invierno (ZCI, una letra) y verano (ZCV, un número), a partir de SCI y SCV
  - zona climática ZC (letra de ZCI y número de ZCV)
    - Depende de GD y n/N: [Documento de apoyo de climas](https://www.codigotecnico.org/pdf/Documentos/HE/20170202-DOC-DB-HE-0-Climas%20de%20referencia.pdf)
      - S.A. Kalogirou, Solar energy engineering: processes and systems (2nd ed.), Elsevier Inc. (2014)
      - n (duration of sunshine) - horas en las que la radiación directa (beam solar irradiance) > 120 W/m² (World Meteorological Organization)
      - N (número teórico máximo de horas de luz) - duración del día (en horas) = 2/15. cos^-1(-tan(L)tan(delta)), L=latitud, delta = declinación (grados) = 23.45.sin(360/365(284 + día_del_año)))
    - GD: Grados día (cálculo de datos horarios):
      - <img src="https://render.githubusercontent.com/render/math?math=GD_{T_b} = \sum {{T_b - T_{ah}} \over 24} \cdot \left\lfloor T_b > T_{ah} \right\rfloor">
        <!-- GD_Tb = Sum( ((Tb - Tah) / 24) si Tb > Tah, o 0 si Tb <= Tah). -->
- Representación de resultados
  - Mapa ZCI
  - Mapa ZCV
  - Mapa de diferencias entre ZCI calculada y de las tablas CTE DB-HE
  - Mapa de diferencias entre ZCV calculada y de las tablas CTE DB-HE

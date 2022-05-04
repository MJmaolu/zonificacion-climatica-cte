# zonificacion-climatica-cte

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Contenidos</h2></summary>
  <ol>
    <li>
      <a href="#sobre-este-proyecto">Sobre este proyecto</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#cómo-replicar-el-flujo-de-trabajo">Cómo replicar el flujo de trabajo</a>
      <ul>
        <li><a href="#creando-un-conda-environment">Creando un conda-environment</a></li>
        <li><a href="#con-snakemake">Con snakemake</a></li>
        <li><a href="#con-binder">Con binder</a></li>
      </ul>
      <li>
        <a href="#resultados-que-podemos-obtener">Resultados que podemos obtener</a>
      </li>
    </li>
  </ol>
</details>

## Sobre este proyecto

<p align="center">
  <b> Actualización de la zonificación climática de localidades españolas según severidades del Código Técnico de la Edificación </b>
</p>

El _Código Técnico de la Edificación (CTE)_ permite asignar a cada localidad una zona climática, que se obtiene a partir de su capital de provincia y la altitud sobre el nivel del mar.

Las [tablas del Anejo B](https://www.codigotecnico.org/pdf/Documentos/HE/DccHE.pdf) del _Documento básico de Ahorro de Energía del CTE (CTE DB-HE)_ recogen esta zonificación y se elaboraron a partir de datos climáticos correspondientes a las capitales de provincia, realizando interpolación geométrica y calculando dos indicadores, la severidad climática de invierno (SCI) y la severidad climática de verano (SCV). Dichas severidades se codifican como zonas climáticas mediante una letra (zona climática de invierno, ZCI) y un número (zona climática de verano, ZCV) que, combinadas, definen una zona climática (ZC).

Esta zonificación climática está vinculada a las exigencias reglamentarias de eficiencia energética de los edificios, especificadas en el _CTE DB-HE_, pero también se utilizan para cuantificar el bono social térmico, etc.

## Cómo replicar el flujo de trabajo

- Si quieres hacerlo en tu máquina local: ejecuta desde el 1 al 3 y luego elige entre hacerlo con [conda](#creando-un-conda-environment) o con [snakemake](#con-snakemake) 
- También puedes ejecutarlo directamente con [binder](#con-binder)

1. Clonar el repositorio

  ```git clone https://github.com/curso-reproducibilidad-team4/zonificacion-climatica-cte.git```

2. Entrar al directorio

  ```cd zonificacion-climatica-cte```

3. Damos permisos de ejecución

  ```chmod -R +x .```

### Creando un conda-environment

Si no tienes conda, puedes ver cómo instalártelo [aquí](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

  4a. Generamos un entorno de conda

  ```conda env create -f environment.yaml```

  5a. Activamos el entorno

  ```conda activate zonificacion-climatica-env```

  6a. Ejecutamos los scripts en el siguiente orden:

  - Generación de los datos para la descarga de archivos climáticos:

      ```python3 src/select_input.py```
  
  - Descarga de archivos climáticos:

     ```python3 src/download_TMY.py```
 
  - Cálculo de indicadores:

      ```python3 src/compute_indicators.py```
  
  - Representación gráfica:

      ```python3 src/plot_results.py```

### Con snakemake

...

### Con binder

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/curso-reproducibilidad-team4/zonificacion-climatica-cte/HEAD)

  1c. Generación de los datos para la descarga de archivos climáticos:

     `python3 src/select_input.py`

  2c. Descarga de archivos climáticos (8130)

     `python3 src/download_TMY.py`

  3c. Cálculo de indicadores

     `python3 src/compute_indicators.py`

  4c. Representación gráfica

     `python3 src/plot_results.py`

## Propuesta

Puesto que ahora disponemos de datos de satélite más precisos y para cualquier punto georeferenciado, se plantea el ejercicio de obtener la zonificación climática a partir de esa información y hacer un análisis comparativo con la zonificación existente del CTE DB-HE.

Realizar la propuesta mediante criterios de ciencia reproducible.

## Herramientas

- Python para el tratamiento previo de datos

## Información de los datos y el proceso

### Fuentes de datos

Municipios y geolocalizción:

- Fuente: Nomenclator oficial del Centro Nacional de Información Geográfica (CNIG):
  - https://datos.gob.es/gl/catalogo/e00125901-spaignngbe
  - http://centrodedescargas.cnig.es/CentroDescargas/catalogo.do?Serie=NGMEN
- Licencia: Compatible CC BY 4.0
- Formato: archivo de datos separados por comas .csv
- Ruta en el repositorio: `datos/ign/MUNICIPIOS.csv`

Información climática

- Fuente: Joint Research Center (JRC)
  - [PV-GIS (JRC)](https://re.jrc.ec.europa.eu/pvg_tools/en/)
  - Descarga a través de API para obtener TMY:
    - [API Support page](https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system/getting-started-pvgis/api-non-interactive-service_en)
    - Estructura de URL: `https://re.jrc.ec.europa.eu/api/v5_2/tmy?lat=40.409&lon=-3.724&usehorizon=1&browser=1&outputformat=csv&startyear=2005&endyear=2020&userhorizon=&js=1&period=1`
- Licencia: CC BY 4.0 (https://ec.europa.eu/info/legal-notice_en)
- Formato: Año meteorológico tipo (TMY) en formato .csv
- Ruta de descarga en el repositorio: `datos/output/tmy

### Software necesario

Programas necesarios y versiones:

- `Python 3`

Dependencias relevantes de Python:

- `pandas`
- `requests`

### Pasos a ejecutar

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/curso-reproducibilidad-team4/zonificacion-climatica-cte/HEAD)

- Definición de la secuencia de tareas

  1. Generación de los datos para la descarga de archivos climáticos:

     `python3 src/select_input.py`

  2. Descarga de archivos climáticos (8130)

     `python3 src/download_TMY.py`

  3. Cálculo de indicadores

     `python3 src/compute_indicators.py`

  4. Representación gráfica

     `python3 src/plot_results.py`

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

# encoding: utf-8

"""Selección de datos de entrada de los municipios

Selecciona los datos de entrada relevantes del archivo
`data/ign/MUNICIPIOS.csv` del IGN y genera el archivo de
datos `data/output/Municipios.csv` que contendría:

- COD_INE
- COD_PROV
- PROVINCIA
- NOMBRE_ACTUAL
- LONGITUD_ETRS89
- LATITUD_ETRS89
- ALTITUD
- ARCHIVO_TMY


Las coordenadas geográficas de los siguientes municipios dan lugar a posiciones sobre el mar,
de modo que deben ser corregidas para descargar los datos:

- NOMBRE_ACTUAL, LONGITUD_ETRS89, LATITUD_ETRS89 -> nueva LONG, nueva LAT
- 11016000000_Chipiona.csv, -6.44220215,36.73790677 -> -6.435, 36.736
- 11030000000_Rota.csv, -6.36315877,36.62011111 -> -6.358, 36.617
- 15901000000_Cariño.csv, -7.868424967,43.74035104 -> -7.869, 43.741
- 17048000000_Castell-Platja d'Aro.csv, 3.06798443,41.81426606 -> 3.067, 41.817
- 27066000000_Viveiro.csv, -7.5973072639999994,43.66074911 -> -7.595, 43.662
"""

import pandas as pd
import os

# from download_TMY import MUNICIPIOS_FILE

MUNICIPIOS_FILE = "data/ign/MUNICIPIOS.csv"
MUNICIPIOS_FILE_FORMATTED = "data/output/Municipios.csv"

FIX_DATA = {
    "Chipiona": {"LONGITUD_ETRS89": -6.435, "LATITUD_ETRS89": 36.736},
    "Rota": {"LONGITUD_ETRS89": -6.358, "LATITUD_ETRS89": 36.617},
    "Cariño": {"LONGITUD_ETRS89": -7.869, "LATITUD_ETRS89": 43.741},
    "Castell-Platja d'Aro": {"LONGITUD_ETRS89": 3.067, "LATITUD_ETRS89": 41.817},
    "Viveiro": {"LONGITUD_ETRS89": -7.595, "LATITUD_ETRS89": 43.662},
}

if __name__ == "__main__":
    print("Cargando datos de municipios...")
    df = pd.read_csv(
        MUNICIPIOS_FILE,
        encoding="latin1",
        sep=";",
        decimal=",",
        dtype={
            "COD_INE": str,
            "ID_REL": str,
            "COD_GEO": str,
            "COD_PROV": str,
            "PROVINCIA": str,
            "NOMBRE_ACTUAL": str,
            "POBLACION_MUNI": int,
            "SUPERFICIE": float,
            "PERIMETRO": float,
            "COD_INE_CAPITAL": str,
            "CAPITAL": str,
            "POBLACION_CAPITAL": int,
            "HOJA_MTN25_ETRS89": str,
            "LONGITUD_ETRS89": float,
            "LATITUD_ETRS89": float,
            "ORIGENCOOR": str,
            "ALTITUD": float,
            "ORIGENALTITUD": str,
        },
        usecols=[
            "COD_INE",
            "COD_PROV",
            "PROVINCIA",
            "NOMBRE_ACTUAL",
            "LONGITUD_ETRS89",
            "LATITUD_ETRS89",
            "ALTITUD",
        ],
    )

    # Sustituimos los nombres con / para generar un nombre de arcivo válido
    df["ARCHIVO_TMY"] = df[["COD_INE", "NOMBRE_ACTUAL"]].apply(
        lambda x: "{}_{}.csv".format(x[0], x[1].replace("/", "__")), axis=1
    )

    # Corregimos las coordenadas de los municipios que dan lugar a posiciones sobre el mar
    for muni, value in FIX_DATA.items():
        print("Corrigiendo localización de municipio: {}...".format(muni))
        new_long = value["LONGITUD_ETRS89"]
        new_lat = value["LATITUD_ETRS89"]
        df.loc[df.NOMBRE_ACTUAL == muni, "LONGITUD_ETRS89"] = new_long
        df.loc[df.NOMBRE_ACTUAL == muni, "LATITUD_ETRS89"] = new_lat

    if not os.path.isdir("data/output"):
        os.makedirs("data/output")

    df.to_csv(MUNICIPIOS_FILE_FORMATTED, index=False, encoding="utf-8")
    print("Datos de {} municipios cargados.".format(len(df)))

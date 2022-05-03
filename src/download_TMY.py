"""
download_TMY.py

Llamadas a la API de PVGIS para obtener datos climáticos en formato TMY.
Documentación de la API en:
https://joint-research-centre.ec.europa.eu/pvgis-photovoltaic-geographical-information-system/getting-started-pvgis/api-non-interactive-service_en

"""

#import argparse
import pandas as pd
import requests
import time
import os

from select_input import MUNICIPIOS_FILE_FORMATTED

DIR_TMY = "data/output/tmy/"
TIME_SLEEP = 0.05 


def select_lon_lat_from_ine_cod(ine_cod, df_municipios): # no lo usamos
    """
    Devuelve la información de latitud y longitud del municipio al que hace referencia
    el código INE
    Args:
        ine_cod (int)   Código INE del municipio
        df_municipios (pd.Dataframe)    Df con la información relevante sobre los municipios
    Return:
        lat (float)  latitud ETRS89
        lon (float)  longitud ETRS89    
    """
    data = df_municipios.loc[df_municipios['COD_INE'] == ine_cod, 
                ['LONGITUD_ETRS89', 'LATITUD_ETRS89']].values[0]
    lon, lat = data
    return lon, lat

def write_url(lat, lon):
    """
    Compone la url

    Args:
        lat (float) Latitud ETRS89 (en grados decimales).
        lon (float) Longitud ETRS89 (en grados decimales).
    """
    url = "https://re.jrc.ec.europa.eu/api/v5_2/tmy?lat={}&lon={}&outputformat=csv".\
        format(str(lat), str(lon))
    return url

def write_tmy_file(lon, lat, tmy_file_name):
    """
    0. Comprueba que el nombre del fichero no contenga "/", y si lo tiene lo
        sustituye por "__" para que no cause problema de rutas
    1. Comprueba que el fichero tmy especificado como parámetro no esté ya en 
        el directorio ${DIR_TMY}
    2. Escribe la url de consulta
    3. Descarga la información en el fichero
    """

    if "/" in tmy_file_name:
        tmy_file_name = tmy_file_name.replace("/", "__")
    if not os.path.isfile(tmy_file_name): # tmy_file_name not in os.listdir(DIR_TMY):
        url = write_url(lat, lon)
        data = requests.get(url)
        with open(DIR_TMY + tmy_file_name, 'wb') as f:
                print()
                print("Conectando con '{}' ...". format(url))
                print("...Descargando información en '{}'".format(tmy_file_name))
                print()
                f.write(data.content)
        # nos aseguramos de no exceder el límite de llamadas a la API
        time.sleep(TIME_SLEEP)


def main():
    
    # Cargamos los datos de los municipios (fichero formateado)
    df_municipios = pd.read_csv(MUNICIPIOS_FILE_FORMATTED, 
                                header=0,
                                dtype={'COD_INE': str,
                                        'COD_PROV': str,
                                        'PROVINCIA': str,
                                        'NOMBRE_ACTUAL': str,
                                        'LONGITUD_ETRS89': float,
                                        'LATITUD_ETRS89': float,
                                        'ALTITUD': float,
                                        'ARCHIVO_TMY': str})
    
    # Comprobamos que existe el directorio donde guardamos los TMY, si no, 
    # lo creamos
    if not os.path.isdir(DIR_TMY):
        os.makedirs(DIR_TMY)
    
    # Descargamos los datos TMY de cada municipio
    df_municipios.apply(lambda row: 
                            write_tmy_file(row['LONGITUD_ETRS89'],
                                        row['LATITUD_ETRS89'],
                                        row['ARCHIVO_TMY']),
                            axis=1)

if __name__=='__main__':
    main()
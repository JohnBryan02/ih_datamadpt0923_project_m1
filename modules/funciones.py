import argparse
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
import papermill

def ejecutar_notebook(output_path='output.ipynb', output_folder='C:/Users/piece/Documents/ironhack/projects/ih_datamadpt0923_project_m1/data'):
    try:
        # Ejecutar el notebook y guardar en la carpeta de salida
        papermill.execute_notebook(
            'importing_exporting_dfs.ipynb',
            output_path,
            parameters=dict(output_folder=output_folder)
        )
        print(f"El notebook se ejecutó correctamente. Los archivos CSV se guardaron en: {output_folder}")
    except Exception as e:
        print(f"Hubo un error al ejecutar el notebook: {str(e)}")

def bmcercano(lugar):
    df_libm = pd.read_csv('data/final_filas_libm_live.csv')
    filtro = df_libm[df_libm['name_li']== lugar]
    ordenamos = filtro.sort_values(by = 'bmdistance(m)')
    return ordenamos.iloc[0]

def bpcercano(lugar):
    df_libp = pd.read_csv('data/final_filas_libp_live.csv')
    filtro = df_libp[df_libp['name_li']== lugar]
    ordenamos = filtro.sort_values(by = 'bpdistance(m)')
    return ordenamos.iloc[0]

def argument_parser():
    parser = argparse.ArgumentParser(description= 'Estas en un lugar de interes especifico o quieres Todos')
    help_message ='dime un centro cultural o di Todos' 
    help_message2 = 'que quieres bicimad o bicipark'
    parser.add_argument('-f', '--hola', help=help_message)
    parser.add_argument('-b', '--bmobp', help=help_message2)
    args = parser.parse_args()
    return args
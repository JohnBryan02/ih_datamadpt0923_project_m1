# Data Project README file

### :raising_hand: **Nombre** 
Mis primeros spaguettis

### :baby: **Estado**
Ironhack Data Analytics Primer Proyecto Beta

### :running: **Utilidad**
Este proyecto consiste en obtener como resultado el bicimad o bicipark más cercano en función de los centros culturales de Madrid. Aparte de esta información también se añade la disponibilidad de las bicis actuales que hay en la estación cercana y un enlace directo a google maps para que el usuario pueda dirigirse a la estación.

### :computer: **Herramientas**
Python, visual studio, jupyter.


### :wrench: **Configuración**
Librerias que debes tener para que este programa funcione.
- import pandas as pd
- import requests
- import bs4
- from shapely.geometry import Point
- import geopandas as gpd
- import argparse
- from fuzzywuzzy import fuzz
- from fuzzywuzzy import process
- import os
- from dotenv import load_dotenv
- import argparse
- import papermill

### :see_no_evil: **Uso**
Al ejecutar el programa en una terminal se solicitarán dos o tres inputs().

- Primera opción(dos inputs): "Todos" + "bicimad o bicipark" esto generará un dataframe completo con centros culturales y bicimads o biciparks. 
Esto generara un dataframe completo con centros culturales y bicimads o biciparks
- Segunda opción(tres inputs): "Centro cultural" + "bicimad o bicipark" + "Si o No" esto ultimo nos dara un enlace a google maps si lo deseamos.
Esta opción generará un data frame de una única fila con el centro cultural seleccionado y el transporte elegido. Además, tendrás la opción de obtener un enlace a Google Maps.

Problema: tiempo de ejecución demasiado largo.

### :file_folder: **Estructura de carpetas**
```
└── ih_datamadpt0923_project_m1
    ├── .ipynb_checkpoints
    ├── _wip_
    └── data
    │   ├── final_filas_libm_live.csv
    │   └── final_filas_libp_live.csv
    ├── modules
    │   ├── funciones.py
    │   └── geocalculations.py     
    ├── notebooks
    │   └── importing_exporting_dfs.ipynb
    ├── LICENSE
    ├── .env
    ├── README.md
    └── main.py
```


### :shit: **ToDo**
Mejora del tiempo de ejecución.

### :love_letter: **Contact info**
John Bryan xxxxxxxx@gmail.com

---

import argparse
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


#leemos los csv
df_libm = pd.read_csv('../data/final_filas_libm_live.csv')
df_libp = pd.read_csv('../data/final_filas_libp_live.csv')

#hacemos una función para que nos de el bicimad más cercano en función del lugar de interes
def bmcercano(lugar):
    df_libm = pd.read_csv('../data/final_filas_libm_live.csv')
    filtro = df_libm[df_libm['name_li']== lugar]
    ordenamos = filtro.sort_values(by = 'bmdistance(m)')
    return ordenamos.iloc[0]
#bmcercano('Auditorio Carmen Laforet (Ciudad Lineal)')

#hacemos una función para que nos de el bicipark más cercano en función del lugar de interes
def bpcercano(lugar):
    df_libp = pd.read_csv('../data/final_filas_libp_live.csv')
    filtro = df_libp[df_libp['name_li']== lugar]
    ordenamos = filtro.sort_values(by = 'bpdistance(m)')
    return ordenamos.iloc[0]

#usamos parser para introducir los dos argumentos que el usuario necesita proporcionar
def argument_parser():
    parser = argparse.ArgumentParser(description= 'Estas en un lugar de interes especifico o quieres Todos')
    help_message ='dime un centro cultural o di Todos' 
    help_message2 = 'que quieres bicimad o bicipark'
    parser.add_argument('-f', '--hola', help=help_message)
    parser.add_argument('-b', '--bmobp', help=help_message2)
    args = parser.parse_args()
    return args

variable = argument_parser()
argumento = variable.hola
argumento2 = variable.bmobp

#cambiamos a una lista los lugares de interes
choices = df_libm['name_li'].to_list()

#print(type(argumento))
#print(argumento)

#creamos un if para que nos pida el input del usuario y añadimos fuzzy wuzzy para sea mas user friendly y el programa no falle
#separamos el input del lugar para que pueda decidir entre todos o un centro especifico.
input_argumento = input("Ingresa un centro cultural o escribe todos:")
if input_argumento.lower() == 'todos':
    argumento = 'todos'
    print("Has seleccionado {}".format(argumento))
    #pedimos que nos indique si quiere bicimad o bicipark
    argumento2 = input("¿Qué quieres, 'bicimad' o 'bicipark'?: ")
else:
    argumento_matches = process.extract(input_argumento, choices,limit = 2)
    argumento = argumento_matches[0][0]
    #pedimos que nos indique si quiere bicimad o bicipark
    argumento2 = input("¿Qué quieres, 'bicimad' o 'bicipark'?: ")

#hara esto si seleccionamos todo
if argumento.lower() == 'todos' and argumento2.lower() == 'bicimad':
    print("Genero el dataframe con todos los bicimad")
    print(df_libm)
elif argumento.lower() == 'todos' and argumento2.lower() == 'bicipark':
    print("Genero el dataframe con todos los bicipark")
    print(df_libp)
#apartir de aquí hara esto si seleccionamos un centro especifico
else:
    if argumento2.lower() == 'bicimad':
        resultado = bmcercano(argumento)
        print(resultado)
        print("genera el dataframe para el lugar indicado en argumento que es {}".format(argumento))
        #esto nos dara opción a que nos de el enlace directo a google maps para poder guiarse
        opcion_enlace = input("¿Deseas obtener un enlace? (Sí/No): ")
        if opcion_enlace.lower() == ('si'or 'sí'):
             enlace_google_maps = resultado['Google Maps']
             print("Aquí tienes el enlace a Google Maps: {}".format(enlace_google_maps))
        else:
            print("¡Gracias!")
    else:
        resultado = bpcercano(argumento)
        print(resultado)
        print("genera el dataframe para el lugar indicado en argumento que es {}".format(argumento))
        #esto nos dara opción a que nos de el enlace directo a google maps para poder guiarse        
        opcion_enlace = input("¿Deseas obtener un enlace? (Sí/No): ")
        if opcion_enlace.lower() == ('si'or'sí'):
             enlace_google_maps = resultado['Google Maps']
             print("Aquí tienes el enlace a Google Maps: {}".format(enlace_google_maps))
        else:
            print("¡Gracias!")
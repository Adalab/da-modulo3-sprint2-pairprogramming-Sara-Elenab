import pandas as pd
import numpy as np

#columnas a minúsculas
def columnas_minusculas(dataframe):
    """
    Función para cambiar los nombres de las columnas de un datframe a minúsculas y eliminar posibles espacios antes y después de los nombres
    
    Args:
        dataframe (DataFrame): dataframe 

    Returns:
        dataframe (DataFrame): Devuelve el mismo dataframe pero con el nombre de las columnas en minúsculas 
    """
    nuevas_columnas = {columna: columna.lower().strip() for columna in dataframe.columns}
    dataframe.rename(columns=nuevas_columnas, inplace= True)

    return dataframe

def nan_to_str(columna, cadena):
    """
    Convierte los datos nulos de una columna categórica al string introducido

    Args:
        columna (Series): columna de un dataframe donde cambiar los nulos por 'desconocido'
        cadena (str): un string por el que se quiere cambiar los valores nulos

    Returns:
        columna (Series): devuelve la columna del dataframe con los nulos cambiados
    """  
    return columna.replace(np.nan, cadena)

def cambiar_nombre_columnas(dataframe, diccionario):
    """
    Función para cambiar los nombres de las columnas de un datframe
    
    Args:
        dataframe (DataFrame): dataframe 
        diccionario (dict): diccionario dónde las llaves son los nombres de las columnas y los valores los nuevos nombres

    Returns:
        dataframe (DataFrame): Devuelve el mismo dataframe pero con el nombre de las columnas cambiado
    """
    dataframe.rename(columns=diccionario, inplace= True)

    return dataframe
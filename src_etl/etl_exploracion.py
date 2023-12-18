import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)

def leer_csv(archivo,num_col=0):
    """
    Función para convertir un archivo csv en un dataframe
    
    Args:
        archivo (str): Archivo csv separado por comas
        num_col (int): número de columnas que quieres que tenga el dataframe resultante (por defecto, 0 en cuyo caso no se tendrá en cuenta para crear el dataframe)

    Returns:
        df (DataFrame): Devuelve un dataframe directamente del archivo csv
    """

    if num_col == 0:
        dataframe = pd.read_csv(archivo)
    else:
        dataframe = pd.read_csv(archivo,usecols=range(num_col))
    return dataframe
    
    
def exploracion_dataframe(dataframe):
    """
    Función para explorar un dataframe
    
    Args:
        dataframe (DataFrame): dataframe para explorar

    Returns:
        Esta función no devuelve nada directamente, pero realiza varios prints con información de los datos incluidos en el dataframe
    """

    print(f"Los duplicados que tenemos en el conjunto de datos son: {dataframe.duplicated().sum()}")
    print("\n ..................... \n")
    display(dataframe.sample(10))
    display(dataframe.info())
    
    # generamos un DataFrame para los valores nulos
    print("Los nulos que tenemos en el conjunto de datos son:")
    df_nulos = pd.DataFrame(dataframe.isnull().sum() / dataframe.shape[0] * 100, columns = ["%_nulos"])
    display(df_nulos[df_nulos["%_nulos"] > 0])
    
    print("\n ..................... \n")
    print(f"Los tipos de las columnas son:")
    display(pd.DataFrame(dataframe.dtypes, columns = ["tipo_dato"]))
    
    
    print("\n ..................... \n")
    print("Los valores que tenemos para las columnas categóricas son: ")
    dataframe_categoricas = dataframe.select_dtypes(include = "O")
    
    for col in dataframe_categoricas.columns:
        print(f"La columna {col.upper()} tiene las siguientes valore únicos:")
        display(pd.DataFrame(dataframe[col].value_counts()))   
    
    
   
    
   



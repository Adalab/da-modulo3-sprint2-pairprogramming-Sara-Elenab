#%%
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
#%%
def leer_csv(archivo,num_col=0):
    if num_col == 0:
        dataframe = pd.read_csv(archivo,index_col=0)
    else:
        dataframe = pd.read_csv(archivo,usecols=range(num_col),index_col=0)
    return dataframe
    
    
def exploracion_dataframe(dataframe):
    
   
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
        display(pd.DataFrame(dataframe[col].value_counts()).head())   
    
    return dataframe 
    
   
    
   
# %%
df_clientes = leer_csv("Clientes.csv")
exploracion_dataframe(df_clientes)
# %%
df_productos = leer_csv("Productos.csv",6)
exploracion_dataframe(df_productos)
#%%
df_ventas= leer_csv("Ventas.csv")
exploracion_dataframe(df_ventas)

# %%


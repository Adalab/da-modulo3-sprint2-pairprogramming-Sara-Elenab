#%%
import pandas as pd
import numpy as np
from src_etl import etl_exploracion as e
from src_etl import etl_transformacion as t
from src_etl import etl_bbdd as b
from src_etl import queries as q

pd.set_option('display.max_columns', None)


# Exploración #
###############

# Cargamos los tres conjuntos de datos y los exploramos

# %%
## Clientes
df_clientes = e.leer_csv("data/clientes.csv")
e.exploracion_dataframe(df_clientes)

# %%
## Productos
df_productos = e.leer_csv("data/productos.csv",6)
e.exploracion_dataframe(df_productos)

#%%
## Ventas
df_ventas= e.leer_csv("data/ventas.csv")
e.exploracion_dataframe(df_ventas)

# %%
# Transformación #
##################

## Clientes
df_clientes = t.columnas_minusculas(df_clientes)

# nulos: 
    # - columna country nulos por moda (Spain)
df_clientes['country'] = t.nan_to_str(df_clientes['country'], 'Spain')

    # - resto de columnas nulos por desconocido (Spain)
desconocido_clientes  =['email', 'gender', 'city', 'address']
for col in desconocido_clientes:
    df_clientes[col] = t.nan_to_str(df_clientes[col], 'desconocido')

#col id to id_cliente
df_clientes= t.cambiar_nombre_columnas(df_clientes, {'id' : 'id_cliente'})


# %%
## Productos
df_productos = t.columnas_minusculas(df_productos)

#col in to id_producto
#df_productos.index.names = ['id_producto']
df_productos= t.cambiar_nombre_columnas(df_productos, {'id' : 'id_producto'})

#no nulos

#%%
## Ventas
df_ventas = t.columnas_minusculas(df_ventas)
df_ventas.index.names = ['id_cliente']
# fecha_venta a datetime
df_ventas['fecha_venta'] = pd.to_datetime(df_ventas['fecha_venta'])
#no nulos

#%%
# display(df_productos)
# display(df_clientes)
# display(df_ventas)
# print(df_productos.duplicated(subset='id_producto').sum())
# print(df_clientes.duplicated(subset='id_cliente').sum())
# print(df_ventas.duplicated(subset='id_cliente').sum())
print(df_ventas.duplicated(subset=['id_cliente', 'fecha_venta']).sum())
df_ventas.index.names = ['id_venta']

#%%
print("Clientes:")
display(df_clientes.info())
print("---------------\n")
print("Productos:")
display(df_productos.info())
print("---------------\n")
print("Ventas:")
display(df_ventas.info())
print("---------------\n")

# %%

## unir dataframes
#df_clientes_ventas = df_ventas.merge(df_clientes, on='id_cliente', how='left')

#%%
#df_productos_ventas_clientes = df_clientes_ventas.merge(df_productos, on='id_producto', how='left')
# #%%
#df_prod_ventas = df_productos.merge(df_ventas, on='id_producto', how='outer')

# # %%
#df_restaurante = df_prod_ventas.merge(df_clientes, left_index=True, right_index=True, how='outer')

df_cli_vent = df_clientes.merge(df_ventas, on='id_cliente', how='inner')
df_final = df_productos.merge(df_cli_vent, on='id_producto', how='inner' )

# %%
#display(df_prod_ventas.info())
#display(df_restaurante.info())

# display(df_clientes_ventas.info())
# display(df_productos_ventas_clientes.info())

display(df_cli_vent.info())
display(df_final.info())



# %%

# Exploración Unión#
####################

# %%
## Restaurante
e.exploracion_dataframe(df_final)


# %%
# Carga de datos #
##################

#ventas
#df_ventas = df_ventas.reset_index()
lista_tuplas_ventas = [tuple (fila) for fila in df_ventas.values]
print(lista_tuplas_ventas)
b.insertar_datos(q.query_insertar_ventas, "AlumnaAdalab", 'comida_italiana', lista_tuplas_ventas)

#productos
# lista_tuplas_productos = [tuple (fila) for fila in df_productos.values]
# b.insertar_datos(q.query_insertar_productos, "AlumnaAdalab", 'comida_italiana', lista_tuplas_productos)

#clientes
# lista_tuplas_clientes = [tuple (fila) for fila in df_clientes.values]
# b.insertar_datos(q.query_insertar_clientes, "AlumnaAdalab", 'comida_italiana', lista_tuplas_clientes)


# %%

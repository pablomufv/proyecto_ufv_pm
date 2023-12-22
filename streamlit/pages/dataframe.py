import pandas as pd

import streamlit as st
import requests

@st.cache_data
def load_data(url: str):

    #define la busqueda
    r=requests.get(url)
    
    #comprueba que el proceso de exposicion del puerto es correcto
    if r.status_code!=200:
        return None
        
    #lee los datos en formato json pues se expusieron como diccionario
    mijson=r.json()
    
    #accede a los objetos worker y los almacena en listas
    listado=mijson['workers']
    
    #Crea un dataframe con dichas listas
    df=pd.DataFrame.from_records(listado)
    
    #realiza la limpieza de los datos en determinados campos como:
    #iva
    df['work_year']=df['work_year'].str.replace('e', '')

    #formato decimal
    df['work_year']=df['work_year'].astype(int)

    return df

#establece la url o puerto de referencia de los datos
df=load_data('http://fastapi:8000/retrieve_data')

#Título de página
st.title('Vista del dataframe')

#
st.write("""Aquí puede seccionar el dataframe por campos y valores,
 con el objetivo de entender mejor toda la información presentada""")

#############
#st.write(df.columns)

selector_columnas=df.columns

#
filtro_columna=st.selectbox("Seleccione el campo", selector_columnas)

#
filtro_valor=st.selectbox("Seleccione el valor", pd.unique(df[filtro_columna]))

# dataframe filter
df_seleccionado=df[df[filtro_columna]==filtro_valor]

#Represento el dataframe en formato tabla
st.dataframe(df_seleccionado)
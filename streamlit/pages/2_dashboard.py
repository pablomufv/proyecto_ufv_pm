
"""
Establece el proceso de carga de datos desde el puerto de exposicion, y define los elementos y la disposicion de la pestaña de dashboard
"""

import pandas as pd

import streamlit as st
import plotly.express as px

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import RendererAgg

import requests
import seaborn as sns

#define el proceso de carga de los datos desde fastapi
@st.cache_data
def load_data(url: str):

    #define la busqueda
    r = requests.get(url)
    
    #comprueba que el proceso de exposicion del puerto es correcto
    if r.status_code != 200:
        return None
        
    #lee los datos en formato json pues se expusieron como diccionario
    mijson = r.json()
    
    #accede a los objetos worker y los almacena en listas
    listado = mijson['workers']
    
    #Crea un dataframe con dichas listas
    df = pd.DataFrame.from_records(listado)
    
    #realiza la limpieza de los datos en determinados campos como:
    #iva
    df['work_year'] = df['work_year'].str.replace('e', '')

    #formato decimal
    df['work_year'] = df['work_year'].astype(int)

    return df


#define un mensaje de texto
def info_box (texto, color=None):
    st.markdown(f'<div style = "background-color:#4EBAE1;opacity:70%"><p style="text-align:center;color:white;font-size:30px;">{texto}</p></div>', unsafe_allow_html=True)


#emplea el backend 
#matplotlib.use("Agg")

#establece la url o puerto de referencia de los datos
df_merged = load_data('http://fastapi:8000/retrieve_data')



"""
Establece el proceso de carga de datos desde el puerto de exposicion,
 y define los elementos y la disposicion de la pestaña de dashboard
"""

#############################
#CARGA DE LIBRERIAS
###########################

import pandas as pd

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

import matplotlib
import matplotlib.pyplot as plt

from matplotlib.backends.backend_agg import RendererAgg

import requests
import seaborn as sns

###############################
#DEFINICIONES PREVIAS
#############################

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
    st.markdown(f'<div style = "background-color:#FD7347;opacity:100%"><p style="text-align:center;color:white;font-size:20px;">{texto}</p></div>', unsafe_allow_html=True)



##########################################
#INTERFAZ GRÁFICA
#######################################

st.write(f"<style>body{{width: {100}vw;}}</style>", unsafe_allow_html=True)

#Título de página
st.title('Análisis descriptivo')

#establece la url o puerto de referencia de los datos
df_merged = load_data('http://fastapi:8000/retrieve_data')

#obtiene el numero de registros
registros = str(df_merged.shape[0])

#de niveles, residencias y trabajos
niveles = str(len(df_merged.experience_level.unique()))
residencia = str(len(df_merged.employee_residence.unique()))
trabajo = str(len(df_merged.job_title.unique()))

#obtiene las medias de salario y salario en dolares
salario_medio_dolares = str(round(df_merged.salary_in_usd.mean(),2))

#establece colores para seaborn
sns.set_palette("flare")

#selector de campos
optiony1=st.selectbox('Seleccione un eje Y',('Niveles de experiencia', 'Trabajos', 
'Países residencia', 'Países empresas', 'Tamaños empresas'))

#
st.session_state.optiony1=optiony1

###UN ST.WRITE COMENTANDO CADA RESULTADO
#
if optiony1=='Niveles de experiencia':
    ejey1="experience_level"
elif optiony1=='Trabajos':
    ejey1="job_title"
elif optiony1=='Países residencia':
    ejey1="employee_residence"
elif optiony1=='Países empresas':
    ejey1="company_location"
elif optiony1=='Tamaños empresas':
    ejey1="company_size"
else:
    st.write("Aqui aparecerá el contenido que seleccione")

#
st.session_state.ejey1=ejey1

#
st.write("Elija el tipo de gráfico\n")

#subpestañas y sus nombres
tab1, tab2 = st.tabs(["Diagrama de puntos", "Diagrama de sectores"])

####################################################################

df_merged=df_merged.sort_values(ejey1)
fig1=px.scatter(df_merged, x="salary_in_usd", y=ejey1, color=ejey1, color_continuous_scale="Viridis")

###Grafico de otra cosa
fig2=px.pie(df_merged, values="salary_in_usd", names=ejey1)

#incluimos en la primera subpestaña el grafico de puntos con plotly
with tab1:

    #Establecemos el título sobre la representación
    st.header(f"Salario en dolares - {optiony1}")

    #indicamos las columnas con las métricas
    kpi1, kpi2=st.columns(2)

    #presentamos el salario medio
    with kpi1:
        kpi1.metric(label="Salario medio $", value=str(round(df_merged.salary_in_usd.mean(),2)))
    
    #presentamos el número de valores categóricos únicos
    with kpi2:
        ejey1=st.session_state.ejey1
        kpi2.metric(label=f"Nº de {optiony1}", value=str(len(df_merged[ejey1].unique())))

    #establece un encabezado de página
    st.header("Gráfico de puntos sobre cada uno de los datos")

    #representamos el grafico de puntos con cada uno de los datos
    st.plotly_chart(fig1, theme="streamlit", use_container_width=False)

#incluye en la segunda subpestaña el grafico sectorial con plotly
with tab2:

    #representamos el gráfico sectorial o de torta
    st.plotly_chart(fig2, theme=None, use_container_width=True)
    
    
    
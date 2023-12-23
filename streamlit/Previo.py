"""
Define los elementos y formas de la página principal
"""

import streamlit as st
import time

#Define caracteristicas principales de la pagina inicial
st.set_page_config(page_title='Análisis de salarios', layout='wide', page_icon="📈")
st.image('ufv.png')

#Esto crea un objeto placeholder que es básicamente un contenedor vacío donde podemos mostrar cosas
placeholder=st.empty()

#declaramos que escribimos codigo dentro de ese placeholder
with placeholder:
    
    #muestra una animacion de carga
    for seconds in range(3):
        placeholder.write(f"⏳ {seconds} Cargando readme previo")
        time.sleep(1)

#finalmente limpia el contenido del placeholder para dejarlo vacío
placeholder.empty()

#
st.header("Práctica final de Programación II", divider="red")
st.write("Por Pablo Morán")

#mensaje en la barra lateral de pestañas
st.sidebar.success("Aquí puede elegir las páginas")

#texto de esta página en markdown
st.markdown(
    """
    En este servicio de interfaz gráfica tratamos de representar un conjunto de datos y sus diferentes métricas,
     sobre salarios de trabajadores de diferentes empresas a lo largo del mundo, cuya ocupación tiene que ver con 
     la ciencia de datos. Sobre esta misma página, encontrará una barra lateral con diferentes pestañas clicables.
"""
)

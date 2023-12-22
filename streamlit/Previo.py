
"""
Define los elementos y formas de la página principal
"""

import streamlit as st
import time

#Define caracteristicas principales de la pagina inicial
st.set_page_config(page_title='Análisis de salarios', layout='wide', page_icon="📈")
st.image('ufv.png')

#Esto crea un objeto placeholder que es básicamente un contenedor vacío donde podemos mostrar cosas
placeholder = st.empty()

#declaramos que escribimos codigo dentro de ese placeholder
with placeholder:
    #from PIL import Image
    #image = Image.open('mired.png')
    #placeholder.image(image, caption='MiRed semantic engine',use_column_width = 'always') 
    
    #muestra una animacion de carga
    for seconds in range(3):
        placeholder.write(f"⏳ {seconds} Cargando sistema")
        time.sleep(1)

#finalmente limpia el contenido del placeholder para dejarlo vacío
placeholder.empty()

#mensaje en grande
st.write("#Let's go")

#mensaje en la barra lateral de pestañas
st.sidebar.success("Aquí puedes elegir las páginas")

#texto de esta página en markdown
st.markdown(
    """
    Entrada
"""
)

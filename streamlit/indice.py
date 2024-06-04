import streamlit as st
import pandas as pd

# Configura la aplicación para que se abra en la página predeterminada
st.set_page_config(page_title="Mi aplicación Streamlit", layout="wide")


# Define CSS style for centering
style = """
<style>
h1 {
    text-align: center;
}
</style>
"""

# Inject CSS into the Streamlit app
st.markdown(style, unsafe_allow_html=True)

# Display the centered title
st.title("Análisis de Siniestros Viales en Buenos Aires.")

text_to_center = "Entre 2016 y 2021, Buenos Aires experimentó un aumento en los siniestros viales, resultando en un alto número de heridos y fallecidos. Los principales factores incluyeron la infraestructura deficiente, como calles mal diseñadas y señalización inadecuada, y el comportamiento irresponsable de los conductores, con infracciones como exceso de velocidad y distracciones al volante. Para abordar esta problemática, se están evaluando mejoras en la infraestructura vial y campañas de concienciación sobre la seguridad en el tránsito."

st.markdown(f"""
<center class="centered-text">
    {text_to_center}
</center>
""", unsafe_allow_html=True)

text = "Aquí analizaremos en profundidad los datos disponibles para una mejor comprensión de los hechos y las futuras soluciones que puedan prevenir el incremento de victmas."

st.markdown(f"""
<center class="centered-text">
    {text}
</center>
""", unsafe_allow_html=True)

st.markdown("***")

# Replace 'image.jpg' with the actual path to your image
image_path ='https://github.com/Brendromero/PI2_siniestros/blob/main/src/BA.jpg?raw=true'

st.markdown(f"""
<center>
    <img src="{image_path}" alt="My centered image" style="width: 957px; height: 538px;">
</center>
""", unsafe_allow_html=True)

st.markdown("***")

text_to_center = "Navega hacia las siguientes paginas para más información."

st.markdown(f"""
<center class="centered-text">
    {text_to_center}
</center>
""", unsafe_allow_html=True)

st.markdown("***")

# URL de la aplicación
app1_url = "https://visualizacionpy.streamlit.app/"

# Crear un botón que redirija a la URL especificada
if st.button('Ir a la visualización'):
    st.write(f"Redirigiendo a [Visualización]({app1_url})")
    st.experimental_set_query_params()
    js_code = f'window.open("{app1_url}");'
    st.components.v1.html(f'<script>{js_code}</script>', height=0)
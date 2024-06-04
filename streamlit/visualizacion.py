import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

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
st.title("Visualización de Siniestros Viales de la Ciudad de Buenos Aires.")
st.markdown("***")

st.markdown(f"""
<center>
<img style="display: block;-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://github.com/Brendromero/PI2_siniestros/blob/main/src/9-julio.webp?raw=true" width="900" height="438">
</center>
""", unsafe_allow_html=True)
st.markdown("***")

st.markdown("En esta sección, se presentan visualizaciones y análisis de datos.")

# Ruta absoluta al archivo
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "../dataset/siniestros.xlsx")

# Cargar los datos
siniestros = pd.read_excel(file_path)

# Visualizar datos
if st.checkbox("Visualizar datos"):
    st.write(siniestros)
    
# Mostrar head o tail del dataset
if st.checkbox("Ver las primeras o últimas filas del dataset"):
    option = st.radio("Seleccione una opción:", ("Head", "Tail"))
    if option == "Head":
        st.write(siniestros.head())
    elif option == "Tail":
        st.write(siniestros.tail())
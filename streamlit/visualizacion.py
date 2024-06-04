import streamlit as st
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
st.title("Visualización de los datos sobre Siniestros Viales.")

import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# ¡Hola, Monica! 👋
Esta app te ayudará con problemas de encoding.
""")

uploaded_file = st.file_uploader("", type=['csv'])
if uploaded_file is not None:
  #read csv
  df1=pd.read_csv(uploaded_file)
else:
  st.warning("Necesitas cargar el archivo csv")


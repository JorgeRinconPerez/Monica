import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# ¡Hola, Mónica! 👋
Esta app te ayudará con problemas de encoding.
""")

uploaded_file = st.file_uploader("", type=['csv'])
if uploaded_file is not None:
  #read csv
  df=pd.read_csv(uploaded_file, sep=";")
  st.write("Estas son las 10 primeras filas de tu archivo corregido")
  st.write(df.head(10))
  st.write("\n")

  @st.cache
  def convert_df(df):
    return df.to_csv(encoding="mbcs").encode('utf-8')
  csv = convert_df(df)
  st.write("\n")
  st.download_button(
    "Pulsa para descargar",
    csv,
    "Audited data.csv",
    "text/csv",
    key='download-csv')

else:
  st.warning("Para empezar necesitas cargar un archivo .csv")

# import library yang digunakan

import streamlit as st
from web_functions import load_data
from Tabs import home, dataset, predict, visualise
import predictall

Tabs = {
    "Beranda" : home,
    "Dataset" : dataset,
    "Klasifikasi" : predict,
    "Klasifikasi-CSV" : predictall,
    "Visualisasi" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

# membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# load dataset
data, df, x, y = load_data()

# Kondisi Call App Function
if page in ["Klasifikasi", "Dataset", "Visualisasi"]:
    Tabs[page].app(data, df, x, y)
else:
    Tabs[page].app()
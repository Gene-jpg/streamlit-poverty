import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
from sklearn import tree
import streamlit as st

from web_functions import train_model

def app(data, df, x, y):

    warnings.filterwarnings('ignore')
    #st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Sistem Klasifikasi Penduduk Miskin")

    
    model, score = train_model(x,y)
    plt.figure(figsize=(10,6))
    ConfusionMatrixDisplay.from_estimator(model, x, y, values_format='d')
    st.pyplot()

     # Membuat prediksi
    y_pred = model.predict(x)

    # Menghitung metrik evaluasi
    acc = accuracy_score(y, y_pred)
    prec = precision_score(y, y_pred, average='binary')  # Sesuaikan average jika kelas tidak seimbang
    rec = recall_score(y, y_pred, average='binary')

    # Menampilkan metrik
    st.write("### Metrik Evaluasi")
    st.write(f"- **Akurasi**: {acc * 100:.2f} %")
    # st.write(f"- **Presisi**: {prec* 100:.2f}")
    # st.write(f"- **Recall**: {rec* 100:.2f}")

    #     st.graphviz_chart(dot_data)

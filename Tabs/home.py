import streamlit as st

def app():

    # Judul Halaman Aplikasi
    st.title("Sistem Klasifikasi Penduduk Miskin Pemerintah Desa Sidorejo Metode Decision Tree")
    st.text("")
    st.text("")
    st.text("")

    # image_path = "kemiskinan.png"  # Ganti dengan path gambar Anda
    # st.image(image_path, caption="Ini adalah gambar contoh", use_column_width=True)

    st.markdown("<p style='font-size:20px;'>Selamat datang di Sistem Klasifikasi Penduduk Miskin Pemerintah Desa Sidorejo yang digunakan untuk membantu pendataan penduduk miskin di pemerintah Desa Sidorejo dengan menggunakan metode decision tree algoritma C45.</p>", unsafe_allow_html=True)
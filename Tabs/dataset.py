import streamlit as st

def app(data, df, x, y):
    # Judul Halaman Aplikasi
    st.title("Dataset Penduduk Miskin Desa Sidorejo")
    
    # Menampilkan jumlah data
    st.write(f"Jumlah data: {len(data)}")

    data.index = range(1, len(data) + 1)
    data.index.name = 'No'
    data.rename(columns={'nama': 'Nama', 'kelamin': 'Jenis Kelamin', 'pendidikan': 'Pendidikan',
                         'pekerjaan': 'Pekerjaan', 'jumlah_tanggungan': 'Tanggungan Anak',
                         'lantai_rumah': 'Lantai Rumah', 'dinding_rumah': 'Dinding Rumah', 
                         'daya_listrik': 'Daya Listrik', 'sumber_air': 'Sumber Air', 'keputusan': 'Keputusan'}, inplace=True)

    st.dataframe(data)  # Menampilkan data dalam bentuk tabel


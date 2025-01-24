import streamlit as st
from web_functions import predict

def app(data, df, x,y):

    st.title("Klasifikasi Penduduk Miskin")

    col1, col2 = st.columns(2)

    with col1:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_kelamin = {'Laki-laki': 0, 'Perempuan': 1}

        # Membuat select box dengan label pilihan
        pilih_kelamin = st.selectbox('Pilih jenis kelamin Anda', list(opsi_kelamin.keys()))
        
        # Mengambil nilai numerik berdasarkan pilihan
        kelamin = opsi_kelamin[pilih_kelamin]

    with col1:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_pendidikan = {'Perguruan Tinggi': 1, 'SMA/Sederajat': 2, 'SMP/Sederajat': 3, 'SD/Sederajat': 4, 'Tidak Sekolah' : 5}

        # Membuat select box dengan label pilihan
        pilih_pendidikan = st.selectbox('Pilih Pendidikan Anda', list(opsi_pendidikan.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        pendidikan = opsi_pendidikan[pilih_pendidikan]

    with col1:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_pekerjaan = {'Pegawai Negeri': 1, 'Pekerja Swasta': 2, 'Pedagang': 3 , 'Petani': 3, 'Buruh' : 4, 'Tidak Bekerja' : 5}

        # Membuat select box dengan label pilihan
        pilih_pekerjaan = st.selectbox('Pilih Pekerjaan Anda', list(opsi_pekerjaan.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        pekerjaan = opsi_pekerjaan[pilih_pekerjaan]

    with col1:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_tanggungan = {'0 Anak': 1, '1 Anak': 2, '2 Anak': 3, '3 Anak atau Lebih': 4}

        # Membuat select box dengan label pilihan
        pilih_tanggungan = st.selectbox('Jumlah Tanggungan Anak', list(opsi_tanggungan.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        jumlah_tanggungan = opsi_tanggungan[pilih_tanggungan]

    with col2:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_lantai = {'Keramik': 1, 'Tegel/Tembok': 2, 'Tanah/Bambu': 3}

        # Membuat select box dengan label pilihan
        pilih_lantai = st.selectbox('Jenis Lantai Rumah Anda', list(opsi_lantai.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        lantai_rumah = opsi_lantai[pilih_lantai]

    with col2:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_dinding = {'Tembok': 1, 'Semi-Tembok': 2, 'Kayu/Bambu': 3}

        # Membuat select box dengan label pilihan
        pilih_dinding = st.selectbox('Jenis Dinding Rumah Anda', list(opsi_dinding.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        dinding_rumah = opsi_dinding[pilih_dinding]

    with col2:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_listrik = {'900 VA': 1, '450 VA': 2}

        # Membuat select box dengan label pilihan
        pilih_listrik = st.selectbox('Daya Listrik Rumah Anda', list(opsi_listrik.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        daya_listrik = opsi_listrik[pilih_listrik]

    with col2:
        # Dictionary untuk memetakan pilihan ke nilai numerik
        opsi_air = {'PAM/Berbayar': 1, 'Sumur Bor': 2}

        # Membuat select box dengan label pilihan
        pilih_air = st.selectbox('Sumber Air Rumah Anda', list(opsi_air.keys()))

        # Mengambil nilai numerik berdasarkan pilihan
        sumber_air = opsi_air[pilih_air]

    features = [kelamin,pendidikan,pekerjaan,jumlah_tanggungan,lantai_rumah,dinding_rumah,daya_listrik,sumber_air]

    # Tombol Klasifikasi
    if st.button("Klasifikasi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Klasifikasi Sukses...")

        if (prediction == 1):
            st.warning("Penduduk Miskin")
        else:
            st.success("Penduduk Tidak Miskin")

        st.write("Model Yang digunakan Memiliki Tingkat Akurasi ", (score*100), "%")

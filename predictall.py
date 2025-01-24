import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("datamiskinsidorejo100.csv")   

df = df.drop(['nama'], axis = 1)
ind_col = [col for col in df.columns if col != 'keputusan']
dep_col = 'keputusan'
mapping = {
'kelamin': {'pria': 0, 'wanita': 1},
'pendidikan': {'perguruan tinggi': 1, 'sma': 2, 'smp': 3, 'sd': 4, 'tidak sekolah':5},
'pekerjaan': {'pegawai': 1, 'swasta':2, 'pedagang': 2, 'petani': 2, 'pedagang/petani': 2,'buruh': 3, 'tidak bekerja': 4},
'jumlah_tanggungan': {'0': 1, '1':2, '2': 3, '3': 4, '4': 4, '5': 4},
'lantai_rumah': {'keramik': 1, 'tegel/tembok': 2, 'tanah/bambu': 3},
'dinding_rumah': {'tembok': 1, 'semi-tembok': 2, 'kayu/bambu': 3},
'daya_listrik': {'900 va': 1, '450 va': 2},
'sumber_air': {'pam': 1, 'sumur': 2},
'keputusan': {'tidak miskin': 0, 'miskin': 1}
}

df = df.replace(mapping)

X = df[ind_col] #feature
y = df[dep_col] #label

# Bagi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Buat model dan latih
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Aplikasi Streamlit
def app():
    # Judul Halaman Aplikasi

    st.title("Klasifikasi Kemiskinan CSV")
    uploaded_file = st.file_uploader("Upload data baru (CSV)")
    if uploaded_file is not None:
        data_uji = pd.read_csv(uploaded_file)
        
        new_data = data_uji.drop(['nama'], axis = 1)
        mapping = {
        'kelamin': {'pria': 1, 'wanita': 2},
        'pendidikan': {'perguruan tinggi': 1, 'sma': 2, 'smp': 3, 'sd': 4, 'tidak sekolah':5},
        'pekerjaan': {'pegawai': 1, 'swasta':2, 'pedagang': 2, 'petani': 2, 'pedagang/petani': 2,'buruh': 3, 'tidak bekerja': 4},
        'jumlah_tanggungan': {'0': 1, '1':2, '2': 3, '3': 4, '4': 4, '5': 4},
        'lantai_rumah': {'keramik': 1, 'tegel/tembok': 2, 'tanah/bambu': 3},
        'dinding_rumah': {'tembok': 1, 'semi-tembok': 2, 'kayu/bambu': 3},
        'daya_listrik': {'900 va': 1, '450 va': 2},
        'sumber_air': {'pam': 1, 'sumur': 2, 'mata air/sungai': 3},
        }

        new_data = new_data.replace(mapping)
        
        prediction = model.predict(new_data)
        # st.write(" Prediksi Akurasi model:", accuracy * 100, "%")

        # Menampilkan data dalam bentuk tabel
        data_uji.index = range(1, len(data_uji) + 1)
        data_uji.index.name = 'No'
        data_uji.rename(columns={'nama': 'Nama', 'kelamin': 'Jenis Kelamin', 'pendidikan': 'Pendidikan',
                            'pekerjaan': 'Pekerjaan', 'jumlah_tanggungan': 'Tanggungan Anak',
                            'lantai_rumah': 'Lantai Rumah', 'dinding_rumah': 'Dinding Rumah', 
                            'daya_listrik': 'Daya Listrik', 'sumber_air': 'Sumber Air','keputusan': 'Keputusan'}, inplace=True)


        data_uji['Keputusan Prediksi'] = prediction
        data_uji['Keputusan Prediksi'] = data_uji['Keputusan Prediksi'].map({0: 'tidak miskin', 1: 'miskin'})

        # Menampilkan hasil
        # st.write(prediction)

        # Menampilkan hasil tabel
        st.dataframe(data_uji)

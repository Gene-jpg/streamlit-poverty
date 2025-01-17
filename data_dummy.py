import pandas as pd
import numpy as np

# Baca data CSV
file_path = 'data_dummy_penduduk.csv'  # Ganti dengan path file Anda
data = pd.read_csv(file_path)

# Tambahkan kolom status kemiskinan berdasarkan kriteria
def determine_poverty_status(row):
    # Contoh kriteria: penghasilan < 1 juta, tidak bekerja, atau pendidikan SD/sederajat
    if row['daya_listrik'] < '450 va' or row['pekerjaan'] == 'tidak bekerja' or row['pendidikan'] in ['tidak sekolah'] or row['dinding_rumah'] == 'kayu/bambu' or row['dinding_rumah'] == 'semi-tembok' :
        return 'Miskin'
    else:
        return 'Tidak Miskin'

data['keputusan'] = data.apply(determine_poverty_status, axis=1)

# Membuat data dummy
# Misalnya: 1 untuk Miskin, 0 untuk Tidak Miskin
#data['status_kemiskinan_dummy'] = data['status_kemiskinan'].apply(lambda x: 1 if x == 'Miskin' else 0)

# Simpan ke file baru
output_file = 'data_penduduk_dummy.csv'
data.to_csv(output_file, index=False)

print(f"Data dummy telah disimpan ke {output_file}")
import pandas as pd
import numpy as np

# Tentukan jumlah data dummy
jumlah_data = 300

# Membuat data dummy
np.random.seed(42)  # Agar hasil acak bisa direproduksi
data = {
    "nama": [f"Penduduk_{i+1}" for i in range(jumlah_data)],
    "kelamin": np.random.choice(["pria", "wanita"], jumlah_data),
    "pendidikan": np.random.choice(
        ["perguruan tinggi", "sma", "smp", "sd", "tidak sekolah"], jumlah_data),
    "pekerjaan": np.random.choice(
        ["pegawai", "swasta", "pedagang/petani", "buruh", "tidak bekerja"], jumlah_data),
    "jumlah_tanggungan": np.random.randint(0, 6, jumlah_data),
    "lantai_rumah": np.random.choice(
        ["keramik", "tegel/tembok", "tanah/bambu"], jumlah_data),
    "dinding_rumah": np.random.choice(
        ["tembok", "semi-tembok", "kayu/bambu"], jumlah_data),
    "daya_listrik": np.random.choice(
        ["900 va", "450 va"], jumlah_data),
    "sumber_air": np.random.choice(
        ["pam", "sumur"], jumlah_data),
    
}

# Menentukan status kemiskinan (contoh: pendapatan < 1.500.000 dianggap miskin)

batas_kemiskinan = "900 va"
data["keputusan"] = [
    "Miskin" if listrik < batas_kemiskinan else "Tidak Miskin"
    for listrik in data["daya_listrik"]
]

# Konversi ke DataFrame
df = pd.DataFrame(data)

# Tampilkan 5 data pertama
print(df.head())

# Simpan ke file CSV
df.to_csv("data_dummy_penduduk.csv", index=False)
print("Data dummy telah disimpan ke 'data_dummy_penduduk.csv'.")

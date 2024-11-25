#  Deteksi SMS Penipuan by Marchel Ferry Timoteus S(121140195)
Proyek ini adalah aplikasi web untuk mendeteksi SMS penipuan menggunakan teknik machine learning. Aplikasi ini dibangun dengan menggunakan Streamlit dan dapat diakses di link ini.

# Daftar Isi
- Deskripsi
- Fitur
- Instalasi
- Penggunaan
- Struktur Proyek

# Deskripsi
Aplikasi ini dirancang untuk membantu pengguna mendeteksi SMS penipuan dengan cepat dan mudah. Dengan memasukkan teks SMS, aplikasi akan memberikan prediksi apakah SMS tersebut merupakan penipuan atau tidak berdasarkan model machine learning yang telah dilatih.

# Fitur
Deteksi SMS penipuan secara real-time.
Antarmuka pengguna yang sederhana dan intuitif.
Dibangun dengan framework Streamlit untuk kemudahan penggunaan dan pengembangan.

# Instalasi
Untuk menjalankan proyek ini secara lokal, ikuti langkah-langkah berikut:

1. Clone repositori ini:
git clone https://github.com/marselferrys/SMS_Fraud_Detection

2. Masuk ke direktori proyek:
cd SMS_Fraud_Detection

3. Buat dan aktifkan virtual environment (opsional tapi disarankan):
python -m venv env
source env/bin/activate  # Untuk Windows, gunakan `env\Scripts\activate`

4. Instal dependensi:
pip install -r requirements.txt

5. Jalankan aplikasi:
streamlit run stream_nlp.py 

6. Login
username : "mfsamosir"
password : abc123

# Penggunaan
1. Buka aplikasi di browser Anda melalui link yang disediakan setelah menjalankan Streamlit.
2. Masukkan teks SMS yang ingin Anda periksa.
3. Klik tombol "Deteksi" untuk mendapatkan hasil prediksi.
   
# Struktur Proyek
..\SMS_Fraud_Detection

    README.md                           # Penjelasan project
    dataset_sms_spam_v1.csv             # Raw dataset
    key_norm.csv                        # Kata kunci utk kata singkatan
    model_fraud.sav                     # Model deteksi penipuan yang sudah dilatih
    new_selected_feature_tf-idf.sav     # pre-defined vocabulary 
    Fraud_SMS_Detection Notebook.ipynb  # File jupyter notebook model machine learning
    SMS Fraud Detection App.ipynb       # File jupyter notebook testing streamlit app on local
    requirements.txt                    # Daftar dependensi python
    stream_nlp.py                       # File utama Streamlit


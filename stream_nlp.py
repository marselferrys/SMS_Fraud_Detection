import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# --- USER AUTHENTICATION ---
# Data user untuk autentikasi
USER_DATA = {
    "names": ["Marchel Ferry Timoteus S"],
    "usernames": ["mfsamosir"],
    "passwords": ["abc123"]
}

# --- SESSION STATE ---
# Inisialisasi status login
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None

def check_login(username, password):
    """
    Memvalidasi username dan password.
    """
    if username in USER_DATA["usernames"] and password in USER_DATA["passwords"]:
        user_index = USER_DATA["usernames"].index(username)
        return USER_DATA["names"][user_index]  # Kembalikan nama pengguna jika valid
    return None

def logout():
    """
    Mengubah status menjadi logout dan membersihkan data user.
    """
    st.session_state.is_logged_in = False
    st.session_state.current_user = None

# --- LOGIN LOGIC ---
if not st.session_state.is_logged_in:
    # Halaman login
    st.title("Selamat Datang di SMS Fraud Detection")
    
    with st.form("login_form"):
        st.subheader("Silahkan Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

    # Proses login
    if submit:
        if username == "" or password == "":
            st.warning("Please enter your username and password")  # Validasi input kosong
        else:
            user_name = check_login(username, password)
            if user_name:
                st.session_state.is_logged_in = True
                st.session_state.current_user = user_name
                st.success(f"Welcome, {user_name}!")  # Sambutan setelah login berhasil
            else:
                st.error("Invalid username or password.")  # Notifikasi jika login gagal
else:
    # Sidebar dan halaman utama setelah login
    st.sidebar.title(f"Welcome, {st.session_state.current_user}!")
    st.title("Prediksi SMS Penipuan")

    # --- MAIN PROGRAM ---
    # Load model dan vektor TF-IDF
    try:
        model_fraud = pickle.load(open('model_fraud.sav', 'rb'))
        tfidf_vocab = pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))
        loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(tfidf_vocab))
    except FileNotFoundError as e:
        st.error("Model atau file TF-IDF tidak ditemukan.")
        st.stop()

    # Input teks SMS
    clean_teks = st.text_input("Masukkan Teks SMS")

    # Hasil deteksi penipuan
    if st.button("Hasil Deteksi"):
        if clean_teks.strip():  # Validasi input kosong
            try:
                predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
                if predict_fraud == 0:
                    st.success("SMS Normal")
                elif predict_fraud == 1:
                    st.success("SMS Penipuan")
                else:
                    st.success("SMS Promo")
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
        else:
            st.error("Teks tidak boleh kosong!")  # Notifikasi jika teks kosong

    # Tombol logout
    if st.sidebar.button("Logout"):
        logout()

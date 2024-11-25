import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit.runtime.legacy_caching as caching

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

# --- FUNGSI ---
def check_login(username, password):
    """
    Memvalidasi username dan password.
    """
    return username in USER_DATA["usernames"] and password in USER_DATA["passwords"]

def logout():
    """
    Menghapus cache dan mengubah status menjadi logout.
    """
    caching.clear_cache()
    st.session_state.is_logged_in = False
    st.experimental_rerun()

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
        elif check_login(username, password):
            st.session_state.is_logged_in = True
            user_index = USER_DATA["usernames"].index(username)
            st.success(f"Welcome, {USER_DATA['names'][user_index]}!")  # Sambutan setelah login berhasil
            st.experimental_rerun()
        else:
            st.error("Invalid username or password.")  # Notifikasi jika login gagal
else:
    # Sidebar dan halaman utama setelah login
    user_index = USER_DATA["usernames"].index(USER_DATA["usernames"][0])
    st.sidebar.title(f"Welcome, {USER_DATA['names'][user_index]}!")
    st.title("Prediksi SMS Penipuan")

    # --- MAIN PROGRAM ---
    # Load model dan vektor TF-IDF
    model_fraud = pickle.load(open('model_fraud.sav', 'rb'))
    tfidf_vocab = pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))
    loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(tfidf_vocab))

    # Input teks SMS
    clean_teks = st.text_input("Masukkan Teks SMS")

    # Hasil deteksi penipuan
    if st.button("Hasil Deteksi"):
        if clean_teks.strip():  # Validasi input kosong
            predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))
            if predict_fraud == 0:
                st.success("SMS Normal")
            elif predict_fraud == 1:
                st.success("SMS Penipuan")
            else:
                st.success("SMS Promo")
        else:
            st.error("Teks tidak boleh kosong!")  # Notifikasi jika teks kosong

    # Tombol logout
    if st.button("Logout"):
        logout()

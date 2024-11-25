import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Aditya Priadi Pradana", "Marchel Ferry Timoteus S", "Riski Nur Rohman", "Linda Septiana", "Monixca Fernandes Awangga Tirta"]
usernames = ["appradana", "mfsamosir", "rnrohman", "lsana", "mfatirta"]
passwords = ["xxx", "xxx", "xxx", "xxx", "xxx"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)
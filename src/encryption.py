from cryptography.fernet import Fernet
import pandas as pd

def generate_key():
    return Fernet.generate_key()

def encrypt_data(df, key):
    f = Fernet(key)
    encrypted_data = df.applymap(lambda x: f.encrypt(str(x).encode()).decode())
    return encrypted_data

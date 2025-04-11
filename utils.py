import pandas as pd

def load_reviews(file_path):
    return pd.read_csv(file_path)

def preprocess_text(text):
    return text.strip().lower()

import pandas as pd
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def load_dataset(filepath):
    df = pd.read_csv(filepath)
    df['sentence'] = df['sentence'].apply(clean_text)
    df['following_constituent'] = df['following_constituent'].apply(clean_text)
    return df

if __name__ == "__main__":
    df = load_dataset("dataset/dataset.csv")
    print("Dataset berhasil dimuat!")
    print("Jumlah data:", len(df))
    print()
    print(df.head())
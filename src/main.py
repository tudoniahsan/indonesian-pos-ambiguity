import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from preprocess import load_dataset
from classifier import classify

# Load dataset
df = load_dataset("dataset/dataset.csv")

# Prediksi setiap baris
predictions = []
for index, row in df.iterrows():
    pred = classify(row["word"], row["following_constituent"])
    predictions.append(pred)

df["prediction"] = predictions

# Hitung akurasi
correct = (df["POS"] == df["prediction"]).sum()
accuracy = correct / len(df)

print("=== HASIL EVALUASI ===")
print(f"Total data   : {len(df)}")
print(f"Benar        : {correct}")
print(f"Salah        : {len(df) - correct}")
print(f"Akurasi      : {accuracy:.2%}")

# Simpan hasil ke CSV
df.to_csv("results/results.csv", index=False)

# Error analysis
errors = df[df["POS"] != df["prediction"]]
errors.to_csv("results/error_analysis.csv", index=False)

print()
print("=== ERROR ANALYSIS ===")
print(f"Total error  : {len(errors)}")
print()
print("Error per kata:")
print(errors.groupby("word")[["POS","prediction"]].value_counts().to_string())
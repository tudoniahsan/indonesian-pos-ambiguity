import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
import matplotlib.pyplot as plt

# Load hasil
df = pd.read_csv("results/results.csv")

# Hitung akurasi per kata
words = df["word"].unique()
accuracies = []

for word in words:
    subset = df[df["word"] == word]
    acc = (subset["POS"] == subset["prediction"]).sum() / len(subset)
    accuracies.append(acc * 100)

# Buat grafik
plt.figure(figsize=(10, 6))
bars = plt.bar(words, accuracies, color="steelblue", edgecolor="black")

# Tambah angka di atas bar
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, 
             bar.get_height() + 1, 
             f"{acc:.1f}%", 
             ha="center", fontsize=10)

plt.title("Akurasi per Kata — Indonesian POS Ambiguity Resolution", fontsize=13)
plt.xlabel("Kata")
plt.ylabel("Akurasi (%)")
plt.ylim(0, 110)
plt.axhline(y=82.89, color="red", linestyle="--", label="Rata-rata: 82.89%")
plt.legend()
plt.tight_layout()
plt.savefig("results/accuracy_chart.png")
plt.show()
print("Grafik disimpan di results/accuracy_chart.png")
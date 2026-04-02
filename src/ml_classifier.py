import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pandas as pd
from preprocess import load_dataset
from features import extract_features
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = load_dataset("dataset/dataset.csv")

# Exclude sama — category shift not determined by following constituent
df = df[df['word'] != 'sama'].copy()

# Extract features untuk setiap baris
feature_list = []
for index, row in df.iterrows():
    f = extract_features(row["following_constituent"])
    f["word"] = row["word"]
    feature_list.append(f)

# Buat feature dataframe
feat_df = pd.DataFrame(feature_list)

# Encode kolom word dan boolean jadi angka
feat_df["has_predicate"] = feat_df["has_predicate"].astype(int)
feat_df["has_pronoun"] = feat_df["has_pronoun"].astype(int)
feat_df["has_modal"] = feat_df["has_modal"].astype(int)

word_encoder = LabelEncoder()
feat_df["word"] = word_encoder.fit_transform(feat_df["word"])

# Label
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df["POS"])

# Features
X = feat_df[["word", "has_predicate", "has_pronoun", "has_modal", "token_length"]]

# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi
accuracy = accuracy_score(y_test, y_pred)

print("=== ML CLASSIFIER RESULTS ===")
print(f"Total evaluated : 215 (sama excluded)")
print(f"Train set       : {len(X_train)} sentences")
print(f"Test set        : {len(X_test)} sentences")
print(f"Akurasi ML      : {accuracy:.2%}")
print()
print("=== COMPARISON ===")
print(f"Rule-based      : 82.33% (215 sentences evaluated)")
print(f"ML (Logistic)   : {accuracy:.2%} (test set only, 80/20 split)")
print()
print("=== DETAIL PER KELAS ===")
print(classification_report(
    y_test, y_pred,
    labels=range(len(label_encoder.classes_)),
    target_names=label_encoder.classes_,
    zero_division=0
))
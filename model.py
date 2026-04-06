import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import re

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df = pd.read_csv("Resume.csv")

df = df[["Resume_str", "Category"]].copy()
df.columns = ["resume", "role"]

df.dropna(inplace=True)

df["resume"] = df["resume"].apply(clean_text)
df["role"] = df["role"].apply(clean_text)

df = df.head(2000).reset_index(drop=True)

df["combined"] = df["resume"] + " " + df["role"]

vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2), max_features=5000)
matrix = vectorizer.fit_transform(df["combined"])

with open("data.pkl", "wb") as f:
    pickle.dump(df, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("matrix.pkl", "wb") as f:
    pickle.dump(matrix, f)

print("Model ready!")
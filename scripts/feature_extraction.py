import json
import os
import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Paths
INPUT_PATH = "data/processed/resumes.json"
OUTPUT_PATH = "data/processed/tfidf_features.pkl"

# Load processed resumes
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    resumes = json.load(f)

# Extract text and categories
resume_texts = [resume["text"] for resume in resumes]
categories = [resume["category"] for resume in resumes]  # Labels

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000)  # Limiting to 5000 most important words
tfidf_matrix = vectorizer.fit_transform(resume_texts)

# Save the TF-IDF model and feature matrix
os.makedirs("data/processed", exist_ok=True)
with open(OUTPUT_PATH, "wb") as f:
    pickle.dump((tfidf_matrix, categories, vectorizer), f)

print(f"✅ TF-IDF feature extraction completed. Saved to {OUTPUT_PATH}")

import os
import pandas as pd
import re
import json
import spacy
import nltk
from nltk.corpus import stopwords

# Download NLTK stopwords if not present
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load SpaCy model for Named Entity Recognition (NER)
nlp = spacy.load("en_core_web_sm")

# Paths
DATA_PATH = "data/ResumeDataSet.csv"
#DATA_PATH = "data\ResumeDataSet_Cleaned.csv"
OUTPUT_PATH = "data/processed/resumes.json"
#OUTPUT_PATH = "data/processed/resumes2.json"

# Function to clean text
def clean_text(text):
    text = re.sub(r"\n", " ", text)  # Remove newlines
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase
    text = " ".join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Function to extract skills and entities using spaCy
def extract_entities(text):
    doc = nlp(text)
    skills = []
    education = []
    experience = []

    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE"]:  # Organizations (Can be universities)
            education.append(ent.text)
        elif ent.label_ in ["DATE"]:  # Dates (Can be experience-related)
            experience.append(ent.text)
        elif ent.label_ in ["PRODUCT", "WORK_OF_ART"]:  # Approximate skill extraction
            skills.append(ent.text)

    return {
        "skills": list(set(skills)),
        "education": list(set(education)),
        "experience": list(set(experience)),
    }

# Read dataset
df = pd.read_csv(DATA_PATH, encoding="utf-8")

# Process each resume
processed_resumes = []
for index, row in df.iterrows():
    resume_text = clean_text(row["Resume"])  # Assuming "Resume" is the column name
    extracted_data = extract_entities(resume_text)

    processed_resumes.append({
        "id": index,
        "category": row["Category"],  # Assuming "Category" is a column
        "text": resume_text,
        "skills": extracted_data["skills"],
        "education": extracted_data["education"],
        "experience": extracted_data["experience"],
    })

# Save processed data
os.makedirs("data/processed", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(processed_resumes, f, indent=4)

print(f"✅ Processed {len(processed_resumes)} resumes and saved to {OUTPUT_PATH}")

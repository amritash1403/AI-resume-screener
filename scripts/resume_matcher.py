import pickle
import os
import re
import spacy
import fitz  # PyMuPDF for PDF text extraction
import nltk
from nltk.corpus import stopwords
from sklearn.preprocessing import LabelEncoder

# Download NLTK stopwords if not present
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Paths
MODEL_PATH = "models/svm_resume_classifier.pkl"

# Load trained model and vectorizer
with open(MODEL_PATH, "rb") as f:
    svm_model, vectorizer, label_mapping = pickle.load(f)

# Reverse mapping to get category names
label_decoder = {idx: label for label, idx in label_mapping.items()}

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"❌ Error extracting text from PDF: {e}")
    return text.strip()

# Function to clean extracted text
def clean_text(text):
    text = re.sub(r"\n", " ", text)  # Remove newlines
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase
    text = " ".join([word for word in text.split() if word not in stop_words])  # Remove stopwords
    return text

# Function to predict job category from PDF resume
def predict_resume_category(pdf_path):
    resume_text = extract_text_from_pdf(pdf_path)  # Extract text from PDF
    if not resume_text:
        print("❌ No text found in the PDF. Please upload a valid resume.")
        return None, None

    cleaned_text = clean_text(resume_text)  # Clean extracted text
    tfidf_vector = vectorizer.transform([cleaned_text])  # Convert to TF-IDF format
    predicted_label_index = svm_model.predict(tfidf_vector)[0]  # Predict category index
    predicted_category = label_decoder[predicted_label_index]  # Convert to category name

    # Get confidence scores for all categories
    confidence_scores = svm_model.predict_proba(tfidf_vector)[0]
    top_matches = sorted(zip(label_mapping.keys(), confidence_scores), key=lambda x: x[1], reverse=True)

    print("\n🔹 Predicted Job Category:", predicted_category)
    print("\n🔹 Top Matching Categories:")
    for job, score in top_matches[:3]:  # Show top 3 matches
        print(f"   {job}: {score:.2f}")

    return predicted_category, top_matches[:3]

# Test the function
if __name__ == "__main__":
    sample_pdf = r"C:\Users\Harsh Kumar\OneDrive\Documents\Placement Information\1CR21AI025_HARSH KUMAR_RESUME.pdf"  # Replace with an actual PDF file path
    predict_resume_category(sample_pdf)

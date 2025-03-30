import os
import pickle
import fitz  # PyMuPDF for PDF text extraction
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize Flask app
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["SECRET_KEY"] = "supersecretkey"

# Ensure upload directory exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# Load trained model and vectorizer
MODEL_PATH = r"C:\Users\Harsh Kumar\OneDrive\Documents\Extion Infotech Projects\resume_screening\models\svm_resume_classifier.pkl"
with open(MODEL_PATH, "rb") as f:
    svm_model, vectorizer, label_mapping = pickle.load(f)
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

# Function to predict job category
def predict_resume_category(pdf_path):
    resume_text = extract_text_from_pdf(pdf_path)
    if not resume_text:
        return None, None

    tfidf_vector = vectorizer.transform([resume_text])
    predicted_label_index = svm_model.predict(tfidf_vector)[0]
    predicted_category = label_decoder[predicted_label_index]

    confidence_scores = svm_model.predict_proba(tfidf_vector)[0]
    top_matches = sorted(zip(label_mapping.keys(), confidence_scores), key=lambda x: x[1], reverse=True)

    return predicted_category, top_matches[:3]

# Route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "resume" not in request.files:
            flash("❌ No file uploaded!")
            return redirect(request.url)

        file = request.files["resume"]

        if file.filename == "":
            flash("❌ No file selected!")
            return redirect(request.url)

        if file and file.filename.endswith(".pdf"):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            predicted_category, top_matches = predict_resume_category(filepath)
            return render_template("result.html", category=predicted_category, matches=top_matches)

        else:
            flash("❌ Please upload a valid PDF file!")
            return redirect(request.url)

    return render_template("index.html")

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)

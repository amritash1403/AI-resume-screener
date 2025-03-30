📌 README.md for AI-Powered Resume Screening


# 📝 Project Title:

AI-Powered Resume Screening System

# 🎯 Project Description

This project automates the resume screening process using Natural Language Processing (NLP) and Machine Learning (ML). The system extracts skills, experience, and qualifications from resumes (PDFs) and matches them to job descriptions. It provides recruiters with ranked recommendations based on the best fit.

With 99.48% accuracy achieved using SVM (Support Vector Machine), this system significantly enhances hiring efficiency.

# 🚀 Features

✅ Upload resumes in PDF format
✅ Extracts skills, experience, and qualifications
✅ Uses TF-IDF vectorization for feature extraction
✅ SVM model with 99.48% accuracy for classification
✅ Ranked recommendations for better hiring decisions
✅ Dark mode support for better UI experience
✅ Flask-based web app for easy interaction

# 🏗 Project Structure

📂 AI_Resume_Screener
│── 📂 data
│   ├── ResumeDataSet.csv                # Original dataset
    ├── ResumeDataSet_Cleaned.csv        #one mode dataset i have added just to check
│   ├── processed
│   │       # Cleaned dataset after preprocessing
│── 📂 models
│   ├── svm_resume_classifier.pkl        # Trained SVM model
│── 📂 scripts
│   ├── data_preprocessing.py            # Cleans and preprocesses data
│   ├── feature_extraction.py            # Extracts text features using TF-IDF
│   ├── model_training.py                # Trains the SVM model
│   ├── resume_matcher.py                # Matches resumes to job descriptions
│── 📂 webapp
│   │── 📂 static
│   │   ├── script.js                     # JS for frontend behavior
│   │   ├── style.css                      # CSS with dark mode support
│   │── 📂 templates
│   │   ├── index.html                     # Resume upload page
│   │   ├── result.html                    # Results page showing matches
│   │── 📂 uploads                          # Folder to store uploaded resumes
│   │── app.py                              # Main Flask application
│── requirements.txt                         # Required Python dependencies
│── README.md                                # Project documentation

# 🛠 Technologies Used

🔹 Python
🔹 Flask (for web application)
🔹 Scikit-learn (for ML model training)
🔹 Natural Language Processing (NLP)
🔹 Support Vector Machine (SVM)
🔹 TF-IDF (Term Frequency-Inverse Document Frequency)
🔹 PyPDF2 (for PDF text extraction)
🔹 Bootstrap 5 (for UI)

# 📊 Model Performance

✅ Algorithm: Support Vector Machine (SVM)
✅ Accuracy: 99.48%
✅ Evaluation Metrics: High Precision & Recall

# 🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/amritash1403/AI-resume-screener.git
cd AI-Resume-Screener

2️⃣ Create a Virtual Environment

python -m venv resume-screening-env
source resume-screening-env/bin/activate  # Mac/Linux
resume-screening-env\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Application

python webapp/app.py

Access the web app at http://127.0.0.1:5000/

# 📌 Usage Guide

1️⃣ Upload resumes in PDF format
2️⃣ System extracts skills & experience
3️⃣ Resumes are matched with job descriptions
4️⃣ Ranked recommendations are displayed

# 🔥 Future Enhancements

🔹 Support for multiple resume uploads
🔹 Advanced NLP with BERT/GPT models
🔹 Integration with real-time job portals

# 📝 License

This project is open-source under the MIT License.


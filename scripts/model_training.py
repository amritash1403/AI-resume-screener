import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Paths
FEATURES_PATH = "data/processed/tfidf_features.pkl"
MODEL_PATH = "models/svm_resume_classifier.pkl"

# Load the TF-IDF features and labels
with open(FEATURES_PATH, "rb") as f:
    tfidf_matrix, categories, vectorizer = pickle.load(f)

# Convert labels (categories) to a format suitable for ML
unique_labels = list(set(categories))
label_mapping = {label: idx for idx, label in enumerate(unique_labels)}
y = [label_mapping[cat] for cat in categories]

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, y, test_size=0.2, random_state=42)

# Initialize and train the SVM classifier
svm_model = SVC(kernel="linear", probability=True)  # Linear kernel works well for text data
svm_model.fit(X_train, y_train)

# Make predictions on test data
y_pred = svm_model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=unique_labels))

# Save the trained model
os.makedirs("models", exist_ok=True)
with open(MODEL_PATH, "wb") as f:
    pickle.dump((svm_model, vectorizer, label_mapping), f)

print(f"✅ Model training complete. Saved model to {MODEL_PATH}")

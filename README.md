Automated Resume Screening System (ARSS)
💼 Overview
In today’s fast-paced recruitment environment, HR departments receive thousands of resumes for job openings, making manual screening time-consuming and error-prone. The Automated Resume Screening System (ARSS) is designed to streamline and automate the resume evaluation process using Machine Learning (ML) and Natural Language Processing (NLP).

This system intelligently analyzes resumes, extracts key features like skills, experience, and qualifications, and categorizes candidates efficiently—significantly reducing the workload for recruiters.

🚀 Features
📂 Upload and parse resumes

🧠 Classify candidate resumes using machine learning (KNN, NLP)

🧾 Extracts and evaluates data based on:

Skills

Experience

Education

📊 Visualizes resume categories and data insights

🔍 Helps HR professionals identify suitable candidates quickly

🧰 Tech Stack & Libraries
Frontend: HTML, CSS, JavaScript

Backend: Python with Flask

Libraries/Frameworks:

scikit-learn

pandas

NumPy

matplotlib

seaborn

pickle

re (Regex)

openpyxl (for reading Excel files)

nltk (Natural Language Toolkit)

📁 Project Structure
php
Copy
Edit
Automated-Resume-Screening/
│
├── app.py                      # Flask app entry point
├── UpdatedResumeDataSet.xlsx  # Resume dataset
├── model/                      # Contains pickled ML models
│   ├── resume_model.pkl
│   ├── vectorizer.pkl
│
├── templates/                  # HTML templates
│   ├── index.html
│   └── result.html
│
├── static/                     # CSS, JS, images
│
├── generate_resume_model.py   # Script to train and save resume classification model
├── create_vectorizer.py       # Vectorizer training and saving
├── generate_pickle.py         # (Optional) Merges model/vectorizer into one step
├── requirements.txt           # List of required Python packages
🧪 How to Run
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/yourusername/Automated-Resume-Screening.git
cd Automated-Resume-Screening
2. Set up a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Generate model files
bash
Copy
Edit
python generate_resume_model.py
python create_vectorizer.py
5. Run the Flask App
bash
Copy
Edit
python app.py
6. Open in browser
Go to: http://127.0.0.1:5000

📌 Future Improvements
Integrate OCR for PDF/Docx resume uploads

Add support for real-time job description matching

Enhance UI with React or Vue.js

Deploy to cloud using AWS/GCP/Azure

👥 Authors
M. Prasanna Kumar & Team – Final Year B.Tech Project (2025)

📄 License
This project is developed for academic purposes.

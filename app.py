from flask import Flask, render_template, request
import pandas as pd
import re
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)

# Load pickled vectorizer
vectorizer_path = os.path.join('model', 'vectorizer.pkl')
with open(vectorizer_path, 'rb') as f:
    vectorizer = pickle.load(f)

# --- Preprocessing Function ---
def preprocess_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', str(text)).lower()

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/process', methods=['POST'])
def process():
    file = request.files['file']
    job_description = request.form.get('job_description', '').strip()
    
    if not file or not job_description:
        return render_template('index.html', result=[])

    ext = file.filename.split('.')[-1]
    try:
        if ext == 'csv':
            data = pd.read_csv(file)
        elif ext in ['xls', 'xlsx']:
            data = pd.read_excel(file)
        else:
            return render_template('index.html', result=[])
    except Exception:
        return render_template('index.html', result=[])

    if 'Resume' not in data.columns:
        return render_template('index.html', result=[])

    # Clean and preprocess
    data = data[['Resume']].dropna().head(10)
    data['Candidate'] = [f"Candidate {chr(65+i)}" for i in range(len(data))]
    data['cleaned_resume'] = data['Resume'].apply(preprocess_text)

    # Use the submitted job description
    job_vector = vectorizer.transform([preprocess_text(job_description)])

    resume_vectors = vectorizer.transform(data['cleaned_resume'])
    similarity_scores = cosine_similarity(job_vector, resume_vectors).flatten()

    # Convert similarity scores to percentages (0-100)
    data['ATS_Score'] = (similarity_scores * 100).round().astype(int)
    data = data.sort_values(by='ATS_Score', ascending=False).reset_index(drop=True)
    data['Rank'] = data.index + 1

    result = data[['Candidate', 'ATS_Score', 'Rank']].to_dict(orient='records')
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

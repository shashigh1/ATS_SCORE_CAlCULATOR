# 📄 ATS Resume Score Calculator (AI-Powered)

An AI-powered web app to evaluate how well your resume matches a job description using semantic similarity. Built using **Streamlit**, **Sentence Transformers**, and **NLP** techniques — ideal for job seekers looking to optimize their resume for Applicant Tracking Systems (ATS).

---

## 🔗 Demo

🚀 [Click here to use the app](https://ats-score-calculator-skk.streamlit.app/)

---

## ✨ Features

✅ Upload resume in **PDF or DOCX** format  
✅ Paste any **job description**  
✅ Get a real-time **ATS match score** (semantic similarity)  
✅ Powered by **Sentence Transformers**  
✅ Lightweight, fast, and fully browser-based  

---

## 📸 Preview
<img width="960" height="759" alt="Screenshot 2025-07-26 183001" src="https://github.com/user-attachments/assets/a7b89ad5-269d-4599-9e81-06eb8b4418bc" />

---

## 🧠 How It Works

1. **Text Extraction**  
   - PDF → via `PyPDF2`  
   - DOCX → via `python-docx`

2. **Text Embedding**  
   - Embeds resume and job description using `paraphrase-MiniLM-L6-v2` from `sentence-transformers`

3. **Similarity Calculation**  
   - Uses **cosine similarity** to compute a match score between resume and job description

4. **Score Output**  
   - Displays a percentage match score and a progress bar in the UI

---

## 🛠️ Tech Stack

| Component           | Library/Tool               |
|---------------------|----------------------------|
| Web App             | Streamlit                  |
| NLP Model           | Sentence Transformers      |
| PDF Parsing         | PyPDF2                     |
| DOCX Parsing        | python-docx                |
| ML Utils            | scikit-learn, numpy, pandas|

---

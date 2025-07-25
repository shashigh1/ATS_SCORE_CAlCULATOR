import streamlit as st
from io import BytesIO
from resume_parser import extract_text_from_pdf, extract_text_from_docx
from score_engine import get_similarity_score

st.title("📄 ATS Resume Score Calculator (AI-Powered)")
st.markdown("Upload your Resume and paste the Job Description to get your ATS Match Score.")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("Paste the Job Description here:")

if resume_file and jd_text:
    if resume_file.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(resume_file)
    else:
        resume_text = extract_text_from_docx(resume_file)

    if resume_text.strip() == "":
        st.error("Could not extract text from resume.")
    else:
        score = get_similarity_score(resume_text, jd_text)
        st.markdown(f"### 🎯 ATS Score: **{score}%**")
        st.progress(score / 100)  # Fix: normalize to [0.0, 1.0]


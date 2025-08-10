import streamlit as st
import tempfile
from utils.extractor import extract_text_from_pdf, extract_text_from_docx
from agent.meeting_agent import analyze_meeting

st.title("AI Meeting Minutes Agent")

uploaded_file = st.file_uploader("Upload your meeting transcript (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])

if st.button("Process Transcript"):
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        
        if uploaded_file.name.endswith(".pdf"):
            transcript = extract_text_from_pdf(tmp_path)
        elif uploaded_file.name.endswith(".docx"):
            transcript = extract_text_from_docx(tmp_path)
        else:
            transcript = open(tmp_path, "r").read()
        
        st.subheader("📄 Processed Output")
        result = analyze_meeting(transcript)
        st.write(result)
    else:
        st.warning("Please upload a file first.")

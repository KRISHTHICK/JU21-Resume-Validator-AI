import streamlit as st
from utils.extract import extract_text
from agent.validator_agent import validate_resume

st.set_page_config(page_title="Resume Validator AI", layout="centered")
st.title("📄 Resume Validator AI")

uploaded_file = st.file_uploader("Upload your resume (.pdf or .docx)", type=["pdf", "docx"])
job_role = st.selectbox("Select a job role to match", ["Data Scientist", "Software Engineer", "Product Manager"])

if uploaded_file and job_role:
    with st.spinner("Analyzing your resume..."):
        text = extract_text(uploaded_file)
        report = validate_resume(text, job_role)

    st.subheader("Validation Report")
    st.markdown(report)
    st.download_button("Download Report", report, file_name="Resume_Validation_Report.txt")

import streamlit as st
import google.generativeai as genai
genai.configure(api_key="AIzaSyCcBdD1457j4lIgzYuH025l3SRtVTJvrek")
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Cover Letter Generator")

job_title = st.text_input("Job Title")
summary = st.text_area("Resume Summary")

if st.button("Generate Cover Letter"):
    prompt = f"""
    Write a professional cover letter for the role of {job_title}
    using the following resume summary:
    {summary}
    """
    response = model.generate_content(prompt)
    st.write(response.text)

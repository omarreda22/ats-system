import streamlit as st
import requests
import base64

from PyPDF2 import PdfReader
from docx import Document

from .utils import extract_text_from_pdf, extract_text_from_docx

API_KEY = "AIzaSyB1ddWMMS0A8JwgmGq6aW67eKAUMoSmzNA"


def analyze_documents(resume_text, job_description):
    custom_prompt = f"""
    Please analyze the following resume in the context of the job description provided. Strictly check every single line in job description and analyze my resume whether there is a match exactly. Strictly maintain high ATS standards and give scores only to the correct ones. Focus on hard skills which are missing and also soft skills which are missing. Provide the following details.:
    1. The match percentage of the resume to the job description. Display this.
    2. A list of missing keywords accurate ones.
    3. Final thoughts on the resume's overall match with the job description in 3 lines.
    4. Recommendations on how to add the missing keywords and improve the resume in 3-4 points with examples.
    Please display in the above order don't mention the numbers like 1. 2. etc and strictly follow ATS standards so that analysis will be accurate. Strictly follow the above templates omg. don't keep changing every time.
    Strictly follow the above things and template which has to be displayed and don't keep changing again and again. Don't fucking change the template from above.
    Title should be Resume analysis and maintain the same title for all. Also if someone uploads the same unchanged resume twice, keep in mind to give the same results. Display new ones only if they have changed their resume according to your suggestions or at least few changes.
    Job Description: {job_description}
    Resume: {resume_text}
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"role": "user", "parts": [{"text": custom_prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

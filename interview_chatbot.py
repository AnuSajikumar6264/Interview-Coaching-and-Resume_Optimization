from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define the function to generate a response from the Gemini model
def get_gemini_response(input, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated model name
    response = model.generate_content([input, prompt])
    return response.text

# Define the Streamlit app for mock interview
st.set_page_config(page_title="Job Interview Preparation Bot")
st.header("Job Interview Preparation System")
input_text = st.text_area("Enter Job Role or Interview Focus:", key="input")

# Mock interview flow
interview_type = st.selectbox(
    "Select Mock Interview Focus:",
    ("Behavioral", "Technical", "Situational", "General", "Skills-based")
)

submit1 = st.button("Start Mock Interview")
submit2 = st.button("Get Feedback")

# Interview Prompts
interview_prompts = {
    "Behavioral": """
    You are a recruiter conducting a behavioral interview. Ask questions that are designed to assess the candidate's experience in handling various situations.
    Use the STAR (Situation, Task, Action, Result) method to evaluate the responses.
    """,
    "Technical": """
    You are a technical interviewer for a software engineer position. Ask coding and problem-solving questions related to algorithms, data structures, and system design.
    Provide hints and guidance based on the candidate's answers.
    """,
    "Situational": """
    You are conducting a situational interview. Pose hypothetical job-related scenarios and assess how the candidate would handle them.
    Focus on decision-making and problem-solving abilities.
    """,
    "General": """
    You are conducting a general interview. Ask questions related to the candidate's career goals, strengths, weaknesses, and motivations.
    Evaluate their communication skills, fit for the job, and overall impression.
    """,
    "Skills-based": """
    You are assessing the candidate's specific technical skills. Ask about their expertise in areas like programming languages, tools, frameworks, or specific skills related to the job.
    Provide feedback on their response.
    """
}

# Mock interview or feedback generation
if submit1:
    if input_text:
        prompt = interview_prompts.get(interview_type, "")
        response = get_gemini_response(input_text, prompt)
        st.subheader(f"{interview_type} Interview Question:")
        st.write(response)
    else:
        st.write("Please enter the job role or interview focus.")

elif submit2:
    if input_text:
        prompt = f"""
        You are a recruiter giving feedback on a candidate's answer to a mock interview. Provide constructive feedback, highlighting strengths and areas for improvement.
        The candidate's answer: {input_text}
        """
        response = get_gemini_response(input_text, prompt)
        st.subheader("Interview Feedback:")
        st.write(response)
    else:
        st.write("Please enter a response for feedback.")

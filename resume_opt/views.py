import os
import base64
import io
from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
from PIL import Image
import pdf2image
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def index(request):
    return render(request, 'resume_opt/index.html', {})


def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    images = pdf2image.convert_from_bytes(uploaded_file.read())
    first_page = images[0]
    img_byte_arr = io.BytesIO()
    first_page.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    return [{"mime_type": "image/jpeg", "data": base64.b64encode(img_byte_arr).decode()}]

def upload_resume(request):
    if request.method == 'POST':
        input_text = request.POST.get("job_description")
        uploaded_file = request.FILES.get("resume")
        action = request.POST.get("action")

        if uploaded_file:
            try:
                pdf_content = input_pdf_setup(uploaded_file)
                prompt = "Your evaluation prompt here..."
                response = get_gemini_response(input_text, pdf_content, prompt)
                return JsonResponse({"response": response})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
    return render(request, "resume_opt/upload_resume.html")

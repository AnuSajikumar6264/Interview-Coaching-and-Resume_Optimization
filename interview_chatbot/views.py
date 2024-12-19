from django.shortcuts import render
from django.http import JsonResponse
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def index(request):
    return render(request, 'interview_chatbot/index.html', {})


def chatbot_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get("user_input")
        if user_input:
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([user_input])
                return JsonResponse({"response": response.text})
            except Exception as e:
                return JsonResponse({"error": str(e)}, status=500)
    return render(request, "interview_chatbot/chatbot.html")

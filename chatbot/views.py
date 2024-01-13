import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
import google.generativeai as genai
from IPython.display import display
from django.http import JsonResponse
from django.views.decorators.http import require_POST

genai.configure(api_key="AIzaSyBScJtnFsDnlhV6ns9qsz0XlTT-Q3s6PNQ")
model = genai.GenerativeModel('gemini-pro')

os.environ['GOOGLE_API_KEY'] = "AIzaSyBKFnOBKkoUfF7GZVmjEYER4X9Mzw3p9oE"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

chat_model = genai.GenerativeModel('gemini-pro')


@require_POST
def handle_chat(request):
    chat = chat_model .start_chat(history=[])
    user_message = request.POST.get('message', '')
    response = chat.send_message("You are a bot that gives counsellor in Attention-deficit/hyperactivity disorder (ADHD).There is a patient that is suffering from this disease and wants to know more about these. ")
    response = chat.send_message(user_message)
    outputofbot = response.text
    return JsonResponse({'response': outputofbot})


    

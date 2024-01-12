from django.http import HttpResponse
from django.shortcuts import render,redirect
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from django.http import JsonResponse
from django.views.decorators.http import require_POST

genai.configure(api_key="AIzaSyBScJtnFsDnlhV6ns9qsz0XlTT-Q3s6PNQ")
model = genai.GenerativeModel('gemini-pro')



# def handle_chat(request):
#     if request.method=='POST':
#         user_input = request.POST['message']
#         if not user_input:
#            return redirect('home')
#       
#         output = response.text
#         return render(request,'home.html',{'output':output})

    


@require_POST
def handle_chat(request):
    user_message = request.POST.get('message', '')
    response = model.generate_content(user_message)
    bot_response=response.text
    return JsonResponse({'response': bot_response})

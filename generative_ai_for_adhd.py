# !pip install -q -U google-generativeai
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "API KEY HERE"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

chat_model = genai.GenerativeModel('gemini-pro')
###
chat = chat_model .start_chat(history=[])

response = chat.send_message("You are a bot that gives counsellor in Attention-deficit/hyperactivity disorder (ADHD).There is a patient that is suffering from this disease and wants to know more about these. ")
response = chat.send_message("Question from frontend here")
outputofbot=response.text
import warnings
warnings.filterwarnings("ignore")

import google.generativeai as genai

genai.configure(api_key="AIzaSyBjSw94fARVmJtt3FfcrJg1KaRvons1Eps")

model=genai.GenerativeModel("models/gemini-2.5-flash")

while True:
    user=input("You: ")
    if user.lower()=="exit":
        break;
    response=model.generate_content(user)
    print("ChatBot: ",response.text)
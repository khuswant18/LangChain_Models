from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() 
model = GoogleGenerativeAI(model="gemini-2.5-pro")

while True:
    user_input = input('You:')
    if user_input=="exit":
        break 

    result = model.invoke(user_input)
    print("AI",result) 
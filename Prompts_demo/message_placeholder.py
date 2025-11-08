from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_google_genai import GoogleGenerativeAI 
from dotenv import load_dotenv 
load_dotenv()

model = GoogleGenerativeAI(model="gemini-2.5-pro") 

chat_tempelate = ChatPromptTemplate([ 
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'), #abhi tak jitni bhi baat hui hai usse chat history mai save karliya tha ab agli baar user ka ai ko context rahega kya baat hui thi 
    ('human','{query}')
])

chat_history = []

with open('Prompts_demo/chat_history.txt',"r") as f:
    for line in f:
        chat_history.append(("human", line.strip()))

prompt = chat_tempelate.invoke({'chat_history':chat_history,"query":"where is my refund"})
model.invoke(prompt)  
print(prompt) 
 
 

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
) 

model = ChatHuggingFace(llm=llm) 

temp1 = PromptTemplate(
    template= "Write a detailed prompt on {topic}",
    input_variables=['topic']
)

temp2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=['text']
)

prompt1 = temp1.invoke({'topic': "black hole"})
result1 = model.invoke(prompt1)
print("First result:", result1)

prompt2 = temp2.invoke(result1.content)
result2 = model.invoke(prompt2)
print("\nSummary:", result2) 
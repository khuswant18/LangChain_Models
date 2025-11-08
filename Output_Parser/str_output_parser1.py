from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
) 

parser = StrOutputParser()

model = ChatHuggingFace(llm=llm) 

temp1 = PromptTemplate(
    template= "Write a detailed prompt on {topic}",
    input_variables=['topic']
)

temp2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=['text']
)

chain = temp1 | model | parser | temp2 | model | parser  

result = chain.invoke({"topic":"black hole"})

print(result) 




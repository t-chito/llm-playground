from langchain_openai import ChatOpenAI
from openai import OpenAI

llm_openai = ChatOpenAI(temperature=0, model="gpt-4-turbo-preview")
client = OpenAI
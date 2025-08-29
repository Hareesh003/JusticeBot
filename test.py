
import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    api_key=os.getenv('FEATHERLESS_API_KEY'),
    base_url="https://api.featherless.ai/v1",
    model="mistralai/Mistral-7B-Instruct-v0.2",
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    (
        "human",
        "I love programming."
    ),
]
ai_msg = llm.invoke(messages)
print(ai_msg)
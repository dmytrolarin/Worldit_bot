''' 
Модуль для роботи з API OpenAI

У цьому файлі прописана логіка взаємодії бота з серверами OpenAI,
що дозволить боту формувати відповіді на основі штучного інтелекту
'''
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# 
load_dotenv()
# 
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")
# 
client_openai = AsyncOpenAI(api_key= OPENAI_SECRET_KEY)

async def get_response_from_chatgpt(question):
    ''''''
    #
    response = await client_openai.chat.completions.create(
        model = "gpt-4o-mini", #
        messages = [{
            "role": "user", #
            "content": question # 
        }]
    )
    #
    return response.choices[0].message.content

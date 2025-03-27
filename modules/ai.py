''' 
Модуль для роботи з API OpenAI

У цьому файлі прописана логіка взаємодії бота з серверами OpenAI,
що дозволить боту формувати відповіді на основі штучного інтелекту
'''
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

# Знаходимо файл ".env"
load_dotenv()

# Отримуємо секретний ключ OpenAI з файлу ".env" та зберігаємо у константу
OPENAI_SECRET_KEY = os.getenv("OPENAI_SECRET_KEY")
# Створюємо об'єкт OpenaAI для асинхронних запитів та підключаємо секертний ключ
client_openai = AsyncOpenAI(api_key= OPENAI_SECRET_KEY)

async def get_response_from_chatgpt(question):
    '''Функція надсилає запит до ChatGPT та повертає відповідь'''

    # Формуємо запит до ChatGPT та зберігаємо відовідь у об'єкт response
    response = await client_openai.chat.completions.create(
        model = "ft:gpt-4o-mini-2024-07-18:personal::BFjgOzAt", # Модель ChatGPT, на яку користувач зробить запит
        messages = [
        {
            'role':'system',
            'content': "Ти -  бот на Discord-сервері IT-школи WorldIT призначений для надання студентам відповідей у веселій формі щодо навчання в нашій школі."
        },
        {
            "role": "user", # Вказуємо, що запитання від користувача
            "content":  question # Контент запитання від користувача
        }]
    )
    # Повертаємо контент відповіді від ChatGPT
    return response.choices[0].message.content

''' 
Модуль для роботи з API OpenAI

У цьому файлі прописана логіка взаємодії бота з серверами OpenAI,
що дозволить боту формувати відповіді на основі штучного інтелекту
'''
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import io

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

async def get_image_from_dalle(prompt):
    '''Функкція генерує зображення за промптом на основі моделі DALL-E
    та повертає url згенерованого зображення'''

    # Формуємо запит до серверів OpenAI для генерацій зображень
    response = await client_openai.images.generate(
        model = "dall-e-3", # Модель DALL-E
        prompt = prompt, # Промпт (запит з описом зображення, яке треба згенероувати)
        size = "1024x1024", # Розмір зображення
        quality = "standard" # Якість зображення
    )
    # Повертаємо URL згенерованого зображення
    return response.data[0].url

async def get_speech_from_tts(input):
    '''Функція, що повертає файл, згенерований на основі моделі TTS (Text To Speech).
    Файл, що поверне функція буде ауйдіофайлом з озвученим текстом'''

    # Формуємо запит до серверів OpenAI для аудіо на основі тексту
    response = await client_openai.audio.speech.create(
        model = "gpt-4o-mini-tts", # Модель TTS
        voice = "ash", # Голос озвучування
        input = input # Запит (текст, який треба озвучити)
    )
    # Створюємо об'єкт файлу, який збережено до оперативної пам'яті
    audio_file = io.BytesIO(response.content)
    # Повертаємо аудіофайл
    return audio_file
    
    
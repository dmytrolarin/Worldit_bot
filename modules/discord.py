'''
Модуль для роботи з API discord 

У цьому файлi прописана логiка взаємодiї бота з  discord сервером
(отримання, обробка та вiдправлення повiдомлень на сервер)
'''
from discord import Intents, Client
from .ai import get_response_from_chatgpt 
from dotenv import load_dotenv
import os

# Знаходимо файл ".env"
load_dotenv()

# Отримуємо токен з файлу ".env" для роботи з Discord-ботом та зберігаємо у константу
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Створюємо об'єкт, що надає боту базові права (напр., отримувати повідомлення без контенту, відслідковувати нових учасників сервера тощо)
intents = Intents.default()
# Надаємо боту право на читання вмісту повідомлень
intents.message_content = True
# Створюємо об'єкт бота з попередньо вказаними правами
bot_client = Client(intents = intents)

# Декоратор, що робить функцію нижче подією бота
@bot_client.event
async def on_ready():
    '''Функція-подія, що відпрацює, коли бот буде запщено (бот стане онлайн)'''

    # Отримуємо ім'я бота
    name_bot = bot_client.user
    # Виводимо інформацію у консоль, що бот з відповідним іменем запущено
    print(f"{name_bot} запущено")
    
# Декоратор, що робить функцію нижче подією бота
@bot_client.event
async def on_message(message):
    '''Функція-подія, що відпрацює, коли бот отримає повідомлення від користувача'''
    
    # Перевірка, чи не є автором отриманого повідомлення сам бот
    if message.author != bot_client.user:
        # Отримуємо відповідь від ChatGPT
        response = await get_response_from_chatgpt(message.content)
        # Отримуємо поточний канал, де повідомлення було надсілано
        current_channel = message.channel
        # Бот насдилає повідомлення у поточний канал
        await current_channel.send(response)

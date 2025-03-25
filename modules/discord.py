'''
Модуль для роботи з API discord 

У цьому файлi прописана логiка взаємодiї бота з  discord сервером
(отримання, обробка та вiдправлення повiдомлень на сервер)
'''
from discord import Intents, Client

# 
TOKEN = ""

# 
intents = Intents.default()
# 
intents.message_content = True
# 
bot_client = Client(intents = intents)

# 
@bot_client.event
async def on_ready():
    ''''''
    #
    name_bot = bot_client.user
    # 
    print(f"{name_bot} запущено")
    
# 
@bot_client.event
# 
async def on_message(message):
    ''''''
    
    #
    if message.author != bot_client.user:
        # 
        content_message = message.content
        # 
        await message.channel.send(content_message)

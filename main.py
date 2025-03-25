''' 
Головний модуль для запуску дiскорд бота
'''
from modules import discord, ai


def main():
    ''''''
    
    # 
    discord.bot_client.run(token = discord.TOKEN)

# 
if __name__ == '__main__':
    # 
    main()
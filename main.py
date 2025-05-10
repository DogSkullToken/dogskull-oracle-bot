import os
import asyncio
import threading
from dotenv import load_dotenv
import nest_asyncio

from bot.twitter_bot import iniciar_twitter_bot
from bot.telegram_bot import iniciar_telegram_bot

# 🧠 Habilita reuso de loop no Windows (VS Code, etc)
nest_asyncio.apply()

# 🔁 Carrega variáveis do arquivo .env
load_dotenv()

# 🧙 Rodar bot do Telegram com suporte a asyncio
def run_telegram_bot():
    asyncio.run(iniciar_telegram_bot())

if __name__ == "__main__":
    print("🔁 Iniciando Twitter bot...")
    twitter_thread = threading.Thread(target=iniciar_twitter_bot)
    twitter_thread.start()

    print("🧙 Iniciando Telegram bot...")
    run_telegram_bot()

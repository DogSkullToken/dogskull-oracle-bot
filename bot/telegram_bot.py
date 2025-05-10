import asyncio
import nest_asyncio
import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot.oracle import gerar_profecia
from bot.config import TELEGRAM_TOKEN, STATIC_IMAGE_PATH

# Ativa log para ver erros
logging.basicConfig(level=logging.INFO)

# Corrige problema de loop no Windows/VSCode
nest_asyncio.apply()

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Welcome to DogSkull Oracle! Use /prophecy to receive a vision.")

# Comando /prophecy com tratamento de erro
async def profecia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        texto = gerar_profecia()
        await update.message.reply_text(f"📜 Prophecy:\n{texto}")
    except Exception as e:
        logging.error(f"Erro ao gerar profecia: {e}")
        await update.message.reply_text("⚠️ The Oracle is silent... Something went wrong.")

# Comando /image
async def imagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open(STATIC_IMAGE_PATH, 'rb') as img:
            await update.message.reply_photo(photo=InputFile(img))
    except Exception as e:
        logging.error(f"Erro ao enviar imagem: {e}")
        await update.message.reply_text("⚠️ Could not send the image.")

# Comando /stop
async def parar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⛔ The Oracle is now resting...")

# Inicializa o bot
async def iniciar_telegram_bot():
    if not TELEGRAM_TOKEN:
        print("❌ TELEGRAM_TOKEN está vazio. Verifique seu .env.")
        return

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("prophecy", profecia))
    app.add_handler(CommandHandler("image", imagem))
    app.add_handler(CommandHandler("stop", parar))

    print("🤖 Telegram bot running...")
    await app.run_polling()

# Execução direta
if __name__ == "__main__":
    asyncio.run(iniciar_telegram_bot())

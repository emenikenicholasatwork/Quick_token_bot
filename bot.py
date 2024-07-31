import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Updater, Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Quick Bot", web_app=WebAppInfo(url="https://main--quicktokenbot.netlify.app/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Welcome! Quick bot under product but thanks to NKY.. you can have an overview  😇😇😇', reply_markup=reply_markup)

def main() -> None:
    application = Application.builder().token(BOT_TOKEN).build();
    application.add_handler(CommandHandler("start", start))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
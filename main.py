import os
import telebot
from telebot import types

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

GRUPO_LINK = "https://t.me/+9Q3TlnPHo4llNTc5"
CANAL_LINK = "https://t.me/+9Q3TlnPHo4llNTc5"
STORIES_LINK = "https://t.me/+9Q3TlnPHo4llNTc5"

MSG_START = "Se você chegou até aqui, é porque está interessado no que viu na bio🤭"

def send_buttons(chat_id):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("💥 Acessar Grupo Exclusivo", url=GRUPO_LINK))
    keyboard.add(types.InlineKeyboardButton("🔥 Canal da Maya", url=CANAL_LINK))
    keyboard.add(types.InlineKeyboardButton("📸 Stories", url=STORIES_LINK))
    bot.send_message(chat_id, MSG_START, reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start(message):
    send_buttons(message.chat.id)

print("Bot rodando...")
bot.infinity_polling()

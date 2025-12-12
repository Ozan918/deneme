import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")   # Render ortam değişkeni
bot = telebot.TeleBot(TOKEN)

BOT_ADI = "@m3ulive_bot"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 f"Merhaba! 👋\n\nBen {BOT_ADI}.\n"
                 "M3U8 yayın botuyum. Bana bir link veya komut gönder :)")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Mesajını aldım: " + message.text)

bot.infinity_polling()

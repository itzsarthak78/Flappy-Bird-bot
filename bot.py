import telebot
from telebot import types
from flask import Flask
from threading import Thread

# --- 1. SET YOUR VARIABLES HERE ---
TOKEN = "YOUR_BOT_TOKEN_HERE"
GAME_URL = "https://itzsarthak78.github.io/Flappy-Bird/"
START_MSG = "🐦 **Welcome to Flappy Bird!**\n\nTap the button below to start your adventure and set a high score!"
PLAY_MSG = "🕹️ **Ready to flap?**\nClick the button to open the game in your Telegram."

# --- 2. INITIALIZE BOT ---
bot = telebot.TeleBot(TOKEN)
app = Flask('')

@app.route('/')
def home():
    return "Bot is Online!"

# --- 3. COMMAND HANDLERS ---
def get_keyboard():
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(GAME_URL)
    btn = types.InlineKeyboardButton(text="🕹️ Play Now", web_app=web_app)
    markup.add(btn)
    return markup

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, START_MSG, reply_markup=get_keyboard(), parse_mode="Markdown")

@bot.message_handler(commands=['play'])
def handle_play(message):
    bot.send_message(message.chat.id, PLAY_MSG, reply_markup=get_keyboard(), parse_mode="Markdown")

# --- 4. ANTI-SLEEP WEB SERVER ---
def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- 5. START BOT ---
if __name__ == "__main__":
    keep_alive()  # Starts the web server
    print("Bot is running...")
    bot.infinity_polling()
    

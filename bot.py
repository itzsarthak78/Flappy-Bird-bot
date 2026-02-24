import telebot
from telebot import types

# 1. Paste your Bot Token from @BotFather here
TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

# 2. Your Game URL (must be HTTPS)
GAME_URL = "https://itzsarthak78.github.io/Flappy-Bird/"

def get_game_keyboard():
    """Helper function to create the Web App button."""
    markup = types.InlineKeyboardMarkup()
    # WebAppInfo opens the link inside Telegram as an overlay
    web_app = types.WebAppInfo(GAME_URL)
    btn = types.InlineKeyboardButton(text="🕹️ Play Flappy Bird", web_app=web_app)
    markup.add(btn)
    return markup

# Handler for both /start and /play commands
@bot.message_handler(commands=['start', 'play'])
def send_welcome(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    
    welcome_text = (
        f"Hi {user_name}! 🐦\n\n"
        "Welcome to the **Flappy Bird Bot**. "
        "Challenge your friends and beat the high score!\n\n"
        "Tap the button below to start playing right now."
    )
    
    bot.send_message(
        chat_id, 
        welcome_text, 
        reply_markup=get_game_keyboard(),
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("Bot is starting... Press Ctrl+C to stop.")
    bot.infinity_polling()
  

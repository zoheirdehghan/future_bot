import logging
logging.basicConfig(level=logging.DEBUG)

print("🚀 Bot is starting...")
from dotenv import load_dotenv
load_dotenv()

import os
import openai
import telebot

# خواندن کلیدها
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
import os
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
print("🔑 TELEGRAM_TOKEN =", TELEGRAM_TOKEN)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY
if TELEGRAM_TOKEN:
    print("🔑 TELEGRAM_TOKEN =", TELEGRAM_TOKEN[:8] + "…")
else:
    print("❌ TELEGRAM_TOKEN is None!")
if OPENAI_API_KEY:
    print("🔑 OPENAI_API_KEY =", OPENAI_API_KEY[:8] + "…")
else:
    print("❌ OPENAI_API_KEY is None!")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(msg):
    bot.reply_to(msg, "سلام! هر چیزی بپرس تا آینده‌ت رو پیش‌بینی کنم.")

@bot.message_handler(func=lambda m: True)
def handle_all(msg):
    prompt = (
        "You are a mystical fortune teller. "
        f"The user says: \"{msg.text}\". "
        "Predict their future in a fun, creative style."
    )
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}],
            max_tokens=150
        )
        fortune = resp.choices[0].message.content.strip()
    except Exception:
        fortune = "متأسفم، الان پیش‌گویی در دسترس نیست."
    bot.reply_to(msg, fortune)

if __name__ == "__main__":
    print("🚀 Bot is starting…")    # ← این خط را اضافه کن
    print("✅ Starting the bot now...")
while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=100, long_polling_timeout=100)
        except Exception as e:
            print("⚠️ Polling error:", e)
            time.sleep(15)

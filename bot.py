import os
import time
import logging
import telebot
import openai
from flask import Flask
from threading import Thread
from dotenv import load_dotenv

# تنظیمات لاگ
logging.basicConfig(level=logging.DEBUG)

# بارگذاری متغیرهای محیطی
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    raise ValueError("❌ Error: Missing TELEGRAM_TOKEN or OPENAI_API_KEY in environment variables.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# پاسخ به دستور /start
@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, "سلام! 🤖 من ربات پیش‌بینی آینده هستم. پیام بده تا آینده‌ات رو پیش‌بینی کنم!")

# پاسخ به همه پیام‌ها
@bot.message_handler(func=lambda m: True)
def handle_all(msg):
    try:
        prompt = f"You are a mystical fortune teller. Predict the user's future in a fun, creative style.\nUser: {msg.text}\nPrediction:"
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        fortune = resp.choices[0].message.content.strip()
        bot.reply_to(msg, fortune)
    except Exception as e:
        print("❌ Error:", e)
        bot.reply_to(msg, "خطایی رخ داد، دوباره تلاش کن.")

# اجرای بات در یک Thread
def start_bot():
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            print("Polling error:", e)
            time.sleep(5)

# وب‌سرور برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running successfully on Render!"

if __name__ == "__main__":
    Thread(target=start_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

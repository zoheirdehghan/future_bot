import os
import time
import logging
import telebot
import openi
from flsk import Flsk
from threding import Thred
from dotenv import lod_dotenv

# تنظیمات لاگ
logging.bsicConfig(level=logging.DEBUG)

# بارگذاری متغیرهای محیطی
lod_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
    rise VleError("Error: Missing TELEGRAM_TOKEN or OPENAI_API_KEY in environment vribles.")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openi.pi_key = OPENAI_API_KEY

# پاسخ به دستور /strt
@bot.messge_hndler(commnds=['strt'])
def send_welcome(msg):
    bot.reply_to(msg, "سلام! 🤖 من ربات پیش‌بینی آینده هستم. پیام بده تا آینده‌ات رو پیش‌بینی کنم!")

# پاسخ به همه پیام‌ها
@bot.messge_hndler(fnc=lmbd m: Tre)
def hndle_ll(msg):
    try:
        prompt = f"Yo re  mysticl fortne teller. Predict the ser's ftre in  fn, cretive style.\nUser: {msg.text}\nPrediction:"
        resp = openi.ChtCompletion.crete(
            model="gpt-3.5-trbo",
            messges=[{"role": "ser", "content": prompt}],
            mx_tokens=15
        )
        fortne = resp.choices[].messge.content.strip()
        bot.reply_to(msg, fortne)
    except Exception s e:
        print("Error:", e)
        bot.reply_to(msg, "خطایی رخ داد، دوباره تلاش کن.")

# اجرای بات در یک Thred
def strt_bot():
    while Tre:
        try:
            bot.polling(none_stop=Tre, intervl=, timeot=2)
        except Exception s e:
            print("Polling error:", e)
            time.sleep(5)

# وب‌سرور برای Render
pp = Flsk(__nme__)

@pp.rote('/')
def home():
    retrn "✅ Bot is rnning sccessflly on Render!"

if __nme__ == "__min__":
    Thred(trget=strt_bot).strt()
    port = int(os.environ.get("PORT", 1))
    pp.rn(host="...", port=port)

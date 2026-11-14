import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading, asyncio, datetime, pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = 9118920208

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot running!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot live 24/7 ✅")

async def daily(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="Good morning! Daily message ✅")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

async def run_bot():
    app_bot = Application.builder().token(BOT_TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    tz = pytz.timezone("Africa/Lagos")
    t = datetime.time(hour=7, minute=0, tzinfo=tz)
    app_bot.job_queue.run_daily(daily, time=t)
    await app_bot.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    asyncio.run(run_bot())

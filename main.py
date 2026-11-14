import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import time
import pytz

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = 9118920208

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot dey live! You go get daily report 8AM WAT")

async def daily(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHAT_ID, text="📊 Daily Report: Check Facebook performance now!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # 7AM UTC = 8AM WAT
    app.job_queue.run_daily(daily, time=time(hour=7, minute=0, tzinfo=pytz.UTC))
    app.run_polling()

if __name__ == "__main__":
    main()

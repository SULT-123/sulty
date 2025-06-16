import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN") or "7845142531:AAFx0oAhK9CjIsaDZB6ySFQkBicigSXyqNk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 أهلاً بك في بوت الأسهم.\nاكتب /help لرؤية الأوامر.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📈 أوامر التحليل الفني المتوفرة:
/squeeze - عرض الأسهم التي بها سكويز
/volume - أعلى الأسهم من حيث السيولة
/momentum - أقوى الأسهم زخمًا
/breakout - اختراقات فنية للأسهم
/news - آخر الأخبار المهمة
""")

async def squeeze(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 سكويز الأسهم:\n1. سهم A\n2. سهم B")

async def volume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💧 أعلى الأسهم سيولة:\n1. سهم C\n2. سهم D")

async def momentum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 الأسهم ذات الزخم:\n1. سهم E\n2. سهم F")

async def breakout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📉 اختراقات فنية:\n1. سهم G\n2. سهم H")

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📰 أخبار السوق:\n- السوق يرتفع\n- النفط يهبط")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("squeeze", squeeze))
    app.add_handler(CommandHandler("volume", volume))
    app.add_handler(CommandHandler("momentum", momentum))
    app.add_handler(CommandHandler("breakout", breakout))
    app.add_handler(CommandHandler("news", news))

    print("🤖 البوت يعمل الآن...")
    app.run_polling()

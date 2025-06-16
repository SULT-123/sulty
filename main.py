import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = "8177669243:AAEkY786eA4SGvn0x7gigRbu7iIIzk4fc0c"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبًا بك في بوت التحليل اللحظي للأسهم!\n"
        "🔔 احصل على تنبيهات فنية لحظية\n"
        "اكتب /help لعرض قائمة الأوامر المتاحة"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/subscribe [الرمز] — للاشتراك في تنبيهات سهم\n"
        "/unsubscribe [الرمز] — لإلغاء الاشتراك\n"
        "/list — لعرض الأسهم المشترك بها\n"
        "/start — بدء استخدام البوت"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.run_polling()

if __name__ == "__main__":
    main()
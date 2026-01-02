from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "PUT_YOUR_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📚 المواد"],
        ["📖 الكتب والمراجع"],
        ["✏️ تمارين الدكتور"],
        ["📅 الجداول"],
        ["ℹ️ عن الكلية"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 أهلاً بيك في بوت كلية الحاسبات والذكاء الاصطناعي\n"
        "اختار اللي محتاجه من القايمة 👇",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()

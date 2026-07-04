from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8995256501:AAG-vjaRNR6jcZOzMrMjYj3PzJsCc7AUZl4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام دوست من ❤️\n\nمن اینجام که باهات حرف بزنم. هر چی دلت خواست بگو.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"دریافت شد: {user_text}\n\nممنون که بهم گفتی...")

if name == 'main':
    print("ربات شروع به کار کرد...")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & \~filters.COMMAND, handle_message))
    
    print("در حال اتصال...")
    app.run_polling()

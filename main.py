from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import os

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL = "https://t.me/AzCinemakino"
BOT2 = "https://t.me/GiftGoBot?startapp=ref_fb6cb2"
INSTAGRAM = "https://www.instagram.com/azcinemakino"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 1-kanal", url=CHANNEL)],
        [InlineKeyboardButton("🤖 2-bot", url=BOT2)],
        [InlineKeyboardButton("📷 Instagram", url=INSTAGRAM)],
        [InlineKeyboardButton("✅ Obunani tekshirish", callback_data="check")]
    ]

    await update.message.reply_text(
        "🎬 *AzCinema Bot*\n\n"
        "Botdan foydalanish uchun quyidagi tugmalarni bosing.",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "✅ Tekshirish funksiyasi keyingi bosqichda qo'shiladi."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check, pattern="check"))

app.run_polling()

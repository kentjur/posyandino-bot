from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8735994739:AAE0UVS7VfdGGvIOm3_Rt_bka4tsL7Xnb5c"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🦕 Bot Posyandu Dino aktif!")
    
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    data = text.split("|")

    if len(data) != 3:
        await update.message.reply_text(
            "Format salah!\n\nContoh:\n/check Briella | Bonitasaura | 7"
        )
        return

    nama = data[0].strip()
    jenis = data[1].strip()
    umur = int(data[2].strip())

    berat = umur * 2

    hasil = f"""
🦕 Nama: {nama}
🦖 Jenis: {jenis}
📅 Umur: {umur} bulan
⚖️ Estimasi berat: {berat} kg
"""

    await update.message.reply_text(hasil)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("check", check))

print("Bot jalan...")
app.run_polling()
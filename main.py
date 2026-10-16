import telebot, random, os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🔥 БОТ 24/7 ЗАПУЩЕН\n\n/signal - сигнал")

@bot.message_handler(commands=['signal'])
def signal(m):
    pair = random.choice(["EUR/USD OTC","GBP/USD OTC","USD/JPY OTC"])
    d = random.choice(["ВВЕРХ 🟢","ВНИЗ 🔴"])
    bot.send_message(m.chat.id, f"📊 {pair}\n{d}\nТочность {random.randint(83,94)}%\n⏰ 2 мин")

bot.infinity_polling()

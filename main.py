import telebot
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 أهلاً بك في بوت\n"
        "✍📄 الترند بنفسك\n\n"
        "🚀 اصنع ترندك وشارك روابطك بسهولة."
    )


print("✅ البوت يعمل الآن...")

bot.infinity_polling()

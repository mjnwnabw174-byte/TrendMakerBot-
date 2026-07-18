import telebot

from config import BOT_TOKEN, check_config
from database import create_tables
from handlers import register_handlers


# فحص الإعدادات
check_config()

# إنشاء البوت
bot = telebot.TeleBot(BOT_TOKEN)


# تجهيز قاعدة البيانات
create_tables()


# تشغيل جميع أوامر البوت والأزرار
register_handlers(bot)


print("✅ ✍📄 الترند بنفسك يعمل الآن...")


# تشغيل البوت
bot.infinity_polling()

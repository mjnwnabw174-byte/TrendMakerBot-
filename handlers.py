from telebot import TeleBot
from telebot.types import CallbackQuery

from keyboards import main_menu
from database import add_user


def register_handlers(bot: TeleBot):

    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user

        add_user(
            user.id,
            user.username,
            user.first_name
        )

        bot.send_message(
            message.chat.id,
            "👋 أهلاً بك في ✍📄 الترند بنفسك\n\n"
            "اختر من القائمة:",
            reply_markup=main_menu()
        )


    @bot.callback_query_handler(func=lambda call: True)
    def callbacks(call: CallbackQuery):

        if call.data == "exchange":
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "📈 نظام التبادل سيتم تجهيزه في المرحلة القادمة."
            )

        elif call.data == "add_link":
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "➕ أرسل رابط TikTok لإضافته."
            )

        elif call.data == "profile":
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "👤 سيتم عرض حسابك هنا قريبًا."
            )

        elif call.data == "leaders":
            bot.answer_callback_query(call.id)
            bot.send_message(
                call.message.chat.id,
                "🏆 قائمة المتصدرين قيد التجهيز."
          )

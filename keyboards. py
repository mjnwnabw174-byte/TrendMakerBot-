from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "📈 تبادل الترند",
            callback_data="exchange"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "➕ إضافة رابط",
            callback_data="add_link"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "👤 حسابي",
            callback_data="profile"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "🏆 المتصدرين",
            callback_data="leaders"
        )
    )

    return keyboard


def admin_menu():
    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton(
            "📊 الإحصائيات",
            callback_data="stats"
        )
    )

    keyboard.add(
        InlineKeyboardButton(
            "📢 إذاعة",
            callback_data="broadcast"
        )
    )

    return keyboard

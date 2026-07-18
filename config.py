import os
from dotenv import load_dotenv

load_dotenv()

# توكن البوت (يوضع في Railway وليس هنا)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# بيانات المطور
OWNER_ID = 7361451060
OWNER_USERNAME = "@mahwb7"

# اسم البوت
BOT_NAME = "✍📄 الترند بنفسك"

# رابط Google Apps Script
GOOGLE_SCRIPT_URL = os.getenv("GOOGLE_SCRIPT_URL")

# ملف قاعدة البيانات
DATABASE_FILE = "bot_database.db"


def check_config():
    if not BOT_TOKEN:
        print("⚠️ تحذير: BOT_TOKEN غير موجود")

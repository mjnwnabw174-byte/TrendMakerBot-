import os
from dotenv import load_dotenv

load_dotenv()

# توكن البوت من Railway Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

# معلومات المطور
OWNER_ID = 7361451060
OWNER_USERNAME = "@mahwb7"

# رابط Google Apps Script
GOOGLE_SCRIPT_URL = os.getenv("GOOGLE_SCRIPT_URL")

# اسم قاعدة البيانات
DATABASE_NAME = "bot_database.db"


if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN غير موجود في متغيرات البيئة")

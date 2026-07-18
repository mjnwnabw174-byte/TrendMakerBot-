import requests

from config import GOOGLE_SCRIPT_URL


def send_to_sheet(data):
    """
    إرسال البيانات إلى Google Apps Script
    """

    if not GOOGLE_SCRIPT_URL:
        print("⚠️ رابط Google Script غير موجود")
        return False

    try:
        response = requests.post(
            GOOGLE_SCRIPT_URL,
            json=data,
            timeout=10
        )

        if response.status_code == 200:
            return True

        return False

    except Exception as e:
        print("خطأ Google Sheets:", e)
        return False



def save_link(user_id, username, link):
    """
    حفظ رابط TikTok
    """

    data = {
        "action": "add_link",
        "user_id": user_id,
        "username": username,
        "link": link
    }

    return send_to_sheet(data)

import sqlite3
from config import DATABASE_FILE


def connect():
    return sqlite3.connect(DATABASE_FILE)


def create_tables():
    db = connect()
    cursor = db.cursor()

    # جدول المستخدمين
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        points INTEGER DEFAULT 0,
        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # جدول الروابط
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        link TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    db.commit()
    db.close()


def add_user(user_id, username, first_name):
    db = connect()
    cursor = db.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (id, username, first_name)
        VALUES (?, ?, ?)
        """,
        (user_id, username, first_name)
    )

    db.commit()
    db.close()


def get_users_count():
    db = connect()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    db.close()
    return count

import sqlite3

class AlexDatabase:
    def __init__(self, db_path=r"D:\alex_platform\alex_data.db"):
        self.db_path = db_path
        self._init_db()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS lessons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    topic TEXT NOT NULL,
                    content_md TEXT NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    def save_lesson(self, topic, content_md):
        with self._get_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO lessons (topic, content_md) VALUES (?, ?)",
                (topic, content_md)
            )
            conn.commit()
            return cursor.lastrowidS
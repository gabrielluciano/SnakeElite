import sqlite3
from datetime import datetime

class DBProxy:
    def __init__(self, db_name="scoreboard.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    timestamp DATETIME NOT NULL
                )
            """)

    def add_score(self, name, score):
        with self.conn:
            self.conn.execute(
                "INSERT INTO scores (name, score, timestamp) VALUES (?, ?, ?)",
                (name, score, datetime.now())
            )

    def get_scores(self):
        with self.conn:
            cursor = self.conn.execute(
                "SELECT name, score, timestamp FROM scores ORDER BY score DESC, timestamp DESC"
            )
            return cursor.fetchall()

    def __del__(self):
        self.conn.close()

import sqlite3
import os
from typing import List, Dict
from .models import TransactionIn, Transaction
from datetime import datetime


class DB:
    def __init__(self, path: str = "data/budget.db"):
        # create data dir if needed
        d = os.path.dirname(path)
        if d:
            os.makedirs(d, exist_ok=True)
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self._init_tables()

    def _init_tables(self):
        cur = self.conn.cursor()
        cur.execute(
            """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT
        )
        """
        )
        self.conn.commit()

    def add_transaction(self, t: TransactionIn) -> Transaction:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO transactions (amount, date, category, description) VALUES (?, ?, ?, ?)",
            (t.amount, t.date.isoformat(), t.category, t.description),
        )
        self.conn.commit()
        transaction_id = cur.lastrowid
        return Transaction(id=transaction_id, **t.dict())

    def list_transactions(self, limit: int = 100) -> List[Transaction]:
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY date DESC LIMIT ?", (limit,))
        rows = cur.fetchall()
        return [
            Transaction(
                id=row["id"],
                amount=row["amount"],
                date=datetime.fromisoformat(row["date"]).date(),
                category=row["category"],
                description=row["description"],
            )
            for row in rows
        ]

    def summary_by_month(self, year: int, month: int) -> Dict[str, float]:
        cur = self.conn.cursor()
        start = f"{year:04d}-{month:02d}-01"
        if month == 12:
            end = f"{year+1:04d}-01-01"
        else:
            end = f"{year:04d}-{month+1:02d}-01"
        cur.execute(
            """
        SELECT category, SUM(amount) as total FROM transactions
        WHERE date >= ? AND date < ?
        GROUP BY category
        """,
            (start, end),
        )
        return {row["category"]: row["total"] for row in cur.fetchall()}

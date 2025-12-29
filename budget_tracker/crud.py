from .db import DB
from .models import TransactionIn

# default module-level DB; tests can override
db = DB()


def add_transaction(t: TransactionIn):
    return db.add_transaction(t)


def list_transactions(limit: int = 100):
    return db.list_transactions(limit)


def monthly_summary(year: int, month: int):
    return db.summary_by_month(year, month)

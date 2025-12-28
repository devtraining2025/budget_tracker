from budget_tracker.db import DB
from budget_tracker.models import TransactionIn
from datetime import date

def test_add_and_list_transactions(tmp_path):
    dbfile = str(tmp_path / "test.db")
    db = DB(dbfile)
    t = TransactionIn(amount=12.5, date=date(2025,12,25), category="groceries", description="milk")
    added = db.add_transaction(t)
    assert added.id is not None
    txs = db.list_transactions()
    assert len(txs) == 1
    assert abs(txs[0].amount - 12.5) < 1e-9


def test_summary_by_month():
    db = DB(":memory:")
    db.add_transaction(TransactionIn(amount=10, date=date(2025,12,1), category="a"))
    db.add_transaction(TransactionIn(amount=20, date=date(2025,12,2), category="a"))
    db.add_transaction(TransactionIn(amount=5, date=date(2025,11,30), category="b"))
    s = db.summary_by_month(2025, 12)
    assert s["a"] == 30
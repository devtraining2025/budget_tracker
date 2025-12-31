from fastapi import FastAPI
from .models import TransactionIn, Transaction
from .crud import add_transaction, list_transactions, monthly_summary
from typing import List

app = FastAPI(title="Budget Tracker API")


@app.post("/transactions/", response_model=Transaction)
def create_tx(tx: TransactionIn):
    return add_transaction(tx)


@app.get("/transactions/", response_model=List[Transaction])
def get_txs(limit: int = 100):
    return list_transactions(limit)


@app.get("/summary/{year}/{month}")
def get_summary(year: int, month: int):
    return monthly_summary(year, month)

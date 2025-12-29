from pydantic import BaseModel
from datetime import date
from typing import Optional


class TransactionIn(BaseModel):
    amount: float
    date: date
    category: str
    description: Optional[str] = None


class Transaction(TransactionIn):
    id: int

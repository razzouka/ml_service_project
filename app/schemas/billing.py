from pydantic import BaseModel
from datetime import datetime


class CreditTransactionOut(BaseModel):
    id: int
    amount: int
    transaction_type: str
    description: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class BillingInfoOut(BaseModel):
    credit_balance: int
    transactions: list[CreditTransactionOut]

    class Config:
        from_attributes = True
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.credit_transaction import CreditTransaction


def apply_credit_transaction(
    db: Session,
    user: User,
    amount: int,
    transaction_type: str,
    description: str | None = None,
):
    new_balance = user.credit_balance + amount

    if new_balance < 0:
        raise HTTPException(status_code=400, detail="Insufficient credits")

    user.credit_balance = new_balance

    tx = CreditTransaction(
        user_id=user.id,
        amount=amount,
        transaction_type=transaction_type,
        description=description,
    )

    db.add(user)
    db.add(tx)


def charge_prediction_credits(
    db: Session,
    user: User,
    model_id: int,
    cost: int = 1,
):
    apply_credit_transaction(
        db=db,
        user=user,
        amount=-cost,
        transaction_type="debit",
        description=f"Prediction charge for model {model_id}",
    )
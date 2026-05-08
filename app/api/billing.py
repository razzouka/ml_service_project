from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.credit_transaction import CreditTransaction
from app.models.user import User
from app.core.security import get_current_active_user
from app.schemas.billing import BillingInfoOut

router = APIRouter(prefix="/billing", tags=["billing"])


@router.get("/me", response_model=BillingInfoOut)
def get_my_billing(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    transactions = (
        db.query(CreditTransaction)
        .filter(CreditTransaction.user_id == current_user.id)
        .order_by(CreditTransaction.created_at.desc())
        .all()
    )

    return {
        "credit_balance": current_user.credit_balance,
        "transactions": transactions,
    }
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.models.promo_code import PromoCode
from app.models.promo_redemption import PromoRedemption
from app.core.security import get_current_active_user
from app.schemas.promo import PromoRedeemRequest, PromoRedeemResponse
from app.services.billing import apply_credit_transaction

router = APIRouter(prefix="/promo", tags=["promo"])


@router.post("/redeem", response_model=PromoRedeemResponse)
def redeem_promo_code(
    payload: PromoRedeemRequest,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    promo = db.query(PromoCode).filter(PromoCode.code == payload.code).first()

    if not promo:
        raise HTTPException(status_code=404, detail="Promo code not found")

    if not promo.is_active:
        raise HTTPException(status_code=400, detail="Promo code is inactive")

    if promo.expires_at and promo.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Promo code has expired")

    if promo.times_used >= promo.max_activations:
        raise HTTPException(status_code=400, detail="Promo code usage limit reached")

    existing = (
        db.query(PromoRedemption)
        .filter(
            PromoRedemption.user_id == current_user.id,
            PromoRedemption.promo_code_id == promo.id,
        )
        .first()
    )

    if existing:
        raise HTTPException(status_code=400, detail="Promo code already redeemed by this user")

    try:
        redemption = PromoRedemption(
            user_id=current_user.id,
            promo_code_id=promo.id,
        )
        db.add(redemption)

        promo.times_used += 1
        db.add(promo)

        apply_credit_transaction(
            db=db,
            user=current_user,
            amount=promo.credit_amount,
            transaction_type="promo",
            description=f"Redeemed promo code {promo.code}",
        )

        db.commit()
        db.refresh(current_user)

        return {
            "message": "Promo code redeemed successfully",
            "code": promo.code,
            "credit_amount": promo.credit_amount,
            "new_balance": current_user.credit_balance,
        }

    except Exception:
        db.rollback()
        raise
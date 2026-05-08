from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.database import Base


class PromoCode(Base):
    __tablename__ = "promo_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    credit_amount = Column(Integer, nullable=False)
    expires_at = Column(DateTime, nullable=True)
    max_activations = Column(Integer, default=1, nullable=False)
    times_used = Column(Integer, default=0, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
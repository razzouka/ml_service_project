from pydantic import BaseModel


class PromoRedeemRequest(BaseModel):
    code: str


class PromoRedeemResponse(BaseModel):
    message: str
    code: str
    credit_amount: int
    new_balance: int
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.auth import router as auth_router
from app.api.models import router as models_router
from app.api.predictions import router as predictions_router
from app.api.billing import router as billing_router
from app.api.promo import router as promo_router

from app.db.database import Base, engine
from app.models.user import User
from app.models.model import Model
from app.models.prediction_job import PredictionJob
from app.models.credit_transaction import CreditTransaction
from app.models.promo_code import PromoCode
from app.models.promo_redemption import PromoRedemption

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ML Service MVP")

app.include_router(auth_router)
app.include_router(models_router)
app.include_router(predictions_router)
app.include_router(billing_router)
app.include_router(promo_router)

Instrumentator().instrument(app).expose(app, endpoint="/metrics")

@app.get("/")
def root():
    return {"message": "ML service is running"}
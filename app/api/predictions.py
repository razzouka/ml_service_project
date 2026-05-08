from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import joblib
import numpy as np

from app.db.database import get_db
from app.models.user import User
from app.models.model import Model
from app.models.prediction_job import PredictionJob
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.core.security import get_current_active_user
from app.services.billing import charge_prediction_credits

router = APIRouter(prefix="/predictions", tags=["predictions"])


@router.post("/", response_model=PredictionResponse)
def create_prediction(
    request: PredictionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    db_model = (
        db.query(Model)
        .filter(Model.id == request.model_id, Model.user_id == current_user.id)
        .first()
    )

    if not db_model:
        raise HTTPException(status_code=404, detail="Model not found")

    try:
        model = joblib.load(db_model.file_path)

        input_features = [list(request.input_data.values())]
        prediction = model.predict(input_features)

        prediction_value = prediction[0]
        if isinstance(prediction_value, np.generic):
            prediction_value = prediction_value.item()

        result = {"prediction": prediction_value}

        prediction_job = PredictionJob(
            user_id=current_user.id,
            model_id=request.model_id,
            input_data=request.input_data,
            status="success",
            result=result,
        )
        db.add(prediction_job)

        charge_prediction_credits(
            db=db,
            user=current_user,
            model_id=request.model_id,
            cost=1,
        )

        db.commit()
        db.refresh(prediction_job)

        return prediction_job

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
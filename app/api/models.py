from fastapi import APIRouter, Depends, UploadFile, HTTPException, Form, File
from sqlalchemy.orm import Session
from pathlib import Path
import shutil
import uuid

from app.db.database import get_db
from app.models.model import Model
from app.models.user import User
from app.core.security import get_current_active_user
from app.schemas.models import ModelOut

router = APIRouter(prefix="/models", tags=["models"])

UPLOAD_DIR = Path("uploads/models")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload", response_model=ModelOut)
def upload_model(
    file: UploadFile = File(...),
    name: str = Form(...),
    description: str | None = Form(None),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith(".pkl"):
        raise HTTPException(status_code=400, detail="Only .pkl files allowed")

    unique_filename = f"{uuid.uuid4()}_{file.filename}"
    saved_path = UPLOAD_DIR / unique_filename

    with open(saved_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db_model = Model(
        name=name,
        description=description,
        user_id=current_user.id,
        file_path=str(saved_path),
    )
    db.add(db_model)
    db.commit()
    db.refresh(db_model)

    return db_model


@router.get("/my", response_model=list[ModelOut])
def list_my_models(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
):
    models = db.query(Model).filter(Model.user_id == current_user.id).all()
    return models
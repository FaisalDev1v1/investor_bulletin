from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.model_base import SessionLocal
from resource.alerts import alert_service, alert_schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[alert_schema.AlertResponse])
def fetch_alerts(db: Session = Depends(get_db)):
    try:
        alerts = alert_service.get_alerts(db)
        return alerts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

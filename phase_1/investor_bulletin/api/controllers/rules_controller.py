from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.model_base import SessionLocal
from resource.alert_rules import alert_rule_schema, alert_rule_service

router = APIRouter()

@router.post("/alert-rules/")
def create_alert_rule(alert_rule: alert_rule_schema.AlertRuleCreate, db: Session = Depends(SessionLocal)):
    return alert_rule_service.create_alert_rule(db, alert_rule)

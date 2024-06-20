""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from sqlalchemy.orm import Session
from db.models import AlertRule
from resource.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate

def get_alert_rules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(AlertRule).offset(skip).limit(limit).all()

def create_alert_rule(db: Session, alert_rule: AlertRuleCreate):
    db_alert_rule = AlertRule(**alert_rule.dict())
    db.add(db_alert_rule)
    db.commit()
    db.refresh(db_alert_rule)
    return db_alert_rule

def get_alert_rule(db: Session, alert_rule_id: int):
    return db.query(AlertRule).filter(AlertRule.id == alert_rule_id).first()

def delete_alert_rule(db: Session, alert_rule_id: int):
    db_alert_rule = get_alert_rule(db, alert_rule_id)
    if db_alert_rule:
        db.delete(db_alert_rule)
        db.commit()
    return db_alert_rule

def update_alert_rule(db: Session, alert_rule_id: int, alert_rule: AlertRuleUpdate):
    db_alert_rule = get_alert_rule(db, alert_rule_id)
    if db_alert_rule:
        # Optimized approach for updating non-None values:
        for key, value in alert_rule.dict().items():
            if value is not None:
                setattr(db_alert_rule, key, value)

        # Optional: Handle potential errors during update
        try:
            db.commit()
        except Exception as e:
            db.rollback()
            raise e  # Re-raise the exception for handling by the caller

        return db_alert_rule  # Return the updated alert rule (optional)


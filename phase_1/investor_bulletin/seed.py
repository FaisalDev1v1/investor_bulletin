import sys
from sqlalchemy.orm import Session
from db.model_base import SessionLocal
from resource.alert_rules import alert_rule_service, alert_rule_schema

def seed_data(db: Session):
    initial_alert_rules = [
        {"name": "Apple Alert", "threshold": 150.0, "symbol": "AAPL"},
        {"name": "Microsoft Alert", "threshold": 250.0, "symbol": "MSFT"},
        {"name": "Google Alert", "threshold": 2800.0, "symbol": "GOOG"},
        {"name": "Amazon Alert", "threshold": 3500.0, "symbol": "AMZN"},
        {"name": "Meta Alert", "threshold": 300.0, "symbol": "META"},
    ]

    for alert_rule in initial_alert_rules:
        alert_rule_service.create_alert_rule(db, alert_rule_schema.AlertRuleCreate(**alert_rule))

def main():
    db = SessionLocal()
    seed_data(db)
    db.close()

if __name__ == "__main__":
    main()

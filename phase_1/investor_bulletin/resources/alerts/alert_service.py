""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from resource.alert_rules.alert_rule_dal import get_alert_rules
from resource.market.market_service import get_market_prices
from resource.alerts.alert_model import Alert

def get_alerts(db):
    alert_rules = get_alert_rules(db)
    market_prices = get_market_prices()

    alerts = []

    for rule in alert_rules:
        current_price = float(market_prices.get(rule.symbol, 0))
        if current_price >= rule.threshold:
            alert = Alert(
                name=rule.name,
                symbol=rule.symbol,
                threshold=rule.threshold,
                current_price=current_price,
                message=f"{rule.symbol} has reached the threshold price of {rule.threshold}"
            )
            alerts.append(alert)

    return alerts

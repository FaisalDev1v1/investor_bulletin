""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
# from resources.alert_rules.alert_rule_schema import AlertRuleCreate
# from resources.alert_rules.alert_rule_dal import create_alert_rule

# def create_new_rule( rule: AlertRuleCreate, session ):
#     return create_alert_rule( rule=rule, session=session)
def create_alert(message):
    # Logic to create a new alert record
    print(f"Creating alert record for message: {message}")
    # You can add database logic here to store the alert

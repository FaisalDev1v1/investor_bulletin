""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
# from resources.alerts.alerts_schema import AlertCreate
# from resources.alerts.alert_dal import create_alert

# def create_new_alert( rule: AlertCreate, session ):
#     return create_rule( rule=rule, session=session)
# resource/alert/alert_service.py
class AlertService:
    def __init__(self):
        self.alerts = []

    def create_alert(self, message):
        alert = {"message": message, "status": "new"}
        self.alerts.append(alert)
        print(f"Alert created: {alert}")

# Example usage
if __name__ == "__main__":
    alert_service = AlertService()
    alert_service.create_alert("THRESHOLD_ALERT: Alert threshold reached!")

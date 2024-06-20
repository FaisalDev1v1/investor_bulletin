""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
# from pydantic import BaseModel

# class AlertCreate(BaseModel):
from pydantic import BaseModel

class AlertResponse(BaseModel):
    name: str
    symbol: str
    threshold: float
    current_price: float
    message: str
